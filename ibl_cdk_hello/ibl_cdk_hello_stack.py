from aws_cdk import (
    NestedStack,
    aws_ec2,
    aws_ecs_patterns,
    aws_ecs
)
from constructs import Construct

class IblCdkHelloApplicationStack(NestedStack):

    def __init__(self, scope: Construct, construct_id: str, my_vpc: aws_ec2.Vpc, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        
        # my_ecs_cluster = aws_ecs.Cluster(
        #     self,
        #     "IBLEcsHelloCluster",
        #     cluster_name="ibl-jo-hello-cluster"
        # )
        
        # my_ecs_cluster.add_asg_capacity_provider(
            
        # )
        # my_ecs_solution = aws_ecs_patterns.ApplicationLoadBalancedEc2Service(
        #     self,
        #     "LoadBalancerServiceOnEC2",
        #     memory_limit_mib=1024,
        #     task_image_options=aws_ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
        #         image=aws_ecs.ContainerImage.from_registry("public.ecr.aws/dnxsolutions/nginx-hello:1.0.1")
        #     ),
        #     desired_count=1,
        #     cluster=my_ecs_cluster
        # )