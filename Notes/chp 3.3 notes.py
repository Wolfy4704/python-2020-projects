#Brayden Woodard
#9/20
#ch 3.3 notes

var = "something else" 
result = str.format("the {0:>50} {1:^50} {2:<50}", "test2", "testing", var, "-----------------------------------------------------------------------------")
print(result)
print(str.format("Example 'd': {0:15d}", 1500000))
print(str.format("Example ',': {0:15,}", 1500000))
print(str.format("Example 'e': {0:15e}", 3.14159))
print(str.format("Example 'f': {0:15f}", 3.14159))
print(str.format("Example '%': {0:15.2%}", 0.75))
