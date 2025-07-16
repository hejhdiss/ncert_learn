
import requests
from bs4 import BeautifulSoup
from googlesearch import search

def get_google_answer(query):

    """
    Perform a Google search and get the top 1 result. The function tries to get
    the text content of the webpage and return the first 1000 characters of it.

    Args:
        query (str): The search query

    Returns:
        str or False: The first 1000 characters of the webpage content if the
        search is successful, otherwise False.
    """

    try:
        # Perform a Google search and get the top 1 result
        results = search(query, num_results=1)
        if results:
            url = results[0]

            # Send a request to the URL
            response = requests.get(url)
            response.raise_for_status()  # Check for HTTP errors

            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract text from the webpage (assuming it's in <body> tag)
            body_text = soup.get_text(separator=' ', strip=True)

            # Print the first 1000 characters of the page text
            return body_text[:1000] # Print first 1000 characters of the page text
        else:
            return False
    except Exception as e:
        return False


def is_connected():

    """
    Check if the system is connected to the internet by sending a request to Google's website.

    Returns:
        bool: True if the internet is connected, otherwise False.
    """

    try:
        # Try to get a response from a reliable website (Google's DNS server)
        response = requests.get('http://www.google.com', timeout=5)
        # If the status code is 200, the internet is connected
        if response.status_code == 200:
            return True
    except requests.RequestException:
        # If an error occurs (like no internet connection), return False
        return False
def getgoogleanswer(query):

    """
    Perform a Google search and return the content of the top result if
    connected to the internet.

    Args:
        query (str): The search query.

    Returns:
        str or False: The first 1000 characters of the webpage content if the
        search is successful and connected to the internet, otherwise False.
    """

    if is_connected():
        return get_google_answer(query)
    else:
        return False



