import json


def handler(event, context):
    print(event)
    return get_games()


def get_games():
    return {
        'headers': {
            'x-next': 'https://link.com',
            'Content-Type': 'application/json'
        },
        'statusCode': 200,
        'body': json.dumps([])
    }
