def show_excitement(str, n):
    if(n==0):
        return str
    else:
        return str*n

str = "I am super excited for this course! "

print(show_excitement(str, 5))