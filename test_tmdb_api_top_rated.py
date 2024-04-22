import requests

# Test Case #1: Valid Authorization Credential for Access Token Auth 
def test_can_call_using_valid_access_token():
    url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNzZlYTI2YjFjYjdmNmVkZjU4NTdmZjFjZDZmMjJkYSIsInN1YiI6IjY2MWFmNzUxOTY3Y2M3MDE2NTlmMTRmMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ihj9mfgT5uGYfAvO_a-xDKBPqLy-ludiRH3NyCMrRQ0"
    }
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    print(response.status_code)


# Test Case #2: Invalid Authorization Credential for Access Token Auth
def test_cannot_call_using_invalid_access_token():
    url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer xx"
    }
    response = requests.get(url, headers=headers)
    assert response.status_code == 401
    print(response.status_code)


# Test Case #3: Valid Authorization Credential for API Key Auth
def test_can_call_using_valid_api_key():
    url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1&api_key=276ea26b1cb7f6edf5857ff1cd6f22da"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    print(response.status_code)


# Test Case #4: Invalid Authorization Credential for API Key Auth
def test_cannot_call_using_invalid_api_key():
    url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1&api_key=xx"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 401
    print(response.status_code)


# Test Case #5: Page Zero
def test_cannot_call_page_zero():
    url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=0"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNzZlYTI2YjFjYjdmNmVkZjU4NTdmZjFjZDZmMjJkYSIsInN1YiI6IjY2MWFmNzUxOTY3Y2M3MDE2NTlmMTRmMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ihj9mfgT5uGYfAvO_a-xDKBPqLy-ludiRH3NyCMrRQ0"
    }
    response = requests.get(url, headers=headers)
    assert response.status_code == 400
    print(response.status_code)


# Test Case #6: Page 501
def test_cannot_call_page_501():
    url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=501"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNzZlYTI2YjFjYjdmNmVkZjU4NTdmZjFjZDZmMjJkYSIsInN1YiI6IjY2MWFmNzUxOTY3Y2M3MDE2NTlmMTRmMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ihj9mfgT5uGYfAvO_a-xDKBPqLy-ludiRH3NyCMrRQ0"
    }
    response = requests.get(url, headers=headers)
    assert response.status_code == 400
    print(response.status_code)


# Test Case #7: Change Language using Valid Country Code
def test_can_call_change_language_using_valid_country_code():
    url = "https://api.themoviedb.org/3/movie/top_rated?language=ja&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNzZlYTI2YjFjYjdmNmVkZjU4NTdmZjFjZDZmMjJkYSIsInN1YiI6IjY2MWFmNzUxOTY3Y2M3MDE2NTlmMTRmMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ihj9mfgT5uGYfAvO_a-xDKBPqLy-ludiRH3NyCMrRQ0"
    }
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    print(response.status_code)


# Test Case #8: Change Language using Invalid Country Code
def test_cannot_call_change_language_using_invalid_country_code():
    url = "https://api.themoviedb.org/3/movie/top_rated?language=japanese&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNzZlYTI2YjFjYjdmNmVkZjU4NTdmZjFjZDZmMjJkYSIsInN1YiI6IjY2MWFmNzUxOTY3Y2M3MDE2NTlmMTRmMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ihj9mfgT5uGYfAvO_a-xDKBPqLy-ludiRH3NyCMrRQ0"
    }
    response = requests.get(url, headers=headers)
    assert response.status_code == 400
    print(response.status_code)


# Test Case #9: View Regional Release Dates
def test_can_call_regional_release_dates():
    url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1&region=it"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNzZlYTI2YjFjYjdmNmVkZjU4NTdmZjFjZDZmMjJkYSIsInN1YiI6IjY2MWFmNzUxOTY3Y2M3MDE2NTlmMTRmMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ihj9mfgT5uGYfAvO_a-xDKBPqLy-ludiRH3NyCMrRQ0"
    }
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    print(response.status_code)


# Test Case #10: Invalid Region Defaults to Primary Release Date
def test_can_call_defaults_to_primary_release_dates_using_invalid_region():
    url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1&region=italian"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNzZlYTI2YjFjYjdmNmVkZjU4NTdmZjFjZDZmMjJkYSIsInN1YiI6IjY2MWFmNzUxOTY3Y2M3MDE2NTlmMTRmMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ihj9mfgT5uGYfAvO_a-xDKBPqLy-ludiRH3NyCMrRQ0"
    }
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    print(response.status_code)