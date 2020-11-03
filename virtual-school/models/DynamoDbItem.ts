import { DynamoDbTable } from "@aws/dynamodb-data-mapper";
import { hashKey } from '@aws/dynamodb-data-mapper-annotations/build/hashKey';
import { rangeKey } from '@aws/dynamodb-data-mapper-annotations/build/rangeKey';

export class DynamoDbItem {
    protected tableName: string;
    constructor(tablename: string) {
        this.tableName = tablename;
    }

    get [DynamoDbTable]() {
        return this.tableName;
    }

    @hashKey()
    PK: string; // as defined in serverless.yml
    @rangeKey()
    SK: string; //as defined in serverless.yml
}
