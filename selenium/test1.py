#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import re
import sys
import datetime
import random
from inspect import currentframe, getframeinfo

host = '172.17.37.180'
username = 'admin'
passwd = 'admin'
Log_File = "/var/log/webtest/"+datetime.date.today().strftime('%Y-%m-%d')
test_mode = True

class color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    END = '\033[0m'

def Login(browser, username, passwd):
    try:
        WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']")))
    except:
        return False
    browser.find_element_by_class_name('login-form-btn.login-btn.qStr').click()
    time.sleep(1)
    browser.find_element_by_id('username').send_keys(username)
    browser.find_element_by_id('pwd').send_keys(passwd)
    browser.find_element_by_id('submit').click()
    try:
        WebDriverWait(browser, 30).until(
        EC.visibility_of_element_located((By.XPATH, "//button[text()='admin']"))
        )
    except:
        return False

    return True

def Write_Log(message):
    with open(Log_File, 'a+') as fd:
        fd.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S  ')+ message +"\n")
    print message

def main(*argv):
    interface = sys.argv[1] if len(argv) > 1 else 'eth3'
    Write_Log("<<IPv4 Static IP Set Up>> Starting")
    profile = webdriver.FirefoxProfile()
    browser = webdriver.Firefox(profile)
    if test_mode:
        browser.set_window_size(80,90)
        time.sleep(1)
        browser.set_window_position(800,10)
        time.sleep(1)
        browser.set_window_size(800,900)
        time.sleep(2)
    browser.get('http://'+host)

    if not Login(browser, username, passwd):  # Login Test
        Write_Log(color.RED+"Login Fail"+color.END)
        sys.exit(0)

    browser.get('http://'+ host +':8084/apps/netmgr/?mod=tcpip')
    time.sleep(5)

    while browser.find_element_by_xpath("//div[@id='LockOverlayDiv']").is_displayed():
        time.sleep(2)

    if interface_exist(browser, 'bond'):
        Write_Log(color.RED+"Bonding Exist !!Fail"+color.END)
        sys.exit(0)

    time.sleep(2)

    while not EC.element_to_be_clickable((By.XPATH, "//div[@data-interface='"+interface+"']/div[1]/div[5]")):
        time.sleep(2)
        print "Wait interface-list-container"

    Write_Log("Interfaces List Page Loaded")

    browser.find_element_by_xpath("//div[@data-interface='"+interface+"']/div[1]/div[5]").click()


    try:
        WebDriverWait(browser,10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='ipv4-fixed']"))
        )
    except:
        Write_Log("Config Button Not Present!!Failed")

    browser.find_element_by_xpath("//span[@lankey='ip_setting_2']").click()
    time.sleep(1)

    while True:
        profile.set_preference("javascript.enabled", False)
        static_ip = '192.168.'+str(random.randint(0,100))+'.'+str(random.randint(1,100))
        static_ip = static_ip.split('.')
        browser.find_element_by_xpath("//tbody/tr[3]/td[3]/input[1]").clear()
        browser.find_element_by_xpath("//tbody/tr[3]/td[3]/input[1]").send_keys(static_ip[0])
        browser.find_element_by_xpath("//tbody/tr[3]/td[4]/input[1]").clear()
        browser.find_element_by_xpath("//tbody/tr[3]/td[4]/input[1]").send_keys(static_ip[1])
        browser.find_element_by_xpath("//tbody/tr[3]/td[5]/input[1]").clear()
        browser.find_element_by_xpath("//tbody/tr[3]/td[5]/input[1]").send_keys(static_ip[2])
        browser.find_element_by_xpath("//tbody/tr[3]/td[6]/input[1]").clear()
        browser.find_element_by_xpath("//tbody/tr[3]/td[6]/input[1]").send_keys(static_ip[3])

        netmask = '255.255.252.0'
        netmask = netmask.split('.')
    # must excute twice to choose correctly
        browser.find_element_by_xpath("//select[@class='qselect IPv4_form n_ip netmask1']/option[@value="+netmask[0]+"]").click()
        browser.find_element_by_xpath("//select[@class='qselect IPv4_form n_ip netmask1']/option[@value="+netmask[0]+"]").click()
        browser.find_element_by_xpath("//select[@class='qselect IPv4_form n_ip netmask2']/option[@value="+netmask[1]+"]").click()
        browser.find_element_by_xpath("//select[@class='qselect IPv4_form n_ip netmask2']/option[@value="+netmask[1]+"]").click()
        browser.find_element_by_xpath("//select[@class='qselect IPv4_form n_ip netmask3']/option[@value="+netmask[2]+"]").click()
        browser.find_element_by_xpath("//select[@class='qselect IPv4_form n_ip netmask3']/option[@value="+netmask[2]+"]").click()
        browser.find_element_by_xpath("//select[@class='qselect IPv4_form n_ip netmask4']/option[@value="+netmask[3]+"]").click()
        browser.find_element_by_xpath("//select[@class='qselect IPv4_form n_ip netmask4']/option[@value="+netmask[3]+"]").click()

        static_gateway = [static_ip[0], static_ip[1], static_ip[2], '200']
        browser.find_element_by_xpath("//input[@class='qinput IPv4_form js-gateway first g_ip static_gateway1']").clear()
        browser.find_element_by_xpath("//input[@class='qinput IPv4_form js-gateway first g_ip static_gateway1']").send_keys(static_gateway[0])
        browser.find_element_by_xpath("//input[@class='qinput IPv4_form js-gateway g_ip static_gateway2']").clear()
        browser.find_element_by_xpath("//input[@class='qinput IPv4_form js-gateway g_ip static_gateway2']").send_keys(static_gateway[1])
        browser.find_element_by_xpath("//input[@class='qinput IPv4_form js-gateway g_ip static_gateway3']").clear()
        browser.find_element_by_xpath("//input[@class='qinput IPv4_form js-gateway g_ip static_gateway3']").send_keys(static_gateway[2])
        browser.find_element_by_xpath("//input[@class='qinput IPv4_form js-gateway last g_ip static_gateway4']").clear()
        browser.find_element_by_xpath("//input[@class='qinput IPv4_form js-gateway last g_ip static_gateway4']").send_keys(static_gateway[3])

        browser.find_element_by_xpath("//select[@class='qselect l long network_speed']/option[@value=100]").click()

        profile.set_preference("javascript.enabled", True)
        start = time.time()
        browser.find_element_by_xpath("//input[@value='Apply']").click()

        time.sleep(5)
