
"""
@author: Kianoush 

GitHUb:https://github.com/Kianoush-h
YouTube: https://www.youtube.com/channel/UCvf9_53f6n3YjNEA4NxAkJA?view_as=subscriber
LinkedIn: https://www.linkedin.com/in/kianoush-haratiannejadi/

Email: haratiank2@gmail.com

"""



from instabot import Bot

import instabot 


username = 'kia_python'
password = 'KIA_python@'

bot = Bot()
bot.login(username = 'kia_python',
          password = 'KIA_python@')





tag_list = ['python', 'programmer', 'Kinaoush'],

for i in tag_list:
    bot.like_hashtag(i)
    

users = ['python','python.learning','codder', 'kinaoush']

bot.follow_users(user_ids='python.learning')



locs = ['Montreal', 'Canada', 'US','Iran']

for i in locs:
    bot.like_location_feed(i,amount=10)



bot = InstaBot('login', 'password',
               like_per_day=1000,
               more_than_likes=10,
               
               max_like_for_one_tag=5,
               log_mod = 0)


Bot(login = 'kia_python',
          password = 'KIA_python@',
          like_per_day = 1000,
            media_max_like=0,
            media_min_like=0,
            follow_per_day=0,
            follow_time=5*60*60,
            unfollow_per_day=0,
            comments_per_day=0,
            tag_list=['cat', 'car', 'dog'],
            max_like_for_one_tag = 5,
            unfollow_break_min = 15,
            unfollow_break_max = 30,
            log_mod = 0,
            proxy='')





