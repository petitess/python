import requests

client_id = 'x'
client_secret = 'x'
tenant_id = 'x'
primary_smtp_address = 'passwordreminder@x.se'

def send_email_via_graph():
    # Get access token
    token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
    token_data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
        'scope': 'https://graph.microsoft.com/.default' #Mail.Send
    }
    
    token_response = requests.post(token_url, data=token_data)
    access_token = token_response.json()['access_token']
    
    # Send email
    graph_url = f"https://graph.microsoft.com/v1.0/users/{primary_smtp_address}/sendMail"
    
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    
    email_data = {
        "message": {
            "subject": "Test Email via Graph API",
            "body": {
                "contentType": "HTML",
                "content": "<h2>Hello!</h2> This is a test email via Graph API."
            },
            "toRecipients": [
                {
                    "emailAddress": {
                        "address": "karol.sek@x.se"
                    }
                }
            ]
        },
        "saveToSentItems": "true"
    }
    
    response = requests.post(graph_url, headers=headers, json=email_data)
    
    if response.status_code == 202:
        print("✓ Email sent successfully via Graph API!")
    else:
        print(f"✗ Failed: {response.status_code} - {response.text}")

send_email_via_graph()
