# CabreraP3
# Programmer: Robert Cabrera
# EMail: rcabrera14@cnm.edu
# Purpose: This program will enable to user to interact with points

from array import array
from asyncio.windows_events import NULL
from cgi import test
from distutils.util import subst_vars
from doctest import testfile
from operator import concat
import os
import os.path
from os.path import exists
from pathlib import Path
from pickle import NONE
import re
import ast
from unicodedata import name
from cmath import cos, sin
from math import atan2
import math

#had to ensure files are in utf-8 (initial files made in either notepad or notepad++)
#function header for this particular program

#my path C:\Users\sc420f\Documents\LTP\PythonProgrammingCIS1250\Competency3Program
def header():
        print("This function will print a summary explaining the purpose of the program.")
        print("CabreraP3")
        print("Programmer: Robert Cabrera")
        print("EMail: rcabrera14@cnm.edu")
        print("This program will enable to user to interact with points\n")
        
def check_if_file_exists():
    global name_of_file
    name_of_file = input("\nWhat is the name of the file you would like to check for (list) :: ")
    dir=input("\nWhat's the path of your files for this program (Comp3) :: ")
    wd = Path(dir,name_of_file)
    #define cwd
    os.chdir(dir)
    if wd.is_file():  
        print("\nThis file exists",wd,"\n")
    else:
        print("\nThe file ",name_of_file," does not exist in ",wd,"\n\nPlease enter a valid file location/file name\n")
        anemptylist=[]
        #check_if_file_exists();# the instruction said to return an empty list, i wasn't sure if this met the requirement 
        return anemptylist 
    return name_of_file

def get_choice():
    choices = ["O","I","A","R","E","F","S","Q"]
    choice = input("What would you like to do next [O]pen a point file, [I]nfo, [A]dd a point, [R]emove a point, [E]dit a point, [F]ind closest, [S}ave points file, [Q]uit ::  ")      
    return choice   

def open_file(name_of_file):
    file = open(name_of_file, 'r', encoding='utf-8-sig')
    count = 0
    a=""
    test=[]
    for line in file:
        ##strip symbols, split on comma , for every element for every line in the file
        info = ([x.strip() for x in line.split(',')])
        #regular expression below scrapes only coordinate info
        LatLon = map(float, re.findall('-?\d*\.?\d+', line))
        x = next(LatLon)
        y = next(LatLon)
        a = "{},{},{},{}".format(info[0],x,y,info[3]) 
        test.append(a)
        count += 1
    file.close()
    print("\n",test,"\n")
    test=tuple(test)
    return test
    
def get_info(info): #display a single points information
    substring = input("What data point are you selecting (Select Santa Fe or Albuquerque right now) :: ")
    if substring != "Santa Fe" and substring != "Albuquerque":
        print("\nthat doesn't match any of the points i have PLEASE TRY AGAIN\n")
        substring = input("What data point are you selecting (Select Santa Fe or Albuquerque right now) :: ")
    i=0
    for i in range(len(info)): 
        if substring in info[i]: #check that this is the correct data that the user requested 
            print("\nHere is the information you requested",info[i],"\n")
           
def add_a_point(info):  
    test=[]          
    name = input("Please Enter Name xxx :: ")
    lat = float(input("Please Enter Lat xx.xx :: "))
    lon = float(input("Please Enter Longitude xx.xx :: "))
    detail = input("Please Enter Description for the point xxx :: ") 
    a = "'{}',{},{},'{}'".format(name,lat,lon,detail)
    test.append(a)
    info=list(info)
    info.append(test[0])
    info=tuple(info)
    print(info)
    
def remove_a_point(info): #R
    info = list(info)
    i=0
    remove_this = input("\nwhich point would you like to remove (enter city name or use O to get list of cities again) :: ") 
    if remove_this == "O":
        print("\n",info)
        remove_a_point(info)
    elif remove_this != "Santa Fe" and remove_this != "Albuquerque":
        print("\nSorry I did not understand that\n You're going to get better at typing Albuquerque i promise")
        remove_a_point(info)
    else:
        for i in range(len(info)):
            if len(info) > 1 and remove_this in info[i]:
                   del info[i]
        print("\nWe've removed what you asked\nHere's is the edited list\n\n   ",info,"\n")    
    info=tuple(info)
    #do you want remove_a_point() to return the new info , i wasn't sure what level of persistenance was required 
           
