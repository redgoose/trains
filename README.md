
## Design

### General

* Following PEP8
* Reserved comments to explain non-obvious code

### Graph object

* Encapsulating logic into Graph class to make reusable for future graph related problems
* Using an adjacency list for internal graph representation
* Chose to retain vertex labels and use those as keys for simplicity, hence use of dicts instead of arrays. Would be more space efficient to switch to using arrays keyed with ids.

# assumptions:
# no bad data to railroad
