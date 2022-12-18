from typing import Any, Union

import requests


def get_app_data(app_id):
    """
    Retrieve all data points that exist on the app data page for the app with the
    given 'app_id'.
    """

    try:
        response = requests.get(f'https://itunes.apple.com/lookup?id={app_id}')
        app_data = response.json()['results'][0]
    except Exception:
        app_data = {}

    return app_data


def get_top_free_apps(country: str, limit_number: int) -> dict[str, Any]:
    """
    Retrieve a list of the top 'num_apps' free Apple apps.
    """

    try:
        response = requests.get(f'https://itunes.apple.com/{country}/rss/topfreeapplications/limit={limit_number}/json')
        apps = response.json()['feed']['entry']
    except Exception:
        apps = {}

    return apps


def categorize_app(app_data: dict) -> str:
    """
    Categorize the given app data as a TV app, Music app, Game or other.
    """

    categories = app_data.get('primaryGenreName', '')
    options = {'tv': 'TV app',
               'music': 'Music app',
               'games': 'Game'}

    for category, tag in options.items():
        if category == categories.lower():
            return tag

    return f'Other({categories})'


def is_kids_friendly(app_data: dict) -> bool:
    """
    Determine if the given app is kids friendly.
    """

    if app_data.get('contentAdvisoryRating') == '4+':
        return True

    return False


def customize_app_data(country: str, limit: int) -> Union[str, dict]:
    apps_result = {}
    top_free_apps = get_top_free_apps(country, limit)

    try:
        for top_free_app in top_free_apps:
            app = {}
            app_id = top_free_app['id']['attributes']['im:id']
            app_data = get_app_data(app_id)
            name = app_data['trackName']
            app['id'] = app_id
            app['category'] = categorize_app(app_data)
            app['kids_friendly'] = is_kids_friendly(app_data)
            app['rating'] = app_data['averageUserRating']
            apps_result[name] = app
    except Exception:
        return "Sorry, application can't generate top free apple apps. Please try again"

    return apps_result
