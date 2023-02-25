monthConversions = {
    'Jan': 'January',
    'Feb': 'February',
    'Mar': 'March',
    'Apr': 'April',
    'May': 'May',
    'Jun': 'June',
    'Jul': 'July',
    'Aug': 'August',
    'Sep': 'September',
    'Oct': 'October',
    'Nov': 'November',
    'Dec': 'December',
}

print(monthConversions['Nov']) # November
print(monthConversions['Mar']) # March
# get method
print(monthConversions.get('Dec')) # December
print(monthConversions.get('Luv')) # None
print(monthConversions.get('Luv', 'Not a valid Key')) # Not a valid Key

