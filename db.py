#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sqlite3
def createDataBase():
  con = sqlite3.connect('mydatabase.db')
  c = con.cursor()
  #c.execute('drop table data;')
  c.execute('create table clients (id INTEGER PRIMARY KEY, name VARCHAR(45), age INTEGER);')
  c.execute('create table employees (id INTEGER PRIMARY KEY, name VARCHAR(45), age INTEGER);')
  con.commit()
