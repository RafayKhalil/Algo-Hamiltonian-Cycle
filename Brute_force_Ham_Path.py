from itertools import permutations

def is_valid_cycle(perm, adj, N):
    """
    Check if a given permutation of vertices represents a valid Hamiltonian cycle.
    """
    # Check if all consecutive vertices are connected
    for i in range(N - 1):
        if adj[perm[i]][perm[i + 1]] == 0:
            return False
    # Check if the last vertex is connected to the first vertex to complete the cycle
    if adj[perm[N-1]][perm[0]] == 0:
        return False
    return True

def hamiltonian_cycle_bruteforce(adj):
    """
    Checks for a Hamiltonian cycle in a graph using a brute force approach.
    """
    N = len(adj)  # Number of vertices
    all_perms = permutations(range(N))
    
    for perm in all_perms:
        if is_valid_cycle(perm, adj, N):
            complete_cycle = perm + (perm[0],)
            return True, complete_cycle  # Return True and the complete cycle
    return False, None  # Return False if no valid cycle is found

# Example graph represented by an adjacency matrix
adj_matrix = [
    [0, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0]
]

# Check for a Hamiltonian cycle
result, cycle = hamiltonian_cycle_bruteforce(adj_matrix)
if result:
    print("Hamiltonian Cycle exists:", cycle)
else:
    print("No Hamiltonian Cycle found.")





