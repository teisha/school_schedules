import { DataMapper, DeleteOptions, GetOptions, PutOptions } from "@aws/dynamodb-data-mapper";
import { DynamoDbItem } from "../../virtual-school/models/DynamoDbItem";

export class DynamoService {
    private mapper: DataMapper;

    async get<T extends DynamoDbItem>(getObject: T, options?: GetOptions): Promise<T> {
        return this.mapper.get(getObject, options);
    }

    public async batchGet<T extends DynamoDbItem>(keys: Array<T>): Promise<Array<T>> {
        const itemsReturned: Array<T> = [];
        for await (const item of this.mapper.batchGet(keys)) {
            itemsReturned.push(item);
        }
        return Promise.resolve(itemsReturned);
    }

    public async batchPut<T extends DynamoDbItem>(itemsToAdd: Array<T>): Promise<Array<T>> {
        const itemsSaved: Array<T> = [];
        for await (const item of this.mapper.batchPut(itemsToAdd)) {
            itemsSaved.push(item);
        }
        return Promise.resolve(itemsSaved);
    }

    async query<T extends DynamoDbItem>(ctor: new () => T, queryValues: any): Promise<Array<T>> {
        const itemsReturned: Array<T> = [];
        console.log(new ctor());
        for await (const item of this.mapper.query(ctor, queryValues)) {
            itemsReturned.push(item);
        }
        return Promise.resolve(itemsReturned);
    }

    async put<T extends DynamoDbItem>(dbItem: T, options?: PutOptions): Promise<T> {
        return this.mapper.put(dbItem, options);
    }

    async delete<T extends DynamoDbItem>(dbItem: T, options?: DeleteOptions): Promise<T> {
        return this.mapper.delete(dbItem, options);
    }
}
