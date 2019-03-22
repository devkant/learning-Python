import  os

def rename_files():
    #get file names form folder
    file_list   =   os.listdir(r"C:\Users\lenovo\Desktop\prank")
    print(file_list)
    saved_path=os.getcwd()
    os.chdir(r"C:\Users\lenovo\Desktop\prank")
    #for each file, rename file name
    remove="0123456789"    
    table=str.maketrans("","",remove)  
    for file_name in file_list:
        print("OldName  -   "+file_name)
        print("NewName  _   "+file_name.translate(table))
        os.renames(file_name,file_name.translate(table))
rename_files()               

