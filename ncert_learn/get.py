import requests
import phonenumbers
from phonenumbers import geocoder, carrier

def get_ip_details(ip_address):
    """
    Fetch details about an IP address using an IP geolocation service.

    Args:
        ip_address (str): The IP address to query.

    Returns:
        dict: A dictionary containing details about the IP address, or an error message.
    """
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to fetch details: {response.status_code}"}
    except requests.RequestException as e:
        return {"error": f"Network error: {str(e)}"}

def get_phone_number_details(phone_number):
    """
    Fetch details about a phone number, including country and carrier.

    Args:
        phone_number (str): The phone number (with country code) to analyze.

    Returns:
        dict: A dictionary with details about the phone number.
    """
    try:
        parsed_number = phonenumbers.parse(phone_number)
        country = geocoder.description_for_number(parsed_number, "en")
        carrier_name = carrier.name_for_number(parsed_number, "en")
        is_valid = phonenumbers.is_valid_number(parsed_number)

        return {
            "country": country,
            "carrier": carrier_name,
            "is_valid": is_valid
        }
    except phonenumbers.NumberParseException as e:
        return {"error": f"Invalid phone number: {str(e)}"}

# Example Usage

