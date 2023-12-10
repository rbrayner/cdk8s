#!/usr/bin/env python
"""This module contains a class for a demo application"""
from imports import k8s
from constructs import Construct
from cdk8s import App, Chart


class Core(Chart):
    """The Core class"""
    def __init__(self, scope: Construct, app_id: str):
        super().__init__(scope, app_id)

        label = {"app": "hello"}

        k8s.KubeDeployment(self, "hello-deployment",
            spec=k8s.DeploymentSpec(
                replicas=3,
                selector=k8s.LabelSelector(match_labels=label),
                template=k8s.PodTemplateSpec(
                    metadata=k8s.ObjectMeta(labels=label),
                    spec=k8s.PodSpec(containers=[
                        k8s.Container(
                            name="hello",
                            image="pbitty/hello-from:latest",
                            ports=[k8s.ContainerPort(container_port=80)]
                        )
                    ])
                )
            )
        )

        k8s.KubeService(self, "service",
            spec=k8s.ServiceSpec(
                type="NodePort",
                ports=[
                    k8s.ServicePort(port=80, node_port=31000)
                ],
                selector=label,
            ),
        )

app = App()
Core(app, "hello")

app.synth()
