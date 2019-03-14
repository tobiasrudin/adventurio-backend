def from_numbers_to_strings(game):
    game['startPos']['long'] = str(game['startPos']['long'])
    game['startPos']['lat'] = str(game['startPos']['lat'])
    for path in game['paths']:
        for point in path:
            point['long'] = str(point['long'])
            point['lat'] = str(point['lat'])
    return game


def from_strings_to_numbers(game):
    game['startPos']['long'] = float(game['startPos']['long'])
    game['startPos']['lat'] = float(game['startPos']['lat'])
    for path in game['paths']:
        for point in path:
            point['long'] = float(point['long'])
            point['lat'] = float(point['lat'])
    return game
