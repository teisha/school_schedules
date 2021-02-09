
let config = {}
if (process.env.NODE_ENV == "local") {
    config = require("./environment/config.local.js")
} else {
    config = require("./environment/config.js")
}

module.exports = {
    env: {
        DYNAMODB: config.data_table,
        API_URL: config.api_url,
        config: config.cognito_config
    },
    serverRuntimeConfig: {
        // Will only be available on the server side
        MY_SECRET: process.env.MY_SECRET,
    },
    publicRuntimeConfig: {
        // Will be available on both server and client
        API_ENDPOINT: '/myapi/version/1',
    },
};