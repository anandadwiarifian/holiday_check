# Holiday Checker
The script check whether a given date is a holiday or not in a given country.

To achieve that, it consumes a public API from [calendarific.com](https://calendarific.com/), a RESTful API that provides holiday data from 230 countries. 

Personal purpose of this project is to learn about API consuming. 

## Setting Up
* Python >= 3.6
* Install libraries used in this repo 
```
pip install -r requirements.txt
```
* Get an API KEY by signing up in the [calendarific.com](https://calendarific.com/), site.
* Define a constant variable API_KEY with your API key in [the script](/holidayCheck.py)
```
API_KEY = <your_API_key>
```
* Delete the lines where I imported my API_Key in [the script](/holidayCheck.py) (line 4 to 7) 
* Run the script
```
python holidayCheck.py
```

## Info about the script
### Input
The script asks two inputs from the user:
1. Date

The date we want to check whether it's a holiday or not in a given country. The script will only accept date with 'YYYY-MM-DD' format and correct date (e.g., not 2021-02-31). The script will also reject if the date is later than 2049 since [calendarific.com](https://calendarific.com/), only has data until 2049.

2. Country code

The code of the country we want to check whether it's a holiday or not on a given date. The script will only accept the country code in two digit format.

### Output
If the given date in a given country is a holiday, the script will return the type, the name, and the description of the holiday.

Else, the script will tell you that the given date is not a holiday in the given country.


