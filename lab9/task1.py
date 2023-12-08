from typing import Optional, TextIO

def file_open(filename, mode) -> Optional[TextIO]:
    try:
        file = open(filename, mode)
    except Exception as e:
        print("File", filename, "wasn't opened! Error:", e)
        return None
    else:
        print("File", filename, "was opened!")
        return file

file1_name = "TF16_1.txt"
file2_name = "TF16_2.txt"

# а)
file1_w = file_open(file1_name, "w")
if file1_w is not None:
    file1_w.write("The flight number 1717 is postponed for 40 minutes, the boarding will start at 5 a.m.")
    print(f"Successfully written into {file1_name}")
    file1_w.close()
    print(f"Closed {file1_name}")

# б)
file1_r = file_open(file1_name, "r")
file2_w = file_open(file2_name, "w")
if file1_r is not None and file2_w is not None:
    vowel_words = []
    for chunk in file1_r.read().split(", "):
        for word in chunk.split(" "):
            if word[0].lower() in ('a','e','i','o','y','u'):
                vowel_words.append(word)
    file2_w.write("\n".join(vowel_words))
    file1_r.close()
    file2_w.close()

# в)
file2_r = file_open(file2_name, "r")
if file2_r is not None:
    print(file2_r.read())

