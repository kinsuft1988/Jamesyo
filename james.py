#!/usr/bin/env python
import sys
import getopt

import os
import json
import generateHeadInfo
import generateImport
import generateMfileContent
import generateController
import translateJsonToModel

from generateHeadInfo import generateHeadInfoH, generateHeadInfoM, generateControllerHeadInfoH, generateControllerHeadInfoM
from generateImport import generateImportH
from generateMfileContent import generateMfileInfo
from generateController import generatetControllerH, generatetControllerM
from translateJsonToModel import handleJsonToModel


def readJsonFile(path):

    f = open(path, 'r')

    strFile = f.read()
    f.close()
    return strFile


def reducerJson(jsonDic):

    if not os.path.exists('./output/Views'):
        os.makedirs('./output/Views')

    fileHeadDir = './output/Views/%s.h' % (jsonDic['name']
                                           [0:1].upper() + jsonDic['name'][1:])
    outFile = open(fileHeadDir, 'w')

    stringHead = generateHeadInfo.generateHeadInfoH(jsonDic)
    stringImport = generateImportH(jsonDic)

    outFile.write(stringHead + stringImport)
    outFile.close()

    fileMainDir = './output/Views/%s.m' % (jsonDic['name']
                                           [0:1].upper() + jsonDic['name'][1:])
    outMainFile = open(fileMainDir, 'w')

    stringHeadM = generateHeadInfoM(jsonDic)
    stringMfileInfo = generateMfileInfo(jsonDic)

    outMainFile.write(stringHeadM + stringMfileInfo)
    outMainFile.close()

    for child in jsonDic.get('children'):

        if child.get('children'):
            reducerJson(child)


def generaterControllerFile(jsonDic):

    if not os.path.exists('./output/Controllers'):
        os.makedirs('./output/Controllers')

    fileHeadDir = './output/Controllers/%s.h' % (jsonDic['name']
                                                 [0:1].upper() + jsonDic['name'][1:] + "Controller")

    outFile = open(fileHeadDir, 'w')

    stringHead = generateControllerHeadInfoH(jsonDic)
    stringContentH = generatetControllerH(jsonDic)
    writeString(outFile, stringHead + stringContentH)
    outFile.close()

    fileMainDir = './output/Controllers/%s.m' % (jsonDic['name']
                                                 [0:1].upper() + jsonDic['name'][1:] + "Controller")
    outMainFile = open(fileMainDir, 'w')
    stringHeadM = generateControllerHeadInfoM(jsonDic)
    stringContentM = generatetControllerM(jsonDic)
    writeString(outMainFile, stringHeadM + stringContentM)
    outMainFile.close()


def writeString(f, string):
    if string.find("sdlajsldjalsdjask") == -1:
        f.write(string)
    else:
        if string == "\r":
            f.write(string)
        else:
            index = string.index("\r")
            f.write(string[0:index])
            writeString(f, string[index + 1:])


opts, args = getopt.getopt(sys.argv[1:], "hg:c:j:", [
                           "help", "version"])

for opt, value in opts:

    if opt == "--version":
        print "james version 0.0.8"

    if opt == "-g":
        str = readJsonFile(('./%s.json') % value)
        dic = json.loads(str)
        reducerJson(dic)

    if opt == "-c":

        str = readJsonFile(('./%s.json') % value)
        dic = json.loads(str)
        reducerJson(dic)
        generaterControllerFile(dic)

    if opt == "-j":
        str = readJsonFile(('./%s.json') % value)
        dic = json.loads(str)
        handleJsonToModel(dic)
