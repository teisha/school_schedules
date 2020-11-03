export interface ILoginData {
    Key: string;
    AllDay: boolean;
    Day: string;
    DayName: string;
    EndTime: string;
    Month: string;
    Observed: boolean;
    Prompt: string;
    Translation: { [lang: string]: string };
    StartTime: string;
    Tax: boolean;
    Year: string;
    FullDate: string;
}
