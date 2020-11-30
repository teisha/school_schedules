/* eslint-disable no-undef */

import Router from 'next/router'
import ICognitoConfig from '../models/ICognitoConfig'
import jwtDecode from 'jwt-decode';
import IUser from '../models/IUser';
import IAuthToken from '../models/IAuthToken';


export class CognitoService {
    constructor() {}

    isUserSignedIn(): boolean {
        return (
            localStorage.getItem('cognito_token') &&
            localStorage.getItem('cognito_token').length > 0
        );
    }

    getAuthToken(): string {
        return localStorage.getItem('cognito_token');
    }

    setAuthToken(token: string): void {
        localStorage.setItem('cognito_token', token);
    }

    validateToken(token: string, config: ICognitoConfig): boolean {
        const data = jwtDecode(token);
        return data['aud'] == config.cognito_client_id
    }

    // ID_TOKEN:
    // Header:
    // {
    //   "kid": "Rxbdb92wGEU0xHXUPYxMZ7+smUTI3QoGhXig5ZC8hEE=",
    //   "alg": "RS256"
    // }
    // Payload:
    // {
    //   "at_hash": "-rxDAP7ECkLP5DswG8uRsg",
    //   "sub": "f9cdee7c-a58e-49ec-8115-69808cce9c51",
    //   "aud": "7p1g2ho5eslm2vea7jf8o8f2ao",
    //   "email_verified": true,
    //   "event_id": "2379cba1-c051-4308-bff4-fd456c464fee",
    //   "token_use": "id",
    //   "auth_time": 1606507750,
    //   "iss": "https://cognito-idp.us-east-1.amazonaws.com/us-east-1_89k06lCSA",
    //   "cognito:username": "laimaB",
    //   "exp": 1606511350,
    //   "iat": 1606507750,
    //   "email": "ahsiet4@yahoo.com"
    // }
    parseIdToken(token: string): IAuthToken {
        const data = jwtDecode(token);
        console.log(data);
        return {
            rawtoken: token,
            cognito_username: data['cognito:username'],
            email: data['email'],
            auth_time: data['auth_time'],
            expires: data['exp'],
            issued_at: data['iat'],
            is_expired: false
        };
    }

    // ACCESS TOKEN:
    // Header:
    // {
    //   "kid": "eeebqdwD2AQIY+EEbrUdX61GseYG/uJgpwRD3M5FW9k=",
    //   "alg": "RS256"
    // }
    // Payload:
    // {
    //   "sub": "f9cdee7c-a58e-49ec-8115-69808cce9c51",
    //   "event_id": "2379cba1-c051-4308-bff4-fd456c464fee",
    //   "token_use": "access",
    //   "scope": "openid profile email",
    //   "auth_time": 1606507750,
    //   "iss": "https://cognito-idp.us-east-1.amazonaws.com/us-east-1_89k06lCSA",
    //   "exp": 1606511350,
    //   "iat": 1606507750,
    //   "version": 2,
    //   "jti": "f98e0d1c-42b0-4c42-88b4-9ef9ab9fbaba",
    //   "client_id": "7p1g2ho5eslm2vea7jf8o8f2ao",
    //   "username": "laimaB"
    // }

    async redirectToSignIn(config: ICognitoConfig): Promise<void> {
        const url = `https://${config.cognito_domain}.auth.${config.region}.amazoncognito.com/login?response_type=${config.cognito_response_type}&client_id=${config.cognito_client_id}&redirect_uri=${config.cognito_redirect_url}`;
        console.log(url);
        if (!process.env.REGION) {
            await Router.push('/index');
        }
        window.location.href = url;
    }
}