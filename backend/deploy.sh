REGION=us-east-1
S3_BUCKET=serverless-deploy-all-lsft-projects
STACK_NAME=visual-schedules
PROFILE=power-user

cd src && \
/home/linuxbrew/.linuxbrew/bin/sam build && \
sam package --output-template-file packaged-template.yaml --s3-bucket ${S3_BUCKET} --region ${REGION} --profile ${PROFILE} && \
sam deploy --template-file packaged-template.yaml --region ${REGION} --capabilities CAPABILITY_IAM --stack-name ${STACK_NAME}  --parameter-overrides ProjectName=${STACK_NAME} --profile ${PROFILE}


outputs=$(aws cloudformation describe-stacks --stack-name $STACK_NAME --output json --query 'Stacks[0].Outputs')
echo $outputs > './outputs.json'
echo $outputs