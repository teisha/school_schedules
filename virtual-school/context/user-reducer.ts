import IUser from '../models/IUser';

export const LOGIN = 'LOGIN';

const setUser = (username: string, state) => {
    const updatedUser: IUser = { ...state.user };
    //get user data from token.email
    console.log(`set User: ${updatedUser}`);
    return { ...state, user: updatedUser };
};

export const userReducer = (state, action) => {
    switch (action.type) {
    case LOGIN:
        return setUser(action.token, state);
    default:
        return state;
    }
};
