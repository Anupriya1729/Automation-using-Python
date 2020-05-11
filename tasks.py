# Modules to be imported.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from google_images_download import google_images_download
import requests

print ("Welcome to Selenium Automation")
print("ENTER 1 to send an email")
print("ENTER 2 to send check broken hyperlinks")
print("ENTER 3 to download top 10 photos")
n=int(input("ENTER YOUR CHOICE : "))

if n==1:
    # Your login details.
    email = "anupriya91998@gmail.com"
    passwd = "asdfghjkl456@"
    recieve_email=input("Enter the target email : ")
    sub=input("Enter the subject : ")
    msg=input("Enter your message : ")

    # Browser : chrome.
    options = webdriver.ChromeOptions() 
    options.add_argument("start-maximized")
    options.add_argument('disable-infobars')
    driver=webdriver.Chrome(options=options, executable_path=r'C:\chromedrivers\chromedriver')
    driver.get("http://www.gmail.com")
    time.sleep(2)

    # GMAIL login.
    username=driver.find_element_by_css_selector("#identifierId.whsOnd.zHQkBf")
    username.send_keys(email)
    time.sleep(2)
    n=driver.find_element_by_css_selector(".RveJvd.snByac")
    n.click()
    time.sleep(2)
    password=driver.find_element_by_css_selector(".whsOnd.zHQkBf")
    password.send_keys(passwd)
    time.sleep(2)
    login=driver.find_element_by_css_selector(".RveJvd.snByac")
    login.click()

    #SEND email.
    """
    Write a program that takes an email address and string of text on the command line and then, using Selenium,
    logs into your email account and sends an email of the string to the provided address. 

    """
    time.sleep(7)

    composeElem=driver.find_element_by_css_selector("#\:ki > div > div")
    composeElem.click()

    time.sleep(7)

    toElem = driver.find_element_by_name("to")
    toElem.send_keys(recieve_email)

    time.sleep(2)

    subjElem = driver.find_element_by_name("subjectbox")
    subjElem.send_keys(sub)

    time.sleep(7)

    bodyElem = driver.find_element_by_css_selector('#\:rb')
    bodyElem.send_keys(msg)
    time.sleep(4)

    sendmsg = driver.find_element_by_css_selector('#\:pw')
    sendmsg.click()

    # GMAIL logout.
    logout11=driver.find_element_by_css_selector("#gb > div.gb_Pd.gb_6d.gb_Xd > div.gb_Wc.gb_Oa.gb_Vc.gb_4d > div > div.gb_Ja.gb_gd.gb_Ag.gb_g.gb_Kf > div > a")
    logout11.click()
    time.sleep(2)
    logout1=driver.find_element_by_css_selector(".gb_8a")
    logout1.click()
    time.sleep(2)
    logout2=driver.find_element_by_css_selector("#gb_71")
    logout2.click()

    # Closing Browser.
    driver.quit()
    print("Message sent")

elif n==2:
    website=input("Enter the website name: ")
    options = webdriver.ChromeOptions() 
    options.add_argument("start-maximized")
    options.add_argument('disable-infobars')
    driver=webdriver.Chrome(options=options, executable_path=r'C:\chromedrivers\chromedriver')
    driver.get(website)
    links = driver.find_elements_by_css_selector("a")
    c=0
    for link in links:
        r = requests.head(link.get_attribute('href'))
        print(link.get_attribute('href'), r.status_code)
    driver.quit()
    print("Task completed")

elif n==3:
    # details.
    search = input("search keyword : ")

    # Browser : chrome.
    options = webdriver.ChromeOptions() 
    options.add_argument("start-maximized")
    options.add_argument('disable-infobars')
    driver=webdriver.Chrome(options=options, executable_path=r'C:\chromedrivers\chromedriver')
    driver.get("https://www.google.com/imghp?hl=en")
    time.sleep(2)

    # search
    s=driver.find_element_by_css_selector("#sbtc > div > div.a4bIc > input")
    s.send_keys(search)
    s.submit()
    time.sleep(2)

    #find all images
    images = driver.find_elements_by_tag_name('img')
      
    #download first 10 images
    response = google_images_download.googleimagesdownload()
    arguments = {"keywords":search,"limit":10,"print_urls":True}
    paths = response.download(arguments)

    driver.quit()
    print("Downloaded Successfully")

else:
    print("Invalid Input")

