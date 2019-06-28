
def find_route(route, segments):
    current_location = route[len(route) -1]
    for segment in segments:
        if current_location == segment[0]:
            route_copy = route.copy()
            segments_copy = segments.copy()

            route_copy.append(segment[1])
            segments_copy.remove(segment)
            
            # Era l'ultimo segmento da appicicare?
            if len(segments) == 1:
                return route_copy
            else: 
                return find_route(route_copy, segments_copy)
            

    return None




DATASETS = [
    {
        "origin": 'YUL',
        "segments": [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')],
        "route": ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']
    },
    {
        "origin": 'COM',
        "segments": [('SFO', 'COM'), ('COM', 'YYZ')],
        "route": None
    },
    {
        "origin": 'A',
        "segments": [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')],
        "route": ['A', 'C', 'A', 'B', 'C']
    }
]

for data in DATASETS:
    route = find_route([data["origin"]], data["segments"])
    assert route == data["route"]
