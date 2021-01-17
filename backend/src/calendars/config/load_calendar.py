import boto3
import botocore.session

session = boto3.session.Session(profile_name='power-user')
dynamodb = session.resource('dynamodb' )
table = dynamodb.Table('dev-visual-schedules-data-table')
print(table.creation_date_time)

with table.batch_writer() as batch:
    batch.put_item(
    Item={
        'pk':  "SCHOOL|2020|FISD",
        'sk':  "SCHEDULE",
        'start':  "08/31/2020",
        'end':  "05/27/2021"
        }
    )    
    batch.put_item(
    Item={
        'pk':  "SCHOOL|2020|FISD",
        'sk':  "EARLY_DISMISSAL|1",
        'start':  "12/18/2020"
        }
    )
    batch.put_item(
    Item={
        'pk':  "SCHOOL|2020|FISD",
        'sk':  "EARLY_DISMISSAL|2",
        'start':  "05/27/2021"
        }
    )   
    batch.put_item(
        Item={
            'pk':  "SCHOOL|2020|FISD",
            'sk':  "HOLIDAY|Labor Day",
            'start':  "09/07/2020"
        }
    )
    batch.put_item(
        Item={
            'pk':  "SCHOOL|2020|FISD",
            'sk':  "HOLIDAY|Teacher Professional Day 1",
            'start':  "10/12/2020"
        }
    )
    batch.put_item(
        Item={
            'pk':  "SCHOOL|2020|FISD",
            'sk':  "HOLIDAY|Thanksgiving Break Day 1",
            'start':  "11/23/2020"
        }
    )
    batch.put_item(
        Item={
            'pk':  "SCHOOL|2020|FISD",
            'sk':  "HOLIDAY|Thanksgiving Break Day 2",
            'start':  "11/24/2020"
        }
    )   
    batch.put_item(
        Item={
            'pk':  "SCHOOL|2020|FISD",
            'sk':  "HOLIDAY|Thanksgiving Break Day 3",
            'start':  "11/25/2020"
        }
    )  
    batch.put_item(
        Item={
            'pk':  "SCHOOL|2020|FISD",
            'sk':  "HOLIDAY|Thanksgiving Day",
            'start':  "11/26/2020"
        }
    ) 
    batch.put_item(
        Item={
            'pk':  "SCHOOL|2020|FISD",
            'sk':  "HOLIDAY|Thanksgiving Break Day 5",
            'start':  "11/27/2020"
        }
    ) 
    batch.put_item(
        Item={
            'pk':  "SCHOOL|2020|FISD",
            'sk':  "HOLIDAY|Winter Break Day 1",
            'start':  "12/21/2020"
        }
    )    
    batch.put_item(
        Item={
            'pk':  "SCHOOL|2020|FISD",
            'sk':  "HOLIDAY|Winter Break Day 2",
            'start':  "12/22/2020"
        }
    ) 
    batch.put_item(
        Item={
            'pk':  "SCHOOL|2020|FISD",
            'sk':  "HOLIDAY|Winter Break Day 3",
            'start':  "12/23/2020"
        }
    ) 
    batch.put_item(
        Item={
            'pk':  "SCHOOL|2020|FISD",
            'sk':  "HOLIDAY|Winter Break Day 4",
            'start':  "12/24/2020"
        }
    ) 
    batch.put_item(
        Item={
            'pk':  "SCHOOL|2020|FISD",
            'sk':  "HOLIDAY|Winter Break Day 5",
            'start':  "12/25/2020"
        }
    ) 
    batch.put_item(
        Item={
            'pk':  "SCHOOL|2020|FISD",
            'sk':  "HOLIDAY|Winter Break Day 6",
            'start':  "12/28/2020"
        }
    ) 
    batch.put_item(
        Item={
            'pk':  "SCHOOL|2020|FISD",
            'sk':  "HOLIDAY|Winter Break Day 7",
            'start':  "12/29/2020"
        }
    ) 
    batch.put_item(
        Item={
            'pk':  "SCHOOL|2020|FISD",
            'sk':  "HOLIDAY|Winter Break Day 8",
            'start':  "12/30/2020"
        }
    ) 
    batch.put_item(
        Item={
            'pk':  "SCHOOL|2020|FISD",
            'sk':  "HOLIDAY|Winter Break Day 9",
            'start':  "12/31/2020"
        }
    ) 
    batch.put_item(
        Item={
            'pk':  "SCHOOL|2020|FISD",
            'sk':  "HOLIDAY|Winter Break Day 10",
            'start':  "01/01/2021"
        }
    )                                              
    batch.put_item(
        Item={
            'pk':  "SCHOOL|2020|FISD",
            'sk':  "HOLIDAY|Martin Luther King Jr Day",
            'start':  "01/18/2021"
        }
    )    
    batch.put_item(
        Item={
            'pk':  "SCHOOL|2020|FISD",
            'sk':  "HOLIDAY|Teacher Professional Day 2",
            'start':  "02/15/2021"
        }
    )    
    batch.put_item(
        Item={
            'pk':  "SCHOOL|2020|FISD",
            'sk':  "HOLIDAY|Spring Break Day 1",
            'start':  "03/15/2021"
        }
    ) 
    batch.put_item(
        Item={
            'pk':  "SCHOOL|2020|FISD",
            'sk':  "HOLIDAY|Spring Break Day 2",
            'start':  "03/16/2021"
        }
    )  
    batch.put_item(
        Item={
            'pk':  "SCHOOL|2020|FISD",
            'sk':  "HOLIDAY|Spring Break Day 3",
            'start':  "03/17/2021"
        }
    )  
    batch.put_item(
        Item={
            'pk':  "SCHOOL|2020|FISD",
            'sk':  "HOLIDAY|Spring Break Day 4",
            'start':  "03/18/2021"
        }
    )  
    batch.put_item(
        Item={
            'pk':  "SCHOOL|2020|FISD",
            'sk':  "HOLIDAY|Spring Break Day 5",
            'start':  "03/19/2021"
        }
    )   
    batch.put_item(
        Item={
            'pk':  "SCHOOL|2020|FISD",
            'sk':  "HOLIDAY|Good Friday",
            'start':  "04/02/2021"
        }
    )                                
    batch.put_item(
        Item={
            'pk':  "SCHOOL|2020|FISD",
            'sk':  "TERMS|Nine Weeks 1",
            'start':  "08/31/2020",
            'end':  "10/16/2020"
        }
    ) 
    batch.put_item(
        Item={
            'pk':  "SCHOOL|2020|FISD",
            'sk':  "TERMS|Nine Weeks 2",
            'start':  "10/19/2020",
            'end':  "12/18/2020"
        }
    ) 
    batch.put_item(
        Item={
            'pk':  "SCHOOL|2020|FISD",
            'sk':  "TERMS|Nine Weeks 3",
            'start':  "01/04/2021",
            'end':  "03/12/2021"
        }
    ) 
    batch.put_item(
        Item={
            'pk':  "SCHOOL|2020|FISD",
            'sk':  "TERMS|Nine Weeks 4",
            'start':  "03/22/2021",
            'end':  "05/27/2021"
        }
    ) 
                 
