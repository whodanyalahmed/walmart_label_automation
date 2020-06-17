from selenium import webdriver
import selenium
from os.path import join
import time,sys,os,shutil,zipfile,pandas
from sys import platform


print("\n\nProcessing.....")

def resource_path(relative_path):
    base_path = sys.path[0]
    return os.path.join(base_path, relative_path)

def delete_dup_file():
    prompt = input("prompt: You wanted to Delete all files with the name ItemReport in Downloads:(y/n) ")
    if(prompt == "y" or prompt == "Y"):
        print("\ninfo: Checking duplicate files. ")
        file_to_del = {}
        items = os.listdir(from_path)
        for names in items:
            
            if names.startswith("PO_Data"):
                full_file_path = os.path.join(from_path, names)
                file_to_del[names] = full_file_path
            # else:
            #     print("info: no duplicate files found")
        # print("Deleting: Some file with the same name is already there")
        for name,path in file_to_del.items():
                print("\nDeleting: "+name+" file with the same name is already there")
                os.remove(path)
                print("\nsuccess: Done Deleting"+name)
    else:
        print("\ninfo: Ignoring duplicate files in downloads")

def find_file(from_path):
    while(True):
        items = os.listdir(from_path)
        for names in items:
            if names.startswith("PO_Data"):
                filename = names
                return filename
            else:
                print("\ninfo: waiting for file to download")



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
driver.find_element_by_xpath("//input[@data-automation-id='pwd']").send_keys("password")

while(True):
    if(driver.title == "Retail Link"):
        print("\nwaiting: user input...")
        time.sleep(5)
    else:
        driver.get('https://supplier.walmart.com/orderManagement')
        time.sleep(3)
        print("\nsuccess: Going to dashboard")
        break

# click download
time.sleep(3)
# driver.find_element_by_class_name("icon-download").click()
# driver.find_element_by_css_selector("button.icon-download").click()
driver.find_element_by_xpath("//button[@data-sel-id='ExportButton']").click()
print("\nSuccess: Clicked on Download")
# driver.find_element_by_link_text("Download").click()
# driver.find_element_by_tag_name("label").click()
time.sleep(3)
# click Export All Items
# driver.find_element_by_css_selector('button.wm-btn-blue.btn-download').click()
driver.find_element_by_xpath("//li[text()='Export All Items']").click()
print("\nSuccess: Clicked Export All item")


time.sleep(2)
# Move from downloads to this folder
report_fname= find_file(from_path)

if(os.path.exists(from_path)):
    if platform == "linux" or platform == "linux2":
        from_path = from_path+"/"+report_fname
    else:
        from_path = from_path+"\\"+report_fname
shutil.move(from_path,des_path)
print("\nSuccess: moved file.")


driver.close()
print("\nsuccess: closed window.")

# time.sleep(3)

# with zipfile.ZipFile(os.path.join(des_path,report_fname),"r") as zip_ref:
#     zip_ref.extractall(join(des_path,"zip"))
# print("\ninfo: zip file extracted")

# time.sleep(3)

# zip_dir = os.path.join(des_path,"zip")
csv_fname= find_file(des_path)
# print(csv_fname)
# print(zip_dir)
df = pandas.read_excel(os.path.join(des_path,csv_fname))
cus_df = df[['PO#','Customer Name','Customer Phone Number','Ship to Address 1','Ship to Address 2','City','State','Zip','SKU','Item Description','Qty','Carrier','Package ASN']]

print(cus_df)


print("\n\nComplete....")
