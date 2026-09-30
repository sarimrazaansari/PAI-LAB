def add_mark_bad(mark, marks=[]):
    marks.append(mark)
    return marks

print(add_mark_bad(50))
print(add_mark_bad(60))

def add_mark(mark, marks=None):
    if marks is None:
        marks = []
    marks.append(mark)
    return marks

print(add_mark(50))
print(add_mark(60))