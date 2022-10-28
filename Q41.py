#Camryn Hurley

hashtag = '#'
def count_hashtag(lines, hashtag):
    count = 0
    index = 0
    while index < len(lines):
        if lines[index:index+len(hashtag)] == hashtag:
            count += 1
            index += len(hashtag)
        else:
            index += 1
    return count
