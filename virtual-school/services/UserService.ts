import IUser from '../models/IUser';
import HttpService from './HttpService'


class UserService {
    httpService: HttpService;
    constructor() {
        this.httpService = new HttpService();
    }

    async getUserData ( username: string, rawtoken: string) : Promise<IUser> {
        const httpService = new HttpService()
        console.log(`GET USERNAME FROM TOKEN: ${username}`)
        const params = {
            url:  `users/${username}`,
            objectName: `pk='USER',sk='${username}'`
        }
        try {
            const user_data = await httpService.get(params, username, rawtoken)
            console.log(`USER DATA FROM USERSERVICE: ${JSON.stringify(user_data)}`)
            return user_data as IUser
            //get user data from token.email
        } catch (error) {
            console.error(`Could not retrieve user data for ${username}`)
            console.error(error.message)
        } 
    }
}


export default UserService