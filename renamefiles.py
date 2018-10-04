import os
def rename_files():
    file_list=os.listdir(r"C:\Users\Sanjeev\Desktop\prank")
    print(file_list)
    saved_path=os.getcwd()
    os.chdir(r"C:\Users\Sanjeev\Desktop\prank")
    remove="0123456789"    
    table=str.maketrans("","",remove)
    for file_name in file_list:
      os.rename(file_name,file_name.translate(table))    
rename_files()
