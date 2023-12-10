#!/usr/bin/env python3
"""This module contains a webservice demo"""
from constructs import Construct
from cdk8s import App, Chart
from webservice import WebService


class WebServices(Chart):
    """The WebServices class"""
    def __init__(self, scope: Construct, app_id: str):
        super().__init__(scope, app_id)

        WebService(self, "hello", image="pbitty/hello-from:latest", replicas=3, node_port=31000)

        WebService(self, "world", image="nginx:latest", replicas=3, node_port=32000)

app = App()
WebServices(app, "web-services")

app.synth()
