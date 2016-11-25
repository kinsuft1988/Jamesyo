# Jamesyo

##JSON ==> Model (Objective-C)

###when the json path is testModel.json

      {
        "id": 2,
        "seq": 1,
        "subject": "subject_01",
        "pic_url": "images/pic_01.gif",
        "alt_Text": "subject_01",
        "target_url": "target_url_01",
        "testBanner" : {
            "id" : 2
        },
        "justArray" : [
            {
                "id":3,
                "name": "hehe"
            }
        ]
      }


###then use the command:

python james.py -j testModel

```
input the Model Name: BannerItem

rename The Dic Object testBanner  with name: TestDic

name the Item in the  the array  justArray : JustItem

```

####At last will create the file: 
+ BannerItem.h  BannerItem.m 
+ TestDic.h  TestDic.m
+ JustItem.h JustItem.m

##Thanks [ESJsonFormat-Xcode](https://github.com/EnjoySR/ESJsonFormat-Xcode)   [MJExtension](https://github.com/CoderMJLee/MJExtension)