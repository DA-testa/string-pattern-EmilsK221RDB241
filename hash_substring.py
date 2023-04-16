# python3

def read_input():

    mode = input().strip()

    if mode == "I":

        text = input().strip()
        pattern = input().strip()

    elif mode == "F":
        with open("./tests/06") as f:

            text = f.readline().strip()
            pattern = f.readline().strip()

    else:
        raise ValueError("Invalid input")

    return pattern, text


def print_occurrences(output):
    
    if output:
        
        print(' '.join(map(str, output)))
        
    else:
        
        print("Pattern not found in text")
    
    
def get_occurrences(pattern, text):

    pattern_l = len(pattern)
    text_l = len(text)

    pattern_h = hash(pattern)
    text_h = hash(text[:pattern_l])

    x = []

    for n in range(text_l - pattern_l + 1):

        if text_h == pattern_h and pattern == text[n: n + pattern_l]:
            x.append(n)

        if n < text_l - pattern_l:
            text_h = hash(text[n + 1: n + pattern_l + 1])

    return x


if __name__ == '__main__':
    
    print_occurrences(get_occurrences(*read_input()))

