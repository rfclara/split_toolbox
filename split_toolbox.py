import sys
import os
from collections import defaultdict

if len(sys.argv) < 2:
    print("Usage: python split_toolbox.py <input_file>")
    sys.exit(1)

input_file = sys.argv[1]
segments = {}
current_id = None

with open(input_file, "r", encoding="latin1") as infile:
    header = infile.readline()  # Take the first line as header
    for line in infile:
        if line.startswith("\\id"):
            parts = line.strip().split()
            if len(parts) > 1:
                current_id = parts[1]
            else:
                print(f"Malformed \\id line: {line.strip()}")
                current_id = None
                continue
        if current_id:
            if current_id not in segments:
                segments[current_id] = []
            segments[current_id].append(line)

#write all segments for each id to one file, with header from original file
for id_name, lines in segments.items():
    filename = f"{id_name}.txt"
    with open(filename, "w", encoding="utf-8") as outfile:
        outfile.write(header)
        outfile.writelines(lines)