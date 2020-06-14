from selenium import webdriver
import selenium
import time,sys,os,shutil,zipfile
from sys import platform


print("\n\nProcessing.....")

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

def delete_dup_file():
    print("info: Checking duplicate files. ")
    file_to_del = {}
    items = os.listdir(from_path)
    for names in items:
        if names.startswith("ItemReport"):
            full_file_path = os.path.join(from_path, names)
            file_to_del[names] = full_file_path
        else:
            print("info: no duplicate files found")
    # print("Deleting: Some file with the same name is already there")
    for name,path in file_to_del.items():
            print("Deleting: "+name+" file with the same name is already there")
            os.remove(path)
            print("success: Done Deleting"+name)


def find_file(from_path):
    while(True):
        items = os.listdir(from_path)
        for names in items:
            if names.startswith("ItemReport"):
                filename = names
                return filename
            else:
                print("info: waiting for file to download")
                time.sleep(5)



if platform == "linux" or platform == "linux2":
    # linux
    path = resource_path('driver/chromedriver')
else:
    path = resource_path('driver/chromedriver.exe')
    # Windows...

# current working path
des_path = sys.path[0]
# Detecting linux or windows
if platform == "linux" or platform == "linux2":
    from_path = str(sys.path[4]).replace(".local/lib/python3.8/site-packages",
    "Downloads")
else:
    from_path = str(sys.path[-1]).replace("AppData\\Local\\Programs\\Python\\Python38-32\\lib\\site-packages",
    "Downloads")

delete_dup_file()


driver =webdriver.Chrome(path)
# open link
req=driver.get('https://supplier.walmart.com/')

if(driver.title == "Privacy error" or driver.title == "supplier.walmart.com") :
    print("\n\nerror: its a privacy error")
    driver.find_element_by_id("details-button").click()
    driver.find_element_by_id("proceed-link").click()
else:
    print("\n\nsuccess: Got no privacy error")
time.sleep(3)
# click login
driver.find_element_by_id("loginPage").click()
time.sleep(3)

# enter email
email = driver.find_element_by_xpath("//input[@class='form-control__formControl___3uDUX']").send_keys('developer@poschsports.com')
# enter pass
# driver.find_element_by_id("pwd").send_keys("developer@poschsports.com")

while(True):
    if(driver.title == "Retail Link"):
        print("waiting: user input...")
        time.sleep(5)
    else:
        print("success: Going to dashboard")
        break

# click download
time.sleep(3)
# driver.find_element_by_class_name("icon-download").click()
driver.find_element_by_css_selector("button.icon-download").click()

print("\nSuccess: Clicked on Download")
# driver.find_element_by_link_text("Download").click()
# driver.find_element_by_tag_name("label").click()
time.sleep(3)
# click download report
driver.find_element_by_css_selector('button.wm-btn-blue.btn-download').click()

print("\nSuccess: Clicked download report")


time.sleep(2)
# Move from downloads to this folder
report_fname= find_file(des_path)

if(os.path.exists(from_path)):
    if platform == "linux" or platform == "linux2":
        from_path = from_path+"/"+report_fname
    else:
        from_path = from_path+"\\"+report_fname
shutil.move(from_path,des_path)
print("Success: moving file.")


driver.close()
print("success: closed window.")

time.sleep(3)

with zipfile.ZipFile(os.path.join(des_path,report_fname),"r") as zip_ref:
    zip_ref.extractall("zip")


print("\n\nComplete....")