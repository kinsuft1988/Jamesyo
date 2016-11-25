import json
import os
import sys
import types
import generateHeadInfo

from generateHeadInfo import generateHeadInfoH, generateHeadInfoM


def handleJsonToModel(dic):

    if not os.path.exists('./outputModel/'):
          os.makedirs('./outputModel/')

    fileName = raw_input("input the Model Name: ")
    handleJsonToModelWithFileName(dic, fileName)


def handleJsonToModelWithFileName(dic, fileName):

	fileName = upperFirstLetter(fileName)
	fileHeadDir = './outputModel/%s.h' % fileName
	outFile = open(fileHeadDir, 'w')

	dicNameModify = {}

	dicName = {'name': fileName}
	stringHead = generateHeadInfoH(dicName)
	stringImport = handleJsonHFileContent(dic, fileName,dicNameModify)

	outFile.write(stringHead + stringImport)
	outFile.close()

	fileMainDir = './outputModel/%s.m' % fileName
	outMainFile = open(fileMainDir, 'w')

	stringHeadM = generateHeadInfoM(dicName)
	stringMfileInfo = handleJsonMFileContent(dic,fileName,dicNameModify)

	outMainFile.write(stringHeadM + stringMfileInfo)
	outMainFile.close()

def handleJsonHFileContent(dic,name,dicNameModify):
    str = "#import <UIKit/UIKit.h>" + "\n\n" + "importTag"

    str += "@interface " + name + " : " + "NSObject" + "\n\n"


    for singglePorperty in dic:
    	type(dic[singglePorperty]) 
    	if type(dic[singglePorperty]) is types.StringType:
       	    str += "@property (nonatomic, strong) NSString* %s;" % singglePorperty   + "\n"  
       	elif type(dic[singglePorperty]) is types.IntType:
       	    str += "@property (nonatomic) NSInteger %s;" % singglePorperty   + "\n"    
       	elif type(dic[singglePorperty]) is types.UnicodeType:
       	    str += "@property (nonatomic, strong) NSString* %s;" % singglePorperty   + "\n" 
       	elif type(dic[singglePorperty]) is types.DictType:
   		    fileName = raw_input("rename The Dic Object %s  with name: " % singglePorperty) 
   		    str += ("@property (nonatomic, strong) %s* %s;" % (upperFirstLetter(fileName),lowerFirstLetter(fileName))) + "\n" 
   		    dicNameModify[singglePorperty] = fileName;
   		    handleJsonToModelWithFileName(dic[singglePorperty],fileName)
   		    str = str.replace("importTag","#import \"%s.h\" \nimportTag" % upperFirstLetter(fileName))
       	elif type(dic[singglePorperty]) is types.ListType:
   		    fileName = raw_input("name the Item in the  the array  %s : " % singglePorperty) 
   		    str += ("@property (nonatomic, strong) NSArray<%s*>* %s;" % (upperFirstLetter(fileName),lowerFirstLetter(singglePorperty))) + "\n" 
   		    dicNameModify[singglePorperty] = fileName;
   		    handleJsonToModelWithFileName(dic[singglePorperty][0],fileName)
   		    str = str.replace("importTag","#import \"%s.h\" \n importTag" % upperFirstLetter(fileName))
       	else :
       		print  type(dic[singglePorperty])

    str += "\n" + "@end"
    str = str.replace("importTag","\n")
    return str

def handleJsonMFileContent(dic,name,dicNameModify):
    str = "#import \"%s.h\" " % name + "\n\n"

    str += "@implementation " + name + "\n\n"

    if len(dicNameModify) > 0:
    	str += "+ (NSDictionary *)objectClassInArray" + "\n"
    	str += "\t" + "{" + "\n" 
    	str += "\t" + "return @{" + "\n"
    	for key in dicNameModify:
    			if  type(dic[key]) is types.ListType:
    				str += "\t" + " @\"%s\" : [%s class] " % (lowerFirstLetter(key),dicNameModify[key]) + "," + "\n"

    	str = str[:-2]
    	str += "\n"
    	str += "\t" "};" + "\n"
    	str += "}" + "\n"

    if len(dicNameModify) > 0:
    	str += "+ (NSDictionary *)replacedKeyFromPropertyName" + "\n"
    	str += "\t" + "{" + "\n" 
    	str += "\t" + "return @{" + "\n"
    	for key in dicNameModify:
    			if  type(dic[key]) is types.DictType:
    				str += "\t" + " @\"%s\" : @\"%s\" " % (lowerFirstLetter(dicNameModify[key]),lowerFirstLetter(key)) + "," + "\n"

    	str = str[:-2]
    	str += "\n"
    	str += "\t" "};" + "\n"
    	str += "}" + "\n"
    			
    str += "\n" + "@end"

    return str

def upperFirstLetter(str):
	 return (str[0:1].upper() + str[1:])
def lowerFirstLetter(str):
	 return (str[0:1].lower() + str[1:])	 
