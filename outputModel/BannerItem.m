// //  BannerItem.m//  xwd////  Created by kinsuft on 2016/11/25.//  Copyright 2016 year CTiOS-org. All rights reserved.//#import "BannerItem.h" 

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
	 @"testDic" : @"testBanner" 
	};
}

@end