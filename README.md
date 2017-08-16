## Jamesyo
### 通过JSON的描述方式快速生成iOS的Controller,View以及Model文件

### -g命令:生成基本的View文件
用法: python james.py -g ./TestJsonFile/orderProgressDetail

### -c命令:生成View以及Controller文件
 python james.py -c ./TestJsonFile/orderProgressDetail

#### 注意:针对tableView,先将tableView按照普通的层级处理后(-c命令)，再单独的对cell的json文件处理，生成对应的view （-g命令）
 举例: 
  python james.py -c ./TestJsonFile/orderProgressDetail 
  
python james.py -g ./TestJsonFile/oderProgressUnArrivedStatusCell

python james.py -g ./TestJsonFile/orderProgressTransferMoneyFailedCell

### -j命令:生成基本的Model文件
 python james.py -c ./TestModel/banner

这里的Model文件配合MJExtension使用，实际上是由于Xcode插件被禁止了之后，替代ESJsonFormat-Xcode来使用的

这里感谢ESJsonFormat-Xcode和MJExtension的作者


### JSON配置规则
#### 基本规则
  一个节点有name,classType的必要配置属性，以及children这个选择配置属性
  
   name:变量名
   
classType:类型,如果是最底层的节点，classType应对应一个基本的UIKit的或者自定义的控件类型

  children:对应子节点，用于组合嵌套的表达结构

  举例:
  
```
  {
    "name": "orderProgressDetailView",
    "classType": "UIView",
    "children": [
        {
            "name": "orderInfoView",
            "classType": "UIView",
            "children": [

                {
                    "name": "lblOrderNumberIndicator",
                    "classType": "UILabel"
                },
                {
                    "name": "lblOrderNumber",
                    "classType": "UILabel"
                }
            ]
        },
        {
            "name": "tableView",
            "classType": "UITableView"
        },
        {
            "name": "btnConfirm",
            "classType": "UIButton"
        }

    ]

}
```

这段json描述了页面含有一个基本的UIView(orderProgressDetailView),然后它包含了三个子View(orderInfoView,tableView,btnConfirm)

 其中orderInfoView又拥有两个子View（lblOrderNumberIndicator,lblOrderNumber）


#### 扩展功能"isScroll"
    使用方法: view.json的根节点添加 "isScroll": "YES"
    功能介绍: View的基本页面变为可滚动页面
 

#### 扩展功能"isNavGradient"
    使用方法: view.json的根节点添加"isNavGradient"项即可，见./TestJsonFile/loanView.json
    功能介绍:       针对初始页面导航部分背景色需要为clearColor，但是滚动后又需要导航背景色的情况
    实现方式: 
       （1）在controller中添加了btnGradientNavBackTappedEventHandle事件
       （2）在view中增加了navView的，以及delloc中的removeObserver
