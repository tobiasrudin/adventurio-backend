import json


def handler(event, context):
    print(event)
    return get_game()


def get_game():
    return {
        'headers': {
            'Content-Type': 'application/json'
        },
        'statusCode': 200,
        'body': json.dumps({})
    }
