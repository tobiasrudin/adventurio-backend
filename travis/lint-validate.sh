#! /bin/bash
yamllint ./template.yaml
yamllint ./specs/
sam validate -t ./template.yaml