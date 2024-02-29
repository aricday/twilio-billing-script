#!/bin/zsh

# initialise CSV file with headers
echo "MessageSID,Price,From" > UsagePricingCURL.csv

# Twilio account and token (replace these values with your own ones)
account_sid="ACcaac1490e4a1571aa16fe249a5dba9ea"
auth_token="f42f8e14593819ab4099e8c03809b956"

# read the MessageSIDs.txt file line by line
while read sid; do
  # call the Twilio API to get details about the SMS
  response=$(curl -s -u $account_sid:$auth_token \
    https://api.twilio.com/2010-04-01/Accounts/$account_sid/Messages/$sid.json)

  # parse response to extract 'price' and 'from' using the jq utility
  price=$(echo $response | jq -r '.price')
  from=$(echo $response | jq -r '.from')

  # write sid, price and from to the file
  echo "$sid,$price,$from" >> UsagePricingCURL.csv
done < MessageSIDs.txt
