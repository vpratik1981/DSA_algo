#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 17:17:03 2024

@author: gq06
"""
import calendar as cal
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """
    Calculates the number of days between two dates.
    """
    
    # TODO - by the end of this lesson you will have
    #  completed this function. You do not need to complete
    #  it yet though! 
    
    numberOfdays=0
    n_leap_year=0
    
    if year1%4==0 and month1<2:
        n_leap_year+=1
    if year2%4==0 and month2>=2:
        n_leap_year+=1
    year_diff = year2-year1
    
    if year_diff//4 >0:
        n_leap_year+=(year_diff//4)
        
    # diff_month = month2-month1
    dif_day = day2-day1
    
    numberOfdays = dif_day+(year_diff*365)+n_leap_year
    
   # cal_1= cal. 
    
    return numberOfdays

def testDaysBetweenDates():
    
    # test same day
    assert(daysBetweenDates(2017, 12, 30,
                              2017, 12, 30) == 0)
    # test adjacent days
    assert(daysBetweenDates(2017, 12, 30, 
                              2017, 12, 31) == 1)
    # test new year
    assert(daysBetweenDates(2017, 12, 30, 
                              2018, 1,  1)  == 2)
    # test full year difference
    assert(daysBetweenDates(2012, 6, 29,
                              2013, 6, 29)  == 365)
    
    print("Congratulations! Your daysBetweenDates")
    print("function is working correctly!")
    
testDaysBetweenDates()