## Remove notification

```
$ awslocal s3api put-bucket-notification-configuration --bucket testbucket --notification-configuration "{}"
```

## Registering s3 bucket notification (on create record) using a JSON notification file 

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
