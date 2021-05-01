import requests
from datetime import datetime

# Import API_KEY
import sys
sys.path.insert(0, '/home/adarifian/learn_api/credentials/')
from credentials import CALENDARIFIC_API_KEY

errorcodes = {
    401: 'Unauthorized Missing or incorrect API token in header.',
    422: 'Un-processable Entity meaning something with the message isn’t quite right, this could be malformed JSON or incorrect fields. In this case, the response body contains JSON with an API error code and message containing details on what went wrong.',
    500: "Internal Server Error This is an issue with Calendarific's servers processing your request. In most cases the message is lost during the process, and we are notified so that we can investigate the issue.",
    503: 'Service Unavailable During planned service outages, Calendarific API services will return this HTTP response and associated JSON body.',
    429: 'Too many requests. API limits reached.',
    600: 'Maintenance The Calendarific API is offline for maintenance.',
    601: 'Unauthorized Missing or incorrect API token.',
    602: 'Invalid query parameters.',
    603: 'Authorized Subscription level required.'
}

baseurl = 'https://calendarific.com/api/v2/holidays'


def holidayCheck(fulldate: str, country_code: str) -> str:
    """Check if the given date (str) is a holiday in the given country_code (str).
    The data is available for both historical and future dates until 2049.

    Args:
        date (str): string of a date with 'YYYY-MM-DD' format and before 2049
        country_code (str): 2 digit code of the country

    Returns:
        str: A sentence that explain the name of the holiday or if is not a holiday 
    """
    if len(country_code) != 2:
        return 'Please input the correct country code'

    try:
        date = datetime.strptime(fulldate, '%Y-%m-%d')
    except ValueError as error:
        return 'Error inputted date: '+ str(error.args[0]).replace('%Y-%m-%d','YYYY-MM-DD')

    year = date.year
    if int(year) > 2049:
        return 'Data is not available for dates after year 2049.'
    month = date.month
    day = date.day

    country_code = country_code.upper()
    query_params = {'api_key': CALENDARIFIC_API_KEY,
                    'country': country_code, 'year': year, 'month': month, 'day': day}
    response = requests.get(baseurl, params=query_params)
    response_json = response.json()
    response_code = response_json['meta']['code']
    if response_code != 200:
        try:
            return errorcodes[response_code]
        except KeyError:
            return f'Service Unavailable. Please try again later'

    try:
        holiday_name = response_json['response']['holidays'][0]['name']
        holiday_description = response_json['response']['holidays'][0]['description']
        holiday_type = response_json['response']['holidays'][0]['type'][0]

        return f'{fulldate} in {country_code} is a {holiday_type}: {holiday_name}. {holiday_description}'
    except IndexError:
        return f'{fulldate} is not a holiday in {country_code}'


if __name__ == '__main__':
    while True:
        print('Holiday Checker\n'
              'Use this app to check if a date in your country is a holiday or not\n'
              'We support both historical and future dates until 2049\n'
              'This app utilized calendarific.com services\n'
              'Input the date and country code below or press Ctrl+C to exit the app'
              '\n')
        date = input("Please input the date in 'YYYY-MM-DD' format: ")
        country = input("Please input the 2 digit code of the country: ")
        print(holidayCheck(date, country))
        print('\n'+'----'*10)