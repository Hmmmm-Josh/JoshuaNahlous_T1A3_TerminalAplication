# JoshuaNahlous_T1A3_TerminalApplication
 T1A3 - Terminal Application IP log reader

#### Link to Source Control Repository
* https://github.com/Hmmmm-Josh/JoshuaNahlous_T1A3_TerminalApplication

#### Link to Slide Deck Video
* 
#### Provide full attribution to referenced sources (where applicable).
Mockaroo was used to create a fake IP data logs https://www.mockaroo.com/

### Features within the application
* Count the number of unique IP addresses.
* * `--unique_clients` allows the user to find the most unique IP adresses within the logs.

* Calculate the top 3 most active IP addresses.
* * `--most_active_clients` allows the user to find the most active IP adresses within the logs how active they are.


* Calculate the top 3 most visited URLs.
* * `--most_visited_paths` allows the user to find the most acitve file paths any user has gone to and shows how many people have gone to it.




## How to Run: Main Program
* Make sure the latest Python is insatlled
* Run `python main.py ./src/programming-task-example-data.log`and add the desired function on the end `[-h] [--lines LINES] [--status_codes STATUS_CODES] [--traffic TRAFFIC] [--unique_clients UNIQUE_CLIENTS] [--most_active_clients MOST_ACTIVE_CLIENTS] [--most_visited_paths  MOST_VISITED_PATHS]`
* Follow the input prompts...
* arguments displayed to run in code are... `[-h] [--lines LINES] [--status_codes STATUS_CODES] [--traffic TRAFFIC] [--unique_clients UNIQUE_CLIENTS] [--most_active_clients MOST_ACTIVE_CLIENTS] [--most_visited_paths  MOST_VISITED_PATHS]` insert these into code for a desired outcome


## How to Run: Test Program
* Make sure Pytest is installed
* Run `pytest test_HttpLogProcessor.py`
  This will Run several Tests within the Program

## CLI Usage
```
usage: main.py [-h] [--lines] [--status_codes] [--traffic] [--unique_clients] [--most_active_clients] [--most_visited_paths] file
```

## Dependecies
* Python3
* A working computer
### System/Hardware requirements 
* Intel Core i5 processor or equivalent
* 4 GB RAM (8 GB preferred)
* 1 GB available hard disk space
* Internet connection

## How to use any command line arguments made for the application
* Type `Help`
* Type out options in console



## Decisions & Explanations

### HTTP Log Format

Here's an example of a basic HTTP log file that can be used with the parser:

```
192.168.1.1 - - [01/Jan/2021:15:00:00 -0500] "GET /index.html HTTP/1.1" 200 2048
192.168.1.2 - - [01/Jan/2021:15:05:00 -0500] "POST /submit.html HTTP/1.1" 404 256
192.168.1.3 - - [01/Jan/2021:15:10:00 -0500] "GET /images/logo.png HTTP/1.1" 200 4096
192.168.1.4 - - [01/Jan/2021:15:15:00 -0500] "GET /about.html HTTP/1.1" 200 2048
```

Each line in the file represents a single HTTP request made to a server. The fields in the file typically include:

- the IP address of the client making the request
- the date and time of the request
- the request method (GET, POST, etc.)
- the requested resource
- the HTTP version
- the HTTP status code returned by the server
- the size of the response in bytes

### `HttpLogParser` Class

The `HttpLogParser` class is a utility class that is used to parse and process HTTP log files. The class is initialized with the file path of the log file, and it reads the file and converts it into a list of dictionaries where each dictionary represents a single log entry.

The class has several methods to extract useful information from the log file, such as:

- `get_total_lines()`: Returns the number of lines in the log file.
- `get_total_traffic()`: Returns the total traffic in bytes for all requests in the log file.
- `get_status_code_count()`: Returns a dictionary that contains the count of each status code in the log file.
- `get_total_unique_ip_addresses()`: Returns the total number of unique IP addresses in the log file.
- `get_most_active_ip_addresses()`: Returns the top 3 most active IP addresses in the log file.
- `get_most_active_paths()`: Returns the top 3 most visited URLs in the log file.

Additionally, there is a `most_frequent()` method that is used to calculate the most frequent elements in a list, based on the count of each element in the list. This method is used by `get_most_active_ip_addresses()` and `get_most_active_paths()`.

The class uses some external libraries like `re`, `collections` and `heapq`. The class uses `re.compile(LOG_LINE_REGEX)` to compile a regular expression `LOG_LINE_REGEX` to match the log entries and extract the relevant information, `collections` to keep a count of unique ip addresses and `heapq` to find the most frequent elements.

### Top K Frequent Elements Function

The function `most_frequent` takes two arguments as input, a list of strings `items` and an integer `k`, and returns a list of strings as output.

It first initializes an empty list called `res` to store the most frequent strings.

It then creates a Counter object, `dict`, from the input list of strings, which keeps track of the number of occurrences of each string in the list.

It then iterates through the Counter object and for each string, `val`, and its count, `count`, in the Counter object, if the length of the current result list `res` is less than `k`, it pushes a tuple `(count, val)` representing the count and the string value into the `res` list using the `heappush()` function. If the length of the `res` list is equal or greater than `k`, it pushes the tuple into the list and then pops the smallest tuple out of the list using `heappushpop()`.

This results in the `res` list containing `k` tuples with the most frequent `val` and its corresponding count in descending order.

Finally it returns a list containing only the most frequent `val` by iterating through the `res` list and extracting the second element of each tuple, which is the `val`.
---