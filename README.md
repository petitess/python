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
### PUT
```py
from azure.identity import DefaultAzureCredential
import requests
import json
import datetime
now = datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S GMT")
credential = DefaultAzureCredential()
json_get = {
    "name": "func-int",
    "type": "Microsoft.Storage/storageAccounts/blobServices/containers",
    "properties": {
        "leaseStatus": "Unlocked",
        "leaseState": "Available",
        "lastModifiedTime": "2026-01-03T07:10:44.0000000Z",
    },
}
scopes = ["https://storage.azure.com/.default"]
token = credential.get_token(*scopes)
url = f"https://stcostmanagment01.blob.core.windows.net/func-int/README.md"
file_content = f'''## This is a sample README file.

This file is stored in Azure Blob Storage.
~~~json
{json.dumps(json_get, indent=4)}
~~~
'''
headers = {
    "Authorization": f"Bearer {token.token}",
    "Content-type": "application/octet-stream",
    "x-ms-date": f"{now}",
    "x-ms-version": "2020-04-08",
    "Accept": "application/octet-stream;odata=fullmetadata",
    "x-ms-blob-content-disposition": "attachment",
    "x-ms-blob-type": "BlockBlob",
}
response = requests.put(url, headers=headers, data=file_content.encode('utf-8'))
response.raise_for_status()
json_get["status_code"] = response.status_code
print(json.dumps(json_get, indent=4))

```
