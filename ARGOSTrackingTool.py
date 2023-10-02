#--------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Li Jia Go (lijia.go@duke.edu)
# Date:   Fall 2023
#--------------------------------------------------------------

#Create a variable pointing to the data file
file_name = './data/raw/sara.txt'

#Create a file object from the file
file_object = open(file_name,'r')

#Read contents of file into a list
lineString = file_object.readline()

#Pretend we read one line of data from the file
#while lineString != '' #while lineString is not equal to an empty list

#read line by line so it does not need to pull in the data file into the computer's memory
while lineString: 

    #Check if line is a dataline
    if lineString[0] in ("#", "u"):
        lineString = file_object.readline()
        continue

    #Split the string into a list of data items
    lineData = lineString.split() #for split if you don't specify, it will treat it as splitting by empty space as default

    #Extract items in list into variables
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7]

    #Print the location of sara
    print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")

    #Read next line
    lineString = file_object.readline()