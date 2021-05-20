#!/usr/bin/env bash

echo " +-+-+-+-+-+-+-+-+-+-+-+-+-+ "
echo " |M|o|n|g|o|D|B|-|A|t|l|a|s| "
echo " +-+-+-+-+-+-+-+-+-+-+-+-+-+ "
echo "Hello $(whoami)!"
echo "Welcome to your MongoDB Atlas Project:{{ cookiecutter.project_name }}"
echo "Next steps:"
echo "cd {{ cookiecutter.project_name }}"
echo "sam build"
echo "sam deploy --guided --extra-parameters \$(./export mongocli-parameters.py)"

