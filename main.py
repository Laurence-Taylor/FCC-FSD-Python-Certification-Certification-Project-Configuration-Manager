# I validate even the case when key-value in Test_settings are not lower_cases asuming for Example: theme==Theme.

def check_wrong_scenarios(settings_dictionary, key_value_tuple):
    # cheking key_value_tuple is a tuple
    is_secuence = isinstance(key_value_tuple,(tuple))
    if not is_secuence:
        return 'Invalid format: expected a tuple.'
    # cheking settings_dictionary is a dictionary
    is_dictionary = isinstance(settings_dictionary,(dict))
    if not is_dictionary:
        return 'Invalid format: expected a Dict.'  


def add_setting (settings_dictionary, key_value_tuple):
    #**************   Checking wrong scenarios    *****************
    msg_wrong_scenario = check_wrong_scenarios(settings_dictionary, key_value_tuple)
    if  msg_wrong_scenario != None:
        return msg_wrong_scenario

    # **************   Solving problem     ************************ 
    # Unpacking key and value from key_value_tuple and setting lowercase
    new_key, new_value = key_value_tuple
    new_key = new_key.lower()
    new_value = new_value.lower()
    # Cheking that key doesn't exist and return message if already exist
    for key, value in settings_dictionary.items():
        if key.lower() == new_key:
            return f"Setting '{key.lower()}' already exists! Cannot add a new setting with this name."
    # Add new key-value pair to dictionary in lower case and return message
    settings_dictionary[new_key] = new_value
    return f"Setting '{new_key}' added with value '{new_value}' successfully!"

def update_setting(settings_dictionary, key_value_tuple):
    #**************   Checking wrong scenarios    *****************
    msg_wrong_scenario = check_wrong_scenarios(settings_dictionary, key_value_tuple)
    if  msg_wrong_scenario != None:
        return msg_wrong_scenario 

    # **************   Solving problem     ************************ 
    # Unpacking key and value from key_value_tuple and setting lowercase
    new_key = key_value_tuple[0].lower()
    new_value = key_value_tuple[1].lower()
    # Check if exists the key and then update it or not and throw the corresponding message 
    for key, value in settings_dictionary.items():
        if key.lower() == new_key:
            settings_dictionary[key] = new_value
            return f"Setting '{new_key}' updated to '{new_value}' successfully!"
    return f"Setting '{new_key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings_dictionary, key_to_delete):
    #**************   Checking wrong scenarios    *****************
    # cheking settings_dictionary is a dictionary
    is_dictionary = isinstance(settings_dictionary,(dict))
    if not is_dictionary:
        return 'Invalid format: expected a Dict.' 

    # **************   Solving problem     ************************ 
    key_to_delete_lower = key_to_delete.lower()
    for key, _ in settings_dictionary.items():
        if key.lower() == key_to_delete_lower:
            settings_dictionary.pop(key)
            return f"Setting '{key_to_delete_lower}' deleted successfully!"
    return 'Setting not found!'

def view_settings(settings_dictionary):
    #**************   Checking wrong scenarios    *****************
    # cheking settings_dictionary is a dictionary
    is_dictionary = isinstance(settings_dictionary,(dict))
    if not is_dictionary:
        return 'Invalid format: expected a Dict.' 
    # cheking settings_dictionary is not empty
    if not settings_dictionary:
        return 'No settings available.'

    # **************   Solving problem     ************************
    # Filling the formated string to return
    return_settings = 'Current User Settings:\n'
    for key, value in settings_dictionary.items(): 
        return_settings += key.capitalize() + ': ' + value + '\n'
    return return_settings

test_settings = {'ThEme': 'Dark','notifications':'Enabled',
'Volume':'high'}

print (view_settings(test_settings))
print(test_settings)

print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

test_tuple = ('color', 'Blue')
print (add_setting (test_settings, test_tuple))
print('\n', test_settings)

print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

test_tuple = ('theme', 'White')
print (update_setting (test_settings, test_tuple))
print('\n', test_settings)

print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

print (delete_setting (test_settings, 'VOLUME'))
print('\n', test_settings)

print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

print(view_settings(test_settings))

