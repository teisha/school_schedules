import { loadEnvConfig } from 'next/dist/lib/load-env-config';
import { join } from 'path';

// api will call endpoint

// laimaB / nowAUser!123

// AWS.config.credentials = new AWS.SharedIniFileCredentials({ profile: "kawasaki-dev" });
// AWS.config.update({ region: "us-east-1" });

describe ('Login', () => {
    beforeAll(() => {
        loadEnvConfig(join(__dirname, '.../'), true);
    })
    it(' makes a call to correct endpoint with username and password', () => {
        
    })
})