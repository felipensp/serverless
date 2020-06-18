## Python code

```
$ cat test.py 
def handler(event, context):
	print('teste')
	return {'foo': 'bar'}
```

## Creating new lambda

```
$ awslocal lambda create-function --function-name handler --runtime python3.8 --handler test.handler --zip-file fileb://test.zip --role rl
{
    "FunctionName": "handler",
    "FunctionArn": "arn:aws:lambda:us-east-1:000000000000:function:handler",
    "Runtime": "python3.8",
    "Role": "rl",
    "Handler": "test.handler",
    "CodeSize": 232,
    "Description": "",
    "Timeout": 3,
    "LastModified": "2020-06-18T13:51:13.083+0000",
    "CodeSha256": "LwaqAhYKbEooxBhi52NG7O0SkkRRrNcEKa+sukt7AMM=",
    "Version": "$LATEST",
    "VpcConfig": {},
    "TracingConfig": {
        "Mode": "PassThrough"
    },
    "RevisionId": "1005a85a-0f62-446f-a4c8-39887e7005c5",
    "State": "Active",
    "LastUpdateStatus": "Successful"
}
```

## Manual execution

```
$ awslocal lambda invoke --function-name handler result.log
{
    "StatusCode": 200
}
```

## Checking output

```
$ cat result.log 
{"foo":"bar"}
```
