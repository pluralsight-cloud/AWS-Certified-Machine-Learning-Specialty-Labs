import json
import boto3
import uuid
import random
import time

def lambda_handler(event, context):
    client = boto3.client('kinesis')
    
    while True:
        data = {
            "id": str(uuid.uuid4()),
            "latitude": random.uniform(-90, 90),
            "longtitude": random.uniform(0, 180)
        }
        
        response = client.put_record(
            StreamName="TelemetricsStream",
            PartitionKey="geolocation",
            Data=json.dumps(data)
        )
    
        print(response)
        
        time.sleep(random.random())