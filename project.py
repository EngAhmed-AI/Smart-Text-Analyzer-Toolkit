import os
from text_analyzer.utils import processor
from text_analyzer.analytics import count_the_len
from text_analyzer.keywords import keyword_extraction
from text_analyzer.similarity import text_similarity
from text_analyzer.sentiment import sentiment
from text_analyzer.stack import stack

while (choice := input("which input method do you prefer?\n\
1. Direct Entry\n\
2. Local File Path : ")).strip().lower():

    if choice in ["direct entry", "1"]:

        print("Enter your text To finish ($$END_TEXT$$):")
        lines = []

        while True:
            line = input()

            if "$$END_TEXT$$" in line:
                text_before=line.split("$$END_TEXT$$")[0]
                if text_before:
                    lines.append(text_before)
                break

            lines.append(line)

        text = "\n".join(lines)

        print("Saved successfully ")

        break

    elif choice in ["local file path", "2"]:

        try:

            path = input("Enter the path: ").strip('"').strip()

            if not os.path.exists(path):
                print("Error: path not found")
                continue

            if not os.path.isfile(path):
                print(" The entry is not a file ")
                continue
            if not path.endswith(".txt"):
                print("This file is not in format(.txt)")
                continue
            file_name = os.path.basename(path)

            print(f"your file is {file_name}")
            if os.path.getsize(path) == 0:
                print("Sorry file is empty")
                continue

            with open(path, "r") as f:
                text = f.read().strip()

                print(text)

            break

        except FileNotFoundError:
            print("Error: the file does not exist")
            continue

        except PermissionError:
            print("Error: permission denied")
            continue

        except Exception as e:
            print(f"Error: {e}")
            continue

    else:

        print("Incorrect entry. Please enter the correct value.")
        continue

processed_text = processor(text)
undo_stack = stack()
redo_stack = stack()

undo_stack.push(text)

while True:
    choice = input("1. Consolidated Text Analytics Dashboard\n2. Search for a Word or Phrase\n3. Replace a Word\n4. Keyword Extraction\n5. Text similarity Detector\n6. Undo\n7. Redo\n8. Simple sentiment\n9. Exit The Program:  ")
    if choice == "1":

        count_the_len(processed_text)
    elif choice == "2":
        searched_word = input("Enter the word to search for: ").strip().lower()
        lines = text.split("\n")
        found = False
        for line_num, sentence in enumerate(lines, start=1):
            cleaned_line = processor(sentence)
            if searched_word in cleaned_line:
                words = cleaned_line.split()
                for word_num, word in enumerate(words, start=1):
                    rest_of_text = " ".join(words[word_num-1 :])
                    if rest_of_text.startswith(searched_word):
                        print(f"found your word at : sentence number: {line_num}, word number: {word_num}")  
                        found = True
        if not found:
            print(f"{searched_word} was not found in the text.")
            
    elif choice == "3":
        target_word = input("Enter the word to replace: ").strip().lower()
        replace_word = input("Enter the new word: ").strip().lower()
        if target_word in text:
            redo_stack = stack()
            text = text.replace(target_word, replace_word)
            undo_stack.push(text)
            processed_text = processor(text)
            print("replaced successed")
        else:
            print(f"{target_word} is not in the text")

    elif choice == "4":
        print("Top Extracted Words")
        keywords = keyword_extraction(processed_text)
        if not keywords:
            print("No keywords found")
        else:
            for word, count in keywords:
                print(f"{word}: {count}")

    elif choice == "5":
        second_text = input("Enter the second text to compare: ")

        if second_text:
            score = text_similarity(text, second_text)
            print(f"Similarity score is: {score}")
        else:
            print("No text was entered")

    elif choice == "6":
        if undo_stack.is_Empty() or len(undo_stack.s) <= 1:
            print("there is nothing to undo")
        else:
            current_text = undo_stack.pop()
            redo_stack.push(current_text)
            text = undo_stack.top()
            processed_text = processor(text)
            print(" The undo successed")
            print("The current text is: ", text)

    elif choice == "7":
        if redo_stack.is_Empty():
            print("there is nothing to redo")
        else:
            next_text = redo_stack.pop()
            undo_stack.push(next_text)
            text = next_text
            processed_text = processor(text)
            print("The redo successed")
            print("The current text is: ", text)

    elif choice == "8":
        res, rate = sentiment(text)
        print(f"Sentiment: {res}")
        print(f"Confidence Rate: {rate}")

    elif choice == "9":
        print("Good Bye")
        break

    else:
        print("Error in input please enter a number from 1 to 9")