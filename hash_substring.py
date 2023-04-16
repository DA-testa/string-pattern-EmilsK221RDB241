# python3

def read_input():
    
   
    mode = input().strip()

    if mode == "I":

        text = input().strip()
        pattern = input().strip()

    elif mode == "F":
        try:

            with open("./tests/06") as r:

                pattern = r.readline().strip()
                text = r.readline().strip()

        except FileNotFoundError:

            print("File doesnt exist")
            exit()

    else:
        raise ValueError("Invalid input")

    return pattern, text


def print_occurrences(output):
    
    print(' '.join(map(str, output)))

    
def get_occurrences(pattern, text):
    
    text_l = len(text)
    pattern_l = len(pattern)

    pattern_h = hash(pattern)
    text_h = hash(text[:pattern_l])

    x = []

    for i in range(text_l - pattern_l + 1):

        if pattern_h == text_h and pattern == text[i:i + pattern_l]:
            x.append(i)

        if i < text_l - pattern_l:
            text_h -= hash(text[i + 1:i + pattern_l + 1])
            
    return x


if __name__ == '__main__':
    
    print_occurrences(get_occurrences(*read_input()))

