# venv_linux/bin/python src/calendars/config/load_virtuals.py
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
            'num_weeks':  1,
            }
    ) 
    batch.put_item(
        Item={
            'pk':  "VIRTUAL_SCHEDULE|2020|Delia",
            'sk':  "SETTINGS",
            'num_weeks':  1,
            }
    )     
    #   ---------------- KIERA WEEK 1 --------------------
    batch.put_item(
        Item={
            'pk':  "VIRTUAL_SCHEDULE|2020|Kiera",
            'sk':  "WEEK1|Monday",
            'sync':  ["Math", "Social Studies", "English", "Elective"],
            'async': [ "World Language", "Science", "PE", "Fine Arts"]
            }
    )  
    batch.put_item(
        Item={
            'pk':  "VIRTUAL_SCHEDULE|2020|Kiera",
            'sk':  "WEEK1|Tuesday",
            'sync': ["Science",  "Math", "Fine Arts", "World Language"],
            'async': ["English", "Social Studies",  "PE", "Elective"]
            }
    ) 
    batch.put_item(
        Item={
            'pk':  "VIRTUAL_SCHEDULE|2020|Kiera",
            'sk':  "WEEK1|Wednesday",
            'sync': ["Elective", "Social Studies"] ,
            'async': ["Math", "English", "World Language", "Science", "PE", "Fine Arts"]
            }
    ) 
    batch.put_item(
        Item={
            'pk':  "VIRTUAL_SCHEDULE|2020|Kiera",
            'sk':  "WEEK1|Thursday",
            'sync': [ "Science", "Fine Arts", "Math", "Social Studies", "World Language"],
            'async': ["English", "PE", "Elective"]
            }
    ) 
    batch.put_item(
        Item={
            'pk':  "VIRTUAL_SCHEDULE|2020|Kiera",
            'sk':  "WEEK1|Friday",
            'sync': ["English"] ,
            'async': [ "Science", "Elective", "Math", "Social Studies", "Elective", "PE", "Fine Arts", "World Language"]
            }
    )   
    #   ---------------- KIERA WEEK 2 --------------------
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
    #   ---------------- DELIA WEEK 1 --------------------
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
    #   ---------------- DELIA WEEK 2 --------------------
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

