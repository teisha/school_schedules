import IAuthToken from '../models/IAuthToken'

export const LOGIN = 'LOGIN'

const setAuthToken = (token: string, state) => {
    const updatedToken: IAuthToken = {rawtoken: token}
    console.log(`set AuthToken: ${updatedToken}`)
    return {...state, token: updatedToken }
}


export const tokenReducer = (state, action) => {
    switch (action.type) {
    case LOGIN: 
        return setAuthToken(action.token, state);
    default:
        return state;
    }
}