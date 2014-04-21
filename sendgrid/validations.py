# -*- coding: utf-8 -*-

#########################################################################
#    FileName : validations.py
#    Validation Functions for SendGrid Web API Statistics Parameters
#    Author: Jinu P R
#    CopyRight: My Parichay 2014. All Rights Reserved
#########################################################################

import sys
from datetime import datetime

def is_valid_date(self, date):
    """
        Return True if valid date
               False if not a valid date
               based on the endpoint
    """
    if self.endpoint == "/api/stats.get.json":
        try:
            datetime.strptime(date, '%Y-%m-%d')
            return True
        except:
            return False
    elif self.endpoint == "/api/stats.getAdvanced.json":
        if not self.aggregated_by or self.aggregated_by == "day":
            try:
                datetime.strptime(date, '%Y-%m-%d')
                return True
            except:
                return False
        elif self.aggregated_by and self.aggregated_by == "week":
            try:
                datetime.strptime(date, '%Y-%W')
                return True
            except:
                return False
        elif self.aggregated_by and self.aggregated_by == "month":
            try:
                datetime.strptime(date, '%Y-%m')
                return True
            except:
                return False
        else:
            return False
            
    
def is_valid_country(self,country):
    """
        Return True if valid Country Code
        Return False if not a valid Country Code
        #Note: Only US and CA are supported at this time
    """
    if self.endpoint == "/api/stats.getAdvanced.json":
        possible_country_values =["US", "CA"]
        if country in possible_country_values:
            return True
        else:
            return False
    else:
        return False



def is_valid_aggregate(aggregate):
    """
        Return True if valid Aggregate Value
        Return False if not
        Possible Values: 0 0r 1
    """
    if aggregate == 0  or aggregate == 1:
        return True
    else:
        return False
     
def is_valid_aggregated_by_value(self,aggregated_by):
    """
        Return True if a valid aggregated_by Value 
        Return False if not
        Possible Values: day,week,month
    """
    if self.endpoint == "/api/stats.getAdvanced.json":
        possible_aggregated_by_values =["day","week","month"] 
        if aggregated_by in possible_aggregated_by_values:
            return True
        else:
            return False
    else:
        return False   


def is_valid_data_type(self,data_type):
    """
        Return True if a valid date_type
        Return False if not
        Possible Values: browsers, clients, devices, geo, global, isps  
    """
    if self.endpoint == "/api/stats.getAdvanced.json":
        possible_data_type_values = ["browsers","clients","devices","geo","global","isps"]  
        if data_type in possible_data_type_values:
            return True
        else:
            return False

def is_valid_no_of_days(days):
    """
        Return True if valid and if value greater than zero
        Return False if not
        Possible Values: All integers greater than zero
    """
    try:
        days_value = int(days)
        if days_value > 0:
            return True
    except:
        return False

def is_valid_metric(self, metric):
    """
        Return True if a valid Metric Value
        Return False if not
        Possible Values: open, click, unique_open, unique_click, processed, delivered, drop, bounce,
                         deferred, spamreport, blocked, all
    """
    if self.endpoint == "/api/stats.getAdvanced.json":
        possible_metric_values = [ "open", "click", "unique_open", "unique_click", "processed", "delivered", "drop",
                                  "bounce", "deferred", "spamreport", "blocked", "all" ]
        if metric in possible_metric_values:
            return True
        else:
            return False
    else:
        return False

