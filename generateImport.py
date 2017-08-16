import json


def generateImportH(dic):

    str = "#import <UIKit/UIKit.h>" + "\n"

    for view in dic.get('children'):
        if view.get('children'): 
            viewTypes = view['name'][0:1].upper() + view['name'][1:]  
            str += "#import \"" + \
                 viewTypes[0:1].upper() + viewTypes[1:] + ".h\"" + "\n"

    strPorperties = generatePropertiesH(dic)

    return (str + "\n\n" + strPorperties)


def generatePropertiesH(dic):

    arrImport = childView(dic)
    viewType = arrImport[0][0:1].upper() + arrImport[0][1:]
    viewParentType = dic['classType']
    str = "@interface " + viewType + " : " + viewParentType + "\n\n"

    if dic.get('isNavGradient'):
        str += "@property (nonatomic, strong) CTNavGradientView* navView;" + "\n"

    if dic.get('isScroll'):
        str += "@property (nonatomic, strong) UIScrollView *scrollView;" + "\n"
        str += "@property (nonatomic, strong) UIView *contentView;" + "\n"

    for view in dic.get('children'):
        if view.get('children'):

            viewType = view['name'][0:1].upper() + view['name'][1:]
            str += "@property (nonatomic, strong) " + \
                viewType + " *" + view['name'] + ";\n"

        else:

            str += "@property (nonatomic, strong) " + \
                view['classType'] + " *" + view['name'] + ";\n"          

    str += "\n" + "@end"

    return str


def childView(dic):

    arrFinal = []

    if dic.get('children'):

        arr = []

        str = dic['name']

        arr.append(str)

        for x in dic.get('children'):
            arrFinal = arrayApend(arr, childView(x))

    return arrFinal


def arrayApend(arr1, arr2):

    if arr1:
        for x in arr2:
            arr1.append(x)

    else:
        return

    return arr1

