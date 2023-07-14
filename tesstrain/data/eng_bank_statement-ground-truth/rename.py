import os

# Define the new file name and number
new_name = "eng_1500"
num = 1
i=0
j=0
k=0
# Loop through each file in the directory
for file_name in os.listdir("."):
    # Check if the file has the desired extension
    if file_name.endswith(".box"): 
        new_file_name = f'eng_{i}'+'.box'
        os.rename(file_name, new_file_name)
        i+=1

    if file_name.endswith(".gt.txt"): 
        new_file_name = f'eng_{j}'+'.gt.txt'
        os.rename(file_name, new_file_name)
        j+=1

    if file_name.endswith(".tif"):
        new_file_name = f'eng_{k}'+'.tif'
        os.rename(file_name, new_file_name)
        k+=1
    