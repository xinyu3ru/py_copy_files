#!/bin/env python
# -*- coding: utf-8 -*-

'''
@author: rublog

USAGE:

LICENSE:
This program is free software,

you can use this file under the GNU General Public License(GPL) published by the Free Software Foundation, 

version 3 or later of the GPL license is optional.

You can view The full GPL license here: http://www.gnu.org/licenses/gpl.html.

'''
import os
from os import mkdir
from os.path import join
from os.path import exists
from shutil import copy2 as copy
from shutil import SameFileError
from shutil import SpecialFileError
from chardet.universaldetector import UniversalDetector




def detectcode():
    with open('book.txt', 'rb') as f:
        detector = UniversalDetector()
        for line in f.readlines():
            detector.feed(line)
            if detector.done: break
        detectcode = detector.result['encoding']
        detector.close()
    print(detector.result)
    return detectcode
detectcode = detectcode()

def listbookfile():
    dict1 = {"你好":"hahahah"}
    for root, dirs, files in os.walk('.'):
        for name in files:
            full = join(root, name)
            dict1[name] = full 
    return dict1
dict1 = listbookfile()
print(dict1)
#cc = "知日！知日！这次彻底了解日本3.azw3"
#print(dict1[cc])
def findbook(dict1):
    with open('book.txt', 'r', encoding=detectcode) as f:
        for line in f:
            book = line.replace("\r", "")
            book = book.replace("\n", "")
            book = book.replace("\ufeff", "")
            if book in dict1.keys():
                where1 = dict1[book]#dict1.get(book)
                cpbooks(where1)
            else:
                print("There is no book named "+book+" in your documents!")
            print(where1)
    return where1

def direxist(where1):
    cunzai = exists('.\youneededbook')
    if cunzai is False:
        mkdir('youneededbook', mode=0o777)
    return 1
def cpbooks(where1):
    if direxist(where1) == 1:
        try:
            copy(where1, '.\youneededbook')
        except SameFileError:
            pass
        except SpecialFileError:
            pass
        finally:
            pass
    return 1
qq = findbook(dict1)
