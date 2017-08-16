// //  orderProgressDetailView.h//  xwd////  Created by kinsuft on 2017/08/16.//  Copyright 2017 year CTiOS-org. All rights reserved.//#import <UIKit/UIKit.h>
#import "OrderInfoView.h"


@interface OrderProgressDetailView : UIView

@property (nonatomic, strong) OrderInfoView *orderInfoView;
@property (nonatomic, strong) UITableView *tableView;
@property (nonatomic, strong) UIbutton *btnConfirm;

@end