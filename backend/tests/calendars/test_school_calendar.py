from calendars import school_calendar



#  python -m pytest -s tests/test_friendswood.py >> printout.txt
class TestClass:
    def test_get_data(self):
        runThis = galvestonCounty.GalvestonCountyRunner()
        runThis.get_friendswood_detail()
        print ('Gathering Friendswood Data')
        print(runThis)
        assert runThis.tableauData != None