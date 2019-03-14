import dynamodb_table

table = dynamodb_table.get_table()


def get_game(gameId):
    response = table.get_item(
        Key={
            "id": gameId
        },
        ProjectionExpression='#N,#P,#SP',
        ExpressionAttributeNames={
            '#N': 'name',
            '#P': 'paths',
            '#SP': 'startPos'
        }
    )
    return response.get('Item')
