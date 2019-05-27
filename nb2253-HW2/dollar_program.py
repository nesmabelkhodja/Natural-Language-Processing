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
      r'[\$][\d{1,3}]\,\d{1,3}\,\d{1,3}', # $9,999,999
      r'[\$][\d{1,5}]\.\d{1,2}', # $99999.99
      r'[\$](\d+\.\d{1,2})',  # $9.99
      r'[\$][\d{1,3}]\,\d{1,3}\.\d{1,2}', # $999,999.99, $99,999.99
      r'[\$][\d{1,3}]\,\d{1,3}', #$999,999, $99,999, 9,999
      r'million|millions',
      r'billion|billions',
      r'trillion|trillions'
    ]), re.IGNORECASE)

    try:
        input_file = INPUT_FILE
        output_file = open("dollar_output.txt", 'w+')
        matches = open("dollar_output.txt", "w+")
        nextLine = ""

        for i, line in enumerate(open(input_file)):
            nextLine = line
            for match in re.finditer(PATTERN, line):
                counter += 1
                matches.write(match.group(0)+"\n")
                output_file.write(match.group(0)+"\n")
                nextLine = line.replace(match.group(0), "[" + match.group(0) + "]")

        print "There were " + str(counter) + " matches for dollars. The results were printed to dollar_output.txt"

    except IOError:
        print ("File not found.")

main()