import { ILoginData } from '../ILoginData';
import { LoginModel } from "../LoginModel";
import { DynamoDbItemBuidler } from "./DynamoDbItemBuilder";

export class LoginModelBuilder extends DynamoDbItemBuidler {
    constructor( databaseModel: LoginModel) {
        super();
        this.databaseModel = databaseModel;
    }

    getTableName() {
        return (this.databaseModel as LoginModel).getBaseTable();
    }

    buildDatabaseQuery(Login: string | ILoginData): LoginModel {
        const model = this.copyInjectedModel() as LoginModel;
        if (typeof Login === "string") {
            model.Key = Login;
            return model;
        } else {
            Object.keys(Login).forEach((objectKey) => {
                model[objectKey] = Login[objectKey];
            });
            return model;
        }
    }

    buildReturnValue(result: LoginModel): ILoginData {
        let Login = {} as ILoginData;

        Object.keys(result).forEach((objectKey) => {
            if (!["tableName", "PK", "__BuildContext"].includes(objectKey as string)) {
                if (objectKey === "SK") {
                    Login["Key"] = result[objectKey];
                } else {
                    Login[objectKey] = result[objectKey];
                }
            }
        });
        return Login as ILoginData;
    }
}
