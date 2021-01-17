import boto3
import botocore.session

session = boto3.session.Session(profile_name='power-user')
dynamodb = session.resource('dynamodb' )
table = dynamodb.Table('dev-visual-schedules-data-table')
print(table.creation_date_time)

with table.batch_writer() as batch:
    batch.put_item(
        Item={
            'pk':  "KID_SCHEDULE|2020|Kiera",
            'sk':  "PERIOD|1",
            'start':  "08:45",
            'end': "09:35",
            'TERMS|Nine Weeks 1':  {
                "Class": "Pre AP English 2",
                "Category": "English"
            },
            'TERMS|Nine Weeks 2':  {
                "Class": "Pre AP English 2",
                "Category": "English"
            },
            'TERMS|Nine Weeks 3':  {
                "Class": "Pre AP English 2",
                "Category": "English"
            },
            'TERMS|Nine Weeks 4':  {
                "Class": "Pre AP English 2",
                "Category": "English"
            },                                    
        }
    )
    batch.put_item(
        Item={
            'pk':  "KID_SCHEDULE|2020|Kiera",
            'sk':  "PERIOD|2",
            'start':  "9:42",
            'end': "10:32",
            'TERMS|Nine Weeks 1':  {
                "Class": "AP World History",
                "Category": "Social Studies"
            },
            'TERMS|Nine Weeks 2':  {
                "Class": "AP World History",
                "Category": "Social Studies"
            },
            'TERMS|Nine Weeks 3':  {
                "Class": "AP World History",
                "Category": "Social Studies"
            },
            'TERMS|Nine Weeks 4':  {
                "Class": "AP World History",
                "Category": "Social Studies"
            }
        }
    )    
    batch.put_item(
        Item={
            'pk':  "KID_SCHEDULE|2020|Kiera",
            'sk':  "PERIOD|3",
            'start': "10:39",
            'end': "11:32",
            'TERMS|Nine Weeks 1':  {
                "Class": "Chemistry",
                "Category": "Science"
            },
            'TERMS|Nine Weeks 2':  {
                "Class": "Chemistry",
                "Category": "Science"
            },
            'TERMS|Nine Weeks 3':  {
                "Class": "Chemistry",
                "Category": "Science"
            },
            'TERMS|Nine Weeks 4':  {
                "Class": "Chemistry",
                "Category": "Science"
            }
        }
    )   
    batch.put_item(
        Item={
            'pk':  "KID_SCHEDULE|2020|Kiera",
            'sk':  "PERIOD|4",
            'start': "12:09",
            'end': "12:59",
            'TERMS|Nine Weeks 1':  {
                "Class": "Small Animal Management",
                "Category": "Elective"
            },
            'TERMS|Nine Weeks 2':  {
                "Class": "Small Animal Management",
                "Category": "Elective"
            },
            'TERMS|Nine Weeks 3':  {
                "Class": "Equine Science",
                "Category": "Elective"
            },
            'TERMS|Nine Weeks 4':  {
                "Class": "Equine Science",
                "Category": "Elective"
            }
        }
    )   
    batch.put_item(
        Item={
            'pk':  "KID_SCHEDULE|2020|Kiera",
            'sk':  "PERIOD|5",
            'start':  "13:06",
            'end': "13:56",
            'TERMS|Nine Weeks 1':  {
                "Class": "French 2",
                "Category": "World Language"
            },
            'TERMS|Nine Weeks 2':  {
                "Class": "French 2",
                "Category": "World Language"
            },
            'TERMS|Nine Weeks 3':  {
                "Class": "French 2",
                "Category": "World Language"
            },
            'TERMS|Nine Weeks 4':  {
                "Class": "French 2",
                "Category": "World Language"
            }
        }
    ) 
    batch.put_item(
        Item={
            'pk':  "KID_SCHEDULE|2020|Kiera",
            'sk':  "PERIOD|6",
            'start': "14:03",
            'end': "14:54",
            'TERMS|Nine Weeks 1':  {
                "Class": "Concert Band 2",
                "Category": "Fine Arts"
            },
            'TERMS|Nine Weeks 2':  {
                "Class": "Concert Band 2",
                "Category": "Fine Arts"
            },
            'TERMS|Nine Weeks 3':  {
                "Class": "Concert Band 2",
                "Category": "Fine Arts"
            },
            'TERMS|Nine Weeks 4':  {
                "Class": "Concert Band 2",
                "Category": "Fine Arts"
            }
        }
    )  
    batch.put_item(
        Item={
            'pk':  "KID_SCHEDULE|2020|Kiera",
            'sk':  "PERIOD|7",
            'start':  "15:01",
            'end': "15:53",
            'TERMS|Nine Weeks 1':  {
                "Class": "Pre AP Geometry",
                "Category": "Math"
            },
            'TERMS|Nine Weeks 2':  {
                "Class": "Pre AP Geometry",
                "Category": "Math"
            },
            'TERMS|Nine Weeks 3':  {
                "Class": "Pre AP Geometry",
                "Category": "Math"
            },
            'TERMS|Nine Weeks 4':  {
                "Class": "Pre AP Geometry",
                "Category": "Math"
            }
        }
    )  
    batch.put_item(
        Item={
            'pk':  "KID_SCHEDULE|2020|Kiera",
            'sk':  "PERIOD|8",
            'start':  "16:00",
            'end': "17:00",
            'TERMS|Nine Weeks 1':  {
                "Class": "French On Skype",
                "Category": "External Lessons"
            },
            'TERMS|Nine Weeks 2':  {
                "Class": "French On Skype",
                "Category": "External Lessons"
            },
            'TERMS|Nine Weeks 3':  {
                "Class": "French On Skype",
                "Category": "External Lessons"
            },
            'TERMS|Nine Weeks 4':  {
                "Class": "French On Skype",
                "Category": "External Lessons"
            }
        }
    )                            



