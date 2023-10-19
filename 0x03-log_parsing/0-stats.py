#!/usr/bin/env python3
""" log parsing algorithm """
import sys
import re


"""Define the regular expression pattern to match the desired log format"""
log_pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[([^\]]+)] "GET /projects/\d+ HTTP/1\.1" (\d+) (\d+)$'

for line in sys.stdin:
    """ removing leading and trailing whitespace from line"""
    line == line.rstrip()

    """matching line to the desired input format"""
    match = re.match(log_pattern, line)

    if match:
        """ Extract ip, date, status code, file size"""
        ip_address, date, status_code, file_size = match.groups()
        try:
            for line in range(10):
                print(f'IP Address: {ip_address}, Date: {date}, Status Code: {status_code}, File Size: {file_size}')
        
        except KeyboardInterrupt:
            break

    else:
        print("skipped:", line)
