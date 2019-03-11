#! /bin/bash
if [[ $TRAVIS_BRANCH == 'dev' ]]; then
	export STACKNAME=adventurio-dev
fi