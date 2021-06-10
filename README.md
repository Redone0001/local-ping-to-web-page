# local-ping-to-web-page
A python based short code to debug connectivity issue on a web page to make it easier to understand

all the instruction were tested on mac os

Installation :
1) python3 is require
2) flask is require 'pip install flask' to install flask
3) execute the cmd.sh  './cmd.sh' make sur to be in the folder to perform this one

Usage :

place all the ip adress you want to ping inside the list.txt file
carefull with the syntax it should follow this format :

xxx.xxx.xxx.xxx

yyy.yyy.yyy.yyy

exemple:

192.168.0.1

8.8.8.8

You will have the result in the web page and the terminal.
To acces the web page from 
- your local machine go to : 127.0.0.1:5000/main
- an another machine on your local network : your-local-ip:5000/main (ex : 192.168.0.5:5000/main)

