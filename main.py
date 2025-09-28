import requests

API_URL = "https://my-json-server.typicode.com/marcuzh/router_location_test_api/db"


def fetch_data(api_url: str = API_URL):
    """
    Fetch JSON data from the API.
    Returns: dict with keys 'routers' and 'locations'
    """
    response = requests.get(api_url, timeout=10)
    response.raise_for_status()
    return response.json()


def build_location_map(locations):
    """
    Build a dict mapping location id to location name.
    """
    return {loc["id"]: loc["name"] for loc in locations}


def build_router_map(routers):
    """
    Build a dict mapping router id to location id.
    """
    return {router["id"]: router["location_id"] for router in routers}


def compute_location_router_links(routers, location_map, router_map):
    """
    Compute unique location-to-location router_links.
    """
    connections = set()

    for router in routers:
        router_location = location_map[router["location_id"]]
        for linked_router_id in router["router_links"]:
            linked_location = location_map[router_map[linked_router_id]]
            if router_location != linked_location:  # skip same-location router_links
                # Use frozenset to avoid duplicates (A,B) == (B,A)
                pair = frozenset([router_location, linked_location])
                connections.add(pair)

    # Convert back to tuples for easy printing
    return [tuple(pair) for pair in connections]


def main():
    data = fetch_data()
    locations = data["locations"]
    routers = data["routers"]

    location_map = build_location_map(locations)
    router_map = build_router_map(routers)

    router_links = compute_location_router_links(routers, location_map, router_map)

    for pair in router_links:
        # Because frozenset loses order, sort alphabetically for stable output
        a, b = sorted(pair)
        print(f"{a} <-> {b}")


if __name__ == "__main__":
    main()
