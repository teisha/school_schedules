from _datetime import datetime



class Questioner:
    def __init__(self):
        self.today = datetime.now()

    def what_is_my_schedule_today(self, student: str) :
        print ('Schedule for ', student)
        



if __name__ == "__main__":
    question = Questioner()
    question.what_is_my_schedule_today("kb")