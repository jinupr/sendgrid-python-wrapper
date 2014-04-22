"""
    FileName : test.py
    Sendgrid Test Module for Statistics Web API
    Author: Jinu P R
    CopyRight: My Parichay 2014. All Rights Reserved
"""


import unittest2 as unittest

import sendgrid

SG_USER, SG_PWD = "myparichay", "s3ndgr!d"

class TestSendGrid(unittest.TestCase):

    def setUp(self):
        self.sg = sendgrid.SendGridClient(SG_USER,SG_PWD,endpoint="/api/stats.get.json")

    def test_default_values(self):
        self.assertEqual(self.sg.username, "myparichay")
        self.assertEqual(self.sg.password, "s3ndgr!d")
        self.assertEqual(self.sg.endpoint, "/api/stats.get.json")

        self.general_st = sendgrid.GeneralStatistics()
        self.assertEqual(self.general_st.validate,False)
        self.assertEqual(self.general_st.days,None)
        self.assertEqual(self.general_st.start_date,None)
        self.assertEqual(self.general_st.end_date,None)
        self.assertEqual(self.general_st.category,None)
        self.assertEqual(self.general_st.aggregate,None)
        print self.sg.send(self.general_st)

    def test_input_general_statistics_values(self):
        self.general_st = sendgrid.GeneralStatistics(days=2, 
                                            start_date="2014-04-14",end_date="2014-04-20",
                                            aggregate=0,category="WebD:CampId:3100")
        print self.sg.send(self.general_st)
        self.general_st = sendgrid.GeneralStatistics(days=90, 
                                            aggregate=0,category="WebD:CampId:1",validate=True)
        print self.sg.send(self.general_st)
        

    def test_general_statistics_values(self):
        self.general_st = sendgrid.GeneralStatistics(days=2)
        self.assertEqual(self.general_st.validate,False)
        self.assertEqual(self.general_st.days,2)
        print self.sg.send(self.general_st)
    
    def test_set_days_general_statistics(self):
        self.general_st = sendgrid.GeneralStatistics(validate=True)
        self.assertRaises(ValueError,self.general_st.set_days,"str")
        self.general_st.set_days(2)
        self.assertEqual(self.general_st.days,2)
        print self.sg.send(self.general_st)

    def test_set_start_date_general_statistics(self):
        self.general_st = sendgrid.GeneralStatistics(validate=True)
        self.assertRaises(ValueError,self.general_st.set_start_date,"str")
        self.general_st.set_start_date("2014-04-10")
        self.assertEqual(self.general_st.start_date,"2014-04-10")
        self.general_st.set_end_date("2014-04-14")
        self.assertEqual(self.general_st.end_date,"2014-04-14")
        print self.sg.send(self.general_st)

    def test_set_end_date_general_statistics(self):
        self.general_st = sendgrid.GeneralStatistics(validate=True)
        self.assertRaises(ValueError,self.general_st.set_end_date,"str")
        self.general_st.set_end_date("2014-04-14")
        self.assertEqual(self.general_st.end_date,"2014-04-14")
        self.general_st.set_aggregate(0)
        self.assertEqual(self.general_st.aggregate,0)
        print self.sg.send(self.general_st)

    def test_set_aggregate_general_statistics(self):
        self.general_st = sendgrid.GeneralStatistics(validate=True)
        self.assertRaises(ValueError,self.general_st.set_aggregate,"str")
        self.general_st.set_aggregate(0)
        self.assertEqual(self.general_st.aggregate,0)
        self.general_st.set_aggregate(1)
        self.assertEqual(self.general_st.aggregate,1)
        print self.sg.send(self.general_st)

    def test_set_category_general_statistics(self):
        self.general_st = sendgrid.GeneralStatistics(validate=True)
        self.general_st.set_category("WebD:CampId:3150")
        self.assertEqual(self.general_st.category,"WebD:CampId:3150")
        self.general_st.set_category("WebD:CampId:3100")
        self.assertEqual(self.general_st.category,"WebD:CampId:3100")

        self.general_st.add_category(["WebD:CampId:3150"])
        self.assertEqual(self.general_st.category,["WebD:CampId:3150","WebD:CampId:3100"])

        self.general_st.set_category(["WebD:CampId:3100","WebD:CampId:3150"])
        self.assertEqual(sorted(self.general_st.category),sorted(["WebD:CampId:3100","WebD:CampId:3150"]))

        self.general_st.add_category(["WebD:CampId:3110","WebD:CampId:3151"])
        self.assertEqual(sorted(self.general_st.category),sorted(["WebD:CampId:3100","WebD:CampId:3150",
                        "WebD:CampId:3110","WebD:CampId:3151"]))
        self.general_st.add_category("WebD:CampId:3111")
        self.assertEqual(sorted(self.general_st.category),sorted(["WebD:CampId:3100","WebD:CampId:3111",
                                "WebD:CampId:3150","WebD:CampId:3110","WebD:CampId:3151"]))
          
        self.general_st.set_category("WebD:CampId:3100")
        self.assertEqual(self.general_st.category,"WebD:CampId:3100")
        self.general_st.add_category("WebD:CampId:3105")
        self.assertEqual(sorted(self.general_st.category),sorted(["WebD:CampId:3100","WebD:CampId:3105"]))

        print self.sg.send(self.general_st)

