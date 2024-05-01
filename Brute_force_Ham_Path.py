from itertools import permutations

def is_valid_path(perm, adj, N):
    """
    Check if a given permutation of vertices represents a valid Hamiltonian path.
    """
    for i in range(N - 1):
        if adj[perm[i]][perm[i + 1]] == 0:
            return False
    return True

def hamiltonian_path_bruteforce(adj):
    """
    Checks for a Hamiltonian path in a graph using a brute force approach.
    """
    N = len(adj)  # Number of vertices
    all_perms = permutations(range(N))
    
    for perm in all_perms:
        if is_valid_path(perm, adj, N):
            return True, perm  # Return True and the path if a valid path is found
    return False, None  # Return False if no valid path is found

# Example graph represented by an adjacency matrix
adj_matrix = [
    [0, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0]
]



# Check for Hamiltonian path
result, path = hamiltonian_path_bruteforce(adj_matrix)
if result:
    print("Hamiltonian Path exists:", path)
else:
    print("No Hamiltonian Path found.")
