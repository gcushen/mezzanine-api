steps to add an authenticated application to mezzanine:

- Install mezzanine server
- pip install -U git+https://github.com/att-innovate/mezzanine-api.git
- Navigate to: http://127.0.0.1:8001/api/oauth2/applications/register/)
	Create a new application with the following details:
	Name: EngagementManager
	Client ID: <auto generated>
	Client Secret: <auto generated>
	Client Type: Confidential
	Authorization Grant Type: Client Credentials
	Redirect URI: <leave blank>
	User: <leave blank>
- Copy the Client ID to mezzanine-api/setting.py as a value to param 'ENGAGEMENT_MANAGER_ID'
- Steps to create GET requests for Posts, Pages and Categories:
   1. Generate Token: 
	  curl -X POST -H "Accept: application/json; indent=4" -d 'grant_type=client_credentials' -u"<Client ID>:<Client Secret>" http://127.0.0.1:8000/api/oauth2/token/
	  Example response:
	  {"access_token": "F0QhCm04jAQ2a4fLgRrPV5gjmJ6QdG", "token_type": "Bearer", "expires_in": 36000, "scope": "read write"}
   2. Add the received token as an header:
      curl -H "Authorization: Bearer <received_token>" http://127.0.0.1:8000/api/posts
- Note: Pages need to be created with 'login required' checkbox
      
       
   

