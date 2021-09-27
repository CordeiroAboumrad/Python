import requests
from datetime import datetime, timedelta
import os

USERNAME = os.environ.get(USERNAME)
TOKEN = os.environ.get(TOKEN)
GRAPHID = os.environ.get(GRAPHID)

profile_page = 'https://pixe.la/@jeanpierre'
pixel_adding_endpoint = os.environ.get(ADDING_ENDPOINT)
pixel_adding_headers = {
    'X-USER-TOKEN': TOKEN
}

yesterday = datetime.now() - timedelta(days=1)
yesterday = yesterday.strftime("%Y%m%d")

pixel_adding_body = {
    'date': yesterday,
    'quantity': '1'
}


update_pixel_endpoint = f'https://pixe.la/v1/users/jeanpierre/graphs/jp001/{yesterday}'
update_pixel_header = {
    'X-USER-TOKEN': TOKEN
}
update_pixel_body = {
    'quantity': '2'
}


lastYear = '20200630'

delete_pixel_endpoint = f'https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPHID}/{lastYear}'
delete_pixel_header = {
    'X-USER-TOKEN': TOKEN
}

response = requests.delete(url=delete_pixel_endpoint, headers=delete_pixel_header)
print(response.text)
