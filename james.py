#!/usr/bin/env python
import sys
import getopt

import os
import json
import generateHeadInfo
import translateJsonToModel

from generateHeadInfo import generateHeadInfoH, generateHeadInfoM

from translateJsonToModel import handleJsonToModel


def readJsonFile(path):

    f = open(path, 'r')

    strFile = f.read()
    f.close()
    return strFile




opts, args = getopt.getopt(sys.argv[1:], "hg:c:j:", [
                           "help", "version"])

for opt, value in opts:

    if opt == "--version":
        print "james version 0.0.9"

    if opt == "-j":
        str = readJsonFile(('./%s.json') % value)
        dic = json.loads(str)
        handleJsonToModel(dic)



		

	



