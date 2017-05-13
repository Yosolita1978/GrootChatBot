import praw
import secret
import random
import webbrowser
import time


def bot_loggin():
    "This function return your session in Reddit as an instance"
    reddit = praw.Reddit(username=secret.username,
                         password=secret.password,
                         client_id=secret.client_id,
                         client_secret=secret.client_secret,
                         user_agent=secret.user_agent)
    return reddit


def get_imgs_bot(reddit):

    jpg_url = []
    for submission in reddit.subreddit('wholesomememes').hot(limit=20):
        if submission.url.endswith(".jpg"):
            jpg_url.append(submission.url)

    return jpg_url


def random_url(lst):
    day_url = random.choice(lst)
    return day_url


if __name__ == '__main__':

    reddit = bot_loggin()
    if not reddit.read_only:
        print "Logged to Reddit!!"
    list_urls = get_imgs_bot(reddit)
    picture_day = random_url(list_urls)
    
    while True:
        ask_user = raw_input("Are you having a bad day? Y or N ?")
        if ask_user == "Y":
            number_pictures = len(list_urls)
            print "I have %i wholosome pictures to cheer you up" % (number_pictures)
            check = raw_input("Do you want a wholosome picture? Y or N ?")
            if check == "Y":
                webbrowser.open(picture_day)
                list_urls.remove(picture_day)
                picture_day = random_url(list_urls)
                print "I need a short break"
                time.sleep(5)

            else:
                print "Ok, see you soon!"
                break

        else:
            print "That's the spirit! Have a good one!"
            break
