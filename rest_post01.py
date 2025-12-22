from azure.identity import DefaultAzureCredential
import requests
import json

subscription_id = "123"
resource_group_name = "rg-aa-dev-01"
virtual_network_name = "my-vnet"
location = "eastus"
url = f"https://management.azure.com/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualNetworks/{virtual_network_name}?api-version=2024-05-01"

body = {
    "location": location,
    "properties": {
        "addressSpace": {
            "addressPrefixes": ["10.0.0.0/16"]
        },
        "subnets": [
            {
                "name": "default",
                "properties": {
                    "addressPrefix": "10.0.0.0/24"
                }
            }
        ]
    }
}

credential = DefaultAzureCredential()
token = credential.get_token("https://management.azure.com/.default")

headers = {
    "Authorization": f"Bearer {token.token}",
    "Content-Type": "application/json"
}

response = requests.put(url, headers=headers, json=body)
response.raise_for_status()
print(json.dumps(response.json(), indent=4))
