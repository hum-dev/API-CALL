import requests

def finestFoodOutlet(city, votes):
    # Initialize variables to store the best outlet information
    best_outlet = None
    best_rating = -1
    best_votes = -1

    # Initialize pagination variables
    page = 0
    total_pages = float('inf')  # Initialize with positive infinity

    while page <= total_pages:
        # Create the URL with the current page number
        url = f"https://jsonmock.hackerrank.com/api/food_outlets?city={city}&page={page}"
        
        # Make an HTTP GET request to the API
        response = requests.get(url)
        data = response.json()

        # Update the total pages from the API response
        total_pages = data["total_pages"]

        # Process each outlet on the current page
        for outlet in data["data"]:
            # Check if the outlet has enough votes and a higher rating
            if outlet["user_rating"]["votes"] >= votes and outlet["user_rating"]["average_rating"] > best_rating:
                best_outlet = outlet["name"]
                best_rating = outlet["user_rating"]["average_rating"]
                best_votes = outlet["user_rating"]["votes"]

        # Move to the next page
        page += 1

    # Return the name of the finest food outlet
    return best_outlet

# Example usage:
city_name = "Miami"  # Replace with the desired city name
min_votes = 1000  # Replace with the minimum vote count
result = finestFoodOutlet(city_name, min_votes)
print("Finest Food Outlet:", result)
