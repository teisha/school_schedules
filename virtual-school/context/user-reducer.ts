import IUser from '../models/IUser';
import HttpService from '../services/HttpService';

export const LOGIN = 'LOGIN';

const setUser = async (username: string, state) => {
    let updatedUser: IUser = { ...state.user };
    const httpService = new HttpService();

    const params = {
        url:  `users/${username}`,
        objectName: `pk='USER',sk='${username}'`
    }
    try {
        const user_data = await httpService.get(params)
        //get user data from token.email
        updatedUser = { 
            username: user_data.sk,
            email: user_data.start ,
            firstname: user_data.firstname,
            lastname: user_data.lastname,
            status: user_data.status,
            students: [],
            date_created: new Date(user_data.date_created)  
        }
    } catch (error) {
        console.error(`Could not retrieve user data for ${username}`)
        console.error(error.message)
    }

    console.log(`set User: ${JSON.stringify(updatedUser) }`);
    return { ...state, user: updatedUser };
};

export const userReducer = (state, action) => {
    switch (action.type) {
    case LOGIN:
        return setUser(action.username, state);
    default:
        return state;
    }
};
