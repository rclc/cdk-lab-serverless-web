from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw
    # aws_sqs as sqs,
)

from constructs import Construct

from cdk_dynamo_table_view import TableViewer
from .hitcounter import HitCounter

class CdkLabServerlessWebStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        # Defines an AWS Lambda resource
        my_lambda = _lambda.Function(
            self, 'HelloHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.from_asset('lambda'),
            handler='hello.handler'
            )

        #instantiate a hit counter
        hello_with_counter = HitCounter(
            self, 'HelloHitCounter',
            downstream=my_lambda
        )

        apigw.LambdaRestApi(
            self, 'Endpoint',
            handler=hello_with_counter.handler
        )
        
        TableViewer(
            self, 'ViewHitCounter',
            title='Hello Hits',
            table=hello_with_counter.table
        )
        
        # example resource
        # queue = sqs.Queue(
        #     self, "CdkLabServerlessWebQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
