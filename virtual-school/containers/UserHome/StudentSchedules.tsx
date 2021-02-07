import React from 'react'
import { Accordion,  Card } from 'react-bootstrap'
import { IVirtualSchedule } from '../../models/ISchedule'
import { IStudent } from '../../models/IStudent'
import { IStudentSchedule } from '../../models/IStudentSchedule'
import Schedule from './Schedule'

interface IProps {
    students: IStudent[];
    studentSchedules: IStudentSchedule[];
    getSchedule(student: IStudent): void;
    updateVirtual(virtualSchedule: IVirtualSchedule, student: IStudent): void;
}

const StudentSchedules = (props: IProps) => {
    

    return (
        <Accordion> 
            {
                props.students.map( student => {
                    const studentSchedule = props.studentSchedules.find(schedule => schedule.studentName === student.studentName)  
                    console.log("Schedule for " + student.studentName, studentSchedule)
                    return (
                        <Card key={student.studentName}>
                            <Accordion.Toggle onClick={() => { if (!studentSchedule) { props.getSchedule(student) } }} 
                                as={Card.Header} 
                                eventKey={student.studentName}>
                                {student.studentName}
                                
                            </Accordion.Toggle>
                            <Accordion.Collapse eventKey={student.studentName}>
                                <Card.Body>
                                    {studentSchedule 
                                    ? <Schedule
                                        fullSchedule={studentSchedule.fullSchedule}
                                        currentTerm={studentSchedule.currentTerm}
                                        currentWeek={studentSchedule.currentWeek} 
                                        updateVirtual={(virtual_schedule: IVirtualSchedule) => props.updateVirtual(virtual_schedule, student)} />
                                    : <p> Looking for schedule. Please wait...</p>
                                    }
                                </Card.Body>
                            </Accordion.Collapse>    
                        </Card>
                    )
                })
            }
        </Accordion>
    )
}

export default StudentSchedules