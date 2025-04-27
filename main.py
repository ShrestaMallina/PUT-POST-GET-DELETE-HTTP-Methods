import requests
from datetime import datetime
USER_NAME ="shresta123"
TOKEN = "shreresta1234"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
      "token": USER_NAME,
      "username": TOKEN,
      "agreeTermsOfService":"yes",
      "notMinor":"yes",
}
# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id":GRAPH_ID,
    "name":"Cycling Graph",
    "unit":"km",
    "type":"float",
    "color":"ajisai",
}
headers = {
    "X-USER-TOKEN":TOKEN,
}
# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)
pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

today = datetime.now()
THIS_DAY  = today.strftime("%Y%m%d")
pixel_config = {
     "date":THIS_DAY,
    "quantity":"10.5",
}

# response = requests.post(url=pixel_endpoint,json=pixel_config,headers=headers)
# print(response.text)
update_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{THIS_DAY}"

update_config ={
    "quantity":"20",
}
delete_endpoint =f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{THIS_DAY}"
response = requests.put(url=update_pixel_endpoint,json=update_config,headers=headers)
print(response.text)



