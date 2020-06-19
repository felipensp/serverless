import boto3
import os
import elasticsearch
import json

ES_ENDPOINT_URL = os.environ['LOCALSTACK_HOSTNAME']

SQS_ENDPOINT_URL = 'http://%s:4576' % os.environ['LOCALSTACK_HOSTNAME']
SQS_QUEUE_URL = SQS_ENDPOINT_URL + '/queue/testsqs'

sqs = boto3.client('sqs', endpoint_url=SQS_ENDPOINT_URL)
es = elasticsearch.Elasticsearch(
    hosts = [{'host': ES_ENDPOINT_URL, 'port': 4571}],
)

def handle(event, context):
    msg = {
        'eventTime': event['Records'][0]['eventTime'],
        's3Bucket': event['Records'][0]['s3']['bucket']['name'],
        's3FileName': event['Records'][0]['s3']['object']['key'],
        's3FileEtag': event['Records'][0]['s3']['object']['eTag'],
    }

    es.index(index="test", doc_type="_doc", id=msg['s3FileEtag'], body=msg)
    sqs.send_message(QueueUrl=SQS_QUEUE_URL, MessageBody=json.dumps(msg))

    return {'notification': True}
