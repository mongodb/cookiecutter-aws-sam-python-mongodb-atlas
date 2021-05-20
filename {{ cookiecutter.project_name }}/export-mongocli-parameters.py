#!/usr/bin/env python3

# export-mongocli-parameter.py
# Tool to export mongocli parameters to sam aps and CloudFormation
#
# $source <(./export-mongocli-config.py)
#
import os, sys, toml

homepath=os.path.expanduser("~")

config="%s/.config/mongocli.toml" % homepath

t=toml.load(config)

if len(sys.argv)>1:
    profile = sys.argv[1]
else:
    profile="default"
if not profile in t:
    raise Exception(f"No profile '{profile}' found in {config}")

if len(sys.argv)>2:
    project_name = sys.argv[2]
else:
    project_name = os.path.basename(os.getcwd())

d=t[profile]
print( f"ParameterKey=PublicKey,ParameterValue={d['public_api_key']} ParameterKey=PrivateKey,ParameterValue={d['private_api_key']} ParameterKey=OrgId,ParameterValue={d['org_id']} ParameterKey=ProjectName,ParameterValue={project_name}" )


