import boto3

SQS_ENDPOINT_URL = 'http://localhost:4576'
SQS_QUEUE_URL = 'http://localhost:4576/queue/testsqs'

sqs = boto3.client('sqs',
    endpoint_url=SQS_ENDPOINT_URL)

# print(sqs.list_queues())

print(sqs.send_message(QueueUrl=SQS_QUEUE_URL, MessageBody='test'))
print(sqs.receive_message(QueueUrl=SQS_QUEUE_URL))
