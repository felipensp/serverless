## Remove notification

```
$ awslocal s3api put-bucket-notification-configuration --bucket testbucket --notification-configuration "{}"
```

## SQS - Registering s3 bucket notification

```
$ cat sqs-notif.json 
{
    "QueueConfigurations": [
    {
       "QueueArn": "http://localhost:4576/queue/testbucket-sqs",
       "Events": ["s3:ObjectCreated:*"]
    }]
}
$ awslocal s3api put-bucket-notification-configuration --bucket testbucket --notification-configuration file://sqs-notif.json
```

# Lambda - Registering s3 bucket notification

```
$ cat lambda-notif.json 
{
	"LambdaFunctionConfigurations": [
	{
		"Id":"S3EventsLambdaNotification",
		"LambdaFunctionArn": "arn:aws:lambda:us-east-1:000000000000:function:handler",
		"Events": ["s3:ObjectCreated:*"]
	}]
}
$ awslocal s3api put-bucket-notification-configuration --bucket testbucket --notification-configuration file://lambda-notif.json
```
