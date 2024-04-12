# Testing Summary
## Manual Testing
The majority of our code was tested manually.  We had tried to think of as many possible scenarios of common words that would be used in Discord servers.  A lot of testing was done with the emoji dictionary to get more emoji to replace more words.
## Script Testing
We did some scripted testing with pyautogui to test the throughput and response time of the bot.  The results were that the bot is fairly slow, mostly because it is Python and running on our own computers.  The Discord client does timeout and slow down spam when you try to send to many messages.  