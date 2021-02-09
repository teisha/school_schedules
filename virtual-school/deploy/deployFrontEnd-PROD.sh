set -e

ENVIRONMENT="prod"
REGION=us-east-1
PROFILE=power-user

CLIENT="kids-schedule"
BACKEND_STACK="$ENVIRONMENT-visual-schedules"

# outputs=$(aws cloudformation describe-stacks --region $REGION --stack-name $BACKEND_STACK --output json --query 'Stacks[0].Outputs' --profile ${PROFILE})
# echo $outputs > './outputs.json'
# echo $outputs
rm -rf out
node prepareEnvironment.js PROFILE=$PROFILE REGION=$REGION BACKEND_STACK=$BACKEND_STACK
node overWriteEnv.js ENVIRONMENT=$ENVIRONMENT

cd ../
npm install 

npm run build 


cd deploy
mkdir -p out/_next/static
cp ../.next/server/pages/*.html ./out
cp ../.next/server/pages/*.js ./out
cp -R ../.next/static ./out/_next 
cp -R ../.next/server ./out
cp -R ../.next/static ./out
cp ../.next/*manifest.json ./out
cp ../public/*.* ./out


distributionid=$( cat ./outputs.json | jq -r 'map(select(.OutputKey == "CognitoDistributionId"))[0] | "\(.OutputValue)"' )
hostBucket=$( cat ./outputs.json | jq -r 'map(select(.OutputKey == "HostBucket"))[0] | "\(.OutputValue)"' )
echo "DistributionID - ${distributionid}"
echo "Host Bucket - ${hostBucket}"

aws s3 sync ./out s3://${hostBucket} --delete --profile $PROFILE --region $REGION
aws cloudfront create-invalidation --distribution-id ${distributionid} --paths / --profile $PROFILE --region $REGION


echo "completed"