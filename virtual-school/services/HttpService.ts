import { useContext } from 'react'
import { isContext } from 'vm'
import authContext from "../context/auth-context"
import axios from "../utils/axiosInstance";

class HttpService {
    context = useContext(authContext)

    auth_headers = { "Authorization": "Bearer " + this.context.token.rawtoken }
    

    const get = () => {

    }
}