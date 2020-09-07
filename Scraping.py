
"""
@author: Kianoush 

GitHUb:https://github.com/Kianoush-h
YouTube: https://www.youtube.com/channel/UCvf9_53f6n3YjNEA4NxAkJA?view_as=subscriber
LinkedIn: https://www.linkedin.com/in/kianoush-haratiannejadi/

Email: haratiank2@gmail.com

"""



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd


username_ = 'kia_python'
password_ = 'KIA_python@'

hashtag_list = ['python proj', 'best', 'code', 'linux', 'insta']


# chromedriver_path = 'chromedriver.exe' # Change this to your own chromedriver path!
webdriver = webdriver.Firefox(executable_path='./geckodriver.exe')
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = webdriver.find_element_by_name('username')
username.send_keys(username_)
password = webdriver.find_element_by_name('password')
password.send_keys(password_)

button_login = webdriver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[3]/button/div')
button_login.click()
sleep(3)

notnow = webdriver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
notnow.click() 



for i in range(3):
    try:
        notnow = webdriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        notnow.click()
    except:
        pass
    




new_followed = []
tag = -1
followed = 0
likes = 0
comments = 0

prev_user_list = []




for hashtag in hashtag_list:
    try:
        tag += 1
        webdriver.get('https://www.instagram.com/explore/tags/'+ hashtag_list[tag] + '/')
        sleep(5)
        first_thumbnail = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
        
        first_thumbnail.click()
        sleep(5)    
        try:        
            for x in range(1,10):
                username = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/span/a').text
                
                if username not in prev_user_list:
                    
                    # If we already follow, do not unfollow
                    if webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow':
                        
                        webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
                        
                        new_followed.append(username)
                        followed += 1
    
                        # Liking the picture
                        button_like = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button/div/span')                    
                        button_like.click()
                        likes += 1
                        sleep(3)
    
                        # Comments and tracker
                        comm_prob = randint(1,10)
                        print('{}_{}: {}'.format(hashtag, x,comm_prob))
                        webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[2]/button/div').click()
                        comment_box = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div[1]/form/textarea')
                        
                        if comm_prob > 4:
                            comments += 1 
                            if (comm_prob > 8):
                                comment_box.send_keys('Really cool!')
                                sleep(1)
                            elif (comm_prob > 7) and (comm_prob < 9):
                                comment_box.send_keys('Nice work :)')
                                sleep(1)
                            elif comm_prob > 6:
                                comment_box.send_keys('Nice gallery!!')
                                sleep(1)
                            elif comm_prob > 5:
                                comment_box.send_keys('So cool! :)')
                                sleep(1)
                            # Enter to post comment
                            comment_box.send_keys(Keys.ENTER)
                            sleep(5)
    
                    # Next picture
                    webdriver.find_element_by_link_text('Next').click()
                    sleep(5)
                else:
                    webdriver.find_element_by_link_text('Next').click()
                    sleep(5)
        
        except:
            continue
    except:
        try:
            webdriver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/button[2]').click()
        except:
            continue




















