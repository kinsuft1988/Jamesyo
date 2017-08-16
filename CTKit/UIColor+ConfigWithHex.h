//
//  UIColor+ConfigWithHex.h
//  hyd
//
//  Created by 胡昆 on 16/4/8.
//  Copyright © 2016年 CTiOS. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface UIColor (ConfigWithHex)

+ (UIColor *)getColor:(NSString *)hexColor;
+ (UIColor *)getColor:(NSString *)hexColor WithAlpha:(CGFloat)alpha;

@end
