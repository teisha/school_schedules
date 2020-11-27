import { DynamoDbItem } from "../DynamoDbItem";

export abstract class DynamoDbItemBuidler {
    protected databaseModel: DynamoDbItem;

    copyInjectedModel(): DynamoDbItem {
        return Object.assign(Object.create(Object.getPrototypeOf(this.databaseModel)), this.databaseModel);
    }
}