class TestSendGridAdvancedStatistics(unittest.TestCase):
    def setUp(self):
        self.sg = sendgrid.SendGridClient(SG_USER,SG_PWD,endpoint="/api/stats.getAdvanced.json")
        self.assertEqual(self.sg.username, "myparichay")
        self.assertEqual(self.sg.password, "s3ndgr!d")
        self.assertEqual(self.sg.endpoint, "/api/stats.getAdvanced.json")

    def test_default_values_advanced_statistics(self):
        self.advanced_st = sendgrid.AdvancedStatistics(data_type="global",
                              start_date="2014-04-13", validate=True) 
        self.assertEqual(self.advanced_st.validate,True)
        print self.sg.send(self.advanced_st)

    def test_default_input_values_advanced_statistics(self):
        self.advanced_st = sendgrid.AdvancedStatistics(data_type="global",start_date="2014-04-13",
                                                validate=True,end_date="2014-04-13",metric="all", 
                                                aggregated_by="day",category="WebD:CampId:3100")
        print self.sg.send(self.advanced_st)

    def test_set_data_type_advanced_statistics(self):
        self.advanced_st = sendgrid.AdvancedStatistics(data_type="global", start_date="2014-04-14", validate=True) 
        self.advanced_st.set_data_type("browsers")
        self.assertEqual(self.advanced_st.data_type,"browsers")
        print self.sg.send(self.advanced_st)

    def test_set_start_date_advanced_statistics(self):
        self.advanced_st = sendgrid.AdvancedStatistics(data_type="global",start_date="2014-04-14", validate=True) 
        self.assertRaises(ValueError, self.advanced_st.set_start_date,"browsers")
        self.advanced_st.set_start_date("2014-02-14")
        self.assertEqual(self.advanced_st.start_date,"2014-02-14")
        print self.sg.send(self.advanced_st)

    def test_set_end_date_advanced_statistics(self):
        self.advanced_st = sendgrid.AdvancedStatistics(data_type="global",start_date="2014-04-14", validate=True) 
        self.assertRaises(ValueError, self.advanced_st.set_end_date,"browsers")
        self.advanced_st.set_end_date("2014-04-14")
        self.assertEqual(self.advanced_st.end_date,"2014-04-14")
        print self.sg.send(self.advanced_st)
  
    def test_set_metric_advanced_statistics(self):
        self.advanced_st = sendgrid.AdvancedStatistics(data_type="global",start_date="2014-04-14", validate=True) 
        self.advanced_st.set_metric("bounce")
        self.assertEqual(self.advanced_st.metric,"bounce")
        self.advanced_st.set_metric("all")
        self.assertEqual(self.advanced_st.metric,"all")
        self.assertRaises(ValueError,self.advanced_st.set_metric,"al")
        print self.sg.send(self.advanced_st)
    
    def test_set_category_advanced_statistics(self):
        self.advanced_st = sendgrid.AdvancedStatistics(data_type="global",start_date="2014-04-14", validate=True) 
        self.advanced_st.set_category("WebD:CampId:3150")
        self.assertEqual(self.advanced_st.category,"WebD:CampId:3150")
        self.advanced_st.set_category("WebD:CampId:3100")
        self.assertEqual(self.advanced_st.category,"WebD:CampId:3100")
        print self.sg.send(self.advanced_st)
    
    def test_set_aggregated_by_advanced_statistics(self):
        self.advanced_st = sendgrid.AdvancedStatistics(data_type="global",start_date="2014-04-14", validate=True) 
        self.advanced_st.set_aggregated_by("day")
        self.assertEqual(self.advanced_st.aggregated_by,"day")
        print self.sg.send(self.advanced_st)
    
    def test_set_country_advanced_statistics(self):
        self.advanced_st = sendgrid.AdvancedStatistics(data_type="global",start_date="2014-04-14", validate=True) 
        self.advanced_st.set_country("US")
        self.assertEqual(self.advanced_st.country,"US")
        print self.sg.send(self.advanced_st)
    
    def test_input_values_test__advanced_statistics(self):
        self.advanced_st = sendgrid.AdvancedStatistics(data_type="global",start_date="2014-04-13",validate=True,end_date="2014-04-17",
                                            metric="all",category="WebD:CampId:3100")
        print self.sg.send(self.advanced_st)

    def test_input_values_advanced_statistics(self):
        self.advanced_st = sendgrid.AdvancedStatistics(data_type="global",
                                            start_date="2014-04-13",validate=True,end_date="2014-04-17",
                                            metric="all",category="WebD:CampId:3100",aggregated_by="day",country="US")
        print self.sg.send(self.advanced_st)

    def test_input_aggregated_by_week_values_advanced_statistics(self):
        self.advanced_st = sendgrid.AdvancedStatistics(data_type="global",
                                            start_date="2014-02",validate=True,end_date="2014-04",
                                            metric="all",category="WebD:CampId:3100",aggregated_by="week",country="US")
        print self.sg.send(self.advanced_st)

    def test_input_aggregated_by_mnth_values_advanced_statistics(self):
        self.advanced_st = sendgrid.AdvancedStatistics(data_type="global",start_date="2014-02",end_date="2014-04",
                                            metric="all",category="WebD:CampId:3100",aggregated_by="month")
        print self.sg.send(self.advanced_st)

if __name__ == "__main__":
    unittest.main()
