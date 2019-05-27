import sys
import re

def main():


#read input args
    if len(sys.argv) == 2:
        INPUT_FILE = str(sys.argv[1])
    else:
        print "Error: Incorrect format."
        return

    counter = 0
    PATTERN = re.compile('|'.join([
      r'\(\d{3}\)[\s]\d{3}[\s-]\d{4}', # (123) 123-1234
      r'\(\d{3}\)[-]\d{3}[\s-]\d{4}', # (123)-123-1234
      # r'^\d{3}[\s.-]\d{4}', # 123-1234
      r'\d{3}[-]\d{3}[\s-]\d{4}' # 123-123-1234
    ]), re.IGNORECASE)

    try:
        input_file = INPUT_FILE
        output_file = open("telephone_output.txt", 'w+')
        matches = open("telephone_output.txt", "w+")
        nextLine = ""

        for i, line in enumerate(open(input_file)):
            nextLine = line
            for match in re.finditer(PATTERN, line):
                counter += 1
                matches.write(match.group(0)+"\n")
                output_file.write(match.group(0)+"\n")
                nextLine = line.replace(match.group(0), "[" + match.group(0) + "]")

        print "There were " + str(counter) + " matches for telephone numbers. The results were printed to telephone_output.txt"

    except IOError:
        print ("File not found.")

main()