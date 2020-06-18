import boto3
import os

SQS_ENDPOINT_URL = 'http://%s:4576' % os.environ['LOCALSTACK_HOSTNAME']
SQS_QUEUE_URL = SQS_ENDPOINT_URL + '/queue/testsqs'

sqs = boto3.client('sqs', endpoint_url=SQS_ENDPOINT_URL)

def handle(event, context):
    sqs.send_message(QueueUrl=SQS_QUEUE_URL, MessageBody='test')
    return {'send_sqs': True}
