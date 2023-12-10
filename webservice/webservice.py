"""This module contains a webservice demo"""
from constructs import Construct
from imports import k8s
from cdk8s import Names


class WebService(Construct):
    """The WebServices class"""
    def __init__(
        self,
        scope: Construct,
        app_id: str,
        *,
        image: str,
        replicas=1,
        node_port: int,
        container_port=80
    ):
        super().__init__(scope, app_id)

        label = {"app": Names.to_label_value(self)}

        k8s.KubeService(self, "service",
            spec=k8s.ServiceSpec(
                type="NodePort",
                ports=[
                    k8s.ServicePort(
                        port=container_port,
                        node_port=node_port,
                    )
                ],
                selector=label,
            ),
        )

        k8s.KubeDeployment(self, "deployment",
            spec=k8s.DeploymentSpec(
                replicas=replicas,
                selector=k8s.LabelSelector(match_labels=label),
                template=k8s.PodTemplateSpec(
                    metadata=k8s.ObjectMeta(labels=label),
                    spec=k8s.PodSpec(
                        containers=[
                            k8s.Container(
                                name="web",
                                image=image,
                                ports=[
                                    k8s.ContainerPort(container_port=container_port)
                                ],
                            )
                        ]
                    ),
                ),
            ),
        )
