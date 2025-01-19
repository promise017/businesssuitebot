import requests 
from datetime import datetime, timedelta

GRAPH_API_URL = "https://graph.facebook.com/v12.0/me/messages"

def get_conversations(page_access_token):
    """Fetch conversations from the page."""
    url = "https://graph.facebook.com/v12.0/me/conversations"
    params = {
        "access_token": page_access_token,
        "fields": "participants,updated_time"  # Fetch participant details and the last updated time
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        conversations = data.get('data', [])
        print("Conversations fetched successfully!")
        return conversations
    else:
        print(f"Error fetching conversations: {response.status_code}")
        print(response.json())
        return []

def filter_recent_conversations(conversations):
    """Filter conversations updated within the last 24 hours."""
    recent_users = []
    now = datetime.utcnow()
    twenty_four_hours_ago = now - timedelta(hours=24)

    for convo in conversations:
        updated_time_str = convo.get('updated_time')
        if updated_time_str:
            updated_time = datetime.strptime(updated_time_str, "%Y-%m-%dT%H:%M:%S%z").replace(tzinfo=None)
            if updated_time >= twenty_four_hours_ago:
                participants = convo.get('participants', {}).get('data', [])
                for participant in participants:
                    user_id = participant.get('id')
                    if user_id:
                        recent_users.append((user_id))  #ID
    return recent_users


PAGE_ACCESS_TOKEN = "EAAIzXqKNkmUBOyDYsqOEXYpbenKuYwAJCROlZCZCXUwTjm7zIuFlDmUZA3Ck3DOGjx83YBT1Utqm2eZCauF25Wkgu6E86DyMMSnVhx5tUZCtSqlImsM4zSMardJAuTbxYJGMZATS0lbRqZBcDpZAHyWhd7Xr4vGJDQSAjn8cRSXi3ABQ7DgHa5futl7C1ZBGuwts5IcGlTwU2HNBzNiXYFbfdBMkZD"

# Fetch conversations
conversations = get_conversations(PAGE_ACCESS_TOKEN)

# Filter users who interacted within the last 24 hours
if conversations:
    recent_users = filter_recent_conversations(conversations)
    if recent_users:
        print("Users who interacted with your page within the last 24 hours:")
        for user_id in recent_users:
            print(f"{user_id}")
    else:
        print("No users interacted within the last 24 hours.")
else:
    print("No conversations found.")
    
# Initialize required variables
ACCESS_TOKEN = 'EAAIzXqKNkmUBOyDYsqOEXYpbenKuYwAJCROlZCZCXUwTjm7zIuFlDmUZA3Ck3DOGjx83YBT1Utqm2eZCauF25Wkgu6E86DyMMSnVhx5tUZCtSqlImsM4zSMardJAuTbxYJGMZATS0lbRqZBcDpZAHyWhd7Xr4vGJDQSAjn8cRSXi3ABQ7DgHa5futl7C1ZBGuwts5IcGlTwU2HNBzNiXYFbfdBMkZD'  # Replace with your Page Access Token
USER_PSIDS = recent_users[:]

def inputTaker():
    while(True):
        USER_PSID = input("Enter the user's PSID: or exit to finish ").strip() 
        if USER_PSID.lower()=='exit':
            break # Prompt for user PSID
        if USER_PSID.isdigit():
            USER_PSIDS.append(USER_PSID)
        else:
            print("invalid id")
      

# inputTaker()
print("Debug: Collected PSIDs:", USER_PSIDS)


selector=input("do you want to select image or text?..press 1 for text and 2 for image and 3 for video:")
if selector=='1':
    
    MESSAGE_TEXT = input("what do you want to enter?")  # The message to send

    # Define the endpoint
    GRAPH_API_URL = "https://graph.facebook.com/v12.0/me/messages"

    def send_hello_message(user_psid, message_text):
        try:
            # Prepare the payload
            payload = {
                'recipient': {'id': user_psid},
                'message': {'text': message_text},
            }
            
            # Prepare headers
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {ACCESS_TOKEN}',
            }

            # Make the API request
            response = requests.post(GRAPH_API_URL, json=payload, headers=headers)

            # Check for errors
            if response.status_code == 200:
                print("Message sent successfully:", response.json())
            else:
                print("Failed to send message:", response.status_code, response.json())
        
        except Exception as e:
            print("Error:", e)

    # Call the function
    if __name__ == "__main__":
        if USER_PSIDS:
            for psid in USER_PSIDS:
                send_hello_message(psid, MESSAGE_TEXT)

                   
        else:
            print("User PSID is required.")


if selector=='2':

    def send_image_message(user_psid, media_url):
        try:
            # Prepare the payload with media (image) attachment
            payload = {
                'recipient': {'id': user_psid},
                'message': {
                    # Optional text message
                    'attachment': {
                        'type': 'image',
                        'payload': {
                            'url': media_url,
                            'is_reusable': True  # Optional: set to True if you want to reuse the media
                        }
                    }
                }
            }

            # Prepare headers
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {ACCESS_TOKEN}',
            }

            # Make the API request
            response = requests.post(GRAPH_API_URL, json=payload, headers=headers)

            # Check for errors
            if response.status_code == 200:
                print("Image sent successfully:", response.json())
            else:
                print("Failed to send image:", response.status_code, response.json())

        except Exception as e:
            print("Error:", e)

    if USER_PSIDS:
        media_url=input("enter link")
    for psid in USER_PSIDS:
            send_image_message(psid, media_url)
#     # Example usage
# if USER_PSIDS:
#     media_url=input("enter link")
#     for psid in USER_PSIDS:
#             send_image_message(psid, media_url)
            
    





        #9894592423889137
        #5287070621358167


if selector=='3':

    def send_video_message(user_psid, media_url):
        try:
        # Prepare the payload with media (video) attachment
            payload = {
            'recipient': {'id': user_psid},
            'message': {
                'attachment': {
                    'type': 'video',
                    'payload': {
                        'url': media_url,
                        'is_reusable': True  # Optional: set to True if you want to reuse the media
                    }
                }
             }
            }

        # Prepare headers
            headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {ACCESS_TOKEN}',
        }

        # Make the API request
            response = requests.post(GRAPH_API_URL, json=payload, headers=headers)

        # Check for errors
            if response.status_code == 200:
                print("Video sent successfully:", response.json())
            else:
             print("Failed to send video:", response.status_code, response.json())

        except Exception as e:
            print("Error:", e)

    if USER_PSIDS:
        media_url=input("enter link")
    for psid in USER_PSIDS:
            send_video_message(psid, media_url)