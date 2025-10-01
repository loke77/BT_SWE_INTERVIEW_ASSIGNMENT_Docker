  **Router Location Links — Interview Task**  
**📌 Task Overview**  
This repository contains a Python solution for computing and managing links between routers and their locations, based on a provided JSON data source.
The solution is designed to be:  
**Modular** → each function has a single responsibility.  
**Testable** → unit tests cover main logic and edge cases.  
**Reproducible** → containerized setup ensures consistent execution.  

**🛠️ Solution Design**  
The core logic is implemented in main.py, structured into:  
**build_location_map()** → builds a dictionary of locations.  
**build_router_map()** → builds a dictionary of routers.  
**compute_location_router_links()** → computes links between locations and routers.  

**Output**
Prints the computed location-to-router mapping in the console.  

Additionally, a pictorial representation (**representation_locations_routers.jpg**) is included to visually illustrate the mapping (proactive step beyond requirements).



✅ Testing
Unit tests written in tests/test_main.py using pytest.


Covers:


Core functions (build_location_map, build_router_map, compute_location_router_links).


Edge cases (e.g., missing fields, invalid data).


Run tests:
pytest tests/


**🐳 Containerization**  
The solution includes a Dockerized setup for consistent execution:  
**# Build container**
docker build -t router-location-links .  

**# Run container in detached mode**  
docker run -itd --name router-links router-location-links  

**# Access container shell**  
docker exec -it router-links /bin/bash  

**# Run application**  
python main.py  

**# Run tests**  
pytest -s    


**🚀 Running the Task**
Locally  
**# Run main logic** 
python main.py  

**# Run unit tests**  
pytest tests/  

Dependencies
Python 3.11+


pytest for testing


Dependencies listed in requirements.txt


