import boto3
import botocore.session

session = boto3.session.Session(profile_name='power-user')
dynamodb = session.resource('dynamodb' )
table = dynamodb.Table('visual-schedules-data-table')
print(table.creation_date_time)

with table.batch_writer() as batch:
    batch.put_item(
        Item={
            'pk':  "VIRTUAL_SCHEDULE|2020|Kiera",
            'sk':  "SETTINGS",
            'num_weeks':  2,
            }
    ) 
    batch.put_item(
        Item={
            'pk':  "VIRTUAL_SCHEDULE|2020|Kiera",
            'sk':  "WEEK1|Monday",
            'sync':  ["Math", "Social Studies", "World Language", "Fine Arts"],
            'async': ["English", "Science", "Elective", "PE"]
            }
    )  
    batch.put_item(
        Item={
            'pk':  "VIRTUAL_SCHEDULE|2020|Kiera",
            'sk':  "WEEK1|Tuesday",
            'sync': ["English", "Science", "Elective", "External Lessons"],
            'async': ["Math", "Social Studies", "World Language", "Fine Arts", "PE"]
            }
    ) 
    batch.put_item(
        Item={
            'pk':  "VIRTUAL_SCHEDULE|2020|Kiera",
            'sk':  "WEEK1|Wednesday",
            'sync': ["Math", "Social Studies", "World Language", "Fine Arts"] ,
            'async': ["English", "Science", "Elective", "PE"]
            }
    ) 
    batch.put_item(
        Item={
            'pk':  "VIRTUAL_SCHEDULE|2020|Kiera",
            'sk':  "WEEK1|Thursday",
            'sync': ["English", "Science", "Elective"],
            'async': ["Math", "Social Studies", "World Language", "Fine Arts", "PE"]
            }
    ) 
    batch.put_item(
        Item={
            'pk':  "VIRTUAL_SCHEDULE|2020|Kiera",
            'sk':  "WEEK1|Friday",
            'sync': ["Math", "Social Studies", "World Language", "Fine Arts"] ,
            'async': ["English", "Science", "Elective", "PE"]
            }
    )                    
    batch.put_item(
        Item={
                'pk':  "VIRTUAL_SCHEDULE|2020|Kiera",
                'sk':  "WEEK2|Monday",
                'async': ["Math", "Social Studies", "World Language", "Fine Arts", "PE"],
                'sync': ["English", "Science", "Elective"]
            }
    )  
    batch.put_item(
        Item={
            'pk':  "VIRTUAL_SCHEDULE|2020|Kiera",
            'sk':  "WEEK2|Tuesday",
            'sync': ["Math", "Social Studies", "World Language", "Fine Arts", "External Lessons"],
            'async': ["English", "Science", "Elective", "PE"]
            }
    ) 
    batch.put_item(
        Item={
            'pk':  "VIRTUAL_SCHEDULE|2020|Kiera",
            'sk':  "WEEK2|Wednesday",
            'async': ["Math", "Social Studies", "World Language", "Fine Arts", "PE"],
            'sync': ["English", "Science", "Elective"]
            }
    ) 
    batch.put_item(
        Item={
            'pk':  "VIRTUAL_SCHEDULE|2020|Kiera",
            'sk':  "WEEK2|Thursday",
            'sync': ["Math", "Social Studies", "World Language", "Fine Arts"],
            'async': ["English", "Science", "Elective", "PE"]
            }
    ) 
    batch.put_item(
        Item={
            'pk':  "VIRTUAL_SCHEDULE|2020|Kiera",
            'sk':  "WEEK2|Friday",
            'async': ["Math", "Social Studies", "World Language", "Fine Arts", "PE"],
            'sync': ["English", "Science", "Elective"]
            }
    )   
    batch.put_item(
        Item={
            'pk':  "VIRTUAL_SCHEDULE|2020|Delia",
            'sk':  "WEEK1|Monday",
            'sync':  ["Quest", "OTPT-Speech"],
            'async': ["PE","Calendar"]
            }
    )  
    batch.put_item(
        Item={
            'pk':  "VIRTUAL_SCHEDULE|2020|Delia",
            'sk':  "WEEK1|Tuesday",
            'sync':  ["Quest", "OTPT-Speech"],
            'async': ["PE","Calendar"]
            }
    ) 
    batch.put_item(
        Item={
            'pk':  "VIRTUAL_SCHEDULE|2020|Delia",
            'sk':  "WEEK1|Wednesday",
            'sync':  ["Quest", "OTPT-Speech"],
            'async': ["PE","Calendar"]
            }
    ) 
    batch.put_item(
        Item={
            'pk':  "VIRTUAL_SCHEDULE|2020|Delia",
            'sk':  "WEEK1|Thursday",
            'sync':  ["Quest", "OTPT-Speech"],
            'async': ["PE","Calendar"]
            }
    ) 
    batch.put_item(
        Item={
            'pk':  "VIRTUAL_SCHEDULE|2020|Delia",
            'sk':  "WEEK1|Friday",
            'sync':  ["Quest", "OTPT-Speech"],
            'async': ["PE","Calendar"]
            }
    )                    
    batch.put_item(
        Item={
                'pk':  "VIRTUAL_SCHEDULE|2020|Delia",
                'sk':  "WEEK2|Monday",
            'sync':  ["Quest", "OTPT-Speech"],
            'async': ["PE","Calendar"]
            }
    )  
    batch.put_item(
        Item={
            'pk':  "VIRTUAL_SCHEDULE|2020|Delia",
            'sk':  "WEEK2|Tuesday",
            'sync':  ["Quest", "OTPT-Speech"],
            'async': ["PE","Calendar"]
            }
    ) 
    batch.put_item(
        Item={
            'pk':  "VIRTUAL_SCHEDULE|2020|Delia",
            'sk':  "WEEK2|Wednesday",
            'sync':  ["Quest", "OTPT-Speech"],
            'async': ["PE","Calendar"]
            }
    ) 
    batch.put_item(
        Item={
            'pk':  "VIRTUAL_SCHEDULE|2020|Delia",
            'sk':  "WEEK2|Thursday",
            'sync':  ["Quest", "OTPT-Speech"],
            'async': ["PE","Calendar"]
            }
    ) 
    batch.put_item(
        Item={
            'pk':  "VIRTUAL_SCHEDULE|2020|Delia",
            'sk':  "WEEK2|Friday",
            'sync':  ["Quest", "OTPT-Speech"],
            'async': ["PE","Calendar"]
            }
    )   

