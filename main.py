from GdriveOcr import sendToGoogle
import os
import time
import traceback
from pathlib import Path
from os.path import relpath

## Variables to customize
keep_separate_copy_for_each_file = True             # If separate copy for each file is needed, make this variable True. Otherwise False.
temp_output_file_name = "output.txt"                # Downloaded as output each time a photo is uploaded to Google.
large_output_file_name = "TheLargeFile.txt"         # Where all outputs will be saved.
img_file_extension = "png"                         # IMG file with same extension. dot (.) is prohibited
time_to_sleep = 0                                   # Sleep after each submission to Google. Default is 0. Change if needed.
temp_output_file_path = os.path.realpath(os.path.join(os.getcwd(), temp_output_file_name))
large_output_file_path = os.path.realpath(os.path.join(os.getcwd(), large_output_file_name))

# Folder for stored images
imageFilesFolderName = "img"
imageFilesDir = os.path.realpath(os.path.join(os.getcwd(), imageFilesFolderName))

# Folder for separate copy of OCR output files
SeparateCopyFolderName = "outputs_separately"
SeparateCopyDir = os.path.realpath(os.path.join(os.getcwd(), SeparateCopyFolderName))

# Checking if folders already exists. Otherwise, create them
if os.path.exists(imageFilesFolderName):
    print("* 'img' Directory Found!")
else:
    print("! Couldn't find img directory.")
    try:
        os.mkdir(imageFilesDir)
        print("* Image Directory was created!\n\nNow copy all the image files to the 'img' folder. Press y and enter to continue:")
        input(" ")
    except:
        print("* Can't create 'img' directory!\n\nCreate the 'img' folder in current folder manually and then copy all the image files to the 'img' folder. Press y and enter to continue:")
        input(" ")

if keep_separate_copy_for_each_file == True:
    if os.path.exists(SeparateCopyFolderName):
        print("* 'outputs_separately' Directory Found!")
    else:
        print("! Couldn't find 'outputs_separately' directory.")
        try:
            os.mkdir(SeparateCopyFolderName)
            print("* 'outputs_separately' was created!")
        except:
            print("! Something's wrong. will not save outputs separately.")
            keep_separate_copy_for_each_file == False


# Create list of image file in img folder
##  = os.listdir(imageFilesDir)
imageFileList = []
for path in Path(imageFilesDir).rglob('*.' + img_file_extension):
    imageFileList.append(path)

# THE MAIN TASK
print("### Starting OCR:\n\n")
i = 0

for imgfileDir in imageFileList:
    
    # File sent to Google, output saved in output.txt and also in the large_output_file
    temp = str(imgfileDir).split("/")
    imgfile = temp[len(temp)-1]
    imgfile_path = os.path.realpath(os.path.join(imageFilesDir, imgfileDir))
    try:
        sendToGoogle(imgfile, imgfile_path, temp_output_file_path, large_output_file_name)

        # Keep separate copies if true
        if keep_separate_copy_for_each_file == True:
            separate_output_file_name = os.path.splitext(imgfile)[0] + ".txt"
            separate_output_file_dir = str(os.path.dirname(imgfileDir)).replace(imageFilesFolderName, SeparateCopyFolderName)
            separate_output_file_path = os.path.join(separate_output_file_dir, separate_output_file_name)

            os.makedirs(separate_output_file_dir, exist_ok=True)
            os.rename(temp_output_file_path, separate_output_file_path)

        i += 1
        print(str(i) + ". " + imgfile + "  - DONE")
        time.sleep(time_to_sleep)
    except:
        print("### Something's Wrong. Save the output! ###\n\n")
        print(str(traceback.format_exc()))
        print("\n### Something's Wrong. Save the output! ###\n\n")
        print("Terminating Program...")
        break

print("\n\n* " + str(i) + " image files were sent for OCR!!!")
