#! /usr/bin/env python3
# TikTok OSINT Tool
# @author https://github.com/sc1341
# 
# The creator nor any contributors are responsible for any illicit
# use of this program
#
#

from core.scrapper import Scrapper
from core.banner import banner
import argparse

def arg_parse():
	parser = argparse.ArgumentParser(description="TikTok OSINT Tool")
	parser.add_argument("--username", help="Profile Username", required=True, nargs=1)
	parser.add_argument("--downloadProfilePic", help="Downloads the user profile picture", required=False, action='store_true')
	return parser.parse_args()

def main():
	print(banner)
	args = arg_parse()
	
	tiktok = Scrapper(args.username[0])
	if args.downloadProfilePic == True:
		tiktok.download_profile_picture()

if __name__ == "__main__":
	main()
