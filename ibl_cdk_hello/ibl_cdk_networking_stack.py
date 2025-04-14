from aws_cdk import (
    NestedStack,
    aws_ec2
)
from constructs import Construct

class IblCdkNetworkingStack(NestedStack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        self.vpc = aws_ec2.Vpc(
            self,
            "MyVPC",
            nat_gateways=0
        )
