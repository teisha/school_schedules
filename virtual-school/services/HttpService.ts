import Router from 'next/router';
import { useContext } from 'react'
import authContext from "../context/auth-context"
import axiosInstance from '../utils/axiosInstance';

interface IGetParams {
    url: string;
    objectName: string;
}

class HttpService {
    context = useContext(authContext)
    
    
    async get (params: IGetParams): Promise<any> {
        const app_user = this.context.user ? this.context.user.username : "anonymous"
        console.log("GET: " + JSON.stringify(params) )
        try {
            const response = await axiosInstance.get( params.url , {
                withCredentials: true,
                headers: { "Authorization": "Bearer " + this.context.token.rawtoken }
            })
            return response.data
        } catch (error) {
            console.error(`Failed to retrieve ${params.objectName} for ${app_user}`)
            console.error(error.message)
            console.error(JSON.stringify(error))
            if (error.response && error.response.status === 401) {
                    Router.push('/login?redirected=true')
            }
            return Promise.reject(new Error(error.response || error.message))
        }
    }

    async post (url: string, queryData: any) {
        const app_user = this.context.user ? this.context.user.username : "anonymous"
        console.log("POST: " + url);
        try {
            const response = await axiosInstance.post(url, {
                data: queryData,
                responseType: JSON,
                withCredentials: true
            }, {
                headers: { "Authorization": "Bearer " + this.context.token.rawtoken }
            })

            return response.data
        } catch (error) {
            console.error(`Failed to save ${JSON.stringify(queryData)} at ${url} for ${app_user}`)
            console.error(JSON.stringify(error))
            if (error.response && error.response.status === 401) {
                    Router.push('/login?redirected=true')
            }
            return Promise.reject(new Error(error.response || error.message))
        }
    }
}

export default HttpService