import csv
from urllib.parse import urlparse
import os

def main():

    TEST = False
    MOCK_CSV_FILENAME = 'mock_csv_data.csv'
    OUTPUT_FILENAME = 'output.txt'

    csv_filenames = []
    BASE = 'http://127.0.0.1:8000/api/import/'
    prefixes = []

    

    USER_CSV_FILENAME = 'users.csv'
    USER_PREFIX = 'user/'

    POSTING_CSV_FILENAME = 'postings.csv'
    POSTING_PREFIX = 'posting/'

    RIDE_POSTING_CSV_FILENAME = 'ridePosting.csv'
    RIDE_POSTING_PREFIX = 'ride/'

    ITEM_POSTING_CSV_FILENAME = 'itemPosting.csv'
    ITEM_POSTING_PREFIX = 'itemposting/'

    COMMENT_CSV_FILENAME = 'comments.csv'
    COMMENT_PREFIX = 'comment/'

    csv_filenames.append(USER_CSV_FILENAME)
    prefixes.append(USER_PREFIX)

    csv_filenames.append(POSTING_CSV_FILENAME)
    prefixes.append(POSTING_PREFIX)

    csv_filenames.append(RIDE_POSTING_CSV_FILENAME)
    prefixes.append(RIDE_POSTING_PREFIX)

    csv_filenames.append(ITEM_POSTING_CSV_FILENAME)
    prefixes.append(ITEM_POSTING_PREFIX)

    #csv_filenames.append(COMMENT_CSV_FILENAME)
    #prefixes.append(COMMENT_PREFIX)

    generate_output_file(OUTPUT_FILENAME)

    if not TEST:
        for i in range(len(csv_filenames)):
            urls = generate_urls(csv_filenames[i], BASE, prefixes[i])
            append_to_output_file(OUTPUT_FILENAME, urls)
    else:
        urls = generate_urls(MOCK_CSV_FILENAME, BASE, USER_PREFIX)
        append_to_output_file(OUTPUT_FILENAME, urls)
    

def generate_urls(CSV_FILE, BASE, PREFIX):
    urls = []

    with open(CSV_FILE, newline='') as csvfile:
        reader = csv.reader(csvfile, dialect='excel')
        for row in reader:
            for item in row:
                    if item == "STUDENTS":
                        item = "STUDENT"
            pre_formatted_url = BASE + PREFIX + '/'.join(row)
            url = urlparse(pre_formatted_url).geturl()
            urls.append(url)
    
    return urls

def generate_output_file(OUTPUT_FILENAME):
    output_file = open(OUTPUT_FILENAME, 'w')

def append_to_output_file(OUTPUT_FILENAME, url_array):
    output_file = open(OUTPUT_FILENAME, 'a')
    for url in url_array:
        output_file.write(url + '\n')
    output_file.close()

main()

