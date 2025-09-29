Router Location Links — Interview Task
**Task Overview**

This repository contains a ** Python solution** for computing and managing links between routers and their locations. It includes:

Core logic implemented in main.py.

Unit tests for key functions in tests/test_main.py.

Containerized setup for reproducible execution and testing.

Key Points for the Interviewer

**Solution Approach**

Functions in main.py are modular and testable:

build_location_map()

build_router_map()

compute_location_router_links()

**Testing**

Unit tests written using pytest.

Tests cover main functionalities and edge cases.

Containerized execution ensures consistent environment.

Containerization

Dockerfile works with both Docker and Podman.

Handles module imports correctly using PYTHONPATH.

Supports running the main application (python main.py) or tests (pytest) inside the container.

Running the Task

Locally:

python main.py        # Run main logic
pytest tests/         # Run unit tests


Inside Container:

# Build the container
#docker  
docker build -t router-location-links .  
docker run -itd router-location-links  
docker exec -it "id" /bin/bash  
python main.py  
pytest


Dependencies

Python 3.11+

pytest for testing

All dependencies are listed in requirements.txt.
