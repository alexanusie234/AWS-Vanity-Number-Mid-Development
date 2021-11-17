import json
import boto3
import vanitynumber


client = boto3.client('dynamodb', region_name='place region name here')


callernumber = "place caller number here"
vanitynumbers = vanitynumber.all_wordifications(callernumber)
                    
# Where I selected "best" vanity numbers

vanitynumbersbest = vanitynumbers[1], vanitynumbers[2], vanitynumbers[3], vanitynumbers[5], vanitynumbers[6]

# convert List to String

vanitynumbersstr = str(vanitynumbersbest)

def lambda_handler(event, context):
    client.batch_write_item(RequestItems={
        'vanitynumbers_resultsAA': [{ 'PutRequest': { 'Item': {
            'caller number': { 'S': callernumber },
            'vanity numbers': { 'S': vanitynumbersstr }
        }}}]
    })
  
    