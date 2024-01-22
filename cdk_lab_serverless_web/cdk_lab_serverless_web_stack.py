from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw
    # aws_sqs as sqs,
)
from constructs import Construct

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

        apigw.LambdaRestApi(
            self, 'Endpoint',
            handler=my_lambda
        )
        
        # example resource
        # queue = sqs.Queue(
        #     self, "CdkLabServerlessWebQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
