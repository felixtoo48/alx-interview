#!/usr/bin/env python3
""" log parsing algorithm """
import sys
import re


"""Define the regular expression pattern to match the desired log format"""
ip_pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
log_date_pattern = r'\[([^\]]+)] "GET /projects/\d+ HTTP/1\.1" (\d+) (\d+)'
log_pattern = ip_pattern + r' - ' + log_date_pattern

"""Initializing variables to keep track of statistics"""
file_sizes = []
status_code_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

try:
    line_count = 0
    total_file_size = 0

    for line in sys.stdin:
        """ removing leading and trailing whitespace from line"""
        line = line.rstrip()

        """matching line to the desired input format"""
        match = re.match(log_pattern, line)

        if match:
            """ Extract ip, date, status code, file size"""
            ip_address, date, status_code, file_size = match.groups()

            total_file_size += int(file_size)

            file_sizes.append(int(file_size))

            if int(status_code) in status_code_counts:
                status_code_counts[int(status_code)] += 1

            line_count += 1

            # Print statistics after every 10 lines"""
            if line_count % 10 == 0:
                print(f'File size: {total_file_size}')
                for code, count in sorted(status_code_counts.items()):
                    if count > 0:
                        print(f'{code}: {count}')

except KeyboardInterrupt:
    print("")

# Print the final statistics after processing all lines"""
print(f'File size: {total_file_size}')
for code, count in sorted(status_code_counts.items()):
    if count > 0:
        print(f'{code}: {count}')
