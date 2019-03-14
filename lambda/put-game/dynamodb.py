import dynamodb_table

table = dynamodb_table.get_table()


def put_game(game, gameId):
    response = table.put_item(
        Item={
            "id": gameId,
            "name": game['name'],
            "paths": game['paths'],
            "startPos": game['startPos']
        }
    )
