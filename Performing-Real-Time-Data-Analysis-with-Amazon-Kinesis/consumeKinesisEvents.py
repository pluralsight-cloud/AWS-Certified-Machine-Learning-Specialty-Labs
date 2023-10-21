import json
import base64

def lambda_handler(event, context):
    #print(json.dumps(event))
    
    records = []
    
    for record in event["Records"]:
        data = base64.b64decode(record["kinesis"]["data"]).decode()
        records.append(json.loads(data))
    
    output = {
        "count": str(len(records)),
        "data": records
    }
    
    print(json.dumps(output))