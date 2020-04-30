
import unittest
from requests import get, post, delete, put
___author__='Rivka Eisenstein'
localhost = 'http://localhost:5000'

class TestApi(unittest.TestCase):
    def test_Rout(self):
        index = get(localhost)
#check post
    def test_AddMessage_1(self):
         cc=localhost+'/AddMessage'
         create = post(cc, json= {"application_id": 1, "session_id": "dfrgr", "message_id": 'bb', "partipants": "dfdg","contect": "fdfrrgf"})
         assert create.status_code == 201
#check post with message_id that bee in the database
    def test_AddMessage_2(self):
         cc=localhost+'/AddMessage'
         create = post(cc, json= {"application_id": 1, "session_id": "dfrgr", "message_id": 'cc', "partipants": "dfdg","contect": "fdfrrgf"})
         assert create.status_code == 400
#check post with insert application_id type text
    def test_AddMessage_3(self):
        cc = localhost + '/AddMessage'
        create = post(cc, json={"application_id": "gggg", "session_id": "dfrgr", "message_id": 'ggg', "partipants": "dfdg",
                                "contect": "fdfrrgf"})
        assert create.status_code == 400

#check get
    def test_GetMessage_1(self):
       lassie = get(localhost + '/GetMessage?application_id=1').status_code
       assert lassie == 201
#check get with wrong url
    def test_GetMessage_2(self):
          lassie = get(localhost + '/GetMessage?yyyyyyy=rtgreg').status_code
          assert lassie == 400
#check delete
    def test_DeleteMessage_1(self):
        ret = delete(localhost + '/DeleteMessage',data={'application_id':2})
        assert ret.status_code == 200






