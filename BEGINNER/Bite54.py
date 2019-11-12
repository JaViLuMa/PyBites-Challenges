import textwrap


INDENTS = 4


def print_hanging_indents(poem):
  count = 0

  poem = poem.split("\n")

  for line in poem:
    line = line.strip()

    if not line:
      count = 0
      continue
    else:
      count += 1

    formatted = poem

    if count is not 1:
      formatted = (" " * INDENTS)
    else:
      formatted = ""
      
    print(formatted + line)
    
