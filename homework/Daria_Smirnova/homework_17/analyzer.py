import os
import argparse


def find_five_words(line, find_text, diapozon=5):
    words = line.strip().split()
    results = []
    for i in range(len(words)):
        if find_text.lower() in words[i].lower():
            start = max(0, i - diapozon)
            end = min(len(words), i + diapozon + 1)
            part = " ".join(words[start:end])
            results.append(part)
    return results


def read_logs(folder, find_text, show_all=True):
    if not os.path.isdir(folder):
        print("There is no existing folder with this name")
        return

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            with open(file_path, "r") as file:
                for line_num, line in enumerate(file, start=1):
                    contexts = find_five_words(line, find_text)
                    for context in contexts:
                        print(f"{filename} - string {line_num}: {context}")
                    if not show_all:
                        return


parser = argparse.ArgumentParser()
parser.add_argument("file", help="File name")
parser.add_argument("--text", help="Text for searching")
parser.add_argument("--first", action="store_true", help="Show only the first similarities")
args = parser.parse_args()
print(args.file, args.text, args.first)
read_logs(args.file, args.text.lower(), show_all=not args.first)
