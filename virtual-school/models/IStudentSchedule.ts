import { IFullSchedule } from './ISchedule';
import { IStudent } from './IStudent';

export interface IStudentSchedule {
    studentName: string;
    currentTerm: number;
    currentWeek: number;
    fullSchedule: IFullSchedule;
}