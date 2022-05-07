import datetime


def prediction_history(channel_name, points_to_bet, color, current_loop_count, total_before_bets, six_percent):
    """
    This func handles writing to our log file.
    :param channel_name: Channel name of the Twitch streamer.
    :param points_to_bet: How many points we bet.
    :param color: The color of the bet we placed.
    :param current_loop_count: Current loop iteration before it's increased by the end of the loop.
    :param total_before_bets: Total we had before placing any bets on our current loop.
    :param six_percent: 6.25% of our total
    :return: None.
    """
    time_now = datetime.datetime.now().strftime('%H:%M:%S')
    formatted_date = datetime.datetime.now().strftime('%b-%d-%y')
    with open("Twitch Prediction History.txt", "a") as f:
        f.write(
            f"Streamer: {channel_name} | Points Bet: {points_to_bet} | Color: {color} | "
            f"Loop Count: {current_loop_count} | "
            f"Total before bet: {total_before_bets} | "
            f"6.25% {six_percent} | "
            f"Time: {time_now} | Date: {formatted_date}\n"
        )


def check_prediction_history(channel):
    """
    Reads the last entry of our 'Twitch Prediction History.txt' log file
    :param channel: Channel name for the Twitch streamer.
    :return: False if the channel names do not match, or if the new loop + 1 would be greater than four.
    :return: total_before_bets, current_loop_count, six_percent.
    """
    with open("Twitch Prediction History.txt") as f:
        content = f.readlines()
        for line in content[::-1]:
            last_stream = line
            break

    if channel in last_stream:
        split_stream = last_stream.split("|")
        ttb = int(split_stream[4].split(":")[1].replace(",", ""))
        last_loop = int(split_stream[3].split(":")[1].split()[0]) + 1  # Returns last loop count.
        six_p = int(split_stream[5].split()[1])
        if last_loop > 4:
            return False
        else:
            return ttb, last_loop, six_p
    else:
        return False
