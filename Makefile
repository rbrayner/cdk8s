##@ Target
help:  ## Display this help.
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

install-kind-macos: ## Install kind on MacOS
	@brew install kind

install-kind-linux: ## Install kind on Ubuntu
	@curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.15.0/kind-linux-amd64
	@chmod +x ./kind
	@sudo mv ./kind /usr/local/bin/kind

start: ## Create the kind cluster
	@kind create cluster --config kind/cluster.yaml --name demo

stop: ## Destroy the kind cluster
	@kind delete cluster --name demo

list: ## List the available clusters
	@kind get clusters

deploy-pods:
	@kubectl apply -f pods.yaml

deploy-service:
	@kubectl apply -f service.yaml

deploy-with-cdk8s-basic:
	@cd basic && cdk8s synth && kubectl apply -f dist/hello.k8s.yaml

destroy-with-cdk8s-basic:
	@cd basic && kubectl delete -f dist/hello.k8s.yaml

deploy-with-cdk8s-webservices:
	@cd webservice && cdk8s synth && kubectl apply -f dist/web-services.k8s.yaml

destroy-with-cdk8s-webservices:
	@cd webservice && kubectl delete -f dist/web-services.k8s.yaml

deploy-with-cdk8s-plus:
	@cd plus && cdk8s synth && kubectl apply -f dist/chart-c86185a7.k8s.yaml

destroy-with-cdk8s-plus:
	@cd plus && kubectl delete -f dist/chart-c86185a7.k8s.yaml
