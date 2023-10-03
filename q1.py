import requests

def finestFoodOutlet(city, votes):
    # Initialize variables to store the best outlet information
    best_outlet = None
    best_rating = -1
    best_votes = -1

    # Initialize pagination variables
    page = 1  # Start with page 1
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
            current_rating = outlet["user_rating"]["average_rating"]
            current_votes = outlet["user_rating"]["votes"]

            # Check if the outlet has enough votes
            if current_votes >= votes:
                # Check for a higher rating or tiebreaker condition
                if current_rating > best_rating or (current_rating == best_rating and current_votes > best_votes):
                    best_outlet = outlet["name"]
                    best_rating = current_rating
                    best_votes = current_votes

        # Move to the next page
        page += 1

    # Return the name of the finest food outlet
    return best_outlet
