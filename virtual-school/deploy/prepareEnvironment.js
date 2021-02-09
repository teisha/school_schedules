const AWS = require("aws-sdk")
const fs = require("fs")

const getArg = (variableName) => {
    const entry = process.argv.find((field) => field.startsWith(variableName));
    if (entry) {
        return entry.split("=")[1];
    } else {
        return null;
    }
};

const profile = getArg("PROFILE");
const region = getArg("REGION");
const stackName = getArg("BACKEND_STACK")  // 'bayview-test-tdb-dev'

const credentials = new AWS.SharedIniFileCredentials({ profile: profile });
AWS.config.credentials = credentials;
const cloudformation = new AWS.CloudFormation({ apiVersion: '2010-05-15', region: region })

const populateAttributes = async (stackName) => {
    let outputs = []
    outputs.push({
        "OutputKey": "AWSREGION",
        "OutputValue": region,
        "Description": "AWS Deploy Region"
    })

    const params = {
        StackName: stackName
    };

    try {
        const stack = await cloudformation.describeStacks(params).promise()
        console.log("DESCRIBE")
        console.log(stack)
        const o = stack.Stacks[0].Outputs
        console.log(o)
        for (outputVal in o) {
            // outputs[o[outputVal].OutputKey] = o[outputVal].OutputValue
            outputs.push(o[outputVal])
        }
    } catch (error) {
        console.log(error, error.stack); // an error occurred
    }

    let restApiId
    try {
        const resources = await cloudformation.listStackResources(params).promise();
        console.log("LIST RESOURCES");

        // const entry = process.argv.find((field) => field.startsWith(variableName));
        outputs.push({
            "OutputKey": "CFDistributionId",
            "OutputValue": resources.StackResourceSummaries.find(resource => resource.LogicalResourceId === 'AppDistribution')?.PhysicalResourceId,
            "Description": "Cloud Front Distribution ID to invalidate after files copied"
        })
        // outputs.push({
        //     "OutputKey": "HostBucket",
        //     "OutputValue": resources.StackResourceSummaries.find(resource => resource.LogicalResourceId === 'AppBucket')?.PhysicalResourceId,
        //     "Description": "FrontEnd App Host Bucket - copy files here"
        // })

        // console.log(resources.StackResourceSummaries);
    } catch (error) {
        console.error("Couldn't get resources for stack: " + stackName)
        console.log(error, error.stack); // an error occurred
    }

    // const apiParams = {
    //     StackName: apiStackName
    // }
    // try {
    //     const stack = await cloudformation.describeStacks(apiParams).promise()
    //     // console.log ("DESCRIBE", stack)
    //     const o = stack.Stacks[0].Outputs
    //     console.log(o)
    //     for (outputVal in o) {
    //         // outputs[o[outputVal].OutputKey] = o[outputVal].OutputValue
    //         outputs.push(o[outputVal])
    //     }
    // } catch (error) {
    //     console.error("Couldn't get outputs for stack: " + apiStackName)
    //     console.log(error, error.stack); // an error occurred
    // }
    // try {
    //     const resources = await cloudformation.listStackResources(apiParams).promise();
    //     restApiId = resources.StackResourceSummaries.find(resource => resource.LogicalResourceId === 'CcpApi').PhysicalResourceId
    //     outputs.push({
    //         "OutputKey": "APIGATEWAY",
    //         "OutputValue": restApiId,
    //         "Description": "Gateway ID needed to derive Cognito Domain"
    //     })

    // } catch (error) {
    //     console.error("Couldn't get API gateway for stack: " + apiStackName)
    //     console.log(error, error.stack); // an error occurred
    // }


    return outputs;
}

populateAttributes(stackName)
    .then(data => {
        console.log(data)
        fs.writeFileSync('outputs.json', JSON.stringify(data))
    })


/*
need the URL for the ccpwrapper to stick into
APIGATEWAY - is undefined

[ { "OutputKey": "CognitoClientId",
    "OutputValue": "3tp214oq29gl5sihog5itfcg8f",
    "Description": "Cognito client ID" },
{ "OutputKey": "BackendUrl",
    "OutputValue": "https://rj7cxoslbg.execute-api.us-west-2.amazonaws.com/c89c3a7d-49db-403d-bf0c-b91a5730a068/",
    "Description": "API Gateway backend URL" },
{ "OutputKey": "CognitoRedirectUri",
    "OutputValue": "https://d11e9ee6i7p8xo.cloudfront.net/auth",
    "Description": "Redirect URI for Admin UI configuration" },
{ "OutputKey": "CognitoDomain",
    "OutputValue": "bayview-test-tdb-dev",
    "Description": "Cogntio Domain" },
{ "OutputKey": "HostBucket",
    "OutputValue": "bayview-test-tdb-dev-host-bucket",
    "Description": "S3 bucket created to hold frontend." }
]
*/