import { LoginModelBuilder } from '../../models/builder/LoginModelBuilder';
import { ILoginData } from '../../models/ILoginData';
import { LoginModel } from '../../models/LoginModel';


import { DynamoService } from "../DynamoService";

export class LoginProcessor {
    private mapper: DynamoService;
    private modelBuilder: LoginModelBuilder
    private loginModel: LoginModel;
    constructor() {
        this.mapper = new DynamoService();
        this.loginModel = new LoginModel()
        this.modelBuilder = new LoginModelBuilder(this.loginModel);
    }

    public async put(Login: ILoginData): Promise<LoginModel> {
        const model: LoginModel = this.modelBuilder.buildDatabaseQuery(Login);
        return this.mapper.put(model);
    }

    public async get(Login: string): Promise<LoginModel> {
        const model: LoginModel = this.modelBuilder.buildDatabaseQuery(Login);
        return this.mapper.get(model);
    }
    public async delete(Login: string): Promise<LoginModel> {
        const model: LoginModel = this.modelBuilder.buildDatabaseQuery(Login);
        return this.mapper.delete(model);
    }

    public async getBatch(Logins: string[]): Promise<Array<LoginModel>> {
        const keylist = Logins.map((keyString) => this.modelBuilder.buildDatabaseQuery(keyString));
        return this.mapper.batchGet(keylist);
    }

    public async putBatch(Logins: Array<ILoginData>): Promise<Array<LoginModel>> {
        const itemsToAdd = [];
        Logins.forEach((Login) => {
            itemsToAdd.push(this.modelBuilder.buildDatabaseQuery(Login));
        });
        return this.mapper.batchPut(itemsToAdd);
    }

    public async getAll(): Promise<Array<LoginModel>> {
        const keyOptions = { PK: LoginModel.pkString };
        return this.mapper.query(LoginModel, keyOptions);
    }


}
