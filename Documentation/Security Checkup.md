# Security Checkup
This is a security checkup for the TTE bot as of 4/9/24.

## Heroku and Second Hosting-Only Repository
In order to use direct GitHub integration with Heroku, Heroku requires you to be the owner of the repository or the user hosting the app must have admin level access in a organization repository. In order to get around this, I (John Behrens) had to clone the necessary files to another repository specifically made for hosting the bot.  In its current form, it is a manual process of copying over the relevant files to the hosting repository.

## Token Security
The current implementation has the Discord Oauth token in raw form in the files and GitHub repository.  In its current form, it would be unsafe to ever make the main repository or the separate hosting repository public.  If there is ever a need or desire to make either of the repositories public, it would be necessary to reset the current token so that threat actors cannot run malicious code on the bot.

## User Input Risk
The bot currently intakes user messages to convert words to emojis.  There could be risks of code injection attacks, but how likely such an attack would occur is currently unknown.
