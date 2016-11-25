// 

#import "TestDic.h" 
#import "JustItem.h" 
 
@interface BannerItem : NSObject

@property (nonatomic, strong) NSString* target_url;
@property (nonatomic, strong) TestDic* testDic;
@property (nonatomic) NSInteger seq;
@property (nonatomic, strong) NSArray<JustItem*>* justArray;
@property (nonatomic) NSInteger id;
@property (nonatomic, strong) NSString* alt_Text;
@property (nonatomic, strong) NSString* pic_url;
@property (nonatomic, strong) NSString* subject;

@end