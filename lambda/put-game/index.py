import json
import dynamodb
import coordinates
import uuid_checker


def handler(event, context):
    print(event)
    return put_game(json.loads(event['body']), event['pathParameters']['gameId'])


def put_game(game, gameId):

    if not uuid_checker.is_valid_uuid(gameId):
        return {
            'headers': {
                'Content-Type': 'application/json'
            },
            "statusCode": 400,
            "body": json.dumps({"message": "Error: Invalid UUID format"})
        }

    game = coordinates.from_numbers_to_strings(game)
    dynamodb.put_game(game, gameId)

    return {
        'statusCode': 201
    }
