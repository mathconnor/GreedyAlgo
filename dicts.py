def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    ctr = sum(map(len, aDict.values()))
    return ctr

print(how_many({ 'a': ['aardvark', 'apple'], 'b': ['baboon'], 'c': ['coati']}))
