## Packaging Python lambda with dependencies

```
$ python -m venv venv
$ . venv/bin/activate
$ (venv) pip install boto3
...
$ (venv) deactivate
$ cd venv/lib/python3.8/site-packages
$ zip -r9 ~/aws/test.zip .
$ cd ~/aws
$ zip -g test.zip test.py
```

https://docs.aws.amazon.com/lambda/latest/dg/python-package.html