def edit_a_point(info):  #E
    edit_this_point = input("\nWhich point do you want to edit (pick a city)(O for a list of cities) :: ")        
    if edit_this_point == "O":
        open_file(name_of_file)
        edit_a_point(info)
    elif edit_this_point != "Santa Fe" and edit_this_point != "Albuquerque":
        print("\nIt's spelled : Albuquerque")
        edit_a_point(info)
    elif edit_this_point == "":
        edit_a_point(info)
    else:
        info = list(info)
        i=0
        for i in range(len(info)):
            if edit_this_point in info[i]: #check if this is the right point to perform work on
                name = str(input("\nPlease Enter NEW City Name 'xxx' (if you press ENTER we will keep the original value) :: "))           
                lat = input("\nPlease Enter NEW Latitude xx.xx (if you press ENTER we will keep the original value)  :: ")
                lon = input("\nPlease Enter NEW Longitude xx.xx (if you press ENTER we will keep the original value)  :: ")
                detail = str(input("\nPlease Enter NEW Detail 'xxx' (if you press ENTER we will keep the original value)  :: "))
                #temp =[]
                temp = ([x.strip() for x in str(info[i]).split(',')])
                    #i need every element from every list within list(info[i]) , i wasn't sure of a more eloquent way to do this
                if name == "":
                    name = temp[0]
                    print("\nLocation will stay :: ", name,"\n")   
                if lat == "":
                    lat = temp[1]
                    lat = float(lat)
                    print("\nLatitude will stay :: ", lat,"\n") 
                if lon == "":
                    lon = temp[2]
                    lon = float(lon)
                    print("\nLongitude will stay :: ", lon,"\n") 
                if detail == "":
                    detail = temp[3]
                    print("\nDetail will stay :: ", detail,"\n")
                a = "{},{},{},{}".format(name,lat,lon,detail)
                y=0
                for y in range(len(info)):
                    if len(info) >1 and edit_this_point in info[y]:
                        info[y] = a
                print("PROOF\n",info)
 
def find_closest(info):
    your_loc = tuple(input('\nEnter Lat and Long in decimal format XX.XX separated by spaces XX.XX XX.XX  ::  ').split())             
    x1,y1 = float(your_loc[0]), float(your_loc[1])
    LatLon =[]
    info=list(info)
    n=[]
    t=0
    for i in info:
        ###regular expression below scrapes only line for coordinates dump into list
        LatLon = map(float, re.findall('-?\d*\.?\d+', i))
        x2 = next(LatLon)
        y2 = next(LatLon)
        print("\nthis is the user location (x,y) ::  (",x1,", ",y1,") \n")
        print("this is the 2nd location (x,y) ::  (",x2,", ",y2,") \n")
        print('Let\'s calculate Distance\n')
        A =(math.sin(math.radians((x1-x2)/2))**2+(math.cos(math.radians(x1))*math.cos(math.radians(x2))*(math.sin(math.radians((y1-y2)/2)))**2))
        C =2*math.atan2((A**.5), ((1-A)**.5)) 
        R = 6371 #kilometers
        D=R*C
        #just so it's a little easier to test and read for me 
        dummy = input(f'this is the distance {D} in kilometers :: PRESS ENTER TO CONTINUE :: '.format(D) ) 
        print("\n")
        n.append(D)
        if t >= 1: #we need both distances for comparison so run through haversine until you have both
            if n[0] < n[1]:       #if one value is closer then make that the value of closest and show it to user
                nest = [x for x in str(info[t]).split(',')]
                x2 = nest[1]
                y2 = nest[2]
                closest = x2,y2
                print(closest)
                print(info[0]," is closest\n")
            elif n[1] < n[0]:
                nest = [x for x in str(info[t]).split(',')]
                x2 = nest[1]
                y2 = nest[2]
                closest = x2,y2
                print(closest)
                print(info[1]," is closest\n")
        t += 1        
        
def save_file(info):
    name_of_new_file = input("\nWhat is the name of the NEW file :: ") 
    f = open(name_of_new_file, 'w')
    for i in range(len(info)):
        f.write("".join(info[i]))
        f.write("\n")
    f.close  
      
def main(): 
    header()  
    name_of_file=check_if_file_exists()
    if name_of_file == []:
        name_of_file = check_if_file_exists() #the instruction said return an empty list so i looped it here for ease of use and testing and so there were less TypeErrors
    choice=get_choice()
    while choice != "Q": 
        if choice == "I":  #get me information about a point
            get_info(info)
        elif choice == "O":  #open the file of points
            info = open_file(name_of_file)    
        elif choice == "A": #add a point  
            add_a_point(info)    
        elif choice == "R":   #remove a point 
            remove_a_point(info)
        elif choice == "E":    #edit a point
            edit_a_point(info)
        elif choice == "F":    #find closest point to a point the user enters
            find_closest(info)
        elif choice == "S":     #save the returned info to a file 
            save_file(info)
        else:
            print("I did not understand that")
        choice = input("\n\nWhat would you like to do next [O]pen a point file, [I]nfo, [A]dd a point, [R]emove a point, [E]dit a point, [F]ind closest, [S}ave points file, [Q]uit ::  ")

if __name__ == '__main__':
        main()     
    
def goodbye():
    print("goodbye")
    
goodbye()