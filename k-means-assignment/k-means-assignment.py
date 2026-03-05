def euclidian(a,b):
    dist = 0
    for i in range(len(a)):
        dist += (a[i] - b[i]) ** 2
    dist ** 0.5
    return dist

def k_means_assignment(points, centroids):
    """
    Assign each point to the nearest centroid.
    """
    # Write code here
    assign = list(range(len(points)))
    for i in range(len(points)):
        assign[i] = 0
        current = 1e9
        for j in range(len(centroids)):
            if euclidian(points[i] , centroids[j]) < current:
                current = euclidian(points[i] , centroids[j])
                assign[i] = j
    return assign