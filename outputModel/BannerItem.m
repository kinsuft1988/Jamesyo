// //  BannerItem.m//  xwd////  Created by kinsuft on 2017/08/16.//  Copyright 2017 year CTiOS-org. All rights reserved.//#import "BannerItem.h" 

@implementation BannerItem

+ (NSDictionary *)objectClassInArray
	{
	return @{
	 @"justArray" : [JustItem class] 
	};
}
+ (NSDictionary *)replacedKeyFromPropertyName
	{
	return @{
	 @"testBannerItem" : @"testBanner" 
	};
}

@end