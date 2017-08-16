//
//  UIColor+ConfigWithHex.m
//  hyd
//
//  Created by 胡昆 on 16/4/8.
//  Copyright © 2016年 CTiOS. All rights reserved.
//

#import "UIColor+ConfigWithHex.h"

@implementation UIColor (ConfigWithHex)

// Convert a 6-character hex color to a UIColor object
+ (UIColor *)getColor:(NSString *)hexColor {

  unsigned int red, green, blue;
  NSRange range;
  range.length = 2;

  range.location = 0;
  [[NSScanner scannerWithString:[hexColor substringWithRange:range]]
      scanHexInt:&red];

  range.location = 2;
  [[NSScanner scannerWithString:[hexColor substringWithRange:range]]
      scanHexInt:&green];

  range.location = 4;
  [[NSScanner scannerWithString:[hexColor substringWithRange:range]]
      scanHexInt:&blue];

  return [UIColor colorWithRed:(float)(red / 255.0f)
                         green:(float)(green / 255.0f)
                          blue:(float)(blue / 255.0f)
                         alpha:1.0f];
}

+ (UIColor *)getColor:(NSString *)hexColor WithAlpha:(CGFloat)alpha {

  unsigned int red, green, blue;
  NSRange range;
  range.length = 2;

  range.location = 0;
  [[NSScanner scannerWithString:[hexColor substringWithRange:range]]
      scanHexInt:&red];

  range.location = 2;
  [[NSScanner scannerWithString:[hexColor substringWithRange:range]]
      scanHexInt:&green];

  range.location = 4;
  [[NSScanner scannerWithString:[hexColor substringWithRange:range]]
      scanHexInt:&blue];

  return [UIColor colorWithRed:(float)(red / 255.0f)
                         green:(float)(green / 255.0f)
                          blue:(float)(blue / 255.0f)
                         alpha:alpha];
}

@end
