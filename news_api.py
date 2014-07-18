#-*- coding: utf-8 -*-
"""
  Created by Donald.Liu @ 2014/07/19
  API for news from 新浪/网易/搜狐/腾讯
"""
import threading
import logging
import dateime
import os
import sys


class news_sina(threading.Thread):
  def __init__(self, thread_name):
    threading.Thread.__init__(self, name=thread_name)
  
  def run(self):
    pass
    
class news_tecent(threading.Thread):
  def __init__(self, thread_name):
    threading.Thread.__init__(self, name=thread_name)
  
  def run(self):
    pass

class news_neteasy(threading.Thread):
  def __init__(self, thread_name):
    threading.Thread.__init__(self, name=thread_name)
  
  def run(self):
    pass

class news_sohu(threading.Thread):
  def __init__(self, thread_name):
    threading.Thread.__init__(self, name=thread_name)
  
  def run(self):
    pass







