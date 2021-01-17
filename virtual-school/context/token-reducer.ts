import IAuthToken from '../models/IAuthToken'

export const LOGIN = 'LOGIN'
export const CHECK_EXPIRED = "CHECK_EXPIRED"

const setAuthToken = (token: IAuthToken, state) => {
    const updatedToken = { ...token }
    console.log(`set AuthToken: ${JSON.stringify(updatedToken)}`)
    console.log({...state, token: updatedToken })
    return {...state, token: updatedToken }
}

const logout = (state) => {
    return {...state, token: null }
}

const checkTokenExpired = (state) => {
    const updatedToken: IAuthToken = { ...state.token };
    updatedToken.is_expired = ( Date.now() / 1000) > updatedToken.expires ;
    console.log(`Is this expired?: ${JSON.stringify(updatedToken)} `)
    return {...state, token: updatedToken }
}

export const tokenReducer = (state, action) => {
    switch (action.type) {
    case LOGIN: 
        return setAuthToken(action.token, state);
    case LOGIN: 
        return logout(state);        
    case CHECK_EXPIRED:
        return checkTokenExpired(state);        
    default:
        return state;
    }
}