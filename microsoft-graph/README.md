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

print("Access token acquired successfully.")

graph_url = "https://graph.microsoft.com/v1.0/users"
headers = {
    "Authorization": f"Bearer {token}"
}

users_response = requests.get(graph_url, headers=headers)
users_response.raise_for_status()
users_data = users_response.json()

print("\nAuthenticated context (partial token for verification):")
print(token[:50] + "...")
print("\nUsers retrieved:")
for user in users_data.get("value", []):
    print(f"- {user['displayName']} ({user['userPrincipalName']})")
```
