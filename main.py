def main():
    with open("./books/frankenstein.txt") as f:
        # Read the entire file into book_text first
        book_text = f.read()
        
        # Count words using the book_text string
        words = book_text.split()
        total_words = len(words)
        

        character_count = {}
        for character in book_text.lower():
            if character in character_count:
                character_count[character] += 1
            else:
                character_count[character] = 1

        print(f"--- Begin report of books/frankenstein.txt ---")
        print(f"{total_words} words found in the document")
        print("\n")
        for char, count in character_count.items():
            print(f"The '{char}' character was found {count} times")
        print("--- End report ---")

main()
