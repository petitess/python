import json
from azure.identity import DefaultAzureCredential
import os
import requests
import datetime

now = datetime.datetime.now().strftime("%Y%m%d-%H%M")
appRegObjectId = os.environ.get(
    "X_APP_REG_OBJECT_ID", "8cffb11c-ff12-432a-911b-c7f5a1e39cfe"
)
credential = DefaultAzureCredential()

scopes = ["https://graph.microsoft.com/.default"]
token_graph = credential.get_token(*scopes)

headers = {
    "Authorization": f"Bearer {token_graph.token}",
    "Content-Type": "application/json",
}
url = f"https://graph.microsoft.com/v1.0/applications/{appRegObjectId}"

response_graph = requests.get(url, headers=headers)

url = f"https://graph.microsoft.com/v1.0/applications/{appRegObjectId}/removePassword"
for cred in response_graph.json().get("passwordCredentials"):
    print(cred["keyId"])
    body = {"keyId": cred["keyId"]}
    response_graph = requests.post(url, headers=headers, json=body)
    if response_graph.status_code == 204:
        print(f"removed secret.")
    else:
        print(
            f"Could not removed secret: {response_graph.status_code} - {response_graph.text}"
        )

url = f"https://graph.microsoft.com/v1.0/applications/{appRegObjectId}/addPassword"
body = {
    "passwordCredential": {
        "displayName": f"Secret created on {now}",
        "endDateTime": (
            datetime.datetime.now() + datetime.timedelta(days=3650)
        ).isoformat()
        + "Z",
    }
}
response_graph = requests.post(url, headers=headers, data=json.dumps(body))
print(f"4.hint: {response_graph.json().get('hint')}")

if response_graph.status_code == 200:
    print(f"Created a new secret.")
else:
    print(
        f"Could not create secret: {response_graph.status_code} - {response_graph.text}"
    )
