#!/usr/bin/env python3

import sys
from collections import defaultdict

_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}

def print_msg(total, _count):
    print(f"Total file size: {total}")
    for status in sorted(_count.keys()):
        print(f"{status}: {_count[status]}")

def main():
    total = 0
    _count = defaultdict(int)
    
    try:
        line_count = 0
        for line in sys.stdin:
            line_count += 1
            line = line.strip()
            parts = line.split()
            if len(parts) != 10:
                continue
            
            ip_address, _, _, _, _, _code, file_size = parts
            if _code not in _codes:
                continue
            
            try:
                file_size = int(file_size)
            except ValueError:
                continue
            
            total += file_size
            _count[_code] += 1

            if line_count % 10 == 0:
                print_msg(total, _count)

    except KeyboardInterrupt:
        print_msg(total, _count)
        sys.exit(0)

if __name__ == "__main__":
    main()
