num_replace = {
    "K": 1000,
    "M": 1000000,
    "B": 1000000000
}


def pure_number(string, number):
    mult = 1.0
    if string in num_replace:
        x = num_replace[string]
        x = int(x)
        mult *= x
        return number * mult


def get_points(current_points):
    if "K" in current_points:
        num = float(current_points.split("K")[0])
        character = current_points[len(current_points) - 1:]
        current_points = pure_number(string=character, number=num)
    elif "M" in current_points:
        num = float(current_points.split("M")[0])
        character = current_points[len(current_points) - 1:]
        current_points = pure_number(string=character, number=num)
    return int(current_points)


def how_much_to_bet(six_p, current_loop):
    if current_loop == 1:
        return six_p
    elif current_loop == 2:
        return six_p * 2
    elif current_loop == 3:
        return six_p * 4
    elif current_loop == 4:
        return six_p * 8
