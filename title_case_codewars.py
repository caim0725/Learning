def title_case(title, minor_words=''):
    '''type in title and return all in capitalize 
    if word not in minor_words'''
    if title == '':return ''
    split_title = title.lower().split()
    minor_list = minor_words.lower().split()
    new_title = ''
    for word in split_title:
        if word not in minor_list:
            new_title += word[0].upper() + word[1:] +' '
        else:new_title += word + ' '
    new_title = (new_title[0].upper() + new_title[1:]).rstrip()
    return new_title

print title_case('')
print title_case('THE WIND IN THE WILLOWS', 'The In')
print title_case('the quick brown fox')