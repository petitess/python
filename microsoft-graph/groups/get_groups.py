graph_url = "https://graph.microsoft.com/v1.0/groups?$filter=displayName eq 'Test-SiteAdmins'"
graph_url = "https://graph.microsoft.com/v1.0/groups?$filter=id eq '8d9cf3f8-8351-4f5e-a121-ada350aeb3b2'"
graph_url = "https://graph.microsoft.com/v1.0/groups?$filter=startswith(displayName, 'Test-SiteAdmins')&$count=true&$top=1"
graph_url = "https://graph.microsoft.com/v1.0/groups?$orderby=displayName"

headers = {
    "Authorization": f"Bearer {token}"
}

users_response = requests.get(graph_url, headers=headers)
users_response.raise_for_status()
users_data = users_response.json()
print(users_data)

print("\nAuthenticated context (partial token for verification):")
print(token[:50] + "...")
print("\nGroups retrieved:")
for user in users_data.get("value", []):
    print(f"- {user['displayName']} ({user['id']})")
