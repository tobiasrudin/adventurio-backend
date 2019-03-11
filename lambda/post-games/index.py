def handler(event, context):
    print(event)
    return post_games()


def post_games():
    return {
        'statusCode': 201
    }
