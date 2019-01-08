keywords = {
  "spawn" : 'spawn',
  "print":'print',
  "sum":'sum',
  "isum" : 'isum',
  "comment":'#',
  "variable":'=',
  "start":'start',
  "start_db" : 'database',
  "init_table" : 'table',
  "add_toTable" : 'add',
  "add_Unique" : 'uadd',
  "remove_fromTable" : 'remove',
  "local_db" : 'local'
}

data_types = {
    "string" : 'string',
    "integer" : 'integer',
    "float" : 'float',
    "boolean" : 'boolean',
    "array " : 'array'
}

function_types = {
    "spawn_array" : 'spawn_array',
    "print_string" : 'print_string',
    "real_sum" :'real_sum',
    "string_db" : 'string_db',
}

assign = {
    "assign_var" : 'assign_var',
    "change_value" : 'change_value',
    "print_call" : 'print_call'
}

errors = {
    'var_not_found' : 'Variable does not exist',
    'error2' : 'Exception Bad Formatting',
    'error3' : 'Len exceeded'
}

core_engine = {
  "database" : False,
  "mainWindow" : False,
  "init_table" : False,
  "databaseValue" : ''
  }

config_file = {
    'print_max_loop' : 10
  }

engine = {
    'name' : '',
    'version' : 0.9
}
