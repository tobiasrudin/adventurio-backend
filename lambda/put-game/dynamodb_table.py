import boto3
import os


def get_table():
    TEST_ENV = os.environ['TEST_ENV']
    if TEST_ENV == 'true':
        dynamodb = boto3.resource(
            'dynamodb', endpoint_url='http://dynamodb:8000')
        table = dynamodb.Table('adventurio-games-test')
    else:
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table(os.environ['GAMES_TABLE'])

    return table
