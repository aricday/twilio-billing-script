#!/bin/zsh

# initialise CSV file with headers
echo "MessageSID,Price,From" > UsagePricing.csv

# read the MessageSIDs.txt file line by line
while read sid; do
  # call the Twilio API to get details about the message
  response=$(twilio api:core:messages:fetch --sid "$sid")

  # parse response to extract 'price' and 'from' using the jq utility
  price=$(echo $response | jq -r '.price')
  from=$(echo $response | jq -r '.from')
  
  # write sid, price and from into the csv file
  echo "$sid,$price,$from" >> UsagePricing.csv
done < MessageSIDs.txt
