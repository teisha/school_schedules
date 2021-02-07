export interface IVirtualSchedule {
    student: string;
    year: string;
    day: string;       // Monday, Tuesday ...
    num_weeks: string;
    sync_categories: string[];
    async_categories: string[];
}

/*
Item={
    'pk':  "VIRTUAL_SCHEDULE|2020|Kiera",
    'sk':  "SETTINGS",
    'num_weeks':  1,
    }
Item={
    'pk':  "VIRTUAL_SCHEDULE|2020|Kiera",
    'sk':  "WEEK1|Monday",
    'sync':  ["Math", "Social Studies", "English", "Elective"],
    'async': [ "World Language", "Science", "PE", "Fine Arts"]
    }
*/

export interface IDistrictCalendar {
    school: string;
    year: string;
    type: "HOLIDAY" | "TERMS" | "SCHEDULE" | "EARLY_DISMISSAL";
    name?: string;  //
    start: string;
    end?: string;
}


/*
Item={
    'pk':  "SCHOOL|2020|FISD",
    'sk':  "SCHEDULE",
    'start':  "08/31/2020",
    'end':  "05/27/2021"
    }
Item={
    'pk':  "SCHOOL|2020|FISD",
    'sk':  "EARLY_DISMISSAL|2",
    'start':  "05/27/2021"
    }    
Item={
    'pk':  "SCHOOL|2020|FISD",
    'sk':  "HOLIDAY|Labor Day",
    'start':  "09/07/2020"
}
Item={
    'pk':  "SCHOOL|2020|FISD",
    'sk':  "TERMS|Nine Weeks 4",
    'start':  "03/22/2021",
    'end':  "05/27/2021"
}
*/
export interface IClassesInTerm {
    term_name: string;
    class_name: string;
    category_name: string;
}
export interface IDailySchedule {
    student: string;
    year: number;
    period: number;
    start_time: string;
    end_time: string;
    term: IClassesInTerm[];
}

/*
Item={
    'pk':  "KID_SCHEDULE|2020|Kiera",
    'sk':  "PERIOD|1",
    'start':  "08:45",
    'end': "09:35",
    'TERMS|Nine Weeks 1':  {
        "Class": "Pre AP English 2",
        "Category": "English"
    },
    'TERMS|Nine Weeks 2':  {
        "Class": "Pre AP English 2",
        "Category": "English"
    },
    'TERMS|Nine Weeks 3':  {
        "Class": "Pre AP English 2",
        "Category": "English"
    },
    'TERMS|Nine Weeks 4':  {
        "Class": "Pre AP English 2",
        "Category": "English"
    },                                    
}
*/

export interface IFullSchedule {
        district: IDistrictCalendar[];
        virtual: IVirtualSchedule[];
        daily: IDailySchedule[];
}