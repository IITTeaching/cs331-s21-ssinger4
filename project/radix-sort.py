import urllib
import urllib.request

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def c_sort(lst, index):
    out = [0 for i in range(len(lst))]
    c = [0 for i in range(128)]
    sorted = ["" for _ in lst]
    for i in lst:
        if -index <= len(i):
            c[i[index]] += 1
        else:
            c[0] += 1
    for i in range(128):
        c[i] += c[i-1]
    for i in range(len(lst) -1, -1, -1):
        if -index <= len(lst[i]):
            out[c[lst[i][index]] - 1] = lst[i]
            c[lst[i][index]] -= 1            
        else:
            out[c[0] - 1] = lst[i]
            c[0] -= 1            
    for i in range(len(lst)):
        sorted[i] = out[i]
    return sorted

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    sort = book_to_words(book_url)
    max = 0
    for i in sort:
        if max < len(i):
            max = len(i)
    max = max * -1
    for i in range(-1, max-1, -1):
        sort = c_sort(sort, i)
    return sort
