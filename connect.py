import os
import pandas as pd
Folder_Path = './train'
os.chdir(Folder_Path)
file_list = os.listdir()
file_list.sort(reverse = False)
print(file_list)
#Folder_Path = '/train'  # 要拼接的文件夹及其完整路径，注意不要包含中文
SaveFile_Path = './connact'  # 拼接后要保存的文件路径
SaveFile_Name = 'connect_data.csv'  # 合并后要保存的文件名

for i in file_list:
    df = pd.read_csv(Folder_Path + '/' + i)
    df.to_csv(SaveFile_Path + '//' + SaveFile_Name, encoding="utf_8_sig", index=False, header=False, mode='a+')