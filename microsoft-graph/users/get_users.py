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
