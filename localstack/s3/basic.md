## Creating S3 bucket

```
$ awslocal s3 mb s3://testbucket
make_bucket: testbucket
```

## Copying file to bucket

```
$ awslocal s3 cp test.py s3://testbucket
upload: ./test.py to s3://testbucket/test.py                      
```

## Listing bucket files

```
$ awslocal s3 ls s3://testbucket
2020-06-18 11:15:51         68 test.py
```
