import React, { useContext } from 'react'
import { Button, Table } from 'react-bootstrap'
import AuthContext from '../../context/auth-context';
import { IClassesInTerm, IDailySchedule, IFullSchedule, IVirtualSchedule } from '../../models/ISchedule'
import SchedulerService from '../../services/SchedulerService';
import styles from './Schedule.module.css';

const ASYNC = 'ASYNC';
const SYNC = 'SYNC';
const INACTIVE = 'INACTIVE';

interface IProps {
    fullSchedule: IFullSchedule;
    currentTerm: number;
    currentWeek: number;
    updateVirtual(virtualSchedule: IVirtualSchedule): void;
}
const Schedule = (props: IProps) => {
    const context = useContext(AuthContext)
    console.log("SCHEDULE: ", props.fullSchedule.daily)

    const updateVirtual = async (virt: IVirtualSchedule, 
            categoryName: string,
            syncronicity: string): Promise<void> => {
        console.log(virt)
        if (syncronicity === ASYNC ) {
            console.log(`Change ${categoryName} from ${syncronicity} to SYNC`)
            const catIndex = virt.async_categories.indexOf(categoryName)
            if (catIndex > -1) {
                virt.async_categories.splice(catIndex, 1)
                virt.sync_categories.push(categoryName)
            }
        } else {
            console.log(`Change ${categoryName} from ${syncronicity} to ASYNC`)
            const catIndex = virt.sync_categories.indexOf(categoryName)
            if (catIndex > -1 ) {

                virt.sync_categories.splice(catIndex, 1)
                virt.async_categories.push(categoryName)            
            }
        }
        await props.updateVirtual(virt);
    }

    const getSyncronicity = (category_name : string, virtual: IVirtualSchedule): string => {
        if (virtual.async_categories.includes(category_name)) {
            return ASYNC
        } else if (virtual.sync_categories.includes(category_name)) {
            return SYNC
        } else {
            return INACTIVE
        }
    }

    const getButtonType = (syncronicity: string) => {
        switch (syncronicity) {
            case SYNC:
                return "success";
                break;
            case ASYNC:
                return "primary";
                break;
            default:
                return "dark";
        }
    }

    const returnClassInfo = (termRec: IClassesInTerm, 
        virtualSchedule: IVirtualSchedule) => {
            const syncronicity = getSyncronicity(termRec.category_name, virtualSchedule)

        return (
        <td>        
            <span className={styles.class}>{termRec.class_name}</span> <br />
            <Button variant={getButtonType(syncronicity)}
                onClick={() => {updateVirtual(virtualSchedule, termRec.category_name, syncronicity) }}
            > { syncronicity }
            </Button>
        </td>
        )

    }

    return (
        <>
            <Table striped size="sm">
                <thead>
                    <tr key={"0"}>
                        <th>Times</th>
                        <th>Monday</th>
                        <th>Tuesday</th>
                        <th>Wednesday</th>
                        <th>Thursday</th>
                        <th>Friday</th>
                    </tr>
                </thead>
                <tbody >
                    { props.fullSchedule.daily
                        .filter(daily => daily.term.some(period_class => {
                            // console.log("Schedule in term: " + props.currentTerm, period_class)
                            // console.log(parseInt(period_class.term_name) === props.currentTerm )
                            return parseInt(period_class.term_name) === props.currentTerm 
                        }))
                        .sort(( a, b ) => {
                            // console.log(a)
                            return a.period - b.period
                        })
                        .map( daily => {
                            const term = daily.term.find(term => parseInt(term.term_name) === props.currentTerm)
                            const virtuals = props.fullSchedule.virtual.filter(
                                virtual_sched => parseInt(virtual_sched.num_weeks) === props.currentWeek 
                            );
                            // console.log(term)
                            return (
                            <tr key={daily.period}>
                                <td>
                                    <p  className={styles.metadata}>
                                    <span className={styles.label}>Period: </span>
                                        <span className={styles.data}>{daily.period}</span> <br />
                                    <span className={styles.label}>Start: </span>
                                        <span className={styles.data}>{daily.start_time}</span><br />
                                    <span className={styles.label}>End: </span>
                                        <span className={styles.data}>{daily.end_time}</span></p>
                                </td>
                                { returnClassInfo (term,  virtuals.find(schedule => schedule.day === "Monday" )) }
                                { returnClassInfo (term,  virtuals.find(schedule => schedule.day === "Tuesday" )) }
                                { returnClassInfo (term,  virtuals.find(schedule => schedule.day === "Wednesday" )) }
                                { returnClassInfo (term,  virtuals.find(schedule => schedule.day === "Thursday" )) }
                                { returnClassInfo (term,  virtuals.find(schedule => schedule.day === "Friday" )) }
                            </tr>
                            )
                    })}
                </tbody>
            </Table>
        </>
    )
}
export default Schedule