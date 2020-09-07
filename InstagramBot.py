
"""
@author: Kianoush 

GitHUb:https://github.com/Kianoush-h
YouTube: https://www.youtube.com/channel/UCvf9_53f6n3YjNEA4NxAkJA?view_as=subscriber
LinkedIn: https://www.linkedin.com/in/kianoush-haratiannejadi/

Email: haratiank2@gmail.com

"""



from instabot import Bot


username_ = 'kia_python'
password_ = 'KIA_python@'

bot = Bot()
bot.login(username = username_,
          password = password_)



tag_list = ['python', 'programmer', 'Kinaoush'],

for i in tag_list:
    bot.like_hashtag(i)
    

users = ['python','python.learning','codder', 'kinaoush']

bot.follow_users(user_ids='python.learning')



locs = ['Montreal', 'Canada', 'US','Iran']

for i in locs:
    bot.like_location_feed(i,amount=10)




