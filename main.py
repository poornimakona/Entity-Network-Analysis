
import json
from itertools import combinations
from collections import defaultdict
import networkx as nx

# Read the JSON file
with open("Entity_Network.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Extract reports
reports = {}

for hit in data["hits"]["hits"]:
    source = hit["_source"]
    reports[source["id"]] = source["entities"]

# Standardize entity names
def clean(name):
    name = " ".join(name.split())

    if name.casefold() in ["ravi kumar", "ravi k."]:
        return "Ravi Kumar"

    return name.title()

# Exclude locations from the people network
places = {"Pathankot", "Jammu", "Udhampur"}

# Create weighted edges
edges = defaultdict(int)

for report_id, entities in reports.items():
    people = sorted({
        clean(name)
        for name in entities
        if name.strip().title() not in places
    })

    for person1, person2 in combinations(people, 2):
        edges[(person1, person2)] += 1

# Build graph
G = nx.Graph()

for (person1, person2), weight in edges.items():
    G.add_edge(person1, person2, weight=weight)

# Display edges
print("\n--- WEIGHTED EDGES ---")
for (person1, person2), weight in sorted(edges.items()):
    print(f"{person1} -- {person2}: {weight}")

# Display adjacency list
print("\n--- ADJACENCY LIST ---")
for person in sorted(G.nodes()):
    neighbours = {
        neighbour: G[person][neighbour]["weight"]
        for neighbour in sorted(G.neighbors(person))
    }
    print(person, ":", neighbours)

# Find the most connected people
print("\n--- MOST CONNECTED PEOPLE ---")
if G.number_of_nodes() > 0:
    degrees = dict(G.degree())
    max_degree = max(degrees.values())

    for person, degree in sorted(degrees.items()):
        if degree == max_degree:
            print(person, ":", degree, "connections")

# Find the shortest path
print("\n--- SHORTEST PATH ---")
try:
    path = nx.shortest_path(G, "Arjun Singh", "Imran")
    print(" -> ".join(path))
    print("Number of edges:", len(path) - 1)
except (nx.NetworkXNoPath, nx.NodeNotFound):
    print("No path found between Arjun Singh and Imran.")
