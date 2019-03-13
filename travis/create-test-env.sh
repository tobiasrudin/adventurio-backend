#!/bin/bash
docker network create sam-local
docker run -d -p 8000:8000 --network sam-local \
	--name dynamodb cnadiminti/dynamodb-local
aws dynamodb create-table --table-name adventurio-games-test \
	--attribute-definitions AttributeName=id,AttributeType=S \
	--key-schema AttributeName=id,KeyType=HASH \
	--provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 \
	--endpoint-url http://0.0.0.0:8000
sam local start-api --env-vars ./tests/tavern/sam-local-env-vars.json \
	--docker-network sam-local &