# Colors
GREEN  := $(shell tput -Txterm setaf 2)
CYAN   := $(shell tput -Txterm setaf 6)
RESET  := $(shell tput -Txterm sgr0)


help: ## Print this help
	@echo "$(CYAN)Available targets:$(RESET)"
	@awk -F':.*##' '/^[a-zA-Z0-9_-]+:.*?##/ {printf "  $(GREEN)%-30s$(RESET)  %s\n", $$1, $$2}' Makefile | sort

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

deploy-with-cdk8s-basic: ## cdk8s demo deploy (basic)
	@cd basic && cdk8s synth && kubectl apply -f dist/hello.k8s.yaml

destroy-with-cdk8s-basic: ## cdk8s demo destroy (basic)
	@cd basic && kubectl delete -f dist/hello.k8s.yaml

deploy-with-cdk8s-webservices: ## cdk8s demo deploy (abstraction)
	@cd webservice && cdk8s synth && kubectl apply -f dist/web-services.k8s.yaml

destroy-with-cdk8s-webservices: ## cdk8s demo destroy (abstraction)
	@cd webservice && kubectl delete -f dist/web-services.k8s.yaml

deploy-with-cdk8s-plus: ## cdk8s demo deploy (cdk8s+)
	@cd plus && cdk8s synth && kubectl apply -f dist/chart-c86185a7.k8s.yaml

destroy-with-cdk8s-plus: ## cdk8s demo destroy (cdk8s+)
	@cd plus && kubectl delete -f dist/chart-c86185a7.k8s.yaml

deploy-pods:
	@kubectl apply -f pods.yaml

deploy-service:
	@kubectl apply -f service.yaml
