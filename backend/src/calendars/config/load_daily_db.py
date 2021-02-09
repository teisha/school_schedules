import boto3
import botocore.session

session = boto3.session.Session(profile_name='power-user')
dynamodb = session.resource('dynamodb' )
table = dynamodb.Table('prod-visual-schedules-data-table')
print(table.creation_date_time)

with table.batch_writer() as batch:
    batch.put_item(
        Item={
            'pk':  "KID_SCHEDULE|2020|Delia",
            'sk':  "PERIOD|1",
            'start': "08:40",
            'end': "09:30"                                   
        }
    )
    batch.put_item(
        Item={
            'pk':  "KID_SCHEDULE|2020|Delia",
            'sk':  "PERIOD|2",
            'start': "9:30",
            'end': "10:16"
        }
    )    
    batch.put_item(
        Item={
            'pk':  "KID_SCHEDULE|2020|Delia",
            'sk':  "PERIOD|3",
            'start': "11:20",
            'end': "12:05"
        }
    )   
    batch.put_item(
        Item={
            'pk':  "KID_SCHEDULE|2020|Delia",
            'sk':  "PERIOD|4",
            'start': "12:05",
            'end': "12:49"
        }
    )   
    batch.put_item(
        Item={
            'pk':  "KID_SCHEDULE|2020|Delia",
            'sk':  "PERIOD|5",
            'start': "12:53",
            'end': "13:38"
        }
    ) 
    batch.put_item(
        Item={
            'pk':  "KID_SCHEDULE|2020|Delia",
            'sk':  "PERIOD|6",
            'start': "13:38",
            'end': "14:22"
        }
    )  
    batch.put_item(
        Item={
            'pk':  "KID_SCHEDULE|2020|Delia",
            'sk':  "PERIOD|7",
            'start': "14:26",
            'end': "15:11"
        }
    )  
    batch.put_item(
        Item={
            'pk':  "KID_SCHEDULE|2020|Delia",
            'sk':  "PERIOD|8",
            'start':  "15:11",
            'end': "15:55"
        }
    )     

    batch.put_item(
        Item={
            'pk':  "KID_SCHEDULE|2020|Delia",
            'sk':  "PERIOD|1-AM",
            'start': "09:00",
            'end': "09:30",
            'TERMS|Nine Weeks 1':  {
                "Class": "Calendar Time",
                "Category": "Calendar"
            },
            'TERMS|Nine Weeks 2':  {
                "Class": "Calendar Time",
                "Category": "Calendar"
            },
            'TERMS|Nine Weeks 3':  {
                "Class": "Calendar Time",
                "Category": "Calendar"
            },
            'TERMS|Nine Weeks 4':  {
                "Class": "Calendar Time",
                "Category": "Calendar"
            }            
        }
    )      
    batch.put_item(
        Item={
            'pk':  "KID_SCHEDULE|2020|Delia",
            'sk':  "PERIOD|2-PM",
            'start': "12:50",
            'end': "15:00",
            'TERMS|Nine Weeks 1':  {
                "Class": "One On One Time",
                "Category": "Quest"
            },
            'TERMS|Nine Weeks 2':  {
                "Class": "One On One Time",
                "Category": "Quest"
            },
            'TERMS|Nine Weeks 3':  {
                "Class": "One On One Time",
                "Category": "Quest"
            },
            'TERMS|Nine Weeks 4':  {
                "Class": "One On One Time",
                "Category": "Quest"
            }   
        }
    )                          
