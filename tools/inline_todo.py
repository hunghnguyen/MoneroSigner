#!/usr/bin/env python3

import os
import re
from datetime import datetime

# Define the directory where your source files are located
source_directory = 'src'

# Define the output file name
output_file = 'INLINE_TODO.md'

# Define the regex pattern to match TODO comments
todo_pattern = re.compile(r'# TODO:(?P<tag>\w+:)?\s*(?P<content>.*?)\s*(?P<date>\d{4}-\d{2}-\d{2})?$')

# Initialize lists to store the collected data
todos = []

# Traverse the source directory and collect TODO comments
for root, dirs, files in os.walk(source_directory):
    for file in files:
        if file.endswith('.py'):  # Assuming your source files have a .py extension
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                for line_number, line in enumerate(f, start=1):
                    match = todo_pattern.search(line)
                    if match:
                        tag = match.group('tag').strip(':') if match.group('tag') else ''
                        content = line.strip()
                        date = match.group('date') if match.group('date') else '9999-12-31'  # Default to a far future date if no date is provided
                        todos.append({'file': file_path, 'line': line_number, 'tag': tag, 'content': content, 'date': date})

# Sort the todos by urgency (date) and then by file name
todos.sort(key=lambda x: (x['date'], x['file']))

# Generate the output file
with open(output_file, 'w') as f:
    # Write the index
    f.write('# Index\n')
    f.write('- [Urgent](#urgent)\n')
    f.write('- [By File](#by-file)\n')

    # Write the urgent list
    f.write('\n# Urgent\n')
    current_date = ''
    for todo in todos:
        if todo['date'] != current_date:
            current_date = todo['date']
            f.write(f"\n## {current_date}\n")
        f.write(f"- [{todo['file']}](file://{todo['file']}):{todo['line']}\n")
        f.write(f"  {todo['content']}\n")

    # Write the list sorted by file name
    f.write('\n# By File\n')
    current_file = ''
    for todo in sorted(todos, key=lambda x: x['file']):
        if todo['file'] != current_file:
            current_file = todo['file']
            f.write(f"\n## [{todo['file']}](file://{todo['file']})\n")
        f.write(f"- Line {todo['line']}: {todo['date']} {todo['tag']}\n")
        f.write(f"  {todo['content']}\n")
