
import csv
from twilio.rest import Client

# Twilio Account SID and Auth Token
account_sid = 'ACcaac1490e4a1571aa16fe249a5dba9ea'
auth_token = 'f42f8e14593819ab4099e8c03809b956'
client = Client(account_sid, auth_token)

# Function to get message details for a given SID
def get_message_details(sid):
    message = client.messages(sid).fetch()
    return {
        'sid': message.sid,
        'price': message.price,
        'from': message.from_
    }

# Read MessageSIDs.txt file
with open('MessageSIDs.txt', 'r') as file:
    message_sids = file.readlines()

# List to store message details
message_details = []

# Calling Twilio API for each SID and adding the details to the list
for sid in message_sids:
    sid = sid.strip()
    details = get_message_details(sid)
    message_details.append(details)

# Write message details into UsagePricing.csv file
with open('UsagePricing4.csv', 'w', newline='') as csvfile:
    fieldnames = ['sid', 'price', 'from']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for details in message_details:
        writer.writerow(details)
