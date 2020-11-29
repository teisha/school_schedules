export default interface IAuthToken {
    rawtoken: string;
    cognito_username?: string;
    email?: string;
    auth_time?: number;
    expires?: number;
    issued_at?: number;
}


//   "auth_time": 1606507750,
//   "iss": "https://cognito-idp.us-east-1.amazonaws.com/us-east-1_89k06lCSA",
//   "cognito:username": "laimaB",
//   "exp": 1606511350,
//   "iat": 1606507750,
//   "email": "ahsiet4@yahoo.com"


// export type DecodedToken = {
//   readonly email: string;
//   readonly exp: number;
// }


//   get authorizationString() {
//       return `Bearer ${this.token}`;
//   }

//   get expiresAt(): Date {
//       return new Date(this.decodedToken.exp * 1000);
//   }

//   get isExpired(): boolean {
//       return new Date() > this.expiresAt;
//   }

//   get isValid(): boolean {
//       return !this.isExpired;
//   }


// }