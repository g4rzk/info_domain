#!/usr/bin/python
# Author : anggaxd
# GitHub : g4rzk
# Facebook : fb.me/g4rzk
# Telegram : t.me/g4rzk

import os
import re
import requests
ses = requests.Session()

class Domain:

	def __init__(self, domain):
		self.domain = domain
		print("\n  -  -==[ GET INFO YOUR DOMAIN ]==- -")

	def __getInfoAge__(self):
		try:
			a = ses.get(f"https://www.whatsmydns.net/domain-age?q={self.domain}", headers={"user-agent":"chrome"}).text
			registered = re.findall(r"><strong>(.*)<\/strong><\/p\>", str(a))[0]
			years = re.findall(r"<strong>(\d+?)<\/strong>", str(a))[0]
			month = re.findall(r"<strong>(\d+?)<\/strong>", str(a))[1]
			days = re.findall(r"<strong>(\d+?)<\/strong>", str(a))[2]
			total_days = re.findall(r"<p>or\s<strong>(\d+?)<\/strong>\s\bd\w+</p>", str(a))[0]
		except:
			pass

		print("\n [#] AGE YOUR DOMAIN :\n")
		print(f" [*] {self.domain} was registered on: ")
		print(f" [*] {registered}")
		print(f" [*] {years} years, {month} month and {days} days ago or {total_days} days.")

	def __getInfoExpired__(self):
		try:
			a = ses.get(f"https://www.whatsmydns.net/domain-expiration?q={self.domain}", headers={"user-agent":"chrome"}).text
			registered = re.findall(r"><strong>(.*)<\/strong><\/p\>", str(a))[0]
			years = re.findall(r"<strong>(\d+?)<\/strong>", str(a))[0]
			month = re.findall(r"<strong>(\d+?)<\/strong>", str(a))[1]
			days = re.findall(r"<strong>(\d+?)<\/strong>", str(a))[2]
			total_days = re.findall(r"<p>or\s<strong>(\d+?)<\/strong>\s\bd\w+</p>", str(a))[0]
		except:
			pass

		print("\n [#] EXPIRED YOUR DOMAIN :\n")
		print(f" [*] {self.domain} expired on: ")
		print(f" [*] {registered}")
		print(f" [*] {years} years, {month} month and {days} days ago or {total_days} days.")


os.system("clear")
garz = Domain(input(" [?] Input Your Domain : ")) 
garz.__getInfoAge__()
garz.__getInfoExpired__()
