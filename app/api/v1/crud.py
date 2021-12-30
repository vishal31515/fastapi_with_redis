import json, datetime
from app.controller.mock_api import MockApi
from app.utils import redis_client


def final_data():
    
    """
        This method is for get final response from redis.
    """
    mock_api_data = None
    redis_response = redis_client.get("mock_api_data")
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    current_time = datetime.datetime.strptime(current_time, "%Y-%m-%d %H:%M")
    if redis_response:
        redis_response = json.loads(redis_response)
        expire_time = redis_response[-1]['expire_time']
        expire_time = datetime.datetime.strptime(expire_time, "%Y-%m-%d %H:%M")
        if current_time < expire_time:
            mock_api_data = redis_response
        else:
            mock_instance = MockApi()
            mock_api_data = mock_instance.prepareData()

    if mock_api_data is None:
        mock_instance = MockApi()
        mock_api_data = mock_instance.prepareData()

    return mock_api_data
