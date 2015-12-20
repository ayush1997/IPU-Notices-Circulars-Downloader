# coding: utf-8
# -*- coding: encoding -*-
import requests
from bs4 import BeautifulSoup
import urllib2

main_dic = {}
def download(url,name_file):
	response = urllib2.urlopen(url)
	lfile = open(name_file, 'w')
	lfile.write(response.read())
	lfile.close()
	print "completed"
def text(ur11_list,url2_list,course):
	c = 1
	len_url1 = len(url1_list)
	len_url2 = len(url2_list)
	for i in url1_list:
		#storing the text in a variable,of the next sibling of ("td",text=u"O")
		
		

		txt = i.find_next_sibling("td").get_text()
		if course in txt:

			date = i.find_next_sibling("td").find_next_sibling("td").find_next_sibling("td").get_text()
			print c,"-------","date","------------",date,"--------",txt


			if i.find_next_sibling("td").find_next_sibling("td").find("a") != None:

				href = i.find_next_sibling("td").find_next_sibling("td").find("a").get("href")
				new_pdf_url_main1 = "http://ggsipuresults.nic.in/ipu/datesheet/" + href
				main_dic[c] = new_pdf_url_main1
				c = c+1
			
			else:
				c = c+1

	for i in url2_list:
		txt = i.find_next_sibling("td").get_text()

		if course in txt:

			date = i.find_next_sibling("td").find_next_sibling("td").find_next_sibling("td").get_text()
			print c,"-------","Date","----------",date,"--------",txt


			if i.find_next_sibling("td").find_next_sibling("td").find("a") != None:

				href = i.find_next_sibling("td").find_next_sibling("td").find("a").get("href")
				new_pdf_url_main2 = "http://ggsipuresults.nic.in/ipu/examnotice/" + href
				main_dic[c] = new_pdf_url_main2
				

				c = c+1
			else:
				c= c+1


	





main_url1 = "http://ggsipuresults.nic.in/ipu/datesheet/datesheetmain.htm"
main_url2 = "http://ggsipuresults.nic.in/ipu/examnotice/examnoticemain.htm"

req1 = requests.get(main_url1)
req2 = requests.get(main_url2)

soup1 = BeautifulSoup(req1.content)
soup2 = BeautifulSoup(req2.content)

url1_list = soup1.find_all("td",text=u"Ο")
url2_list = soup2.find_all("td",text=u"Ο")




while 1:
	try:
		print "Enter course"
		course = raw_input()
		text(url1_list,url2_list,course)
		print "do you wanr to download any,   y/n"
		act = raw_input()
		if act == "y":
			print "enter the serial no of the notice you want to download"
			ser_no = raw_input()
			print "enter by what name do you want to save it as,eg, abc.pdf"
			name_file = raw_input()
			download(main_dic[int(ser_no)],name_file)
			break
		else:
			break

		
		
	except:
		print "wrong input"



