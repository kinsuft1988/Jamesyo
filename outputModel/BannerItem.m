// 

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