import inspect

TAB = '\t'
NEW_LINE = '\n'

################################################
###   Helper Functions

escape_chars = lambda s: s.replace('\\','\\\\').replace('"','\\"')

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

print_null  = lambda k,v,l: '{}"{}": null,{}'.format(TAB*l+TAB,k,NEW_LINE)
print_bool  = lambda k,v,l: '{}"{}": {},{}'.format(TAB*l+TAB,k,str(v).lower(),NEW_LINE)
print_float = lambda k,v,l: '{}"{}": {},{}'.format(TAB*l+TAB,k,v,NEW_LINE)
print_int   = lambda k,v,l: '{}"{}": {},{}'.format(TAB*l+TAB,k,v,NEW_LINE)
print_str   = lambda k,v,l: '{}"{}": "{}",{}'.format(TAB*l+TAB,k,escape_chars(v),NEW_LINE)
print_obj   = lambda k,v,l: '{}"{}": {},{}'.format(TAB*l+TAB,k,to_json(v,l+1),NEW_LINE)

################################################
###   Serialization to JSON

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
    json = '{}{}'.format('{',NEW_LINE)
    for name, value in inspect.getmembers(obj):
        for test, method in FUNCTIONS:
            if test(value) and not name.startswith('__'):
                json = json + method(name, value, level)
                break
    json = json[:-2] + NEW_LINE + '{}{}'.format(TAB*level,'}')

    return json

