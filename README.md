## install azure-identity
```s
pip install azure-identity requests
```
### GET 
```py
from azure.identity import DefaultAzureCredential
import requests
import json
subscription_id = "123"
resource_group_name = "rg-aa-dev-01"
base_url = f"https://management.azure.com/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}?api-version=2024-03-01"
credential = DefaultAzureCredential()
token = credential.get_token("https://management.azure.com/.default")

headers = {
    "Authorization": f"Bearer {token.token}",
    "Content-Type": "application/json"
}

response = requests.get(base_url, headers=headers)
response.raise_for_status() 

print(json.dumps(response.json(), indent=4))
```
