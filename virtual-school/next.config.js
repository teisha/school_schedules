
let config = {}
if (process.env.NODE_ENV == "development") {
    config = require("./environment/config.development.js")
} else {
    config = require("./envitonment/config.production.js")
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