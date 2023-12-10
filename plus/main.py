"""This module contains a kplus demo"""
import cdk8s_plus_27 as kplus
import cdk8s


############### Parameters
LABEL = {"app": "hello"}
PORT_NUMBER = 80
NODE_PORT = 31000
REPLICAS = 2
VERSION = "latest"
IMAGE_NAME = f"pbitty/hello-from:{VERSION}"




app = cdk8s.App()
chart = cdk8s.Chart(app, 'Chart')

deploy = kplus.Deployment(chart, 'HelloDeployment',
    replicas=REPLICAS,
    metadata=cdk8s.ApiObjectMetadata(labels=LABEL),
    containers=[kplus.ContainerProps(
        image=IMAGE_NAME,
        port_number=PORT_NUMBER,
        security_context=kplus.ContainerSecurityContextProps(
            ensure_non_root=False
        )
    )]
)

service = kplus.Service(chart, 'HelloService', type=kplus.ServiceType.NODE_PORT)
service.bind(port=PORT_NUMBER, node_port=NODE_PORT)
service.select(deploy)

app.synth()
