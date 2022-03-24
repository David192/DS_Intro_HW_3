#A

def read_line(n, file):
    try:
        txt_file = open(file)
        for i, line in enumerate(txt_file):
            if i + 1 == n:
                return line
        if isinstance(n, int) != True:
            return "invalid input detected"
        x = len(txt_file.readlines())
        if n > x:
            return "line " + str(n) + " doesn't exist"
    except(FileNotFoundError):
        return "file not found"


#B

def longest_words(file):
    try:
        with open(file, 'r') as infile:
            txt_file = infile.read()
        for char in txt_file:
            if char.isalpha() == False:
                txt_file = txt_file.replace(char,' ')
        words = txt_file.split()
        words.sort(reverse = True, key = len)
        return [word for word in words[0:5]]
    except(FileNotFoundError):
        print('file not found')
        return []

