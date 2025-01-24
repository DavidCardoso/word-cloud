"""Generate a word cloud image from an input file.
    Note: only works with .odt files.

Returns:
    None
"""

import argparse
from odf.opendocument import load
from odf.text import P
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


def read_odt_file(file_path):
    """
    Reads the content of an ODT (Open Document Text) file and extracts the text.

    Args:
        file_path (str): The path to the ODT file to be read.

    Returns:
        str: The extracted text content from the ODT file, with paragraphs joined
            by newline characters.
    """

    # Load the ODT file
    odt_doc = load(file_path)
    text_content = []

    # Iterate over all paragraphs and extract text
    for element in odt_doc.getElementsByType(P):
        text_content.append(str(element))

    # Join all text parts into a single string
    return "\n".join(text_content)


def filter_text(text, custom_stopwords):
    """
    Filters out stopwords and custom words from the input text.

    Args:
        text (str): The input text to be filtered.
        custom_stopwords (set): A set of custom words to be filtered out.

    Returns:
        str: The filtered text.
    """
    stopwords = STOPWORDS.union(custom_stopwords)
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stopwords]
    filtered_text = " ".join(filtered_words)

    return filtered_text


def main():
    """
    Main function to generate a word cloud from an ODT file.
    This function sets up an argument parser to accept the path to an ODT file,
    reads the text from the specified ODT file, generates a word cloud from the
    text, and displays the word cloud using matplotlib.

    Arguments:
        None

    Returns:
        None
    """

    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Generate a word cloud from an ODT file."
    )

    # Add arguments
    parser.add_argument("--input_file", type=str, help="Path to the ODT file")
    parser.add_argument(
        "--output_file",
        type=str,
        help="Output file",
        required=False,
        default="outputs/wordcloud.png",
    )
    parser.add_argument(
        "--custom_stopwords",
        type=str,
        nargs="*",
        help="Custom stopwords to exclude from the word cloud",
        required=False,
        default=[],
    )

    # Parse arguments
    args = parser.parse_args()

    # Read text from the ODT file
    input_text = read_odt_file(args.input_file)

    # Filter text
    filtered_text = filter_text(input_text, set(args.custom_stopwords))

    # Set output file
    output_file = args.output_file

    # Create a word cloud object
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(
        filtered_text
    )

    # Save & Display the word cloud using matplotlib
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig(output_file)
    plt.show()


if __name__ == "__main__":
    main()
