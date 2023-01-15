import argparse
from HttpLogProcessor import HttpLogProcessor

class Main:

  def __init__(self):
    self.parser = argparse.ArgumentParser(description='Process some HTTP log files.')
    self.parser.add_argument(dest='file', type=str, help="The file to read")
    
    self.parser.add_argument('--lines', help='count the number of lines in the file')
    self.parser.add_argument('--status_codes', help='count the number of status codes in the file')
    self.parser.add_argument('--traffic', help='sum the traffic in bytes for all requests in the file')
    self.parser.add_argument('--unique_clients', help='Count the number of unique IP adresses in the file')
    self.parser.add_argument('--most_active_clients', help='Calculate the top 3 most active IP addresses in the file')
    self.parser.add_argument('--most_visited_paths', help='Calculate the top 3 most visited URLs in file')