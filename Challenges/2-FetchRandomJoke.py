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