#        tmp = browser.find_element_by_xpath("//input[@lankey='close' and @value='Close']").get_attribute('style')
        try:
            if browser.find_element_by_xpath("//span[@lankey='ip_duplicate_alert_desc']").is_displayed():
                flag = True
        except:
            flag = False

        if flag:
#            print "visible"
            browser.find_element_by_xpath("//input[@lankey='close' and @value='Close']").click()
            Write_Log("IP Duplicate")
        else:
#            print "GOOD"
            break
        time.sleep(2)

    try:
        WebDriverWait(browser, 20).until(
        EC.invisibility_of_element_located((By.XPATH, "//div[@id='LockOverlayDiv']"))
    )
    except:
        Write_Log("Static IP Set Up Fail in line 141")

    Write_Log('IPv4 STATIC Spend: {0:.3f}s'.format(time.time() - start))

# verify Static IP Set Result

    try:
        WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@data-interface='"+interface+"']/div[@class='qtblDiv']/div[@alt_lankey='information']"))
        )
    except:
        Write_Log("Static IP Set Up Fail in line {0.filename}@{0.lineno}".format(getframeinfo(currentframe())))

    browser.find_element_by_xpath("//div[@data-interface='"+interface+"']/div[@class='qtblDiv']/div[@alt_lankey='information']").click()
    time.sleep(1)

    result = browser.find_element_by_xpath("//span[@name='dhcp']").text.encode('ascii', 'ignore').lower()
    result_static_ip = browser.find_element_by_xpath("//span[@name='ip_address']").text
    static_ip = unicode('.'.join(static_ip), 'unicode-escape')
#    if result == 'static' and result_static_ip == '.'.join(static_ip):
    if result == 'static' and static_ip == result_static_ip:
#check if IP and Status are correct
        Write_Log('IPv4 STATIC Verify '+color.GREEN +'Successfully'+color.END)
        Write_Log('Interface: '+interface)
    else:
        Write_Log('IPv4 STATIC Verify '+color.RED+'Failed'+color.END)

    browser.find_element_by_xpath("//input[@lankey='close']").click()
    Write_Log("<<IPv4 Static IP Set Up>> END")

### DHCP
    Write_Log("<<IPv4 DHCP IP Set Up>> Start")

    try:
        WebDriverWait(browser,10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@data-interface='"+interface+"']/div[1]/div[5]"))
        )
        browser.find_element_by_xpath("//div[@data-interface='"+interface+"']/div[1]/div[5]").click()
    except:
        Write_Log("Interface Set Up Page Loading Fail")
        sys.exit(0)

    try:
        WebDriverWait(browser,10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@lankey='ip_setting_3']"))
        )
        browser.find_element_by_xpath("//span[@lankey='ip_setting_3']").click()
    except:
        Write_Log("Config Button Not Present")

    start = time.time()
    browser.find_element_by_xpath("//input[@value='Apply']").click()

    time.sleep(2)
    try:
        WebDriverWait(browser, 10).until(
        EC.invisibility_of_element_located((By.XPATH, "//span[@lankey='configure']"))
    )
        WebDriverWait(browser, 10).until(
        EC.invisibility_of_element_located((By.XPATH, "//div[@id='LockOverlayDiv']"))
    )
    except:
        Write_Log("DHCP IP Set Up Fail")

    Write_Log('IPv4 DHCP Spend: {0:.3f}s'.format(time.time() - start))

    browser.find_element_by_xpath("//div[@data-interface='"+interface+"']/div[@class='qtblDiv']/div[@alt_lankey='information']").click()
    time.sleep(1)

    result = browser.find_element_by_xpath("//span[@name='dhcp']").text.encode('ascii', 'ignore').lower()
    if result == 'dhcp':
        Write_Log('IPv4 DHCP Verify '+color.GREEN +'Successfully'+color.END)
        Write_Log('Interface: '+interface)
    else:
        Write_Log('IPv4 DHCP Verify '+color.RED+'Failed'+color.END)

    browser.find_element_by_xpath("//input[@lankey='close']").click()
    Write_Log("<<IPv4 DHCP IP Set Up>> END")

    browser.quit()
    Write_Log("-------------------------")

def interface_exist(browser, interface):
    for i in browser.execute_script("return _mod.if_sorted"):
        if re.findall(interface, i.encode('utf-8')):
            return True
    return False

if __name__ == '__main__':
    main(sys.argv)
