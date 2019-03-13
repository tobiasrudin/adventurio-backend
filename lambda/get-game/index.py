import json
import dynamodb


def handler(event, context):
    print(event)
    return get_game(event['pathParameters']['gameId'])


def get_game(gameId):

    if not is_valid_uuid(game['id']):
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Error: Invalid UUID format"})
        }

    game = dynamodb.get_game(gameId)

    if not game:
        return {
            'statusCode': 404,
            'body': json.dumps({'message': 'Requested game does not exist'})
        }

    return {
        'headers': {
            'Content-Type': 'application/json'
        },
        'statusCode': 200,
        'body': json.dumps(game)
    }


def is_valid_uuid(uuid_to_test, version=4):
    """
    Check if uuid_to_test is a valid UUID.

    Parameters
    ----------
    uuid_to_test : str
    version : {1, 2, 3, 4}

    Returns
    -------
    `True` if uuid_to_test is a valid UUID, otherwise `False`.

    Examples
    --------
    >>> is_valid_uuid('c9bf9e57-1685-4c89-bafb-ff5af830be8a')
    True
    >>> is_valid_uuid('c9bf9e58')
    False
    """
    try:
        uuid_obj = UUID(uuid_to_test, version=version)
    except:
        return False

    return str(uuid_obj) == uuid_to_test
