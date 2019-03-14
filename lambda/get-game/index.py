from uuid import UUID
import json
import dynamodb
import coordinates
import uuid_checker


def handler(event, context):
    print(event)
    return get_game(event['pathParameters']['gameId'])


def get_game(gameId):

    if not uuid_checker.is_valid_uuid(gameId):
        return {
            'headers': {
                'Content-Type': 'application/json'
            },
            "statusCode": 400,
            "body": json.dumps({"message": "Error: Invalid UUID format"})
        }

    game = dynamodb.get_game(gameId)

    if not game:
        return {
            'headers': {
                'Content-Type': 'application/json'
            },
            'statusCode': 404,
            'body': json.dumps({'message': 'Requested game does not exist'})
        }

    game = coordinates.from_strings_to_numbers(game)

    return {
        'headers': {
            'Content-Type': 'application/json'
        },
        'statusCode': 200,
        'body': json.dumps(game)
    }
