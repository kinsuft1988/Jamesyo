import json
import datetime

author = 'kinsuft'
org = 'CTiOS-org'
project = 'xwd'


def generateHeadInfoH(dic):

    str = "// " + "\r"
    str += ("//  %s.h" % dic['name']) + "\r"
    str += ("//  %s" % project) + "\r"
    str += "//" + "\r"
    str += ("//  Created by %s on %s." %
            (author, datetime.datetime.now().strftime('%Y/%m/%d'))) + "\r"
    str += ("//  Copyright %s year %s. All rights reserved." %
            (datetime.datetime.now().strftime('%Y'), org)) + "\r"
    str += "//" + "\r\r" 

    return str

def generateHeadInfoM(dic):

    str = "// " + "\r"
    str += ("//  %s.m" % dic['name']) + "\r"
    str += ("//  %s" % project) + "\r"
    str += "//" + "\r"
    str += ("//  Created by %s on %s." %
            (author, datetime.datetime.now().strftime('%Y/%m/%d'))) + "\r"
    str += ("//  Copyright %s year %s. All rights reserved." %
            (datetime.datetime.now().strftime('%Y'), org)) + "\r"
    str += "//" + "\r\r" 

    return str    


def generateControllerHeadInfoH(dic):

    str = "// " + "\r"
    str += ("//  %s.h" % (dic['name'][0:1].upper() + dic['name'][1:] + "Controller")) + "\r"
    str += ("//  %s" % project) + "\r"
    str += "//" + "\r"
    str += ("//  Created by %s on %s." %
            (author, datetime.datetime.now().strftime('%Y/%m/%d'))) + "\r"
    str += ("//  Copyright %s year %s. All rights reserved." %
            (datetime.datetime.now().strftime('%Y'), org)) + "\r"
    str += "//" + "\r\r" 

    return str

def generateControllerHeadInfoM(dic):

    str = "// " + "\r"
    str += ("//  %s.m" % (dic['name'][0:1].upper() + dic['name'][1:] + "Controller")) + "\r"
    str += ("//  %s" % project) + "\r"
    str += "//" + "\r"
    str += ("//  Created by %s on %s." %
            (author, datetime.datetime.now().strftime('%Y/%m/%d'))) + "\r"
    str += ("//  Copyright %s year %s. All rights reserved." %
            (datetime.datetime.now().strftime('%Y'), org)) + "\r"
    str += "//" + "\r\r" 

    return str     