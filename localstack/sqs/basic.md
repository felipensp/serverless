## Creating SQS queue

```
$ awslocal sqs create-queue --queue-name testbucket-sqs
{
    "QueueUrl": "http://localhost:4576/queue/testbucket-sqs"
}
```

## Reading SQS queue

```
$ awslocal s3 cp test.py s3://testbucket # for testing notification
$ awslocal sqs receive-message --queue-url http://localhost:4576/queue/testbucket-sqs
{
    "Messages": [
        {
            "MessageId": "0b62fee3-3b2d-4fef-a1ac-2d2b734556e9",
            "ReceiptHandle": "0b62fee3-3b2d-4fef-a1ac-2d2b734556e9#a76f5ac2-f5bd-44e2-a78f-908d2335b8be",
            "MD5OfBody": "9099898bb5a83e8978c525de2894a0b1",
            "Body": "{\"Records\": [{\"eventVersion\": \"2.0\", \"eventSource\": \"aws:s3\", \"awsRegion\": \"us-east-1\", \"eventTime\": \"2020-06-18T14:50:02.191Z\", \"eventName\": \"ObjectCreated:Put\", \"userIdentity\": {\"principalId\": \"AIDAJDPLRKLG7UEXAMPLE\"}, \"requestParameters\": {\"sourceIPAddress\": \"127.0.0.1\"}, \"responseElements\": {\"x-amz-request-id\": \"0a1b202d\", \"x-amz-id-2\": \"eftixk72aD6Ap51TnqcoF8eFidJG9Z/2\"}, \"s3\": {\"s3SchemaVersion\": \"1.0\", \"configurationId\": \"testConfigRule\", \"bucket\": {\"name\": \"testbucket\", \"ownerIdentity\": {\"principalId\": \"A3NL1KOZZKExample\"}, \"arn\": \"arn:aws:s3:::testbucket\"}, \"object\": {\"key\": \"test.py\", \"size\": 68, \"eTag\": \"d41d8cd98f00b204e9800998ecf8427e\", \"versionId\": null, \"sequencer\": \"0055AED6DCD90281E5\"}}}]}"
        }
    ]
}
```
