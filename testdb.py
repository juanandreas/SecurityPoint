import boto3

dynamodb = boto3.resource('TestDB')

print(dynamodb.creation_date_time)