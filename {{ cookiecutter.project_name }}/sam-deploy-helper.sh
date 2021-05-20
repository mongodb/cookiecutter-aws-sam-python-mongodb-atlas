#!/usr/bin/env bash

# Helper to run sam deploy with
# your MongoDB Atlas settings
stack_name=$(basename $(pwd))
sam deploy --guided \
 --parameter-overrides $(./export-mongocli-parameters.py) \
 --stack-name "${stack_name}"
