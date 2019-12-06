
import bs4
import re
import json
import os
from pathlib import Path

def parse_xmls(path):
    file_names = [f for f in os.listdir(path) if f.endswith(".xml")]
    files_soup = {}
    for fname in file_names:
        files_soup[fname] = bs4.BeautifulSoup(open(path / fname), "lxml")

    return files_soup
