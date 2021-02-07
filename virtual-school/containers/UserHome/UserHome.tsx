import React, { useState, useContext, useEffect } from 'react'
import { Button, Card } from 'react-bootstrap'
import AuthContext from '../../context/auth-context'
import withAuth from '../../hoc/withAuth'
import IUser from '../../models/IUser'
import { IStudent } from '../../models/IStudent'
import SchedulerService from '../../services/SchedulerService'
import StudentSchedules from './StudentSchedules'
import { IStudentSchedule } from '../../models/IStudentSchedule'
import { IDistrictCalendar, IVirtualSchedule } from '../../models/ISchedule'
import { convertDbStringToDate } from '../../utils/stringUtils'

const UserHome = (props) => {
    const [user, setUser] = useState<IUser | null>(null)
    const [studentSchedules, setStudentSchedules] = useState<IStudentSchedule[]>([])
    const context = useContext(AuthContext) 


    useEffect( () => {
        console.log(`IsLoggedIn: ${props.isLoggedIn ? 'Y' : 'N'}`)
        console.log(`PROPS PASSED: ${JSON.stringify(props.user)}`)
        setUser(context.user)
        console.log(context)
        console.log('Home page for ' + context.user?.username)
    }, [])

    const getYear = () => {
        const today = new Date();
        if ( today.getMonth() < 6 ) {
            return today.getFullYear() - 1;
        }
        return today.getFullYear();

    }

    const getCurrentTerm = (district: IDistrictCalendar[]): number => {
        const today = new Date();
        let term = 1
        const schedule_record = district
                .filter( schedule => schedule.type === 'TERMS')
                .filter( schedule => {
                    return convertDbStringToDate(schedule.start) <= today && 
                    convertDbStringToDate(schedule.end) >= today   
                })
        console.log(schedule_record)
        return parseInt(schedule_record[0].name.replace('Nine Weeks ', '')) ||  term;
    }
    const getWeek = (date: Date): number => {
      //define a date object variable with date inside it  
      //find the year of the entered date  
       const oneJan =  new Date(date.getFullYear(), 0, 1);   
       const dateDiffInTime = date.getTime() - oneJan.getTime() 
       // calculating number of days in given year before the given date   
       const numberOfDays =  Math.floor(dateDiffInTime / (24 * 60 * 60 * 1000));   
       console.log(`Days between ${date} and ${oneJan} is ${numberOfDays}`) 
       // adding 1 since to current date and returns value starting from 0   
       const result = Math.ceil(( date.getDay() + 1 + numberOfDays) / 7);     

       return result
    }

    const getCurrentWeek = (district: IDistrictCalendar[], 
            virtual: IVirtualSchedule[]): number => {
        const district_settings = district.find(calendar => calendar.type ==="SCHEDULE") 
        const virtual_settings = virtual.find(calendar => calendar.day ==="SETTINGS") 
        const today = new Date();
        let weekNum = getWeek(today);
        // find the date the school year starts => 
        // get current week number in year
        // get setting num_weeks        
        const startDate = new Date(district_settings.start)
        const start_week = getWeek(startDate)
        let num_weeks = parseInt(virtual_settings.num_weeks )

        // if the year in the current date is greater than the school start date year
            //   add 53 to the current week number
        if (today.getFullYear() > startDate.getFullYear()) {
            weekNum = weekNum + 53
        }
        // remove holiday weeks (Thanksgiving, Christmas, New Years, Spring Break)
        let skipped =0;
        if (weekNum < 53) {
            if ( today > new Date(`12/25/${today.getFullYear()}`)) {
                skipped = 2;
            } else if (today > new Date(`12/25/${today.getFullYear()}`) ) {
                skipped = 1;
            } 
        } else {
            if ( today > new Date(`03/15/${today.getFullYear()}`)) {
                skipped = 4;
            } else if (today > new Date(`01/01/${today.getFullYear()}`) ) {
                skipped = 3;
            } 
        }
        weekNum = weekNum - skipped;

        //return (week - school start date weeknum) modulo num_weeks  + 1?
        return (weekNum - start_week ) % num_weeks + 1;
    }

    const getSchedule = async (student: IStudent) => {
        const year = getYear()
        const service = new SchedulerService();
        try {
            const schedule = await service.getFullSchedule(student.district, 
                    student.studentName, 
                    "" + year,
                    context.token.rawtoken,
                    context.user.username
                    )
            const currentTerm  = getCurrentTerm(schedule.district)
            const currentWeek = getCurrentWeek(schedule.district, schedule.virtual);
            setStudentSchedules(currentStudentSchedules => {
                return [...currentStudentSchedules].concat([{studentName: student.studentName,
                                                            currentTerm: currentTerm,
                                                            currentWeek: currentWeek,
                                                            fullSchedule: schedule }])
            })                    
        } catch (error) {
            console.error("Could not retrieve schedule for " + student.studentName);
            console.log(error.message)
        }
    }

    const updateVirtual = async (virt: IVirtualSchedule, student: IStudent) => {
        console.log("UPDATE TO: ", virt)
        const service = new SchedulerService();
        const updated =  await service.updateVirtualSchedule(virt, context.token.rawtoken, context.user.username)
        console.log(updated)

        // update the state
        await getSchedule(student);
    }

    return (
        <>
            <p>{context.isLoggedIn 
                ? <Button variant="success" size="sm">Welcome {user?.firstname}</Button> 
                : <Button variant="danger" size="sm">Please Log In </Button> 
            }</p>
            { props.isLoggedIn
            ? <>
                <Card>
                    <Card.Title> 
                        Student Schedules
                    </Card.Title>
                    <Card.Body>
                        <ul>
                            { user?.students 
                                ?  <StudentSchedules
                                        students={user.students}
                                        studentSchedules={studentSchedules}
                                        getSchedule={getSchedule}
                                        updateVirtual={updateVirtual}
                                         />
                                : <p> Sign up students to view a schedule. </p>
                            }
                        </ul>
                    </Card.Body>
                </Card>
            </>
            : <>
                <h1> Wait for it ...</h1>
                <span> {JSON.stringify(context)} </span>
            </>
            }
        </>
    )


}

export default withAuth(UserHome);