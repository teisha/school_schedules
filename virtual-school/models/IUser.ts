
export default interface IUser {
    username: string;
    status: "active" | "deactivated";
    firstname?: string;
    lastname?: string;
    email: string;
    students?: string[];
    date_created?: Date;
}