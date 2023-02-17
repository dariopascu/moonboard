import string


def _letter_to_number(letter):
    return string.ascii_uppercase.index(letter)


def move_to_coordinates(moves):
    coordinates = []
    start = []
    end = []
    for move in moves:
        step = move.get('description')
        coordinate = (_letter_to_number(step[0]), int(step[1:]))
        if move.get('isStart'):
            start.append(coordinate)
        if move.get('isEnd'):
            end.append(coordinate)
        coordinates.append(coordinate)
    return coordinates, start, end
