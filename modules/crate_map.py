# from pprint import pprint
from random import uniform
import requests
import folium
from geopy.exc import GeocoderUnavailable
from geopy.geocoders import Nominatim


def crate_list_of_points(name: str, bearer_token: str) -> dict:
    """
    Function create dict of points using request by Twitter API anf geopy
    It crate dict of points with coordinates of locations of given user friends
    """
    geolocator = Nominatim(user_agent="super_puper_extra_important_request")

    base_url = 'https://api.twitter.com/'
    search_url = f'{base_url}1.1/friends/list.json'
    search_headers = {
        'Authorization':f'Bearer {bearer_token}'
    }
    search_params = {
        'screen_name':'@'+name,
        'count':50
    }
    response = requests.get(search_url, headers=search_headers,
                            params=search_params)
    json_response = response.json()

    points = {}
    for user in json_response['users']:
        name = user['screen_name']
        location = user['location']
        try:
            pos = geolocator.geocode(location)
        except GeocoderUnavailable:
            break
        if pos is not None:
            pos = (pos.latitude, pos.longitude)
            try:
                _ = points[pos]
                pos = (uniform(pos[0] - 0.033, pos[0] + 0.033),
                       uniform(pos[1] - 0.033, pos[1] + 0.033))
            except KeyError:
                pass
            points[pos] = name
    return points


def create_map(name: str, points:dict):
    """
    function create web map in html format in which are marked points
    """
    map0 = folium.Map(zoom_start=7)
    tooltip = "flex!"

    point_layer = folium.FeatureGroup(name=f"Friends Search of {name}")
    for pos in points:
        point_layer.add_child(folium.Marker(location=pos,
                                            popup=points[pos],
                                            icon=folium.Icon(icon='cloud'),
                                            tooltip=tooltip))

    map0.add_child(point_layer)
    map0.save('./templates/map.html')


if __name__ == '__main__':
    NAME = 'ElonMusk'
    create_map(NAME, crate_list_of_points(NAME, 'AAAAAAAAAAAAAAAAAAAAAF0GNAEAAAAA4ArRfJj2OS7jd1%2FVFHVK8B0I%2F70%3D9LYseQE9nIGWq6GFnCZVzcwzuI6ObmSWxPSWZbjwqLzFvz0zDJ'))
