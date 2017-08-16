import json

def generatetControllerH(dic):

	 str = "#import <UIKit/UIKit.h>" + "\r\r"
	 str += "@interface %s : UIViewController" % (
	     dic['name'][0:1].upper() + dic['name'][1:] + "Controller") + "\r\r"
	 str += "@end"

	 return str


def generatetControllerM(dic):

	 return generatetMfileImport(dic) + generatetMfileProperties(dic) + generatetMfileImplementation(dic)


def generatetMfileImport(dic):

	str = "#import \"%s.h\"" % (
	    dic['name'][0:1].upper() + dic['name'][1:] + "Controller") + "\r"
	str += "#import \"%s.h\"" % (dic['name']
	                             [0:1].upper() + dic['name'][1:]) + "\r\r"

	return str


def generatetMfileProperties(dic):

	str = "@interface %s ()" % (
	    dic['name'][0:1].upper() + dic['name'][1:] + "Controller") + "\r\r"
	str += "@property (nonatomic, strong) %s *homeView;" % (
	    dic['name'][0:1].upper() + dic['name'][1:]) + "\r\r"
	str += "@end" + "\r\r"

	return str


def generatetMfileImplementation(dic):

	str = "@implementation %s" % (
	    dic['name'][0:1].upper() + dic['name'][1:] + "Controller") + "\r\r"

	str += generateFuncLoadView(dic) + generateFuncViewDidLoad(dic) + \
	                            generateFuncAddTargetActions(dic)

	str += "@end"

	return str


def generateFuncLoadView(dic):

	str = "- (void)loadView" + "\r" + "{\r"
	str += "\t" + \
	    "self.view = %s.new;" % (
	        dic['name'][0:1].upper() + dic['name'][1:]) + "\r"
	str += "\t" + \
	    "self.homeView = (%s *)self.view;" % (dic['name']
	                      [0:1].upper() + dic['name'][1:]) + "\r"
	str += "}" + "\r\r"

	return str


def generateFuncViewDidLoad(dic):

	str = "- (void)viewDidLoad" + "\r" + "{\r"
	str += "\t" + "[super viewDidLoad];" + "\r\r"
	str += "\t" + "[self addTargetActions];" + "\r"
	str += "}" + "\r\r"

	return str


def generateFuncAddTargetActions(dic):

	strAddTargetActions = "#pragma mark - configs" + "\r"
	strActionsHandles = "#pragma mark - actions handle" + "\r"

	strAddTargetActions += "- (void)addTargetActions" + "\r" "{\r\r"

	if dic.get('isNavGradient'):
		strAddTargetActions += "\t[self.homeView.navView addLeftBtnTargets:self action:@selector(btnGradientNavBackTappedEventHandle) forControlEvents:UIControlEventTouchUpInside];" + "\r\r"

	if reducerGenerateActions(dic, "self"):
		strAddTargetActions += reducerGenerateActions(dic, "self")

	strAddTargetActions += "}" + "\r\r"

	strResultHand = reducerGenerateActionsHandle(dic, "self")

	if strResultHand:
		strAddTargetActions += "#pragma mark - actions handle" + "\r"

    	if dic.get('isNavGradient'):
    		strAddTargetActions += "- (void)btnGradientNavBackTappedEventHandle" + "\r" + "{\r\r"
    		strAddTargetActions += "\t[self.navigationController popToRootViewControllerAnimated:YES];" + "\r\r"
    		strAddTargetActions += "}" + "\r\r"
			

	strAddTargetActions += strResultHand  

	return strAddTargetActions


def reducerGenerateActions(dic, string):

	 if dic.get('classType') == "UIButton":

		return "\t[%s.%s  addTarget:self action:@selector(%s) forControlEvents:UIControlEventTouchUpInside];\r\r" % (string, dic['name'],(dic['name'] + "TappedEventHandle"))

	 else:

	 	strTotal = ""

	 	if dic.get('children'):

	 		dicName = dic['name']

	 		if string == "self":
	 			dicName = "homeView"

	 		for subDic in dic['children']:
	 			if reducerGenerateActions(subDic, (string + '.' + dicName)):
	 				strTotal += reducerGenerateActions(subDic, (string + '.' + dicName))

	    	return strTotal


def reducerGenerateActionsHandle(dic, string):

	 if dic.get('classType') == "UIButton":

	 	str = "- (void)%s" % (dic['name'] + "TappedEventHandle") + "\r" + "{\r\r}" + "\r\r"

		return str

	 else:

	 	strTotal = ""

	 	if dic.get('children'):

	 		dicName = dic['name']

	 		if string == "self":
	 			dicName = "homeView"

	 		for subDic in dic['children']:
	 			if reducerGenerateActionsHandle(subDic, (string + '.' + dicName)):
	 				strTotal += reducerGenerateActionsHandle(subDic, (string + '.' + dicName))

	    	return strTotal	    	

	 					
	

