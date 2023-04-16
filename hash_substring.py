# python3

def read_input():

    mode = input().strip()

    if mode not in ['F', 'I']:
        raise ValueError("Invalid input")

    if mode == "F":
        try:
            
            with open("./tests/06") as r:
                
                pattern = r.readline().strip()
                text = r.readline().strip()
                
        except FileNotFoundError:
            
            print("File doesn't exist")
            exit()

    else:

        text = input().strip()
        pattern = input().strip()

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

