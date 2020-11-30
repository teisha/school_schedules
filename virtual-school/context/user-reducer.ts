import IUser from '../models/IUser';

export const LOGIN = 'LOGIN';

const setUser = (username: string, email: string, state) => {
    let updatedUser: IUser = { ...state.user };
    
    //get user data from token.email
    updatedUser = { 
        username: username,
        email: email 
    }

    console.log(`set User: ${JSON.stringify(updatedUser) }`);
    return { ...state, user: updatedUser };
};

export const userReducer = (state, action) => {
    switch (action.type) {
    case LOGIN:
        return setUser(action.username, action.email, state);
    default:
        return state;
    }
};
