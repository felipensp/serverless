## Create domain

```
$ awslocal es create-elasticsearch-domain --domain-name test
{
    "DomainStatus": {
        "DomainId": "000000000000/test",
        "DomainName": "test",
        "ARN": "arn:aws:es:us-east-1:000000000000:domain/test",
        "Created": false,
        "Deleted": false,
        "Endpoint": "http://localhost:4571",
        "Processing": false,
        "ElasticsearchVersion": "7.1",
        "ElasticsearchClusterConfig": {
            "InstanceType": "m3.medium.elasticsearch",
            "InstanceCount": 1,
            "DedicatedMasterEnabled": true,
            "ZoneAwarenessEnabled": false,
            "DedicatedMasterType": "m3.medium.elasticsearch",
            "DedicatedMasterCount": 1
        },
        "EBSOptions": {
            "EBSEnabled": true,
            "VolumeType": "gp2",
            "VolumeSize": 10,
            "Iops": 0
        },
        "CognitoOptions": {
            "Enabled": false
        }
    }
}
```

## Create index

```
$ curl -XPUT localhost:4571/test
{"acknowledged":true,"shards_acknowledged":true,"index":"test"}
```

## Unblock index

```
$ curl -XPUT localhost:4571/test/_settings -d '
{
"index": {
"blocks": {
"read_only_allow_delete": "false"
}
}
}
' -H 'Content-type: application/json'
```

## Create document

```
$ curl -XPUT localhost:4571/test/_create/1 -H 'Content-Type: application/json' -d '{"foo": "bar"}'
{"_index":"test","_type":"_doc","_id":"1","_version":1,"result":"created","_shards":{"total":2,"successful":1,"failed":0},"_seq_no":0,"_primary_term":1}
```

## Get document

```
$ curl -XGET localhost:4571/test/_doc/1
{"_index":"test","_type":"_doc","_id":"1","_version":1,"_seq_no":0,"_primary_term":1,"found":true,"_source":{"foo": "bar"}}
```
