example_tup = (1, 2, 3, 'hi', 'bye')
def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    odds = ()
    for i in range(len(aTup)):
        if i % 2 == 1:
            odds = odds + ((aTup[i]), )
    return odds
print(oddTuples(example_tup))

# def get_data(aTuple):
#     nums = ()
#     words = ()
#     for t in aTuple:
#         nums = nums + (t[0], )
#         if t[1] not in words:
#             words = words + (t[1], )
#     min_nums = min(nums)
#     max_nums = max(nums)
#     unique_words = (len(words))
#     return (min_nums, max_nums, unique_words)
# (small, large, words) = get_data(((1, 'nine'),
#                                   (3, 'yours'),
#                                   (5, 'ours'),
#                                   (7, 'mine')))
#
# print(small, large, words)