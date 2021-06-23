import json
import pymongo
import requests
from requests.auth import HTTPDigestAuth
import os
from jinja2 import Environment, FileSystemLoader

# TODO - Update this for some default locally running MongoDB in docker
# for sam local
DB_URI = os.environ.get('MONGODB_URI')
USERNAME = os.environ.get('MONGODB_USERNAME')
PASSWORD = os.environ.get('MONGODB_PASSWORD')
PROJECT_ID = os.environ.get('MONGODB_ATLAS_PROJECT_ID')
APP_NAME = os.environ.get('APP_NAME')
CLUSTER_NAME = os.environ.get('MONGODB_ATLAS_CLUSTER_NAME')

print( f"DB_URI={DB_URI}")
print( f"USERNAME={USERNAME}")
print( f"PROJECT_ID={PROJECT_ID}")
print( f"APP_NAME={APP_NAME}")
print( f"CLUSTER_NAME={CLUSTER_NAME}")
client = pymongo.MongoClient( host=DB_URI,
                              username=USERNAME,
                              password=PASSWORD,
                              appname=f"sam-app-project-id-{PROJECT_ID}")

print( client )


baseurl = "https://cloud.mongodb.com/api/atlas/v1.0/groups"
url=f"{baseurl}/{PROJECT_ID}/clusters/{CLUSTER_NAME}"
print(f" ------ id: {PROJECT_ID}  --- url:{url}")
cluster = requests.get(url, auth=HTTPDigestAuth(
    os.environ["MONGODB_ATLAS_PUBLIC_KEY"],
    os.environ["MONGODB_ATLAS_PRIVATE_KEY"]))

# TODO// error handle here for failed cluster api call
CLUSTER_ID = cluster.json()['id']
print( f" ~ ~ ~ dyno lookup found CLUSTER_ID={CLUSTER_ID}")

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    try:
        ip = requests.get("http://checkip.amazonaws.com/")
        ip_value = ip.text.strip()
        db = client['sam-app']
        collection = db['ip-logs']
        log = collection.find_one_and_update(
                { "_id" : ip_value },
                { "$inc" : { "counter" : 1 } },
                upsert=True,
                return_document=pymongo.collection.ReturnDocument.AFTER)



        print(f'Updated log entry: {log}')
        print(f' ---> context:{context}')
        print(f' ---> event: {event}')

        atlas_project_href = f"https://cloud.mongodb.com/v2/{PROJECT_ID}#clusters"
        accept_mime=event['headers']['Accept']
        return_object = {
            "message": "MongoDB Rocks!",
            "ip": ip_value,
            "log": log,
            "mongodb_atlas": atlas_project_href
        }
        print(f' --> atlas_project_href={atlas_project_href} accept_mime={accept_mime}')

        if 'text/html' in accept_mime:
            content_type = 'text/html'
            env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates"), encoding="utf8"))
            template = env.get_template("index.html")
            content = template.render(project_id=PROJECT_ID,
                                      project_name=APP_NAME,
                                      cluster_name=CLUSTER_NAME,
                                      cluster_id=CLUSTER_ID,
                                      log_object=return_object)
        else:
            content_type = 'application/json'
            content = json.dumps(return_object)
    except Exception as e:
        # Send some context about this error to Lambda Logs
        print(e)
        raise e

    return {
        "statusCode": 200,
        "body": content,
        "headers": {"content-type" : content_type}
    }
