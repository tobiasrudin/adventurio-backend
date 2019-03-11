#! /bin/bash
if [[ $TRAVIS_BRANCH == 'dev' ]]; then
	setenv STAGE dev
fi