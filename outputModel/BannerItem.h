// //  BannerItem.h//  xwd////  Created by kinsuft on 2017/08/16.//  Copyright 2017 year CTiOS-org. All rights reserved.//#import <UIKit/UIKit.h>

#import "TestBannerItem.h" 
#import "JustItem.h" 
 
@interface BannerItem : NSObject

@property (nonatomic, strong) NSString* target_url;
@property (nonatomic, strong) TestBannerItem* testBannerItem;
@property (nonatomic) NSInteger seq;
@property (nonatomic) CGFloat money;
@property (nonatomic, strong) NSArray<JustItem*>* justArray;
@property (nonatomic) NSInteger id;
@property (nonatomic, strong) NSString* alt_Text;
@property (nonatomic, strong) NSString* pic_url;
@property (nonatomic, strong) NSString* subject;

@end