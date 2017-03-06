#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from urllib2 import urlopen
import time
import os
import sys

host='172.17.37.186'
account='admin'
passwd='soft7777'
#host='172.17.37.191'
#account='admin'
#passwd='admin'
#extension_path='/home/webtest/Downloads/extension_0_0_0_126.crx'
video_link='http://youtu.be/FLcxTKjpZGQ'
default_timeout = 5


def main():
    extension_path = get_extension_path()

    if extension_path == '':
        extension_link="https://clients2.google.com/service/update2/crx?response=redirect&prodversion=55.0.2883.867&x=id%3Dljciphafakdahicbelljmdbnadjopffb%26uc"
        print "no file"

        f = urlopen(extension_link)
        with open('/home/webtest/Downloads/HappyGet2.crx','a+') as fd:
            fd.write(f.read())

        print "file is downloaded"

    extension_path = get_extension_path()

#    print extension_path

    chop = webdriver.ChromeOptions()
    chop.add_extension(extension_path)

    browser = webdriver.Chrome(chrome_options=chop)
#    browser.set_window_size(950,600)
    browser.set_window_position(300,1)
    time.sleep(1)

    time.sleep(default_timeout)

    #'I Accept these term of use'
    browser.find_element_by_xpath("//label[@id='label_p1_chk_tos']").click()
    #'Next'
    browser.find_element_by_xpath("//input[@id='btn_p1_next']").click()

    time.sleep(default_timeout)
    #'NAS IP'
    browser.find_element_by_xpath("//input[@id='txt_p2_nas_address']").send_keys(host)
    #'admin'
    browser.find_element_by_xpath("//input[@id='txt_p2_nas_user']").send_keys(account)
    #'admin'
    browser.find_element_by_xpath("//input[@id='txt_p2_nas_password']").send_keys(passwd)

    # Connect button
    browser.find_element_by_xpath("//input[@id='btn_p2_nas_connect']").click()
    time.sleep(default_timeout*2)
    #'success'
    result = browser.find_element_by_xpath("//span[@id='span_p2_nas_connect_result']").text.encode('utf-8')

    if not result == 'Success':
        print 'result: {}'.format(result)
        print 'Connect to NAS Fail'
        sys.exit(0)
    #'Next'
    browser.find_element_by_xpath("//input[@id='btn_p2_next']").click()

    time.sleep(default_timeout)

    #'Next'
    browser.find_element_by_xpath("//input[@id='btn_p3_next']").click()

    time.sleep(default_timeout)
    #'Next'
    #browser.find_element_by_xpath("//input[@id='btn_p5_next']").click()

    #time.sleep(5)

    browser.get(video_link) # 卡提諾 053
    #browser.find_element_by_xpath("//input[@id=btn_reload_close]").click()

    # print browser.find_element_by_xpath("//div[@id='watch-header]/div[2]/div[2]/span[1]/button[1]'").get_attribute('id').encode('utf-8')
    time.sleep(default_timeout)
    video_name = browser.find_element_by_xpath("//div[@id='watch-headline-title']/h1[1]/span[1]").text.encode('utf-8')
    browser.find_element_by_xpath("//div[@id='watch-header']/div[2]/div[2]/span[1]/button[1]").click()

    time.sleep(default_timeout)
    browser.get('http://{}:8080/hg2/'.format(host))

    #browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND+'t')
    #browser.execute_script('''window.open("http://youtu.be");''')
    time.sleep(default_timeout)

    index=1
    video_list = []
    while True:
        try:
            task_name = browser.find_element_by_xpath("//div[@id='content']/div[@class='task']/div[1]/div["+str(index)+"]/div[1]").text.encode('utf-8')
#            print index, task_name
            video_list.append(task_name)
            index = index + 1
        except Exception as e:
    #        print type(e), e
            break

    for i,j in enumerate(video_list, 1):
        if video_name == j:
            index = i
            break

    #print 'index is: ',index

    video_name_status = "item src-youtube status-download"
    while video_name_status == "item src-youtube status-download":
        video_name_status = browser.find_element_by_xpath("//div[@id='content']/div[@class='task']/div[1]/div["+str(index)+"]").get_attribute("class").encode('utf-8')
        print "{} is downloading".format(video_name)
        time.sleep(default_timeout)

#    print video_name_status

    if video_name_status == 'item src-youtube status-completed':
        print "{} is donwload {}".format(video_name, "Successful")
    else:
        print "{} is donwload {}".format(video_name, "Failed")

    try:
        os.remove("/home/webtest/Downloads/HappyGet2.crx")
    except Exception as e:
       print str(e)
# This is clear
    browser.find_element_by_xpath("//div[@id='header']/div[@class='navbar-inner']/div[@class='container']/ul[1]/li[7]").click()



def get_extension_path():
    for i in os.listdir('/home/webtest/Downloads'):
        if '.crx' in i:
            return  '/home/webtest/Downloads/'+i
    return ''

if __name__ == '__main__':
    main()
