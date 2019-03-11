#! /bin/bash
if [[ $TRAVIS_BRANCH == 'dev' ]]; then
	export STAGE=dev
fi