import json
import requests
import datetime
from app.utils import redis_client
from datetime import timedelta 

class MockApi:

    def prepareData(self):

        try:
            response=[]
            """
                Get data from mock api and store to redis
            """
            mock_api_url = "https://61c6effa9031850017547293.mockapi.io/api/v2/iotmock"
            result = requests.get(mock_api_url)
            data = result.json()
            for i in data:
                data_dict={}
                data_dict['id']=i['id']
                data_dict['latitude']=i['latitude']
                data_dict['longitude']=i['longitude']
                data_dict['longitude']=i['longitude']
                data_dict['datastream']=i['datastream']
                response.append(data_dict)
            updated_time = datetime.datetime.now() + timedelta(hours=1)
            updated_time = updated_time.strftime("%Y-%m-%d %H:%M")
            time_dict={"expire_time":updated_time}
            response.append(time_dict)
        except Exception as e:
            print(str(e))

        redis_client.set("mock_api_data", json.dumps(response))
        return response
