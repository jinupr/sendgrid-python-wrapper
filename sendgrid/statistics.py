# -*- coding: utf-8 -*-

#########################################################################
#    FileName : statistics.py
#    Sendgrid Statistics Web API
#    Author: Jinu P R
#    CopyRight: My Parichay 2014. All Rights Reserved
#########################################################################

import validations
import sys
import datetime

from sendgrid import SendGridClient

class GeneralStatistics(object):
    """ Sendgrid General Statistics Base Class """

    def __init__(self, validate=False, **opts):

        """
            Constructs SendGrid General Statistics Object
            Args:
                    General Statistics
                        days : Number of days
                        start_date : Start date to look up for statistics
                        end_date : End date to look up for statistics
                        aggregate : 0 to indicate not to include all-time locals
                                    1 to indicate to include all-time locals
                        raise_errors: If set to False: in case of error, `.send`
                                      method will return a tuple (http_code, error_message). If set
                                      to True: `.send` will raise SendGridError. Note, from version
                                      1.0.0, the default will be changed to True, so you are
                                      recommended to pass True for forwards compatability.      

        """

        self.possible_values = ['days','start_date','end_date','aggregate','category']
        self.endpoint = "/api/stats.get.json"        
        self.validate = validate

        if self.validate:
           self.validate_args(**opts) 
        else:
            self.days = opts.get("days",None)
            self.start_date = opts.get("start_date",None)
            self.end_date = opts.get("end_date",None)
            self.aggregate = opts.get("aggregate",None)
            self.category = opts.get("category",None)

    def validate_args(self,**opts):

        """ Validates and set values if validate is true """

        self.set_days(opts.get("days", None))
        self.set_start_date(opts.get("start_date", None))
        self.set_end_date(opts.get("end_date", None))
        self.set_aggregate(opts.get("aggregate", None))
        self.set_category(opts.get("category", None))

    def set_days(self,days):

        """ Validates and set days """

        if days and self.validate:
            if validations.is_valid_no_of_days(days):
                self.days = days
            else:
                raise ValueError("Invalid Number of Days")
        else:
            self.days = days

    def set_start_date(self,start_date):

        """ validates and set start_date """

        if start_date and self.validate:
            if validations.is_valid_date(self, start_date):
                self.start_date = start_date
            else:
                raise ValueError("Invalid Start Date Value")
        else:
            self.start_date = start_date

    def set_end_date(self,end_date):

        """ validates and set end_date """

        if end_date and self.validate:
            if validations.is_valid_date(self, end_date):
                self.end_date = end_date
            else:
                raise ValueError("Invalid End Date Value")
        else:
            self.end_date = end_date

    def set_aggregate(self,aggregate):
        
        """ validates and set aggregate value """

        if aggregate and self.validate:
            if validations.is_valid_aggregate(aggregate):
                self.aggregate = aggregate
            else:
                raise ValueError("Invalid Aggregate Value")
        else:
            self.aggregate = aggregate

    def set_category(self,category):

        """ validates and sets category"""

        if category:
            if isinstance(category,str) or isinstance(category,list):
                self.category = category
        else:
            self.category = category

    def add_category(self, category):
        
        """ validates and add to existing category"""

        if isinstance(category,list):
            if isinstance(self.category,list):
                self.category.extend(category)
            elif isinstance(self.category,str):
                category.append(self.category)
                self.category = category
            else:
                raise ValueError("Invalid Category Value Format")
        elif isinstance(category,str):
            if isinstance(self.category,list):
                self.category.append(category)
            elif isinstance(self.category,str):
                self.set_category([self.category])
                self.add_category(category)
        else:
            raise ValueError("Invalid Category Value Format")
    

