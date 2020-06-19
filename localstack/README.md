## Setup

`$ pip3.8 install localstack`

## Starting (no-Docker mode)

`$ localstack start --host`

## Starting (using Docker)

`$ LAMBDA_EXECUTOR=docker localstack start`

## Starting with selected services

`$ SERVICES=s3,lambda,es localhost start`
