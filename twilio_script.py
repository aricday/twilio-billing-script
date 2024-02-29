
import csv
from twilio.rest import Client

# Your Twilio Account SID and Auth Token
account_sid = '$your_account_sid'
auth_token = '$your_auth_token'

# Read the list of Message SIDs from the input file
with open('MessageSIDs.txt', 'r') as file:
    message_sids = [line.strip() for line in file]

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Initialize list to store response data
output_data = []

# Gather pricing and from details for each message SID
for message_sid in message_sids:
    message = client.messages(message_sid).fetch()
    output_data.append({
        'Message SID': message.sid,
        'From': message.from_,
        'Price': message.price
    })

# Write the response data to a new CSV file
with open('UsagePricing.csv', 'w', newline='') as csvfile:
    fieldnames = ['Message SID', 'From', 'Price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for data in output_data:
        writer.writerow(data)

print("Data has been successfully written to UsagePricing.csv")
