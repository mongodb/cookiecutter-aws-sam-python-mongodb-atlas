#!/usr/bin/env bash
cat <<- EOF

 +-+-+-+-+-+-+-+-+-+-+-+-+-+
 |M|o|n|g|o|D|B|-|A|t|l|a|s|
 +-+-+-+-+-+-+-+-+-+-+-+-+-+

Hello $(whoami)!
Welcome to your MongoDB Atlas Project: {{ cookiecutter.project_name }}
Next steps: (you can cut and paste this snippet)

--------------------------------------------------------------------------

cd {{ cookiecutter.project_name }}
sam build
sam deploy --guided --parameter-overrides \$(./export-mongocli-parameters.py)

--------------------------------------------------------------------------

EOF

