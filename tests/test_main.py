import pytest
from main import build_location_map, build_router_map, compute_location_router_links

def test_build_location_map():
    locations = [{"id": 1, "name": "A"}, {"id": 2, "name": "B"}]
    m = build_location_map(locations)
    assert m == {1: "A", 2: "B"}

def test_build_router_map():
    # main.py expects "location_id"
    routers = [{"id": 10, "location_id": 1}, {"id": 11, "location_id": 2}]
    m = build_router_map(routers)
    assert m == {10: 1, 11: 2}

def test_compute_location_router_links():
    # main.py expects "location_id" and "router_links"
    locations = {1: "A", 2: "B", 3: "C"}
    routers = [
        {"id": 10, "location_id": 1, "router_links": [11, 12]},
        {"id": 11, "location_id": 2, "router_links": [10]},
        {"id": 12, "location_id": 3, "router_links": [10]},
    ]
    router_map = {10: 1, 11: 2, 12: 3}
    links = compute_location_router_links(routers, locations, router_map)
    expected = [frozenset(("A", "B")), frozenset(("A", "C"))]
    assert all(frozenset(pair) in expected for pair in links)
