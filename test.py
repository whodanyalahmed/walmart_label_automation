import os,sys,shutil,zipfile,time,pandas
from sys import platform
from os.path import join
des_path = sys.path[0]

def find_file(from_path):
    while(True):
        items = os.listdir(from_path)
        for names in items:
            if names.startswith("ItemReport"):
                filename = names
                return filename
            else:
                print("\ninfo: waiting for file to download")
                time.sleep(5)




# # # Detecting linux or windows
# # if platform == "linux" or platform == "linux2":
# #     from_path = str(sys.path[4]).replace(".local/lib/python3.8/site-packages","Downloads")
# #     from_path = from_path+"/"+find_file()
    
# # else:
# #     from_path = str(sys.path[-1]).replace("AppData\\Local\\Programs\\Python\\Python38-32\\lib\\site-packages","Downloads")
# #     from_path = from_path+"\\"+find_file()
    


# # current working path
# des_path = sys.path[0]
# print(des_path)
# # # Detecting linux or windows
# # if platform == "linux" or platform == "linux2":
# #     from_path = str(sys.path[4]).replace(".local/lib/python3.8/site-packages",
# #     "Downloads")
# # else:
# #     from_path = str(sys.path[-1]).replace("AppData\\Local\\Programs\\Python\\Python38-32\\lib\\site-packages",
# #     "Downloads")

# def find_file(b):
#     items = os.listdir(b)
#     for names in items:
#         print(names)
#         if names.startswith("ItemReport"):
#             filename = names
#             return filename
#         else:
#             print("info: waiting for file to download")

# report_fname= find_file(des_path)
# with zipfile.ZipFile(os.path.join(des_path,report_fname),"r") as zip_ref:
#     zip_ref.extractall(join(des_path,"zip"))
# print("\ninfo: zip file extracted")

# zip_dir = os.path.join(des_path,"zip")
# print(zip_dir)
# csv_fname= find_file(zip_dir)
# print(csv_fname)

# df = pandas.read_csv(os.path.join(zip_dir,csv_fname))
# print(df)


zip_dir = os.path.join(des_path,"zip")
csv_fname= find_file(zip_dir)
df = pandas.read_csv(os.path.join(zip_dir,csv_fname))
print(df['VENDOR ID'])