#!/bin/bash
docker network create sam-local
docker run -d -p 8000:8000 --network lambda-local \
	--name dynamodb cnadiminti/dynamodb-local
aws dynamodb create-table --table-name adventurio-games-dev \
	--attribute-definitions AttributeName=id,AttributeType=S \
	--key-schema AttributeName=id,KeyType=HASH \
	--provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 \
	--endpoint-url http://0.0.0.0:8000
sam local start-api --docker-network sam-local &