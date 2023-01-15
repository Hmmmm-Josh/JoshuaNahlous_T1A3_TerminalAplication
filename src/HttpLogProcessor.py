import heapq
import collections
import re

LOG_LINE_REGEX = r'^(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*\[(?P<timestamp>.*)\]\s"(?P<verb>[A-Z]+)\s(?P<path>[\w\/]+)\s+(?P<protocol>[\w\/\.]+)"\s(?P<status_code>\d+)\s(?P<response_size>\d+).*'

class HttpLogProcessor:
  def __init__(self, file_path: str):
    pattern = re.compile(LOG_LINE_REGEX)
    self.logs: list[dict[str, str]] = []
    with open(file_path) as file:
      for line in file:
        match = pattern.match(line)
        if match:
          self.logs.append(match.groupdict())

  def get_total_lines(self) -> int:
    """
    Count the number of lines in a file.
    """
    return len(self.logs)

  def get_total_traffic(self) -> int:
    """
    Sum the traffic in bytes for all requests in a file.
    """
    total_traffic: int = 0
    for line in self.logs:
      total_traffic += int(line["response_size"])
    return total_traffic