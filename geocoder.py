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

    with open(path, newline='', encoding='utf-8') as input_file:
        reader = csv.reader(input_file)
        rows = list(reader)
        row_count = len(rows)
        with open(f"output_{os.path.basename(input_file.name)}", 'w', newline='', encoding='utf-8') \
                as output_file:
            writer = csv.writer(output_file)
            writer.writerow(["Address", "Latitude", "Longitude", "Formatted Address"])
            geocoded = 0

            for i, row in enumerate(rows):
                if len(row):
                    logging.info(f"{i+1}/{row_count}: {','.join(row)}")

                    url = API_ENDPOINT.format(key=key, address=quote('+'.join(row)))
                    logging.info(url)

                    response = urlopen(url)
                    data = json.loads(response.read())

                    if data.get('results'):
                        result = data['results'].pop(0)
                        writer.writerow([','.join(row),
                                         format(result['geometry']['location']['lat'], '.7f'),
                                         format(result['geometry']['location']['lng'], '.7f'),
                                         result['formatted_address']])
                        geocoded += 1
                    elif 'error_message' in data:
                        logging.error(f"Google Maps Geocoding - {data['error_message']}")
                        exit(1)
                    else:
                        writer.writerow([','.join(row), 'No results', 'No results', 'No results'])
                else:
                    writer.writerow(['', 'No results', 'No results', 'No results'])

            logging.info(f"{geocoded} addresses geocoded successfully.")

except FileNotFoundError:
    logging.error('CSV file not found.')
    exit(1)
except HTTPError as error:
    error_message = json.loads(error.read())['error_message']
    logging.error(f"Google Maps Geocoding [{error.code}: {error.reason}] - {error_message}")
    exit(1)
