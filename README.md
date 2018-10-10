# Trains

## Design

### General

* Following PEP8
* Reserved comments to explain non-obvious code
* This was my second time (ever) working with a graph other than a basic khanacademy course on algorithms 2 week ago

### Assumptions
* Bad data will not be passed to graph object. Minimal exception handling has been added

### Graph object

* Encapsulating logic into Graph class to make reusable for future graph related problems
* Using an adjacency list for internal graph representation
* Chose to retain vertex labels and use those as keys for simplicity, hence use of dicts instead of arrays. Would be more space efficient to switch to using arrays keyed with ids
* Able to support both weighed and non weighted graphs
* Graph could be further abstracted away with a railroad object, but chose not to
* Using DFS-like approach for `get_num_paths`, adapted from [here](https://stackoverflow.com/questions/8885647/find-all-paths-with-cycles-in-directed-graph-given-the-source-vertex)
* Using Dijkstra's algorithm for `get_min_distance`. Algo didn't handle cycles so brute forced a condition for that case. There is likely a more elegant solution
	
## Setup

Requires Git and Docker

### Build

	git clone https://github.com/redgoose/trains.git
	cd trains
	docker build -t trains .

### Run

	docker run trains

Above command will start a container and run the tests or you can run them manually using the following command

	docker run -it trains sh
	python test.py

## Usage

```	
graph = Graph()
graph.add_edge(Edge('A', 'B', 5))
graph.add_edge(Edge('B', 'C', 4))

# get distance for a path
graph.get_distance_for_path(['A', 'B', 'C'])

# get number of paths with exact number of vertices
graph.get_num_paths(start='A', end='B', restriction={'num_vertices': 2})

# get number of paths with max vertices
graph.get_num_paths(start='A', end='B', restriction={'max_vertices': 2})

# get number of paths with max distance
graph.get_num_paths(start='A', end='B', restriction={'max_distance': 10})

# get shortest distance
graph.get_min_distance(start='A', end='C')
```	
