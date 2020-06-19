# Step-by-step

## Create function
```
$ awslocal lambda create-function --function-name handler --runtime python3.8 --handler samples/notif-es-sqs.handle --zip-file fileb://test.zip --role rl
```

## Create queue

```
$ awslocal sqs create-queue --queue-name testsqs
```

## Create s3 bucket

```
$ awslocal s3 mb s3://testbucket
```

## S3 Notification JSON

```
$ cat es-sqs-notif.json 
{
	"LambdaFunctionConfigurations": [
	{
		"Id":"S3EventsLambdaNotification",
		"LambdaFunctionArn": "arn:aws:lambda:us-east-1:000000000000:function:handler",
		"Events": ["s3:ObjectCreated:*"]
	}]
}
```

## Register S3 bucket notification

```
$ awslocal s3api put-bucket-notification-configuration --bucket testbucket --notification-configuration file://es-sqs-notif.json
```

## Testing

```
$ awslocal s3 cp test.py s3://testbucket
```

```
$ awslocal sqs receive-message --queue-url http://localhost:4576/queue/testsqs
{
    "Messages": [
        {
            "MessageId": "d45a13e6-6a95-412e-945c-59837c0ed558",
            "ReceiptHandle": "d45a13e6-6a95-412e-945c-59837c0ed558#df674aee-6c06-4545-8052-a5cf963fa843",
            "MD5OfBody": "6ffe4e4516143495646685e77cb4ce2b",
            "Body": "{\"eventTime\": \"2020-06-19T19:35:49.838Z\", \"s3Bucket\": \"testbucket\", \"s3FileName\": \"test.py\", \"s3FileEtag\": \"d41d8cd98f00b204e9800998ecf8427e\"}"
        }
    ]
}
$ curl -XGET localhost:4571/test/_doc/d41d8cd98f00b204e9800998ecf8427e
{"_index":"test","_type":"_doc","_id":"d41d8cd98f00b204e9800998ecf8427e","_version":2,"_seq_no":1,"_primary_term":1,"found":true,"_source":{"eventTime":"2020-06-19T19:35:49.838Z","s3Bucket":"testbucket","s3FileName":"test.py","s3FileEtag":"d41d8cd98f00b204e9800998ecf8427e"}}
```
