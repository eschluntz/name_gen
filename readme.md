# Domain Name Generator

Unfortunately, finding a good name for a startup often comes down to finding a good (available) domain name. These scripts help the process of searching by autogenerating potential names from your inputs and checking whether the .com domain is available, and (soon!) how easy SEO is for the site.

## Strategy: Two Word Names

I'm a fan of two word names like FaceBook, DropBox, LinkedIn, AirBnb, etc... They're easy to remember, easy to spell, and often there are plenty of domains still out there.

The basic idea: Provide lists of prefixes and suffixes, we'll try out all possible combinations and print out any where the domain is available. 

## Usage
	>>> sudo pip install -r requirements.txt
	>>> vim pre.txt # add your prefixes
	>>> vim post.txt # add your suffixes
	>>> python name_gen.py
	AwesomeAndAvailable.com
	CoolAndAvailable.com
	...