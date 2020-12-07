"""
cynthia rothschild
Dec 5 2020
Save all webpage tabs on internet browers windows
	Info: URL, Tab lable

panda datafram of tabs and url open in all windows on local machine
uses maps, pandas, appscript

future functionality:
can do more than Google Chrome
can sort catorigores: date subject

Purpose: to keep track of all tabs/webapages without keeping the internet browers open
Gives alot more abilities than looking through history on internet brower, which if they crash will not keep track of open tabs
aand save open tabs in cognito mode 
then can save in 
"""
from appscript import *
import os
import pandas as pd
import numpy as np

def get_tabs(win_num):
	"""
	This gets the tabs label and URL for a specific window

	win_num is the window that this function is working on


	returns dataframe of current (One) open window's tabs and urls
	"""
	tabs_lis = list(map(lambda x: x.title(), app('Google Chrome').windows[win_num].tabs())) #, name='Tabs'       
	#print(tabs_lis, '\n\n')

	url_lis  = list(map(lambda x: x.URL(), app('Google Chrome').windows[win_num].tabs()))   #, name='URL'
	#print(url_lis)

	tab_df = pd.DataFrame(tabs_lis)
	url_df = pd.DataFrame(url_lis)


	#might want to also get time from the tab, for future functionality of sortign
		#0_tabs   0_url is created here IDK how to remove  0 at the start
	return tab_df.join(url_df, lsuffix='_tabs', rsuffix='_url')



def tabs_entire_desktop():
	"""
	gets each window and uses get_tabs to get info of each windows tabs url
	each windows tab url info saved in their own dataframe 
	returns a alist of all the dataframs from each window
	"""
	#get_tabs
	#make panda!!
	windows_tabs_lis = []
	n = num_windows_open()

	for n in range(n):
		#include raise error
		windows_tabs_lis.append(get_tabs(n))


	return windows_tabs_lis

def num_windows_open():
	"""
	will hopefully be able to tell how many windows are open on local decevice 
	"""
	'''
	NEED TO FIND PROPERTY -HOW MANY WINDOWS ARE OPEN
		OR
	try:
		while: no errors
			windows_tabs_lis.append(get_tabs())
	except: raise EventError(errornum, errormsg, eventresult)
	'''
	return 4

def sort_by(df): #add parameters
	"""
	will sort the dataframe by catoigory
	if want can work in time and sort by time
	"""
	pass

def save_to_excell(df, sort=False): #other sort parameters
	"""
	save to df to excell
	save list of catigories or hastages
	"""

	pass



def main():
	#make list of hastags or catigories from user and from previous times

	print("limited to only viewing 4 windows open")
	print("Will raise exception EventError if you have less than 4 windows open ")
	print(*tabs_entire_desktop(), sep='\n\n')

if __name__ == '__main__':
	main()