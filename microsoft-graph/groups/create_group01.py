graph_url = "https://graph.microsoft.com/v1.0/groups"
headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
body = {
    "description": "Self help community for library",
    "displayName": "Library Assist",
    "groupTypes": ["Unified"],
    "mailEnabled": False,
    "mailNickname": "library",
    "securityEnabled": True,
}

users_response = requests.post(graph_url, headers=headers, json=body)
users_response.raise_for_status()
users_data = users_response.json()
users_data['id']
users_data['displayName']
