#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 11:28:39 2021

@author: Jakaja Cain
"""




#ping("192.168.1.1")





import os
import platform    # For getting the operating system name
import subprocess  # For executing a shell command


from flask import Flask

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1','-W','200', host]

    return subprocess.call(command) == 0

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # main page
    @app.route('/main')
    def main():
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file1 = open(dir_path+'/list.txt', 'r')
        print('curent dir : '+dir_path+'/list.txt')
        output=""

        while True:
        
            line = file1.readline()
            if not line:
                file1.close()
                break
            
            line=line.rstrip()
            
            if ping(line)==1:
                output+=line + " is up"+'<br>'
            else:
                output+=line + " is down"+'<br>'
            

        
        return output

    return app