import { IStudent } from './IStudent';

export default interface IUser {
    username: string;
    status: "active" | "deactivated";
    firstname?: string;
    lastname?: string;
    email: string;
    students?: IStudent[];
    date_created?: Date;
}