//
//  CTNavGradientView.m
//  hyd
//
//  Created by 胡昆 on 16/4/13.
//  Copyright © 2016年 CTiOS. All rights reserved.
//

#import "CTNavGradientView.h"
#import "CTKit.h"
#import <Masonry.h>

@interface CTNavGradientView ()

@property (nonatomic, strong) UIView* blurView;

@end

@implementation CTNavGradientView

- (id)init
{
    return nil;
}

- (id)initWithConfigBlock:(ConfigBlock)configHandle
{
    self = [super init];

    if (!self)
        return nil;

    [self initProperties];

    [self addViewConstraints];

    [self config];

    __weak CTNavGradientView *weakself = self;

    configHandle(weakself);

    return self;
}

- (void)initProperties
{
    
    
    self.viewBackGradient = [[UIView alloc] init];
    [self addSubview:self.viewBackGradient];
    
    UIBlurEffect *blurEffect = [UIBlurEffect effectWithStyle:UIBlurEffectStyleLight];
    self.blurView = [[UIVisualEffectView alloc] initWithEffect:blurEffect];
    [self.viewBackGradient addSubview:self.blurView];

    self.btnLeft = [UIButton buttonWithType:UIButtonTypeCustom];
    [self addSubview:self.btnLeft];

    self.lblTitel = [[UILabel alloc] init];
    [self addSubview:self.lblTitel];

    self.btnRight = [UIButton buttonWithType:UIButtonTypeCustom];
    [self addSubview:self.btnRight];
    
    self.btnLeftMask = [[UIButton alloc] init];
    [self.viewBackGradient addSubview:self.btnLeftMask];
    
}

- (void)config
{
    self.backgroundColor = [UIColor clearColor];

    self.lblTitel.font = [UIFont fontWithName:Font_Bold size:17.0];
    self.lblTitel.textAlignment = NSTextAlignmentCenter;

    self.viewBackGradient.alpha = 0;
    
    self.viewBackGradient.backgroundColor = [UIColor clearColor];
    
    
}

- (void)addViewConstraints
{
    [self.viewBackGradient mas_makeConstraints:^(MASConstraintMaker *make) {

      make.size.equalTo(self);
      make.center.equalTo(self);

    }];
    
    [self.blurView mas_makeConstraints:^(MASConstraintMaker *make) {
        
        make.size.equalTo(self.viewBackGradient);
        make.center.equalTo(self.viewBackGradient);
        
    }];
    
    [self.btnLeftMask mas_makeConstraints:^(MASConstraintMaker *make) {
        
        make.top.equalTo(self.mas_top).offset(20);
        make.left.equalTo(@20);
        make.width.equalTo(@40);
        make.height.equalTo(@(44));
        
    }];

    [self.lblTitel mas_makeConstraints:^(MASConstraintMaker *make) {

      make.top.mas_equalTo(self).offset(20);
      make.bottom.mas_equalTo(self);
      make.centerX.mas_equalTo(self);
      make.width.mas_equalTo(120);

    }];

    [self.btnLeft mas_makeConstraints:^(MASConstraintMaker *make) {

      make.top.equalTo(self.mas_top).offset(20);
      make.left.equalTo(@20);
      make.width.equalTo(@40);
      make.height.equalTo(@(44));

    }];

    [self.btnRight mas_makeConstraints:^(MASConstraintMaker *make) {

      make.top.equalTo(self.mas_top).offset(20);
      make.right.equalTo(self.mas_right).offset(-20);
      make.width.equalTo(@80);
      make.height.equalTo(@(44));

    }];
}

- (void)addObserverWithScrollView:(UIScrollView *)scrollView;
{
    self.scrollView = scrollView;

    [self.scrollView addObserver:self forKeyPath:@"contentOffset" options:NSKeyValueObservingOptionNew | NSKeyValueObservingOptionOld context:nil];
}

- (void)observeValueForKeyPath:(NSString *)keyPath ofObject:(id)object change:(NSDictionary<NSString *, id> *)change context:(void *)context
{
    CGPoint point = [[change objectForKey:@"new"] CGPointValue];
    self.viewBackGradient.alpha = point.y / 200.0;
    self.btnLeft.alpha = 1 - self.viewBackGradient.alpha;
}

- (void)removeObjectSevers
{
    [self.scrollView removeObserver:self forKeyPath:@"contentOffset"];
}

//- (void)dealloc
//{
//    [self.scrollView removeObserver:self forKeyPath:@"contentOffset"];
//}

- (void)addLeftBtnTargets:(id)taget action:(SEL)selector forControlEvents:(UIControlEvents)controlEvents
{
    [self.btnLeft addTarget:taget action:selector forControlEvents:controlEvents];
    [self.btnLeftMask addTarget:taget action:selector forControlEvents:controlEvents];

}


@end
