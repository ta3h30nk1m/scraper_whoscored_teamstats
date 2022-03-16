"""
https://github.com/joseramon-arias/scraper-whoscored
@author: joseramon
functions that used often for scraping
I didn't use all of these functions but think might be useful for others.  
"""

from unidecode import unidecode
from urllib.parse import unquote

def save_to_file(dataset, file_path):
    """
    Function to save a list of urls into a txt file
    """
    with open(file_path, 'w') as f:
        for item in dataset:
            processed = process_info(item)
            f.write(processed+'\n')
        
def populate_countries_dict(file_path):
    """
    Function to populate dictionary of countries and url numbers.
    """
    
    countries_dict = {}
    
    with open(file_path, 'r') as f:
        for line in f.readlines():
            key_value = line[:-1].split(':')
            countries_dict[key_value[0]] = int(key_value[1])
        
    return countries_dict

def read_from_file(file_path):
    """
    Read a file and return a list with all the lines in the file
    """
    
    file_in_list = []
    
    with open(file_path, 'r') as f:
        for line in f.readlines():
            file_in_list.append(line)
            
    return file_in_list

def append_to_tsv(player, file_path):
    """
    Function to append new data into a tsv file
    """
    with open(file_path, 'a') as f:
        f.write('\t'.join(player)+'\n')
            
def append_to_csv(player, file_path):
    """
    Function to append new data into a tsv file
    """
    with open(file_path, 'a') as f:
        f.write(','.join(player)+'\n')
        
def append_to_file(line, file_path):
    """
    Function to append new data into file
    """
    with open(file_path, 'a') as f:
        f.write(line+'\n')

def process_info(info):
    try:
        processed = unquote(info)
    except:
        processed = info
        pass
    if isinstance(processed, unidecode):
        processed = unidecode(processed)
        
    return processed

