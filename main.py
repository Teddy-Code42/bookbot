import sys
if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    pass

def get_book_text(bookfilepath):
    with open(bookfilepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text(sys.argv[1])
    from stats import word_count
    count = word_count(text)
    from stats import char_count
    count2 = char_count(text)
    from stats import sort_on_list
    count3 = sort_on_list(count2)
    from stats import prettiestlist
    count4 = prettiestlist(count3)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    #print(count3) 
    for characternum in count3:
        tempchar = characternum["char"]
        if tempchar.isalpha():
            tempnum = characternum["num"]
            tempstring = f"{tempchar}: {tempnum}"
            print(tempstring)
        else:
            None

main ()
