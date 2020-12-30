#!/usr/bin/python

import threading 
import time

def news_feeder(week_days):
  d=0
  for day in week_days:
    time.sleep(1)
    d=d+1
    print("New Feed : ", d)
    if(day == "wed"):
      holiday=day
      print("RAN Holiday : ", day)
    if(day == "sun"):
      print("RSA Holiday : ", day)
    holiday=day

def track_holiday():
  for x in range(20):
    time.sleep(1)
    print("Holiday : ", holiday)
    
def print_cube(num): 
    """ 
    function to print cube of given num 
    """
    print("Cube: {}".format(num * num * num)) 
  
def print_square(num): 
    """ 
    function to print square of given num 
    """
    print("Square: {}".format(num * num)) 
  
if __name__ == "__main__": 
    # creating thread 
    days_list={"mon","tue", "wed", "thu", "fri", "sat", "sun"}
    holiday = 'none'
    t1 = threading.Thread(target=print_square, args=(10,)) 
    t2 = threading.Thread(target=track_holiday, args=()) 
    t3 = threading.Thread(target=news_feeder, args=(days_list,))
    
  
    # starting thread 1 
    t1.start() 
    # starting thread 2 
    t2.start() 
    t3.start()
  
    # wait until thread 1 is completely executed 
    t1.join() 
    # wait until thread 2 is completely executed 
    t2.join() 
    t3.join()
    
    # both threads completely executed 
    print("Done!") 