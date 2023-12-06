import cdk8s_plus_27 as kplus
import cdk8s

app = cdk8s.App()
chart = cdk8s.Chart(app, 'Chart')

kplus.Deployment(chart, 'Deployment',
  replicas=1,
  containers=[kplus.ContainerProps(image='nginx')]
)

app.synth()