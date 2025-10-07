import requests

def main():
    # The URL for the Swagger JSON (OpenAPI Spec) from the Petstore example
    swagger_url = "http://petstore.swagger.io/v2/swagger.json"

    print(f"Fetching Swagger data from: {swagger_url}")

    try:
        # Fetch the JSON data from the specified URL
        resp = requests.get(swagger_url)

        # Raise an exception for bad status codes (4xx or 5xx)
        resp.raise_for_status()

        # Parse the JSON content
        swagger = resp.json()

    except requests.exceptions.RequestException as e:
        # Handle connection errors, timeouts, or bad HTTP status codes
        print(f"Error fetching Swagger JSON: {e}")
        # Exit the function if fetching failed
        return

    # Extract and print the paths (endpoints)
    paths = swagger.get('paths', {})

    print("\n--- Endpoints (Paths) ---")
    for path in paths:
        print(path)
    print("-------------------------")

if __name__ == "__main__":
    # Call the main function, which now uses the hardcoded URL
    main()