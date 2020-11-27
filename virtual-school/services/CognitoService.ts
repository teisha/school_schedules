
import Router from "next/router"
import Cookie from "js-cookie"
import { AuthToken } from './auth_token';
import {Decode} from "jwt-simple"
import ICognitoConfig from '../models/ICognitoConfig'


export const COOKIES = {
  authToken: "myApp.authToken"
};

export class CognitoService {
  constructor() {
  }

  isUserSignedIn() {
    return sessionStorage.getItem('cognito_token') && sessionStorage.getItem('cognito_token').length > 0;
  }

  getAuthToken() {
    return sessionStorage.getItem('cognito_token');
  }

  setAuthToken(token: string) {
    sessionStorage.setItem('cognito_token', token);
    Cookie.set(COOKIES.authToken, token);
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
  parseIdToken(token: string) {

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

  async redirectToSignIn(config: ICognitoConfig) {
    const url = `https://${
      config.cognito_domain
      }.auth.${config.region}.amazoncognito.com/login?response_type=${
      config.cognito_response_type
      }&client_id=${config.cognito_client_id}&redirect_uri=${
      config.cognito_redirect_url
      }`
    console.log(url)      
    if (!process.env.REGION) {
      await Router.push("/index");      
    }
    window.location.href = url;
  }

  async getTokenFromResponse(query_params: string) {
    
    const token: AuthToken = new AuthToken(query_params);


    await Router.push("/index");
  }

}