//
//  CTNavGradientView.h
//  hyd
//
//  Created by 胡昆 on 16/4/13.
//  Copyright © 2016年 CTiOS. All rights reserved.
//

#import <UIKit/UIKit.h>

@class CTNavGradientView;
typedef void (^ConfigBlock)(CTNavGradientView *);

@interface CTNavGradientView : UIView

@property (nonatomic, strong) UIButton *btnLeft;
@property (nonatomic, strong) UIButton *btnLeftMask;
@property (nonatomic, strong) UIButton *btnRight;
@property (nonatomic, strong) UILabel *lblTitel;
@property (nonatomic, weak) UIScrollView *scrollView;
@property (nonatomic, strong) UIView *viewBackGradient;

- (id)initWithConfigBlock:(ConfigBlock)configHandle;

//增加渐变的依赖对象scrollview
- (void)addObserverWithScrollView:(UIScrollView *)scrollView;
- (void)removeObjectSevers;

- (void)addLeftBtnTargets:(id)taget action:(SEL)selector forControlEvents:(UIControlEvents)controlEvents;

@end
