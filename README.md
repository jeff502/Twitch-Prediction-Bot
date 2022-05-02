# Twitch-Prediction-Bot
Automatically bet on Twitch Predicitons

This bot works by taking 6.25% of your current channel points and bets it on the option with the least votes at sixity seconds remaining.\
Each time the bot fails to win, it'll double the current bet up to four total bets.\
Bets are recorded into a log file named `Twitch Prediction History.txt`.

The code is highly editable to fit your betting habits.
Change the `points_to_bet` variable to whatever you desire. \
Changing the default to either `blue` or `red` for always believing or doubting.


Change the `channel_name` to the streamer you want to use the bot on.\
Currently, this bot works on the pop out chat window. You can change this if desired.

You'll need to either upload your own cookies into the webdriver (recommended), or log in manually when the bot starts.

For uploading your own cookies, watch this Youtube video: https://youtu.be/vhjKJ7huN-w \
Put your cookies into the file named `twitch_cookies.csv`.

For logging in manually, set the intial sleep to two minutes and comment out (`ctrl+/`) lines `134-139` and uncomment (`ctrl+/`) line `141`. 
