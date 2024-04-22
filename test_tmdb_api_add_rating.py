import requests

# Test Case #1: Valid Authorization Credential for Access Token Auth
def test_can_create_rating_using_valid_access_token():
    url = "https://api.themoviedb.org/3/movie/155/rating"
    payload = "{\"value\":8.5}"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json;charset=utf-8",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNzZlYTI2YjFjYjdmNmVkZjU4NTdmZjFjZDZmMjJkYSIsInN1YiI6IjY2MWFmNzUxOTY3Y2M3MDE2NTlmMTRmMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ihj9mfgT5uGYfAvO_a-xDKBPqLy-ludiRH3NyCMrRQ0"
    }
    response = requests.post(url, data=payload, headers=headers)
    assert response.status_code == 201
    print(response.status_code)


# Test Case #2: Invalid Authorization Credential for Access Token Auth
def test_cannot_create_rating_using_invalid_access_token():
    url = "https://api.themoviedb.org/3/movie/155/rating"
    payload = "{\"value\":8.5}"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json;charset=utf-8",
        "Authorization": "Bearer xx"
    }
    response = requests.post(url, data=payload, headers=headers)
    assert response.status_code == 401
    print(response.status_code)


# Test Case #3: No Movie ID 
def test_cannot_create_rating_with_no_movie_id():
    url = "https://api.themoviedb.org/3/movie/movie_id/rating"
    payload = "{\"value\":8.5}"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json;charset=utf-8",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNzZlYTI2YjFjYjdmNmVkZjU4NTdmZjFjZDZmMjJkYSIsInN1YiI6IjY2MWFmNzUxOTY3Y2M3MDE2NTlmMTRmMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ihj9mfgT5uGYfAvO_a-xDKBPqLy-ludiRH3NyCMrRQ0"
    }
    response = requests.post(url, data=payload, headers=headers)
    assert response.status_code == 404
    print(response.status_code)


# Test Case #4: No Value in Body
def test_cannot_create_rating_with_no_value_body():
    url = "https://api.themoviedb.org/3/movie/155/rating"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json;charset=utf-8",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNzZlYTI2YjFjYjdmNmVkZjU4NTdmZjFjZDZmMjJkYSIsInN1YiI6IjY2MWFmNzUxOTY3Y2M3MDE2NTlmMTRmMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ihj9mfgT5uGYfAvO_a-xDKBPqLy-ludiRH3NyCMrRQ0"
    }
    response = requests.post(url, headers=headers)
    assert response.status_code == 400
    print(response.status_code)


# Test Case #5: Empty Value
def test_cannot_create_rating_with_empty_value():
    url = "https://api.themoviedb.org/3/movie/155/rating"
    payload = "\"{\\\"value\\\":}\""
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json;charset=utf-8",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNzZlYTI2YjFjYjdmNmVkZjU4NTdmZjFjZDZmMjJkYSIsInN1YiI6IjY2MWFmNzUxOTY3Y2M3MDE2NTlmMTRmMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ihj9mfgT5uGYfAvO_a-xDKBPqLy-ludiRH3NyCMrRQ0"
    }
    response = requests.post(url, data=payload, headers=headers)
    assert response.status_code == 400
    print(response.status_code)


# Test Case #6: Zero Rating
def test_cannot_create_rating_with_zero_rating():
    url = "https://api.themoviedb.org/3/movie/155/rating"
    payload = "{\"value\":0}"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json;charset=utf-8",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNzZlYTI2YjFjYjdmNmVkZjU4NTdmZjFjZDZmMjJkYSIsInN1YiI6IjY2MWFmNzUxOTY3Y2M3MDE2NTlmMTRmMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ihj9mfgT5uGYfAvO_a-xDKBPqLy-ludiRH3NyCMrRQ0"
    }
    response = requests.post(url, data=payload, headers=headers)
    assert response.status_code == 400
    print(response.status_code)

# Test Case #7: .1 Rating
def test_cannot_create_rating_with_tenth_decimal_rating():
    url = "https://api.themoviedb.org/3/movie/155/rating"

    payload = "{\"value\":0.1}"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json;charset=utf-8",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNzZlYTI2YjFjYjdmNmVkZjU4NTdmZjFjZDZmMjJkYSIsInN1YiI6IjY2MWFmNzUxOTY3Y2M3MDE2NTlmMTRmMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ihj9mfgT5uGYfAvO_a-xDKBPqLy-ludiRH3NyCMrRQ0"
    }
    response = requests.post(url, data=payload, headers=headers)
    assert response.status_code == 400
    print(response.status_code)


# Test Case #8: Update Rating to .5
def test_can_create_rating_with_five_tenths_decimal():
    url = "https://api.themoviedb.org/3/movie/155/rating"
    payload = "{\"value\":0.5}"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json;charset=utf-8",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNzZlYTI2YjFjYjdmNmVkZjU4NTdmZjFjZDZmMjJkYSIsInN1YiI6IjY2MWFmNzUxOTY3Y2M3MDE2NTlmMTRmMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ihj9mfgT5uGYfAvO_a-xDKBPqLy-ludiRH3NyCMrRQ0"
    }
    response = requests.post(url, data=payload, headers=headers)
    assert response.status_code == 201
    print(response.status_code)


# Test Case #9: Set Higher Value than 10.0
def test_cannot_create_rating_with_higher_value_than_10():
    url = "https://api.themoviedb.org/3/movie/155/rating"
    payload = "{\"value\":10.5}"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json;charset=utf-8",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNzZlYTI2YjFjYjdmNmVkZjU4NTdmZjFjZDZmMjJkYSIsInN1YiI6IjY2MWFmNzUxOTY3Y2M3MDE2NTlmMTRmMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ihj9mfgT5uGYfAvO_a-xDKBPqLy-ludiRH3NyCMrRQ0"
    }
    response = requests.post(url, data=payload, headers=headers)
    assert response.status_code == 400
    print(response.status_code)