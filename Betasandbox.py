e = 'empty'
s = 'ship'

shipPlacementlist = [[e, e, e, e, e, e, e, e, e, e],
                                 [e, s, s, s, e, e, e, s, e, e],
                                 [e, e, e, e, e, s, e, s, e, e],
                                 [e, s, e, e, e, s, e, s, e, e],
                                 [e, e, e, e, e, e, e, s, e, e],
                                 [e, e, e, e, e, s, e, s, e, e],
                                 [e, e, e, e, e, e, e, e, e, e],
                                 [e, e, e, s, s, s, s, e, e, e],
                                 [e, e, e, e, e, e, e, e, e, e],
                                 [s, s, e, e, e, e, e, e, e, e]]


slice = shipPlacementlist[9][0]
print (slice)