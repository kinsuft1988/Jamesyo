// //  orderInfoView.m//  xwd////  Created by kinsuft on 2017/08/16.//  Copyright 2017 year CTiOS-org. All rights reserved.//#import "OrderInfoView.h"
#import "CTKit.h"
#import <Masonry.h>

@interface OrderInfoView ()

@end

@implementation OrderInfoView

- (id)init
{
	self = [super init];

	if (!self)
	  return nil;

	[self initProperties];

	[self addViewConstraints];

	[self config];

	return self;

}

- (void)initProperties
{
	self.lblOrderNumberIndicator = UILabel.new;
	[self addSubview:self.lblOrderNumberIndicator];

	self.lblOrderNumber = UILabel.new;
	[self addSubview:self.lblOrderNumber];

}

- (void)addViewConstraints
{

	[self.lblOrderNumberIndicator mas_makeConstraints:^(MASConstraintMaker *make) {



	}];

	[self.lblOrderNumber mas_makeConstraints:^(MASConstraintMaker *make) {



	}];

}

- (void)config
{
	//config childViews and itself

}

@end

