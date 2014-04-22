# SendGrid-Python #
This library allows you to quickly and easily use SendGrid API using Python.


## Example

```python
import sendgrid

sg = sendgrid.SendGridClient('YOUR_SENDGRID_USERNAME','YOUR_SENDGRID_PASSWORD',endpoint="/api/stats.get.json")


## example for General Statistics

general_st = sendgrid.GeneralStatistics()
general_st.set_days(2)
general_st.set_start_date("2014-04-14")
general_st.set_end_date("2014-04-20")
general_st.set_aggregate(0)
general_st.set_category("WebD:CampId:3100")
status, msg = sg.send(general_st)


#or
general_st = sendgrid.GeneralStatistics(days=2,start_date="2014-04-14",end_date="2014-04-20",
                                aggregate=0,category="WebD:CampId:3100")

status, msg = sg.send(general_st)

## example for Advanced Statistics

#Note: Mandatory Parameters : data_type and start_date
#By default data_type will be global and start_date will be set as current date

advanced_st = sendgrid.AdvancedStatistics()
    

advanced_st.set_data_type("browsers")
advanced_st.set_start_date("2014-02-14")
advanced_st.set_end_date("2014-04-14")
advanced_st.set_metric("bounce")
advanced_st.set_category("WebD:CampId:3150")
advanced_st.set_aggregated_by("day")
advanced_st.set_country("US")
status,msg = sg.send(advanced_st)

#or
advanced_st = sendgrid.AdvancedStatistics(data_type="global",start_date="2014-04-13",validate=True,end_date="2014-04-17",
                                           metric="all",category="WebD:CampId:3100",aggregated_by="day",country="US")
status,msg = sg.send(advanced_st)

```
##Validation 
By default set method will not validate the parameters
however you can pass validate=True to GeneralStatistics or AdvancedStatistics
constructor to validate the parameters before sending

For Example:
```python
        general_st = sendgrid.GeneralStatistics(days=2,start_date="2014-04-14",end_date="2014-04-20",
                                            aggregate=0,category="WebD:CampId:3100",validate=True)
        status, msg = sg.send(general_st)
        

        advanced_st = sendgrid.AdvancedStatistics(data_type="global",start_date="2014-04-13",validate=True,end_date="2014-04-17",
                                            metric="all",category="WebD:CampId:3100")
        status,msg = sg.send(advanced_st)
```




### Error handling

By default, `.send` method returns a tuple `(http_status_code, message)`,
however you can pass `raise_errors=True` to `SendGridClient` constructor,
then `.send` method will raise `SendGridClientError` for 4xx errors,
and `SendGridServerError` for 5xx errors.

```python
from sendgrid import SendGridError, SendGridClientError, SendGridServerError

sg = sendgrid.SendGridClient(username, password, raise_errors=True)

try:
    sg.send(message)
except SendGridClientError:
    ...
except SendGridServerError:
    ...
```

This behavior is going to be default from version 1.0.0. You are
encouraged to set `raise_errors` to `True` for forwards compatibility.

`SendGridError` is a base-class for all SendGrid-related exceptions.

###### Methods for General Statistics

```python
general_st = sendgrid.GeneralStatistics()
```
### Setting the days
```python
general_st.set_days(2)
```

### Setting the start_date
```python
general_st.set_start_date("2014-04-14")
```

### Setting the end_date
```python
general_st.set_end_date("2014-04-20")
```

### Setting the Aggregate
```python
general_st.set_aggregate(0)
```

### Setting the Category 
```python
general_st.set_category("WebD:CampId:3100")
```


### Add Categories
```python
general_st.add_category("WebD:CampId:3150")
```



###### Methods for Advanced Statistics

```python
advanced_st = sendgrid.AdvancedStatistics(data_type="global", start_date="2014-04-14")
```

### Setting the data_type
```python
advanced_st.set_data_type("browsers")
```

### Setting Start date
```python
advanced_st.set_start_date("2014-02-14")
```

### Setting end date
```python
advanced_st.set_end_date("2014-04-14")
```

### Setting Metric
```python
advanced_st.set_metric("bounce")
```

### Setting Aggregated By
```python
advanced_st.set_aggregated_by("day")
```

### Setting Category
    Category Can be a String or a list of categories
```python
advanced_st.set_category("WebD:CampId:3150")
advanced_st.set_category(["WebD:CampId:3150"])
```

### Setting Country
```python
advanced_st.set_country("US")
```


### Add Category
```python
advanced_st.add_category(["WebD:CampId:3150"])
advanced_st.add_category("WebD:CampId:3150")
```





### TODO:

* Add support for other APIs 

### Tests

```bash
python test/__init__.py
```

## MIT License
