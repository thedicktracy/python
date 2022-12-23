# CabreraP1
# Programmer: Robert Cabrera
# EMail: rcabrera14@cnm.edu
# Purpose: provides user capability to find fruit in a string


from cmath import cos, sin
from math import atan2
import math



def header():
        print("This function will print a summary explaining the purpose of the program.")
        print("CabreraP1")
        print("Programmer: Robert Cabrera")
        print("EMail: rcabrera14@cnm.edu")
        print("Purpose: demonstrate use of functions\nThis Program will calculate the distance between two geographic points\n Entered in decimal xx.xx xx.xx format ")
        
header()        

def get_location():
        my_tuple = tuple(input('Enter Lat and Long in decimal format XX.XX separated by spaces (XX.XX XX.XX)::   ').split())
        #print(my_tuple)
        return my_tuple
        

  
    #haversine formula 
def haversine():
        #get point one 
        s=get_location()
        print('this is the fist location ', s) 
        #store point one
        t=get_location()
        print('this is the second location ',t)
        x1,y1 = float(s[0]),float(s[1])
        print("this is the first location (x,y) ::  (",x1,", ",y1,") ")
        x2,y2=float(t[0]),float(t[1])
        print("this is the first location (x,y) ::  (",x2,", ",y2,") ")
        
        print('Let\'s calculate Distance')
        print('The formula for Distance (haversine formula) is D=R*C')     
        A =(math.sin(math.radians((x1-x2)/2))**2+(math.cos(math.radians(x1))*math.cos(math.radians(x2))*(math.sin(math.radians((y1-y2)/2)))**2))
        #print(A)
        C =2*math.atan2((A**.5), ((1-A)**.5)) 
        R = 6371 #kilometers
        print('C is ',C, ' and R is ', R)
        
        
        D=R*C
        print('this is D :: ',D, ' kilometers' )  
           
answer = 'yes'      
while answer == 'yes':
        haversine()
        answer = input('would you like to calculate again (yes/no):: ')
        
print('Goodbye')
        
#A = sin²((Lat1-Lat2)/2) + cos Lat1 ⋅ cos Lat2 ⋅ sin²((Lon1-Lon2)/2)
#C = 2 ⋅ atan2( √A, √(1−A) )
#D = R ⋅ C