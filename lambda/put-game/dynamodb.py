import dynamodb_table

table = dynamodb_table.get_table()


def save_game(game):
    response = table.put_item(
        Item=game
    )
