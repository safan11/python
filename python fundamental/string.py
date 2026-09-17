"""
Python Strings: a beginner-friendly complete lesson

A string is text stored inside quotes. Examples:
	"Hello"
	'Python'
	"123"     # This is text, not the number 123

Run this file with:
	python string.py
"""


def main():
	# ------------------------------------------------------------
	# 1. Creating strings
	# ------------------------------------------------------------
	# You can use single quotes or double quotes. Both create a string.
	first_name = "Asha"
	country = 'India'

	print("1. Creating strings")
	print(first_name)
	print(country)

	# If the text contains an apostrophe, use double quotes outside.
	message = "Python is easy to learn."
	print(message)

	# len() counts the characters in a string, including spaces.
	print("Length of message:", len(message))

	# ------------------------------------------------------------
	# 2. Indexing: getting one character
	# ------------------------------------------------------------
	# Index positions start at 0, not 1.
	# P  y  t  h  o  n
	# 0  1  2  3  4  5
	language = "Python"

	print("\n2. Indexing")
	print("First character:", language[0])
	print("Third character:", language[2])
	print("Last character:", language[-1])

	# ------------------------------------------------------------
	# 3. Slicing: getting part of a string
	# ------------------------------------------------------------
	# text[start:stop] includes start but stops before stop.
	print("\n3. Slicing")
	print("First three characters:", language[0:3])
	print("Characters from position 2:", language[2:])
	print("Characters up to position 4:", language[:4])
	print("Every second character:", language[::2])
	print("Reversed string:", language[::-1])

	# ------------------------------------------------------------
	# 4. Strings are immutable
	# ------------------------------------------------------------
	# Immutable means that an existing string cannot be changed directly.
	# This would cause an error:
	# language[0] = "J"
	# Instead, create a new string.
	new_language = "J" + language[1:]
	print("\n4. New string after replacement:", new_language)

	# ------------------------------------------------------------
	# 5. Combining strings
	# ------------------------------------------------------------
	# The + operator joins strings. This is called concatenation.
	greeting = "Hello, " + first_name + "!"
	print("\n5. Concatenation:", greeting)

	# join() is useful when joining many pieces of text.
	words = ["Learn", "Python", "every", "day"]
	joined_sentence = " ".join(words)
	print("Using join():", joined_sentence)

	# ------------------------------------------------------------
	# 6. f-strings: the recommended way to format text
	# ------------------------------------------------------------
	age = 20
	print("\n6. f-string:")
	print(f"My name is {first_name} and I am {age} years old.")
	print(f"Next year I will be {age + 1} years old.")

	# ------------------------------------------------------------
	# 7. Changing letter case
	# ------------------------------------------------------------
	name = "python programming"
	print("\n7. Changing case")
	print("Uppercase:", name.upper())
	print("Lowercase:", name.lower())
	print("Title case:", name.title())
	print("Capitalized:", name.capitalize())

	# casefold() is useful for case-insensitive comparisons.
	print("Same word ignoring case:", "PYTHON".casefold() == "python".casefold())

	# ------------------------------------------------------------
	# 8. Removing unwanted spaces
	# ------------------------------------------------------------
	# User input often contains accidental spaces before or after the text.
	user_input = "   python   "
	print("\n8. Removing spaces")
	print("Before strip:", repr(user_input))
	print("After strip:", repr(user_input.strip()))
	print("Left side only:", repr(user_input.lstrip()))
	print("Right side only:", repr(user_input.rstrip()))

	# ------------------------------------------------------------
	# 9. Searching inside a string
	# ------------------------------------------------------------
	sentence = "Python is a powerful programming language."
	print("\n9. Searching")
	print("Contains 'powerful'?:", "powerful" in sentence)
	print("Starts with 'Python'?:", sentence.startswith("Python"))
	print("Ends with a period?:", sentence.endswith("."))
	print("Position of 'programming':", sentence.find("programming"))
	print("Number of 'a':", sentence.count("a"))

	# find() returns -1 when the text is not found.
	missing_position = sentence.find("Java")
	print("Position of 'Java':", missing_position)

	# ------------------------------------------------------------
	# 10. Replacing and splitting text
	# ------------------------------------------------------------
	print("\n10. Replacing and splitting")
	old_sentence = "I like Java."
	updated_sentence = old_sentence.replace("Java", "Python")
	print("After replace:", updated_sentence)

	csv_data = "red,green,blue"
	colors = csv_data.split(",")
	print("After split:", colors)

	# ------------------------------------------------------------
	# 11. Checking the kind of characters
	# ------------------------------------------------------------
	print("\n11. Character checks")
	print("'Python'.isalpha():", "Python".isalpha())
	print("'12345'.isdigit():", "12345".isdigit())
	print("'Python123'.isalnum():", "Python123".isalnum())
	print("'   '.isspace():", "   ".isspace())

	# ------------------------------------------------------------
	# 12. Escape characters and multiline strings
	# ------------------------------------------------------------
	# \n means a new line, and \t means a tab space.
	print("\n12. Escape characters")
	print("Line one\nLine two")
	print("Name:\t", first_name)

	# Triple quotes allow a string to continue across multiple lines.
	paragraph = """Python is readable.
It is useful for automation,
data analysis, and web development."""
	print(paragraph)

	# ------------------------------------------------------------
	# 13. Practical example: clean and validate a username
	# ------------------------------------------------------------
	print("\n13. Practical username example")
	username = "  Asha_2026  "
	clean_username = username.strip()

	if len(clean_username) >= 5 and clean_username.replace("_", "").isalnum():
		print(f"'{clean_username}' is a valid username.")
	else:
		print(f"'{clean_username}' is not a valid username.")

	# ------------------------------------------------------------
	# 14. Practical example: format a receipt
	# ------------------------------------------------------------
	print("\n14. Practical receipt example")
	product = "Notebook"
	quantity = 2
	price = 75.50
	total = quantity * price

	print("=" * 30)
	print("SHOP RECEIPT")
	print("=" * 30)
	print(f"Product : {product}")
	print(f"Quantity: {quantity}")
	print(f"Price   : Rs. {price:.2f}")
	print(f"Total   : Rs. {total:.2f}")
	print("=" * 30)

	# ------------------------------------------------------------
	# Quick summary
	# ------------------------------------------------------------
	print("\nQuick summary")
	print("- Use len(text) to count characters.")
	print("- Use text[index] to get one character.")
	print("- Use text[start:stop] to get a section.")
	print("- Use text.strip() to remove outer spaces.")
	print("- Use text.lower() or text.upper() to change case.")
	print("- Use text.replace(old, new) to replace text.")
	print("- Use text.split(separator) to create a list.")
	print("- Use f\"{value}\" to put values inside a string.")


# This condition starts the lesson only when this file is run directly.
# It prevents the lesson from running automatically if another file imports it.
if __name__ == "__main__":
	main()
