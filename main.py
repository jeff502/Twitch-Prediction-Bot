import datetime
import time
from csv import DictReader
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException


CHANNEL_NAME = "loltyler1"
STREAMER = f"https://www.twitch.tv/popout/{CHANNEL_NAME}/chat"

ser = Service("C:\Program Files (x86)\webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=ser)

x_button = '//*[@id="root"]/div/div[1]/div/div/section/div/div[5]/div[2]' \
           '/div[2]/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div[3]/button'
channel_prediction_prompt = (
    '//*[@id="channel-points-reward-center-body"]/div/div/div[1]/div/button'
)

predict_button_xpath = "/html/body/div[1]/div/div[1]/div/div/section/div/div[3]/div/div[2]" \
                       "/div/div[3]/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/div[2]/button"

predict_with_custom_amount = "/html/body/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/section/" \
                             "div/div[6]/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div[2]" \
                             "/div[3]/div/div/div/div/div/div/div/div/div[3]/div[2]/button"

points_xpath = '//*[@id="root"]/div/div[1]/div/div/section/div/div[6]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[2]' \
               '/button/div/div/div/div[2]/span'

blue_votes = '//*[@id="channel-points-reward-center-body"]/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div[3]' \
             '/div[1]/div[1]/div/div/div[2]/p/span'

red_votes = '//*[@id="channel-points-reward-center-body"]/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div[3]' \
            '/div[1]/div[1]/div/div/div[2]/p/span'

blue_field = '//*[@id="channel-points-reward-center-body"]/div/div/div/div/div/div/div[3]' \
             '/div[1]/div/div/div[1]/div/div/div/input'

red_field = "/html/body/div[1]/div/div[1]/div/div/section/div/div[6]/div[2]/div[2]/div[1]/div/div/div[2]/div/div/" \
            "div/div/div/div/div/div[2]/div[3]/div/div/div/div/div/div/div/div/div[3]" \
            "/div[1]/div/div/div[2]/div/div/div/input"

blue_button = '//*[@id="channel-points-reward-center-body"]/div/div/div/div/div/div/div[3]/div[1]/div/div/div[1]' \
              '/div/div/button'
red_button = '//*[@id="channel-points-reward-center-body"]/div/div/div/div/div/div/div[3]/div[1]/div/div/div[2]' \
             '/div/div/button'

blue_end = '//*[@id="root"]/div/div[1]/div/div/section/div/div[6]/div[2]/div[2]/div[1]/div/div/div[2]/div/div' \
           '/div/div/div/div/div/div[1]/div/div[3]/button'
red_end = '//*[@id="root"]/div/div[1]/div/div/section/div/div[6]/div[2]/div[2]/div[1]/div/div/div[2]/div/div' \
          '/div/div/div/div/div/div[1]/div/div[3]/button'

timer = '//*[@id="channel-points-reward-center-body"]/div/div/div[1]/div/button/div/div[2]/p[2]'

my_channel_points = ".fQvHcx"
getting_started_prompt = (
    '//*[@id="channel-points-reward-center-body"]/div/div/div[2]/button'
)
channel_points_reward_body = '//*[@id="channel-points-reward-center-body"]/div/div/div/div/div/div/' \
                             'div[3]/div[2]/button/div/div'

submission_text = ".dQTuLk"

num_replace = {"K": 1000, "M": 1000000, "B": 1000000000}


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


def time_set(total_time):
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


def get_cookie_values(file):
    """
    Takes all the cookies from our csv file.
    Turns them into a list of dicts
    :param file: csv file
    :return: a list of dicts
    """
    with open(file, encoding="utf-8-sig") as f:
        dict_reader = DictReader(f)
        list_of_dicts = list(dict_reader)
    return list_of_dicts


if __name__ == "__main__":
    # Getting the streamer page and uploading our cookies

    # Comment out ⬇ if you want to log in manually. 'ctrl+/'
    driver.get(STREAMER)
    cookies = get_cookie_values("twitch_cookies.csv")
    for i in cookies:
        driver.add_cookie(i)

    driver.refresh()
    # Uncomment ⬇ if you want to log in manually.
    # time.sleep(120)

    # Default values that'll be updated
    current_loop_count = 1
    total_before_bets = 0
    while True:
        try:
            
            time.sleep(2)
            channel_points = driver.find_element(By.CSS_SELECTOR, my_channel_points)
            channel_points.click()
            time.sleep(2)

            # Getting started prompt happens during the first loop only.
            try:
                driver.find_element(By.XPATH, getting_started_prompt).click()
            except NoSuchElementException as e:
                pass

            time.sleep(2)
            driver.find_element(By.XPATH, channel_prediction_prompt).click()

            is_submission_closed = driver.find_element(
                By.CSS_SELECTOR, submission_text
            ).text.lower()

            # Checks if the submissions are closed or if voting has ended. Restarts the loop if True
            
            if "closed" in is_submission_closed:
                try:
                    driver.find_element(By.XPATH, x_button).click()
                except NoSuchElementException as e:
                    pass
                time.sleep(40)
                continue
            elif "ended" in is_submission_closed:
                try:
                    driver.find_element(By.XPATH, x_button).click()
                except NoSuchElementException as e:
                    pass
                time.sleep(40)
                continue
            else:
                pass

            try:
                my_points = driver.find_element(By.XPATH, points_xpath).text
                total_points = get_points(my_points)

                if total_points >= 250000:
                    points = 250000
                else:
                    points = total_points

                if current_loop_count > 4:
                    current_loop_count = 1
                    total_before_bets = 0

                if total_before_bets == 0:
                    total_before_bets = total_points

                # If our new total is higher than when we started, we won.
                if total_before_bets > total_points:
                    current_loop_count = 1
                    total_before_bets = total_points

                six_percent = (round(points * 0.0625))
                points_to_bet = how_much_to_bet(six_p=six_percent, current_loop=current_loop_count)

            except NoSuchElementException as e:
                try:
                    driver.find_element(By.XPATH, x_button).click()
                except NoSuchElementException as e:
                    continue
                continue

            total_time_remaining = driver.find_element(By.XPATH, timer).text
            total_time_for_func = total_time_remaining.split()[0]  # Getting the 0:00 time remaining
            time_set(total_time_for_func)  # Sleeps until 1 minute remaining
            time.sleep(2)

            # Getting total votes for blue and red
            tbv = driver.find_element(By.XPATH, blue_votes).text
            trv = driver.find_element(By.XPATH, red_votes).text

            if tbv == "":
                total_blue_votes = 0
            else:
                total_blue_votes = get_points(tbv)

            if trv == "":
                total_red_votes = 0
            else:
                total_red_votes = get_points(trv)

            # Voting on the 'least' likely option. Whatever has the fewest submissions.
            # Votes 6.25% * N for n loop counts. Maximum of 4 bets before we're out of points.
            # Increases our loop counter
            # Appends to our 'Twitch Prediction History.txt' log file with all relevant data regarding voting.
            driver.find_element(By.XPATH, channel_points_reward_body).click()
            if total_blue_votes > total_red_votes:
                red = driver.find_element(By.XPATH, red_field)
                red.click()
                red.send_keys(points_to_bet)
                time.sleep(2)
                red_vote_button = driver.find_element(By.XPATH, red_button)
                red_vote_button.click()
                time.sleep(2)
                driver.find_element(By.XPATH, red_end).click()

                time_now = datetime.datetime.now().strftime('%H:%M:%S')
                formatted_date = datetime.datetime.now().strftime('%b-%d-%y')
                with open("Twitch Prediction History.txt", "a") as f:
                    f.write(
                        f"Streamer: {CHANNEL_NAME} | Points Bet: {points_to_bet} | Color: Red|"
                        f" Loop Count: {current_loop_count} "
                        f"Time: {time_now} | Date: {formatted_date}\n"
                    )

            else:
                blue = driver.find_element(By.XPATH, blue_field)
                blue.click()
                blue.send_keys(points_to_bet)
                time.sleep(2)
                blue_vote_button = driver.find_element(By.XPATH, blue_button)
                blue_vote_button.click()
                time.sleep(2)
                driver.find_element(By.XPATH, blue_end).click()

                time_now = datetime.datetime.now().strftime('%H:%M:%S')
                formatted_date = datetime.datetime.now().strftime('%b-%d-%y')
                with open("Twitch Prediction History.txt", "a") as f:
                    f.write(
                        f"Streamer: {CHANNEL_NAME} | Points Bet: {points_to_bet} | Color: Blue |"
                        f" Loop Count: {current_loop_count} "
                        f"Time: {time_now} | Date: {formatted_date}\n"
                    )

            current_loop_count += 1
        except (NoSuchElementException, ElementClickInterceptedException) as e:
            pass

        time.sleep(40)
