@echo off
start python manage.py runserver
ping -n 3 127.0.0.1 > nul