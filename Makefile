# Makefile
.DEFAULT_GOAL := help
SHELL := /bin/bash
CMD := podman
IMAGE_NAME := spark-test

help: ## Show this help message
	@echo -e 'Usage: make [target] ...\n'
	@echo 'targets:'
	@egrep '^(.+)\:\ ##\ (.+)' ${MAKEFILE_LIST} | column -t -c 2 -s ':#'

.PHONY: build-images
build-images: ## build the container image(s)
	$(CMD) build -t $(IMAGE_NAME):3.5 --file Containerfile.3.5 .
	$(CMD) build -t $(IMAGE_NAME):4.0 --file Containerfile.4.0 .

.PHONY: fmt
fmt: ## format python files
	uv format

.PHONY: setup
setup: ## setup the basic project structure
	mkdir -p tests/ && touch Containerfile tests/test_pyspark.py

.PHONY: test
test: ## run the unit tests
	$(CMD) run --rm $(IMAGE_NAME)-3.5
	$(CMD) run --rm $(IMAGE_NAME)-4.0
