import json
import csv
import logging
import sys
import os
from urllib.request import urlopen
from urllib.parse import quote
from urllib.error import HTTPError

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)
API_ENDPOINT = 'https://maps.googleapis.com/maps/api/geocode/json?key={key}&address={address}'

try:
    path = sys.argv[1] if len(sys.argv) > 1 else input('Enter the path of the csv file: ')
    key = os.getenv('GOOGLE_MAPS_GEOCODING_API_KEY') or input('Enter the Google Maps Geocoding API KEY: ')

    with open(path, newline='') as input_file:
        reader = csv.reader(input_file)

        with open('output_{name}'.format(name=os.path.basename(input_file.name)), 'w', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(["Address", "Latitude", "Longitude"])
            count = 0

            for row in reader:
                if len(row):
                    response = urlopen(API_ENDPOINT.format(key=key, address=quote('+'.join(row))))
                    encoding = response.info().get_content_charset('utf-8')
                    data = json.loads(response.read().decode(encoding))

                    if data.get('results'):
                        result = data['results'].pop(0)
                        writer.writerow([''.join(row), format(result['geometry']['location']['lat'], '.7f'),
                                         format(result['geometry']['location']['lng'], '.7f')])
                        count += 1
                    elif 'error_message' in data:
                        logging.error('Google Maps Geocoding - {message}'.format(message=data['error_message']))
                        exit(1)
                    else:
                        writer.writerow([''.join(row), 'No results', 'No results'])
                else:
                    writer.writerow(['', 'No results', 'No results'])

            logging.info('{count} addresses geocoded successfully.'.format(count=count))

except FileNotFoundError:
    logging.error('CSV file not found.')
    exit(1)
except HTTPError as error:
    encoding = error.info().get_content_charset('utf-8')
    error_message = json.loads(error.read().decode(encoding))['error_message']
    logging.error('Google Maps Geocoding [{code}: {reason}] - {message}'.format(code=error.code, reason=error.reason,
                                                                                message=error_message))
    exit(1)
