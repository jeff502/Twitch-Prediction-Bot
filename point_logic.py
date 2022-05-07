import time

num_replace = {
    "K": 1000,
    "M": 1000000,
    "B": 1000000000
}


def pure_number(string, number):
    """
    :param string: String with an abbreviations for a thousand, million, billion. ("k", "m", "b")
    :param number: Int
    :return: Returns the pure integer without abbreviations or commas for betting.
    """
    mult = 1.0
    if string in num_replace:
        x = num_replace[string]
        mult *= x
        return int(number * mult)


def get_points(current_points):
    """
    get_points and pure_number work in tandem to return an integer from our displayed channel points.
    :param current_points:
    :return: An integer
    """
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
    """
    :param six_p: 6.25% of our total
    :param current_loop: Current loop iteration
    :return: 6.25% of our total * the current loop
    """
    if current_loop == 1:
        return six_p
    elif current_loop == 2:
        return six_p * 2
    elif current_loop == 3:
        return six_p * 4
    elif current_loop == 4:
        return six_p * 8


def time_set(total_time):
    """
    Sleeps until time =< 1 minute
    :param total_time: Total time remaining on an active prediction
    :return: None
    """
    time_remaining = total_time.split(":")
    if time_remaining[0] == "Prediction":
        return
    minutes = int(time_remaining[0])
    seconds = int(time_remaining[1])

    if minutes == 0:
        return
    elif minutes == 1:
        time.sleep(seconds)
        return
    else:
        time.sleep(((minutes - 1) * 60) + seconds)
        return
