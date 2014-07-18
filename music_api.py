#-*- coding: utf-8 -*-
"""
  Created by Donald.Liu @ 2014/07/19
"""

import threading
import datetime
import os
import logging

class music_neteasy(threading.Thread):
  def __init__(self, thread_name):
    threading.Thread.__init__(self, name=thread_name)
    self.log = logging.getLogger()
    
    pass


class music_baidu:
  def __init__(self):
    pass
    

class music_douban:
  def __init__(self):
    pass
