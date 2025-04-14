#!/usr/bin/env python3
import aws_cdk

from ibl_cdk_hello.ibl_cdk_hello_stack import IblCdkHelloApplicationStack
from ibl_cdk_hello.ibl_cdk_networking_stack import IblCdkNetworkingStack


app = aws_cdk.App()

root_stack = aws_cdk.Stack(
    app,
    "RootStack"
)

network_stack = IblCdkNetworkingStack(
    root_stack, 
    "IblCdkHelloNetworkingStack"
    )
application_stack = IblCdkHelloApplicationStack(
    root_stack, 
    "IblCdkHelloApplicationStack",
    my_vpc=network_stack.vpc
    )

app.synth()

