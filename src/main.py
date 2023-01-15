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
    
  def run(self):
    args = self.parser.parse_args()
    
    if not args.file and (args.lines or args.status_codes or args.traffic or args.unique_clients or args.most_active_clients or args.most_visited_paths):
      raise Exception('Please provide an argument!')

    parser = HttpLogProcessor(args.file)
    
    if args.lines:
      print(f'Number of lines in {args.file}: {parser.get_total_lines()}')
    
    if args.traffic:
      print(f'Total traffic in bytes in {args.file}: {parser.get_total_traffic()}')
    
    if args.status_codes:
      print(f'Number of status codes in {args.file}: {parser.get_status_code_count()}')

    if args.unique_clients:
     
      print(f'Number of unique clients in {args.file}: {parser.get_total_unique_ip_addresses()}')
      
    if args.most_active_clients:
      print(f'Number of most active clients in {args.file}: {parser.get_most_active_ip_addresses()}')
      
    if args.most_visited_paths:
      print(f'Most  in {args.file}: {parser.get_most_active_paths()}')

if __name__ == "__main__":
  main = Main()
  main.run()