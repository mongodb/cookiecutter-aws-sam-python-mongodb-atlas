# Cookiecutter SAM for MongoDB Atlas with Python Lambda functions

This is a [Cookiecutter](https://github.com/audreyr/cookiecutter) template to create a Serverless App based on Serverless Application Model (SAM) and Python 3.8 which uses MongoDB Atlas.

It is important to note that you should not try to `git clone` this project but use `SAM` CLI instead as ``{{cookiecutter.project_slug}}`` will be rendered based on your input and therefore all variables and files will be rendered properly.

## Usage

Generate a new SAM based Serverless App: `sam init --location gh:jasonmimick/cookiecutter-mongodb-atlas-aws-sam-python`

You'll be prompted a few questions to help this cookiecutter template to scaffold this project and after its completed you should see a new folder at your current path with the name of the project you gave as input.

* Create an organizational-level [MongoDB Atlas Programmatic API](https://docs.atlas.mongodb.com/configure-api-access#programmatic-api-keys). The key needs `Project Creator` permissions.

* The aws and sam cli's setup and configured on your development machine. 

* We also recommend [mongocli](https://github.com/mongodb/mongocli) for the easiest way to manage all your MongoDB Atlas needs, cluster and apikeys included!

## Pre-requisite

The project will deploy the MongoDB Atlas AWS Quick Start which provisions complete MongoDB Atlas deployments through CloudFormation using official MongoDB Atlas AWS CloudFormation Resource Types.

Until these resources a more easily available you can use the [get-start-aws](http://) project to bootstrap each AWS region with the Atlas CFN Resource Types:

```bash
curl https://raw.githubusercontent.com/jasonmimick/get-started-aws/main/get-setup.sh | bash -s -- jmimick/atlas-aws us-east-2
```

For example - passing in a docker image tag from the get-started-aws project and the AWS region to deploy into.

## Options

Option | Description
------------------------------------------------- | ---------------------------------------------------------------------------------
`include_safe_deployment` | Sends by default 10% of traffic for every 1 minute to a newly deployed function using [CodeDeploy + SAM integration](https://github.com/awslabs/serverless-application-model/blob/master/docs/safe_lambda_deployments.rst) - Linear10PercentEvery1Minute

## Deployment Parameters

To deploy your serverless app you will need to supply the following:

Parameter  | Required | Description | Default
-----------| - | --------------------------------- | ------------------------------
PublicKey  | Y | Your MongoDB Cloud Public API Key | 
PrivateKey | Y | Your MongoDB Cloud Private API Key |
OrgId      | Y | Your MongoDB Cloud Organization Id | 
ProjectName | N | The name of the project." | `get-started-aws-lambda-python`
ClusterName | N | Name of the cluster as it appears in Atlas. Once the cluster is created, its name cannot be changed. | `Cluster-1`
ClusterInstanceSize | N | Atlas Cluster Tier | `M10` 
ClusterRegion | N | The AWS Region where the Atlas DB Cluster will run. (AWS Region format) | `us-east-1`
ClusterMongoDBMajorVersion | N The version of MongoDB | `latest`

# Credits

* This project was copied and started from [coookiecutter-aws-sam-python](https://github.com/aws-samples/cookiecutter-aws-sam-python) project.

* This project has been generated with [Cookiecutter](https://github.com/audreyr/cookiecutter)

* [Bruno Alla's Lambda function template](https://github.com/browniebroke/cookiecutter-lambda-function)

License
-------

This project is licensed under the terms of the [MIT License with no attribution](/LICENSE)
