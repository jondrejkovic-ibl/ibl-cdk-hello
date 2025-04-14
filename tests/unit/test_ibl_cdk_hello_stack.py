import aws_cdk as core
import aws_cdk.assertions as assertions

from ibl_cdk_hello.ibl_cdk_hello_stack import IblCdkHelloStack

# example tests. To run these tests, uncomment this file along with the example
# resource in ibl_cdk_hello/ibl_cdk_hello_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = IblCdkHelloStack(app, "ibl-cdk-hello")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
