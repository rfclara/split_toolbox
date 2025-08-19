# Toolbox Segment Splitter

This script generates individual Toolbox `.txt` files for each document ID found in a source file.

## What does it do?

- The script reads a Toolbox-formatted `.txt` file containing multiple segments.
- Each segment starts with a line beginning with `\id`, followed by a document ID and a segment number (e.g., `\id about_Kris_1a 050`).
- The script extracts the document ID (the word after `\id` and before the space).
- It collects all segments belonging to the same document ID.
- For each unique document ID, it creates a new `.txt` file named after the ID (e.g., `about_Kris_1a.txt`).
- Each output file starts with the header line: `\_sh v3.0  400  Yali_Text_id`
- All segments for that document ID are written to the corresponding file.

## Usage

### Python (Linux/Mac/Windows)

1. Make sure you have Python 3 installed.
2. Run the script from the command line:
   ```
   python3 split_toolbox.py <input_file>
   ```
   Replace `<input_file>` with the name of your Toolbox `.txt` file.

### Windows Batch File

1. Edit `split_toolbox.bat` and replace `your_long_file.txt` with your actual file name.
2. Double-click `split_toolbox.bat` to run the script, or run from Command Prompt:
   ```
   split_toolbox.bat
   ```

## Example

If your input file contains:
```
\id about_Kris_1a 050
...
\id about_Kris_1a 051
...
\id burning_garden 001
...
```
The script will create:
- `about_Kris_1a.txt` (containing all segments for `about_Kris_1a`)
- `burning_garden.txt` (containing all segments for `burning_garden`)

## Note

Malformed `\id` lines (missing a document ID) are reported and skipped.