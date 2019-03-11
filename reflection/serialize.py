import inspect

################################################
###   Type Tests Functions

is_null     = lambda v: v is None
is_bool     = lambda v: isinstance(v, bool)
is_float    = lambda v: isinstance(v, float)
is_int      = lambda v: isinstance(v, int)
is_str      = lambda v: isinstance(v, str)
is_obj      = lambda v: isinstance(v, (dict, list, object, set, tuple))

################################################
###   Print Functions

print_null  = lambda k,v: print('{}: {}'.format(k,v)) 
print_bool  = lambda k,v: print('{}: {}'.format(k,v)) 
print_float = lambda k,v: print('{}: {}'.format(k,v)) 
print_int   = lambda k,v: print('{}: {}'.format(k,v)) 
print_str   = lambda k,v: print('{}: {}'.format(k,v)) 
print_obj   = lambda k,v: print('{}: {}'.format(k,v)) 

################################################
###   Serialization to JSON

TAB = '\t'
FUNCTIONS = [
    ( is_null,  print_null  ),
    ( is_bool,  print_bool  ),
    ( is_float, print_float ),
    ( is_int,   print_int   ),
    ( is_str,   print_str   ),
    ( is_obj,   print_obj   ),
]

def to_json(obj, level=0):
    '''Serializes the given object to JSON, printing to the console as it goes.'''
    for name, value in inspect.getmembers(obj):
        for test, method in FUNCTIONS:
            if test(value):   
                method(name, value)
    return None

