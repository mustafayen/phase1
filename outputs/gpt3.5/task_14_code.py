# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


def all_prefixes(string):
    prefixes = []
    for i in range(len(string)):
        prefixes.append(string[:i+1])
    return prefixes

# Example usage
print(all_prefixes("hello"))
# Output: ['h', 'he', 'hel', 'hell', 'hello']