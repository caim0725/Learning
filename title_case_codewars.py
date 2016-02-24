def title_case(title, minor_words=''):
    '''type in title and return all in capitalize 
    if word not in minor_words'''
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()
    return ' '.join([word if word in minor_words else word.capitalize() 
                    for word in title])

print title_case('')
print title_case('THE WIND IN THE WILLOWS', 'The In')
print title_case('the quick brown fox')