#!/usr/bin/python
import os
import sys
import datetime
import time
import twitter

def test():

        #run speedtest-cli
        print 'Testing some blazing fast internet speeds'
        a = os.popen("sudo speedtest-cli --simple").read()
        print 'ran'
        #split the 3 line result (ping,down,up)
        lines = a.split('\n')
        print a
        ts = time.time()
        date =datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        #if speedtest couldn't connect set the speeds to 0
        if "Cannot" in a:
                p = 100
                d = 0
                u = 0
        #extract the values for ping down and up values
        else:
                p = lines[0][6:11]
                d = lines[1][10:14]
                u = lines[2][8:11]
        print date,p, d, u


        #connect to twitter
        #you'll get these tokens and security keys when you create your twitter app
        TOKEN="xxxxxxxxxxxxxxxxxx"
        TOKEN_KEY="xxxxxxxxxxxxxxxxx"
        CON_SEC="xxxxxxxxxxxxxxxxxxxxxx"
        CON_SEC_KEY="xxxxxxxxxxxxxxxxxxxx"

        my_auth = twitter.OAuth(TOKEN,TOKEN_KEY,CON_SEC,CON_SEC_KEY)
        twit = twitter.Twitter(auth=my_auth)

        #try to tweet if speedtest couldnt connet.
        #Replace the @xxxx with the Twitter handle of who you want to Tweet at
        if "Cannot" in a:
                try:
                        tweet="Hey @xxxx  internet issues?"
                        twit.statuses.update(status=tweet)
                except:
                        pass

        # tweet if upload speed is less than 1 Mb/s
        elif eval(u)<1:
                print "Tweeting provider with a look of slight anger and disappointment"
                try:
                        tweet="Hey @xxxx My upload speed is currently less than" + str(int(eval(u))) + " Mb/sec. WTF!\\"
                        twit.statuses.update(status=tweet)
                except Exception,e:
                        print str(e)
                        pass
        return
        
if __name__ == '__main__':
        test()
        print 'completed'
