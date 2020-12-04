import IAuthToken from '../models/IAuthToken'
import { CognitoService } from "../services/CognitoService"

export const LOGIN = 'LOGIN'
export const CHECK_EXPIRED = "CHECK_EXPIRED"
let cognito;

const setAuthToken = (token: string, state) => {
    const updatedToken: IAuthToken = cognito.parseIdToken(token)
    console.log(`set AuthToken: ${JSON.stringify(updatedToken)}`)
    return {...state, token: updatedToken }
}

const checkTokenExpired = (state) => {
    const updatedToken: IAuthToken = { ...state.token };
    console.log(`Is this expired?: ${JSON.stringify(updatedToken)} `)
    updatedToken.is_expired = ( Date.now() / 1000) > updatedToken.expires ;
    return {...state, token: updatedToken }
}

export const tokenReducer = (state, action) => {
    cognito = new CognitoService()
    switch (action.type) {
    case LOGIN: 
        return setAuthToken(action.token, state);
    case CHECK_EXPIRED:
        return checkTokenExpired(state);        
    default:
        return state;
    }
}