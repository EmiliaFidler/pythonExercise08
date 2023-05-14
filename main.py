# --- Exercises 08: ---

# 01:
def write_to_file(text, output_file_path):
    try:
        with open(output_file_path, 'x') as file:
            file.write(text)
    except FileExistsError:
        raise RuntimeError('Output file already exists!')


# write_to_file('Hello??', 'file.txt')


import spacy

nlp = spacy.load('en_core_web_sm')

my_string = 'Hello my name is Emilia and you are not watching Disney Channel.'


# 02
def count_stopwords(input_file_path):
    with open(input_file_path, "r") as f:
        text = f.read()
    return count_stopwords_str(text)


def count_stopwords_str(text):
    doc = nlp(text)
    # creates list with all stop tokens
    stop_words = [token for token in doc if token.is_stop]
    return len(stop_words)


print(count_stopwords_str(my_string))


# 03:
def remove_stopwords(input_file_path, output_file_path):
    with open(input_file_path, "r") as f:
        text = f.read()
    result_text = remove_stopwords_str(text)
    with open(output_file_path, "w") as f:
        f.write(result_text)


def remove_stopwords_str(text):
    doc = nlp(text)
    stop_words = [token.text for token in doc if token.is_stop]
    for stop_word in stop_words:
        text = text.replace(f" {stop_word} ", " ")
        text = text.replace(f" {stop_word}.", " ")
    return text


remove_stopwords("file.txt", "file_without_stopwords.txt")


# 04:
def tokenize_text(input_file_path, output_file_path):
    with open(input_file_path, "r") as f:
        text = f.read()

    result_text = tokenize_text_str(text)

    with open(output_file_path, "w") as f:
        f.write(result_text)


def tokenize_text_str(text):
    doc = nlp(text)
    result = ""
    for token in doc:
        result += f'{token.text:{10}}{token.pos_:{10}}{token.dep_:{10}}\n'
    return result


tokenize_text('file.txt', 'tokenized_file.txt')

# 05
from spacy import displacy


def save_visualization(input_file_path, output_file_path):
    with open(input_file_path, "r") as f:
        text = f.read()

    doc = nlp(text)
    result = displacy.render(doc)

    with open(output_file_path, "w") as f:
        f.write(result)


save_visualization("file.txt", "visualization.svg")
