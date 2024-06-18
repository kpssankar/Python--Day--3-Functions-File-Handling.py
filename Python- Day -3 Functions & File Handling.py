#program to create text file
# Specify the directory path

from datetime import datetime

# get current date and time
x = datetime.now()

# create a file with date as a name day-month-year
file_name = x.strftime('%d-%m-%Y.txt')
with open(file_name, 'w') as fp:
    print('created', file_name)


# at specified directory
file_name_3 = r"E:\Desktop docs\IITMADRASGUVIPythonAutomationtraining\Tasks\Selenium\Selenium_tasks\Updated\Timestamp" + x.strftime('%d-%m-%Y.txt')
with open(file_name_3, 'w') as fp:
    print('created', file_name_3)


    
file = open("E:/Desktop docs/IITMADRASGUVIPythonAutomationtraining/Tasks/Selenium/Selenium_tasks/Updated/Timestamp/18-06-2024.txt", "w")

file.write("Current Timestamp is:18/06/2024")
#file.write("This is the second line.")

file.close()

file = open("E:/Desktop docs/IITMADRASGUVIPythonAutomationtraining/Tasks/Selenium/Selenium_tasks/Updated/Timestamp/18-06-2024.txt", "r")
print(file.read())

file.close()








