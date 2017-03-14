*This walkthrough assumes you already have experience using your pi through ssh and command line or terminal.*

*Update you Pi

sudo apt-get update
sudo apt-get upgrade

—————————

*Get these packages

sudo apt-get install python-setuptools
sudo easy_install pip
sudo pip install twython

——————————

*Next we’ll install speed test

pip install speedtest-cli

——————

*Then install Twitter onto your Pi

pip install python-twitter

python setup.py build

python setup.py install

——————————
*Create the Twitter app
Go to:
https://dev.twitter.com/
and create a new app. (You will need a twitter account for this.)

Fill in the name, description and website for your app.

We won’t be authenticating other users, you don’t need to worry about setting a Callback URL.

Find the permissions tab and check the access level of your app, it should be set to Read and Write.

Now we’ll need to create an OAuth access token for our app. This will let us login to our bot’s twitter account and post some tweets.

Make a note of your Consumer Key and Consumer Secret as well as your Access Token and Access Token Secret. You’ll need these later for you Python script.

———————————————
*Now shh into your Raspberry Pi. We’re going to make a directory that we can keep all of our code in:

sudo mkdir speedtest-twitter
cd speedtest-twitter
sudo nano speedtest-twitter.py

Once you’ve opened speedtest-twitter.py in nano (or whatever text editor you use) you’ll paste in the Python script.
(Python script is available on my Github)

Make sure you insert your Consumer Key, Consumer Secret, Access Key and Access Secret with the ones that you got from creating your app.

Once done, you can save the script and exit (CTRL + O, CTRL + X).

You also need to make sure that you are able to execute the file, you can do that by using the following command:

sudo chmod +x twitterbot.py

——————

Now you can start this script by going to the directory where your speedtest-twitter.py script is and trying
sudo python speedtest-twitter.py

————————
 
*You can set this to run automatically at specific times. I have mine set to run every 5 minutes.

To do this, you’ll have to edit your crontab file. Do this by typing 
sudo crontab -e

Mine looks like this…
*/5 * * * * /home/pi/speedtest-twitter/speedtest-twitter.py

*Disclaimer!!!
Don’t be dumb. If you do something stupid with this script it’s on you!





