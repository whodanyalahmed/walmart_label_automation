import os,sys,shutil
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
    

# print(from_path)



# current working path
des_path = sys.path[0]
# Detecting linux or windows
if platform == "linux" or platform == "linux2":
    from_path = str(sys.path[4]).replace(".local/lib/python3.8/site-packages",
    "Downloads")
    print(from_path)
else:
    from_path = str(sys.path[-1]).replace("AppData\\Local\\Programs\\Python\\Python38-32\\lib\\site-packages",
    "Downloads")


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




delete_dup_file()