// //  orderProgressDetailView.m//  xwd////  Created by kinsuft on 2017/08/16.//  Copyright 2017 year CTiOS-org. All rights reserved.//#import "OrderProgressDetailView.h"
#import "CTKit.h"
#import <Masonry.h>

@interface OrderProgressDetailView ()

@end

@implementation OrderProgressDetailView

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
	self.orderInfoView = OrderInfoView.new;
	[self addSubview:self.orderInfoView];

	self.tableView = UITableView.new;
	[self addSubview:self.tableView];

	self.btnConfirm = UIbutton.new;
	[self addSubview:self.btnConfirm];

}

- (void)addViewConstraints
{

	[self.orderInfoView mas_makeConstraints:^(MASConstraintMaker *make) {



	}];

	[self.tableView mas_makeConstraints:^(MASConstraintMaker *make) {



	}];

	[self.btnConfirm mas_makeConstraints:^(MASConstraintMaker *make) {



	}];

}

- (void)config
{
	//config childViews and itself

}

@end

