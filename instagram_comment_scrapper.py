from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service(executable_path="chromedriver.exe")
browser = webdriver.Chrome(service=service)


browser.get("https://www.instagram.com/")
browser.maximize_window()
time.sleep(5)


email = browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")
password = browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")



email.send_keys("*********@hotmail.com") #You need to put your email here
password.send_keys("*********") #You need to put your password here
time.sleep(2)


login_button = browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]/button")
login_button.click()
time.sleep(10)


save_info = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div") #When the account opens, if there is no save info part make this 4 row comment block.
time.sleep(3)
save_info.click()
time.sleep(5)


not_now = browser.find_element(By.CLASS_NAME,"_a9--._ap36._a9_1")
time.sleep(3)
not_now.click()
browser.maximize_window()
time.sleep(5)

account_name= "lucifermichaelson" # You have to follow this person and make the account name exact

base_url = "https://www.instagram.com/"

dynamic_link = base_url + account_name


search_bar = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div")
time.sleep(3)
search_bar.click()
browser.maximize_window()
time.sleep(5)


search_text = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input")
time.sleep(3)
search_text.send_keys(account_name)
time.sleep(5)


searched_items = browser.find_elements(By.CLASS_NAME, "x1i10hfl.x1qjc9v5.xjbqb8w.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3")
time.sleep(3)
searched_items[0].click()
time.sleep(5)


comment_list = []

for i in range(0,25): # This means how many post you want to take comment from optimal is 25 if you making this 25 you need to make 3 or more at below loop with j unless it will cause error

    for j in range(1,5):
        scrollable_element = browser.find_element(By.XPATH,"/html") 
        browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_element)  # Scroll down inside the element using JavaScript
        time.sleep(3)

    time.sleep(5) #You should increase the sleep time for save all the posts

    All_Posts = browser.find_elements(By.CLASS_NAME, "_aagw")
    time.sleep(3)

    All_Posts[i].click()
    time.sleep(3)

    three_dot = browser.find_element(By.CSS_SELECTOR, "body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe.x1qjc9v5.xjbqb8w.x1lcm9me.x1yr5g0i.xrt01vj.x10y3i5r.xr1yuqi.xkrivgy.x4ii5y1.x1gryazu.x15h9jz8.x47corl.xh8yej3.xir0mxb.x1juhsu6 > div > article > div > div.x1qjc9v5.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x78zum5.xdt5ytf.x1iyjqo2.x5wqa0o.xln7xf2.xk390pu.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x65f84u.x1vq45kp.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x11njtxf > div > div > div._aasi > div > div > div > div")
    time.sleep(3) 

    three_dot.click()
    time.sleep(3)

    post_links = browser.find_elements(By.CLASS_NAME, "_a9--._ap36._a9_1")
    time.sleep(3)

    post_links[0].click()
    time.sleep(3)

    PostComment_scroll = browser.find_element(By.CLASS_NAME, "x5yr21d.xw2csxc.x1odjw0f.x1n2onr6")
    time.sleep(3)
    
    for k in range(1,25): # If you want to take more you can make it 50 or more, optimal is 50
        
        browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", PostComment_scroll)  # Scroll down inside the element using JavaScript
        time.sleep(3) 
    
    post_content = browser.find_elements(By.CLASS_NAME,"x1lliihq.x1plvlek.xryxfnj.x1n2onr6.x193iq5w.xeuugli.x1fj9vlw.x13faqbe.x1vvkbs.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.x1i0vuye.xvs91rp.xo1l8bm.x5n08af.x10wh9bi.x1wdrske.x8viiok.x18hxmgj")
    time.sleep(3)

    #Comment class that who posted x193iq5w.xeuugli.x1fj9vlw.x13faqbe.x1vvkbs.xt0psk2.x1i0vuye.xvs91rp.xo1l8bm.x5n08af.x10wh9bi.x1wdrske.x8viiok.x18hxmgj

    for comments in post_content:
        comment_list.append(comments.text)

    browser.get(dynamic_link)

with open("Comments.txt","w",encoding= "UTF-8") as file:
    for comment in comment_list:
        file.write(comment +"\n")


time.sleep(10)
browser.quit()