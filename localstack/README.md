## Setup

`$ pip3.8 install localstack`

## Starting (no-Docker mode)

`$ localstack start --host`

## Starting with selected services

`$ SERVICES=s3,lambda,es localhost start --host`
