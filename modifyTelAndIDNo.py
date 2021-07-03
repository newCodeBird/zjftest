import os, time
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
# this is upload test

class WebObj(object):

    def __init__(self,url,dic):
        ip = url
        # 获取谷歌插件的位置
        # 用谷歌浏览器开启
        # driver = webdriver.Chrome(executable_path=chr_path)
        self.driver = webdriver.Chrome()
        self.driver.get(ip)
        self.driver.implicitly_wait(2)
        self.dic = dic

    def login(self, user, pwd):
        web = self.driver

        # 输入指定帐号
        time.sleep(2)
        web.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[2]/form/div[1]/input').clear()
        web.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[2]/form/div[1]/input').send_keys(user)
        # 输入密码
        time.sleep(2)
        web.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[2]/form/div[2]/input').clear()
        web.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[2]/form/div[2]/input').send_keys(pwd)
        # 点击
        time.sleep(10)

    def folder(self,code):
        web = self.driver
        try:
            # 找到左侧待办箱
            wait_todo_button = WebDriverWait(web, 10, 0.5).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/ul/li[2]/a/span[1]')))
            # 增加延时，否则有些信息收不到
            time.sleep(0.1)
            print('i have find ：', wait_todo_button.text)
            wait_todo_button.click()

            time.sleep(2)
            web.switch_to.frame(1)
            print('enter submit list')

            print('find serach textbox')
            first_item_textbox = WebDriverWait(web, 30, 0.5).until(EC.presence_of_element_located( \
                (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[1]/div[2]/div/input')))
            # 增加延时，否则有些信息收不到
            time.sleep(0.1)
            first_item_textbox.clear()
            first_item_textbox.send_Keys(code)
            print('search input ：', first_item_textbox.text)
            #find search button
            search_button = WebDriverWait(web, 30, 0.5).until(EC.element_to_be_clickable( \
                (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[2]/span/button[1]')))
            time.sleep(0.1)
            web.execute_script("$(arguments[0]).click()", search_button)
            print('click：', search_button.text)

            print('enter edit page')

            # we are now in first frame,we need back to paretn to select edit page
            web.switch_to.parent_frame()
            web.switch_to.frame(2)
            time.sleep(1)

            print('find radio')
            web.switch_to.frame('infoFrame')
            radio = WebDriverWait(web, 30, 0.5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/table/tbody/tr[9]/td/div/div/div/div[2]/div/div/table/tbody/tr[2]/td/div[2]/div/table/tbody/tr[1]/td/div[2]/div/div/label[1]/input')))
            radio.click()

            print('text area')
            checkbox = WebDriverWait(web, 30, 0.5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/table/tbody/tr[7]/td/div/div/div/div[2]/div/div/table/tbody/tr[3]/td/div[2]/div/table/tbody/tr[1]/td/div/div/div/label[1]/input')))
            checkbox.click()
            time.sleep(0.1)
            checkbox.click()
            time.sleep(0.1)
            checkbox.click()

            textarea = WebDriverWait(web, 30, 0.5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/form/div[1]/div[2]/div[2]/div/div/div/table/tbody/tr[9]/td/div/div/div/div[2]/div/div/table/tbody/tr[2]/td/div[2]/div/table/tbody/tr[2]/td/div[2]/div/div/textarea')))
            textarea.clear()
            textarea.send_keys("通过")

            web.switch_to.parent_frame()
            parent_submit_btn = WebDriverWait(web, 30, 0.3).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[1]/div/div/button[2]')))

            time.sleep(0.1)
            print('click：', parent_submit_btn.text)
            parent_submit_btn.click()

            time.sleep(2)
            web.switch_to.frame('layui-layer-iframe3')
            comfirm_submit_btn = WebDriverWait(web, 30, 0.5).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div[2]/div[2]/button')))
            time.sleep(0.5)
            web.execute_script("$(arguments[0]).click()", comfirm_submit_btn)
            print('click：', comfirm_submit_btn.text)
            time.sleep(1)
            print("web refresh")
            web.refresh()
        except Exception as e:
            return print(e)
        finally:
            self.driver = web
            web.refresh()

    # ActionChains(web).send_keys(Keys.ENTER).perform() 自动按回车键

    def quit(self):
        self.driver.quit()


if __name__ == '__main__':

    dic = {}
    with open('C:\\Users\\Administrator\\Desktop\\5w证件.txt') as f:
        ll = f.readlines()
        for i in ll:
            strs = i.split(',')
            sd = []
            for j in strs:
                j = j.strip()
                sd.append(j)
            dic[strs[0]] = sd


    myweb = WebObj("http://19.129.236.7/FSWFJSMIS/login",dic)
    myweb.login("wuyj","11327X")

    for i in dic:
        myweb.folder(i)
    time.sleep(10)
