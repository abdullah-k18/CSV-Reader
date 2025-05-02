import time
import re
from IPython.display import Markdown, display

start_time = time.time()

with open('', 'r', encoding='utf-8') as f:
    lines = f.readlines()

def split_csv_line(line):
    pattern = r',(?=(?:[^"]*"[^"]*")*[^"]*$)'
    return re.split(pattern, line.strip())

headers = split_csv_line(lines[0])

markdown_table = "| " + " | ".join(headers) + " |\n"
markdown_table += "| " + " | ".join(["---"] * len(headers)) + " |\n"

for line in lines[1:6]:
    row = split_csv_line(line)
    if len(row) == len(headers):
        markdown_table += "| " + " | ".join(row) + " |\n"

end_time = time.time()
elapsed_time = end_time - start_time

display(Markdown(markdown_table))