class AdvancedStatistics(object):

    """ Sendgrid Advanced Statistics Base Class """

    def __init__(self, data_type="global",start_date=datetime.date.today().strftime("%Y-%m-%d"), 
                validate=False,**opts):
        """
            Constructs Advanced Statistics Object
            Args:
                Advanced Statistics
                    data_type : Date Type for which statistics has to retrieved
                    start_date : Start date to look up for statistics
                    end_date : End date to look up for statistics
                    metric : Metric for which the statistics has to be retrieved
                    category : Category for which to retrieve Statistics
                    aggregated_by : Aggregation Value for which statistics has to be retrieved
                    country : Country Name for which the statistics has to be retrieved
                    raise_errors: If set to False: in case of error, `.send`
                                      method will return a tuple (http_code, error_message). If set
                                      to True: `.send` will raise SendGridError. Note, from version
                                      1.0.0, the default will be changed to True, so you are
                                      recommended to pass True for forwards compatability.      
        """
        self.endpoint = "/api/stats.getAdvanced.json" 
        self.possible_values = ['data_type','start_date','end_date','metric','aggregated_by','category','country']
        self.validate = validate
        self.data_type = data_type
        self.start_date = start_date
        
        if self.validate:
            self.validate_args(data_type,start_date,**opts) 
        else:
            self.end_date = opts.get("end_date",None)
            self.metric = opts.get("metric",None)
            self.category = opts.get("category",None)
            self.aggregated_by = opts.get("aggregated_by",None)
            self.country = opts.get("country",None)

    def validate_args(self,data_type, start_date, **opts):

        """ validates and set values if validate is True """

        self.set_data_type(data_type)
        self.set_aggregated_by(opts.get("aggregated_by", None))
        self.set_start_date(start_date)
        self.set_end_date(opts.get("end_date", None))
        self.set_metric(opts.get("metric",None))
        self.set_category(opts.get("category", None))
        self.set_country(opts.get("country", None))

    def set_data_type(self,data_type):

        """ validates and set data type """

        if data_type and self.validate:
            if validations.is_valid_data_type(self,data_type):
                self.data_type = data_type
            else:
                raise ValueError("Invalid Data Type Value")
        else:
            self.data_type = data_type

    def set_start_date(self,start_date):

        """ validates and set start_date""" 

        if start_date and self.validate:
            if validations.is_valid_date(self, start_date):
                self.start_date = start_date
            else:
                raise ValueError("Invalid Start Date Value")
        else:
            self.start_date = start_date

    def set_end_date(self,end_date):

        """ validates and set_end_date """

        if end_date and self.validate:
            if validations.is_valid_date(self, end_date):
                self.end_date = end_date
            else:
                raise ValueError("Invalid End Date Value")
        else:
            self.end_date = end_date

    def set_metric(self,metric):

        """  validates and set metric """

        if metric and self.validate:
            if validations.is_valid_metric(self,metric):
                self.metric = metric
            else:
                raise ValueError("Invalid Metric Value Format")
        else:
            self.metric = metric

    def set_category(self,category):

        """ validates and set category """

        if category:
            if isinstance(category,str) or isinstance(category,list):
                self.category = category
        else:
            self.category = category

    def add_category(self, category):

        """ validates and add to existing category """

        if isinstance(category,list):
            if isinstance(self.category,list):
                self.category =self.category.extend(category)
            elif isinstance(self.category,str):
                prev_category = self.category
                self.category = [self.category]
                self.category =self.category.extend(category)
            else:
                raise ValueError("Invalid Category Value Format")
        elif isinstance(category,str):
            if isinstance(self.category,list):
                self.category = self.category.append(category)
            elif isinstance(self.category,str):
                self.category = [self.category].append(category) 
        else:
            raise ValueError("Invalid Category Value Format")

    def set_aggregated_by(self,aggregated_by):

        """ validates and set aggregated_by value """

        if aggregated_by and self.validate:
            if validations.is_valid_aggregated_by_value(self,aggregated_by):
                self.aggregated_by = aggregated_by
            else:
                raise ValueError("Invalid Aggregated By Value Format")
        else:
            self.aggregated_by = aggregated_by

    
    def set_country(self,country):

        """ validates and set country """

        if country and self.validate:
            if validations.is_valid_country(self,country):
                self.country = country 
            else:
                raise ValueError("Invalid Country Value Format")
        else:
            self.country = country


