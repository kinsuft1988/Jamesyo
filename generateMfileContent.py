import json
import generateImport


from generateImport import childView, arrayApend


def generateMfileInfo(dic):

    strPre = generateMainPre(dic)
    strMainContent = generateMainContent(dic)
    strFooter = generateFooterContent(dic)

    return strPre + strMainContent + strFooter


def generateMainPre(dic):
    str = "#import \"" + \
        (dic['name'][0:1].upper() + dic['name'][1:]) + ".h\"" + "\n"
    str += "#import \"CTKit.h\"" + "\n"
    str += "#import <Masonry.h>" + "\n"
    str += "\n"
    str += "@interface " + \
        (dic['name'][0:1].upper() + dic['name'][1:]) + " ()" + "\n"
    str += "\n"
    str += "@end" + "\n\n"
    str += "@implementation " + \
        (dic['name'][0:1].upper() + dic['name'][1:]) + "\n\n"
    return str


def generateMainContent(dic):
    return generateContentInit(dic) + generateContentProperties(dic)  \
        + generateContentViewConstaints(dic) + generateContentConfig(dic)


def generateFooterContent(dic):
    str = "@end" + "\n\n"
    return str


def generateContentInit(dic):

    if dic['classType'] == "UITableViewCell":
    	str = "- (instancetype)initWithStyle:(UITableViewCellStyle)style reuseIdentifier:(NSString *)reuseIdentifier" + "\n"

    else:
		str = "- (id)init" + "\n"	

    str += "{" + "\n"

    if dic['classType'] == "UITableViewCell":
    	str += "\t" + "self = [super initWithStyle:style reuseIdentifier:reuseIdentifier];" + "\n\n"
    else:
    	str += "\t" + "self = [super init];" + "\n\n"

    str += "\t" + "if (!self)" + "\n"
    str += "\t" + "  " + "return nil;" + "\n\n"
    str += "\t" + "[self initProperties];" + "\n\n"
    str += "\t" + "[self addViewConstraints];" + "\n\n"
    str += "\t" + "[self config];" + "\n\n"
    str += "\t" + "return self;" + "\n\n"
    str += "}" + "\n\n"
    return str


def generateContentProperties(dic):
    str = "- (void)initProperties" + "\n"
    str += "{" + "\n"
    superview = "self"

    if dic.get('isScroll'):
    	str += "\t" + "self.scrollView = UIScrollView.new;" + "\n"
    	str += "\t" + " [self addSubview:self.scrollView];" + "\n\n"

    	str += "\t" + "self.contentView = UIView.new;" + "\n"
    	str += "\t" + "[self.scrollView addSubview:self.contentView];" + "\n\n"

    	superview = "self.contentView"

    if dic['classType'] == "UITableViewCell":
    	superview = "self.contentView"

    for view in dic.get('children'):
        if view.get('children'):
            viewType = view['name'][0:1].upper() + view['name'][1:]
            str += "\t" + "self." + \
            	view['name'] + " = " + viewType + ".new;" + "\n"
            str += "\t" + "[%s addSubview:self.%s];" % (superview, view['name']) + "\n\n"

        else:

            viewType = view['classType']
            str += "\t" + "self." + \
                view['name'] + " = " + viewType + ".new;" + "\n"
            str += "\t" + \
                "[%s addSubview:self.%s];" % (superview, view['name']) + "\n\n"

    if dic.get('isNavGradient'):
    	
    	str += "\t" + "self.navView = [[CTNavGradientView alloc] initWithConfigBlock:^(CTNavGradientView *navView) {" + "\n\n"
    	str += "\t  " + "[navView.btnLeft setImage:[UIImage imageNamed:@\"test\"] forState:UIControlStateNormal];" + "\n"
    	str += "\t  " + "navView.btnLeft.titleLabel.textAlignment = NSTextAlignmentLeft;" + "\n\n"
    	str += "\t  " + "[navView.btnLeftMask setImage:[UIImage imageNamed:@\"test\"] forState:UIControlStateNormal];" + "\n"
    	str += "\t  " + "navView.btnLeftMask.titleLabel.textAlignment = NSTextAlignmentLeft;" + "\n\n"
    	str += "\t  " + "UIEdgeInsets insetsImage;" + "\n"
    	str += "\t  " + "insetsImage.left = -20;" + "\n\n"
    	str += "\t  " + "navView.btnLeft.imageEdgeInsets = insetsImage;" + "\n"
    	str += "\t  " + "navView.btnLeftMask.imageEdgeInsets = insetsImage;" + "\n\n"
    	str += "\t  " + "[navView addObserverWithScrollView:self.scrollView];" + "\n\n"
    	str += "\t" + "}];" + "\n\n"
    	str += "\t" + "[self addSubview:self.navView];" + "\n"

    str += "}" + "\n\n"
    return str


def generateContentViewConstaints(dic):
    str = "- (void)addViewConstraints" + "\n"
    str += "{" + "\n\n"

    if dic.get('isScroll'):

    	str += "\t" + "[self.scrollView mas_makeConstraints:^(MASConstraintMaker *make) {" + "\n\n"
    	str += "\t\t" + "make.edges.equalTo(self);" + "\n\n"
    	str += "\t" + "}];" + "\n\n"

    	str += "\t" + "[self.contentView mas_makeConstraints:^(MASConstraintMaker *make) {" + "\n\n"
    	str += "\t\t" + "make.edges.equalTo(self.scrollView);" + "\n"
    	str += "\t\t" + "make.width.equalTo(self.scrollView);" + "\n\n"
    	str += "\t" + "}];" + "\n\n"

    	str += "\t" + "UIView *superview = self.contentView;" + "\n\n"


    for view in dic.get('children'):
    	str += "\t" + "[self.%s mas_makeConstraints:^(MASConstraintMaker *make) {\n" % view['name']
    	str += "\n\n\n" 
    	str += "\t" + "}];" + "\n\n"

    if dic.get('isScroll'):

    	lastSubView = dic['children'][len(dic['children'])-1]

    	str += "\t" + "[self.scrollView mas_makeConstraints:^(MASConstraintMaker *make) {" + "\n\n"
    	str += "\t\t" + "make.bottom.equalTo(self.%s.mas_bottom);" % lastSubView['name']  + "\n\n"
    	str += "\t" + "}];" + "\n\n"

    if dic.get('isNavGradient'):

    	str += "\t" + "[self.navView mas_makeConstraints:^(MASConstraintMaker *make) {" + "\n\n"
    	str += "\t\t" + "make.top.equalTo(self.mas_top);" + "\n"
    	str += "\t\t" + "make.left.equalTo(@0);" + "\n"
    	str += "\t\t" + "make.width.equalTo(self.mas_width);" + "\n"
    	str += "\t\t" + "make.height.equalTo(@(64));" + "\n\n"    	    	    	
    	str += "\t" + "}];" + "\n\n"



    str += "}" + "\n\n"
    return str


def generateContentConfig(dic):
    str = "- (void)config" + "\n"
    str += "{" + "\n"
    str += "\t" + "//config childViews and itself" + "\n\n"
    str += "}" + "\n\n"

    if dic.get('isNavGradient'):
    	str += "- (void)dealloc" + "\n"
    	str += "{\n" 
    	str += "\t" + "[self.navView removeObjectSevers];" + "\n"
    	str += "}\n"

    return str

