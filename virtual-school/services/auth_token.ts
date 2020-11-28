import * as _ from 'lodash' 
import jwtDecode from 'jwt-decode';



export type DecodedToken = {
  readonly email: string;
  readonly exp: number;
}

export class AuthToken {
  readonly decodedToken: DecodedToken;

  constructor(readonly token?: string) {
      // we are going to default to an expired decodedToken
      this.decodedToken = { email: '', exp: 0 };

      // then try and decode the jwt using jwt-decode
      try {
          if  (token) {
              const authResponse = _.fromPairs(
                  _.map(token.split('&'), param => {
                      return param.split('=');
                  })
              );
              this.decodedToken = jwtDecode(authResponse);
          }
      } catch (e) {
      }
  }

  get authorizationString() {
      return `Bearer ${this.token}`;
  }

  get expiresAt(): Date {
      return new Date(this.decodedToken.exp * 1000);
  }

  get isExpired(): boolean {
      return new Date() > this.expiresAt;
  }

  get isValid(): boolean {
      return !this.isExpired;
  }


}