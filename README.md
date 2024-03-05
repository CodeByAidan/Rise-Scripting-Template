# Welcome to Rise Scripting!

---

- [Welcome to Rise Scripting!](#welcome-to-rise-scripting)
  - [Introduction](#introduction)
  - [See this online!](#see-this-online)
  - [Setup](#setup)
    - [1. Main Requirements for Scripting:](#1-main-requirements-for-scripting)
      - [1. Download Visual Studio Code:](#1-download-visual-studio-code)
      - [2. Install Python Extension:](#2-install-python-extension)
      - [3. Open Folder in Visual Studio Code:](#3-open-folder-in-visual-studio-code)
      - [4. Preview the `README.md` file:](#4-preview-the-readmemd-file)
    - [2. Installing Required Libraries:](#2-installing-required-libraries)
      - [Windows:](#windows)
      - [Linux/MacOS:](#linuxmacos)
  - [Usage](#usage)
    - [Tips](#tips)
      - [1. Use Type Annotations for Starting Out:](#1-use-type-annotations-for-starting-out)
      - [2. Python Version + Current Libraries](#2-python-version--current-libraries)
      - [3. Debugging!](#3-debugging)
  - [Scripting Levels](#scripting-levels)
    - [1. Get Weather Data](#1-get-weather-data)
      - [Hints:](#hints)
    - [2. Fetch Random Joke](#2-fetch-random-joke)
    - [3. Calculator](#3-calculator)
    - [4. Palindrome](#4-palindrome)
    - [5. FizzBuzz](#5-fizzbuzz)
  - [Libraries in Rise](#libraries-in-rise)
  - [Links](#links)
    - [Rise Discord - Scripting Issues Channel](#rise-discord---scripting-issues-channel)
    - [Rise Discord - Public Support Channel](#rise-discord---public-support-channel)
    - [Rise Scripting Explained](#rise-scripting-explained)
    - [Discord.py Documentation](#discordpy-documentation)

---

## Introduction

Hi! My name is [bruhs](https://discord.com/users/300291395883892737) or [CodeByAidan](https://github.com/CodeByAidan)
on [Github](https://github.com/) and I am a bit of an experienced member with programming, and
with Rise Scripting. I have been using Rise for a while now, and so I thought I wanted to help
out the community by creating a template for starting out your own scripts. This template is
designed to help you get started with your own scripts, and to help you understand how to use
the Rise/Discord.py API, and with Python in general!

## See this online!

**If you want to read this online, you can visit [here](https://gist.github.com/CodeByAidan/143c648978e7c460fa10ce640392630e)!**

---

## Setup

To get started with this template, you will need to have the following installed:

- [Python 3.8+](https://www.python.org/downloads/)

Then place this folder `template` in `Rise`'s folder!

> [!WARNING]
> Please do not place this in the `Scripts` folder, as it generate problems on loadup with Rise!

### 1. Main Requirements for Scripting:

To set up your environment for scripting, follow these steps:

#### 1. Download Visual Studio Code:

Use [Visual Studio Code](https://code.visualstudio.com/) as your IDE. It's user-friendly and
offers many features to help with scripting.

#### 2. Install Python Extension:

Make sure to have the [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
installed in Visual Studio Code.

#### 3. Open Folder in Visual Studio Code:

Open the folder containing your script in Visual Studio Code.

#### 4. Preview the `README.md` file:

Once the folder is open, navigate to the `README.md` file. Right-click on the file and select
`Open Preview` to view the rendered markdown. Alternatively, you can use the `Ctrl+Shift+V`
keyboard shortcut.

> [!TIP]
> Use the `Ctrl+K V` keyboard shortcut to open the preview panel to the side of the file for
> easier viewing.

> [!TIP]
> I recommend using the Github Markdown Preview, to see tips like this!
> Extension here: https://marketplace.visualstudio.com/items?itemName=bierner.github-markdown-preview

### 2. Installing Required Libraries:

Once you have Python installed, you can then create a virtual environment to store all your
libraries locally! To do this, open a terminal (Windows/Linux: `` Ctrl+Shift+` ``, MacOS:
`` Cmd+Shift+` ``) and type the following command:

```bash
python -m venv .venv
```

This will create a virtual environment in the `.venv` folder. To activate the virtual
environment, type the following command:

#### Windows:

```bash
.venv\Scripts\activate
```

#### Linux/MacOS:

```bash
source .venv/bin/activate
```

Once you have activated the virtual environment, you can then install the required libraries
by typing the following command:

```bash
pip install -r requirements.txt
```

---

## Usage

To start off with Python, you will need to understand the basics of Python. You can learn more
about Python by visiting the [Python Documentation](https://docs.python.org/3/).

Once you have a good understanding of Python, you can then start learning about the [Discord.py API](https://discordpy.readthedocs.io/en/stable/).
This will help you understand how to use the API to interact with Discord.

Once you have a good understanding of Python and the Discord.py API, you can then start
creating your own scripts. You can use this template to help you get started with your own
scripts.

### Tips

Some tips for scripting with Rise:

#### 1. Use Type Annotations for Starting Out:

I recommend when creating a script to use this kinda template:

```python
import asyncio
import discord
from discord.ext import commands
from tkinter import END, Text as textbox

Rise: commands.Bot = commands.Bot(
    command_prefix="?", self_bot=True, intents=discord.Intents.all()
)


# Run using the command: ?file_name
@Rise.command()
async def file_name(ctx: commands.Context[commands.Bot]) -> None:
```

Where `file_name` is substituted with the name of the file you are creating. The reason
being, is that with type annotations, it helps you understand what the function is doing, and
what it is returning. This is useful for when you are creating a script, and you want to
understand what the function is doing. It also allows [Intellisense](https://code.visualstudio.com/docs/editor/intellisense)
(autocomplete) to work properly, so you can autocomplete `ctx.`
and see what you can do with the `ctx` object, and also `Rise.` to see what you can do with
the `Rise` object.

**Now when you want to try the command please change the code to this:**

```python
# import asyncio
# import discord
# from discord.ext import commands
# from tkinter import END, Text as textbox

# Rise: commands.Bot = commands.Bot(
#     command_prefix="?", self_bot=True, intents=discord.Intents.all()
# )


# Run using the command: ?file_name
@Rise.command()
async def file_name(ctx) -> None:
```

That way you can actually use the file, since type annotations are not supported in Rise, and
also `END` is imported from `tkinter` which is not supported in Rise. Also you are NOT setting
up a new bot.

#### 2. Python Version + Current Libraries

**As of Windows 11 version of Rise...**

- Python Version: 3.8.16 (default, Dec 20 2022, 23:15:53) [MSC v.1900 64 bit (AMD64)]
- As for all the libraries as of, March 4th, 2024, the libraries were exported and located in the [module_list_exported.txt](module_list_exported.txt) file.

#### 3. Debugging!

Debugging with Rise is exceptionally fun (sarcasm). The reason being, is that Rise does not
have a built-in debugger, so you cannot use the `pdb` module to debug your scripts. This is
because Rise is a selfbot, and it is not designed to be used for debugging. It is designed to
be used for creating scripts to interact with Discord.

But we do have a way to attempt to debug, simply whenever you're scripting, if the complexity
is not that long, then you can get away using this kind of format:

```py
# Run using the command: ?file_name
@Rise.command()
async def file_name(ctx) -> None:
    import contextlib

    try:
        # ---
        # insert your code here! AND imports!
        # ---
    except Exception as e:
        error_message: str = f"Error: {type(e).__name__} - {str(e)}"
        with contextlib.suppress(Exception):
            textbox.insert(END, "\n\n" + error_message)
        print(error_message)
        await ctx.send(error_message)
```

Or using a function:

```py
import contextlib

# Run using the command: ?file_name
@Rise.command()
async def file_name(ctx) -> None:
    async def error_handler(ctx, e: Exception) -> None:
        """
        Error Handler for the script

        Args:
            ctx (commands.Context): The context of the command.
            e (Exception): The exception that was raised.

        Returns:
            None
        """
        error_message: str = f"Error: {type(e).__name__} - {str(e)}"
        with contextlib.suppress(Exception):
            textbox.insert(END, "\n\n" + error_message)
        print(error_message)

    try:
        # ---
        # insert your code here! AND imports!
        # ---
    except Exception as e:
        await error_handler(ctx, e)
```

---

## Scripting Levels

Solutions will NOT be provided for these, as they are meant to be a challenge for you to solve!

However, if you need help, you can always ask in the [Rise Discord - Scripting Issues Channel](https://discord.com/channels/1001461222396411966/1001461766204686507)!

**(If you can solve all of these, send me a screenshot of them working, and I'll pay for a
month of Nitro for you!)**

> [!NOTE]
> If you forgot who I am, I am [bruhs](https://discord.com/users/300291395883892737)! Send me
> a message if you have completed all of these!

### 1. Get Weather Data

#### Hints:

- Use the [OpenWeatherMap API](https://openweathermap.org/api) to get the weather data.
- Use the `requests` library to make a request to the API. [Requests Documentation](https://docs.python-requests.org/en/master/)
- Use the `json` library to parse the JSON response from the API. [JSON Documentation](https://docs.python.org/3/library/json.html) (**most likely don't need**)

```py
import requests


def get_weather(city: str) -> str:
    """
    Challenge 1 - Get Weather Data

    This function retrieves weather data for a given city using the OpenWeatherMap API.

    Args:
        city (str): The name of the city for which to retrieve weather data.

    Returns:
        str: A string containing the weather information for the given city.
    """
    API_KEY = "your_api_key_here"  # Replace with your OpenWeatherMap API key - https://home.openweathermap.org/api_keys
    # API URL for weather data
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    # Send request to the API
    response = requests.get(url, timeout=5)

    # Parse response and extract weather information
    if response.status_code == 200:
        data = response.json()
        weather_info = ...
        # Extract relevant weather data (e.g., temperature, description)
        # Return weather information
        return "Weather information for " + city + ":\n" + weather_info
    else:
        return "Error: Unable to retrieve weather data"


# Test the function
city_name = "New York"
weather = get_weather(city=city_name)
print(weather)
```

You will first complete this script located in [Challenges/1-GetWeatherData.py](Challenges/1-GetWeatherData.py)!

To complete this, you will need to replace the `...` with the relevant weather data (e.g.,
temperature, description) and then test the function by running the script via
`python Challenges/1-GetWeatherData.py`, make sure you are also in the virtual environment -
[#2. Installing Required Libraries](#2-installing-required-libraries) - while running
`1-GetWeatherData.py`!

Once you are done, you can then substitute the `get_weather()` function in the
`GetWeatherData.py` file located in the `Scripts` folder. Then drag that folder into the
`Rise/Scripts` folder, and then run the command `?get_weather` to see if it works!

### 2. Fetch Random Joke

```py
import requests

def fetch_joke() -> str:
    """
    Challenge 2 - Fetch Random Joke

    This function retrieves a random joke using the Official Joke API.

    Returns:
        str: A string containing the random joke.
    """
    # API URL for random joke
    url = "https://official-joke-api.appspot.com/jokes/random"

    # Send request to the API
    response = requests.get(url, timeout=5)

    # Parse response and extract joke
    if response.status_code == 200:
        data = response.json()
        # Extract joke from response
        # Return the joke
    else:
        return "Error: Unable to retrieve joke"

# Test the function
print(fetch_joke())
```

This challenge is located in [Challenges/2-FetchRandomJoke.py](Challenges/2-FetchRandomJoke.py)!
You will first complete this script, and then test the function by running the script via
`python Challenges/2-FetchRandomJoke.py`, make sure you are also in the virtual environment -
[#2. Installing Required Libraries](#2-installing-required-libraries) - while running
`2-FetchRandomJoke.py`!

This one is a bit easier than the first one, but it is still a challenge! Once you are done,
you can then substitute the `fetch_joke()` function in the `FetchRandomJoke.py` file located in
the `Scripts` folder. Then drag that script `FetchRandomJoke.py` into the `Rise/Scripts`
folder, and then run the command `?FetchRandomJoke` to see if it works!

### 3. Calculator

```py
def simple_calculator(operation: str, num1: float, num2: float) -> float:
    """
    Challenge 3 - Simple Calculator

    Perform a simple calculation on two numbers

    Args:
        operation (str): The operation to perform
        num1 (float): The first number
        num2 (float): The second number

    Returns:
        float: The result of the operation
    """
    # Perform the specified operation on the given numbers
    # Support addition, subtraction, multiplication, and division
    # Return the result
    pass

# Test the function
result = simple_calculator("add", 5, 3)
print(result)
```

This challenge is located in [Challenges/3-Calculator.py](Challenges/3-Calculator.py)!
You will first complete this script, and then test the function by running the script via
`python Challenges/3-Calculator.py`, make sure you are also in the virtual environment -
[#2. Installing Required Libraries](#2-installing-required-libraries) - while running
`3-Calculator.py`!

### 4. Palindrome

```py
def is_palindrome(word: str) -> bool:
    """
    Challenge 4 - Palindrome

    Check if the given word is a palindrome

    Args:
        word (str): The word to check

    Returns:
        bool: True if the word is a palindrome, False otherwise
    """
    # Check if the given word is a palindrome
    # Return True if it is, False otherwise
    pass

# Test the function
result = is_palindrome("radar")
print(result)
```

This challenge is located in [Challenges/4-Palindrome.py](Challenges/4-Palindrome.py)!

You will first complete this script, and then test the function by running the script via
`python Challenges/4-Palindrome.py`, make sure you are also in the virtual environment -
[#2. Installing Required Libraries](#2-installing-required-libraries) - while running
`4-Palindrome.py`!

### 5. FizzBuzz

```py
def fizzbuzz(n: int) -> str:
    """
    Challenge 5 - FizzBuzz

    This function implements the FizzBuzz algorithm.

    Args:
        n (int): The number for which to apply the FizzBuzz algorithm.

    Returns:
        str: The result of the FizzBuzz algorithm for the given number.
    """
    # Return "Fizz" for multiples of 3
    # Return "Buzz" for multiples of 5
    # Return "FizzBuzz" for multiples of both 3 and 5
    # Return the number itself for all other cases
    pass

# Test the function
print(fizzbuzz(15))
```

This challenge is located in [Challenges/5-FizzBuzz.py](Challenges/5-FizzBuzz.py)!

You will first complete this script, and then test the function by running the script via
`python Challenges/5-FizzBuzz.py`, make sure you are also in the virtual environment -
[#2. Installing Required Libraries](#2-installing-required-libraries) - while running
`5-FizzBuzz.py`!

---

## Libraries in Rise

Remember as of March 4th, 2024, the libraries were exported and located in the [module_list_exported.txt](module_list_exported.txt) file, and the Python version is 3.8.16!

**Utility Libraries**

- [chardet](https://pypi.org/project/chardet/) - Character Encoding Detection
- [colorama](https://pypi.org/project/colorama/) - Terminal Colors
- [filetype](https://pypi.org/project/filetype/) - File Type Detection
- [six](https://pypi.org/project/six/) - Python 2 and 3 Compatibility
- [typing](https://docs.python.org/3/library/typing.html) - Type Hinting Support

**Web Development**

- [bs4](https://pypi.org/project/beautifulsoup4/) - Beautiful Soup
- [html5lib](https://pypi.org/project/html5lib/) - HTML Parser
- [soupsieve](https://pypi.org/project/soupsieve/) - CSS Selectors for BeautifulSoup
- [websocket](https://pypi.org/project/websocket-client/) - WebSocket Client
- [aiohttp](https://docs.aiohttp.org/en/stable/) - Asynchronous HTTP Client/Server
- [anyio](https://anyio.readthedocs.io/en/stable/) - Asynchronous I/O Library

**Data Processing**

- [numpy](https://numpy.org/) - Numerical Computing
- [dateutil](https://pypi.org/project/python-dateutil/) - Date Utilities
- [PIL](https://pillow.readthedocs.io/en/stable/) - Python Imaging Library
- [multidict](https://pypi.org/project/multidict/) - Multidimensional Dictionary

**Networking**

- [aiodns](https://pypi.org/project/aiodns/) - Asynchronous DNS Resolver
- [asyncio](https://docs.python.org/3/library/asyncio.html) - Asynchronous I/O Library
- [yarl](https://pypi.org/project/yarl/) - Yet Another URL Library
- [requests](https://requests.readthedocs.io/en/master/) - HTTP Library
- [requests_toolbelt](https://pypi.org/project/requests-toolbelt/) - Additional Utilities for Requests
- [urllib3](https://pypi.org/project/urllib3/) - HTTP Library with Connection Pooling
- [sniffio](https://pypi.org/project/sniffio/) - Asynchronous Networking Library

**Cryptography and Security**

- [bcrypt](https://pypi.org/project/bcrypt/) - Password Hashing
- [cryptography](https://cryptography.io/en/latest/) - Cryptography Library
- [OpenSSL](https://pypi.org/project/pyOpenSSL/) - OpenSSL Wrapper
- [nacl](https://pypi.org/project/PyNaCl/) - Networking and Cryptography Library

**Integration**

- [discord](https://pypi.org/project/discord.py/) - Discord API Wrapper
- [lxml](https://pypi.org/project/lxml/) - XML/HTML Processing

---

## Links

For more information, please visit the following links:

### [Rise Discord - Scripting Issues Channel](https://discord.com/channels/1001461222396411966/1001461766204686507)

### [Rise Discord - Public Support Channel](https://discord.com/channels/1001461222396411966/1001461793773858867)

### [Rise Scripting Explained](https://forums.riseselfbot.xyz/d/79-rise-scripting-explained)

### [Discord.py Documentation](https://discordpy.readthedocs.io/en/stable/)
