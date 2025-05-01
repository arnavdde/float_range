# Author
 Arnav De, arnavde@uoregon.edu
 # float_range
 I felt python was missing a float_range function as part of its core documentation. I've efficiently implemented one of my own for anyone interested. This function will increment by decimal precision of the float given, up to float64.
 # usage
 from float_range import float_range
 
 for x in float_range(1.5, step=0.1):
     print(x)
