import { embed } from "@aws/dynamodb-data-mapper";
import { attribute } from "@aws/dynamodb-data-mapper-annotations";
import { DynamoDbItem } from "./DynamoDbItem";

class Translation {
    [language: string]: string;
}

export class LoginModel extends DynamoDbItem {
    constructor() {
        super(process.env.DYNAMODB);
        this.PK = LoginModel.pkString;
    }
    static pkString: string = "USER";

    public getBaseTable(): string {
        return this.tableName;
    }

    get Key(): string {
        return this.SK;
    }

    set Key(value: string) {
        this.SK = value;
    }

    @attribute()
    AllDay: boolean;
    @attribute()
    Day: string;
    @attribute()
    DayName: string;
    @attribute()
    StartTime: string;
    @attribute()
    EndTime: string;
    @attribute()
    Month: string;
    @attribute()
    Observed: boolean;
    @attribute()
    Prompt: string;
    @attribute({ memberType: embed(Translation) })
    Translation: Translation;
    @attribute()
    Tax: boolean;
    @attribute()
    Year: string;
    @attribute()
    FullDate: string;
}
