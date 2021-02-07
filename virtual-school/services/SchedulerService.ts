
import { IFullSchedule, IVirtualSchedule } from '../models/ISchedule';
import HttpService from './HttpService'


class SchedulerService {
    httpService: HttpService;
    constructor() {
        this.httpService = new HttpService();
    }

    async getFullSchedule( district: string, kid: string, year: string, 
        rawtoken: string, userLoggedIn: string) : Promise<IFullSchedule> {
        const url = "scheduler"
        const httpService = new HttpService()
        console.log(`GET FULL SCHEDULE FOR:  ${district} ${kid} ${year}`)
        console.log(rawtoken)
        const queryData: any = {
            'kidname': kid,
            'year': year,
            'district': district
        }
        try {
            const schedule_data = await httpService.post (url, queryData, rawtoken, userLoggedIn)
            // console.log(`SCHEDULE DATA: ${JSON.stringify(schedule_data)}`)
            return schedule_data as IFullSchedule
            //get user data from token.email
        } catch (error) {
            console.error(`Could not retrieve schedule data for  ${district} ${kid} ${year}`)
            console.error(error.message)
        } 
    }




    async updateVirtualSchedule( schedule: IVirtualSchedule,  
        rawtoken: string, userLoggedIn: string) : Promise<IVirtualSchedule> {
        const url = "scheduler/virtual"
        const httpService = new HttpService()
        console.log(`UPDATE VIRTUAL SCHEDULE:  ${JSON.stringify(schedule)}`)
        const queryData: any = {
            'schedule': schedule
        }
        try {
            const schedule_data = await httpService.post (url, queryData, rawtoken, userLoggedIn)
            // console.log(`SCHEDULE DATA: ${JSON.stringify(schedule_data)}`)
            return schedule_data as IVirtualSchedule
            //get user data from token.email
        } catch (error) {
            console.error(`Could not save schedule data   ${JSON.stringify(schedule)}`)
            console.error(error.message)
        } 
    }    
}

export default SchedulerService