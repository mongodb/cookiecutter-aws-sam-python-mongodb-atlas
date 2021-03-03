import json
import pymongo
import requests
import os

# TODO - Update this for some default locally running MongoDB in docker
# for sam local
DB_URI = os.environ.get('MONGODB_URI')
USERNAME = os.environ.get('MONGODB_USERNAME')
PASSWORD = os.environ.get('MONGODB_PASSWORD')

print( DB_URI )
print( USERNAME )
print( PASSWORD )
client = pymongo.MongoClient( host=DB_URI,
                              username=USERNAME,
                              password=PASSWORD,
                              appname='sam-app')

print( client )


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
    except Exception as e:
        # Send some context about this error to Lambda Logs
        print(e)
        raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "MongoDB Rocks!",
            "ip": ip_value,
            "log": log
        }),
    }
