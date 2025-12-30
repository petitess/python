### Authenticate to Microsoft Graph
```py
import requests

appid = "xyz"
tenantid = "xyz"
secret = "xyz"
token_url = f"https://login.microsoftonline.com/{tenantid}/oauth2/v2.0/token"
data = {
    "grant_type": "client_credentials",
    "scope": "https://graph.microsoft.com/.default",
    "client_id": appid,
    "client_secret": secret
}

response = requests.post(token_url, data=data)
response.raise_for_status() 
token = response.json()["access_token"]
```
