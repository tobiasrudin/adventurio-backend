from decimal import Decimal


def from_numbers_to_strings(game):
    game['startPos']['long'] = str(game['startPos']['long'])
    game['startPos']['lat'] = str(game['startPos']['lat'])
    for path in game['paths']:
        for point in path:
            point['long'] = str(point['long'])
            point['lat'] = str(point['lat'])
    return game


def from_strings_to_numbers(game):
    game['startPos']['long'] = Decimal(game['startPos']['long'])
    game['startPos']['lat'] = Decimal(game['startPos']['lat'])
    for path in game['paths']:
        for point in path:
            point['long'] = Decimal(point['long'])
            point['lat'] = Decimal(point['lat'])
    return game
