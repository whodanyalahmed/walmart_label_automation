import os,sys,shutil,zipfile,time,pandas
from sys import platform
# des_path = sys.path[0]

# def find_file():
#     items = os.listdir(from_path)
#     filename= None

#     for names in items:
#         if names.startswith("ItemReport"):
#             filename = names
#             return filename
#         else:
#             print("error: cant find file in directory")
#             return 1



# # Detecting linux or windows
# if platform == "linux" or platform == "linux2":
#     from_path = str(sys.path[4]).replace(".local/lib/python3.8/site-packages","Downloads")
#     from_path = from_path+"/"+find_file()
    
# else:
#     from_path = str(sys.path[-1]).replace("AppData\\Local\\Programs\\Python\\Python38-32\\lib\\site-packages","Downloads")
#     from_path = from_path+"\\"+find_file()
    


# current working path
des_path = sys.path[0]
    
def find_file(des_path):
    items = os.listdir(des_path)
    for names in items:
        if names.startswith("ItemReport"):
            filename = names
            return filename
        # else:
            # print("info: waiting for file to download")

report_fname= find_file(des_path)
with zipfile.ZipFile(os.path.join(des_path,report_fname),"r") as zip_ref:
    zip_ref.extractall("zip")

zip_dir = os.path.join(des_path,"zip")
csv_fname= find_file(zip_dir)
# print(zip_dir)

df = pandas.read_csv(os.path.join(zip_dir,csv_fname))
print(df)
