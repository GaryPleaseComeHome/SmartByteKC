import datetime
import os.path
import sys
import argparse
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']

CREDENTIALS_FILE = 'C:/Users/Gibby/Documents/SmartByteKC/Operations/client_secret_231791284001-prct1qetvm66r1bjd1jib2eua2js4eho.apps.googleusercontent.com.json'
TOKEN_FILE = 'C:/Users/Gibby/smartbytekc/scripts/token.json'

def get_service():
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
    return build('calendar', 'v3', credentials=creds)

def add_event(summary, description, start_time, end_time, event_type):
    service = get_service()
    # Categorize by prepending [Type] to summary
    formatted_summary = f"[{event_type.capitalize()}] {summary}"
    
    event = {
        'summary': formatted_summary,
        'description': description,
        'start': {'dateTime': start_time, 'timeZone': 'America/Chicago'},
        'end': {'dateTime': end_time, 'timeZone': 'America/Chicago'},
    }
    event = service.events().insert(calendarId='primary', body=event).execute()
    print(f'Event created: {event.get("htmlLink")}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='SmartByteKC Calendar Integration')
    parser.add_argument('summary', help='Event summary')
    parser.add_argument('description', help='Event description')
    parser.add_argument('start_time', help='Start time (ISO format)')
    parser.add_argument('end_time', help='End time (ISO format)')
    parser.add_argument('--type', choices=['personal', 'work'], required=True, help='Event type (personal or work)')
    
    args = parser.parse_args()
    
    add_event(args.summary, args.description, args.start_time, args.end_time, args.type)
