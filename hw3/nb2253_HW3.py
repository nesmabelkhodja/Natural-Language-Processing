import operator

#writes output to file "submission.pos"
def output_file(results):
    with open("submission.pos", "w+") as file:
        for i in range(len(results)):
            if results[i][0] != "":
                file.write("%s\t%s\n" % (results[i][0], results[i][1]))
            else:
                file.write("\n")

#finds max after checking and accounting for exception                
def find_max_except(pos, prob_POS, prior_POS, table_prev):
    key = (prior_POS, pos)
    try:
        max_num = prob_POS * table_prev[pos][key]
    except:
        max_num = prob_POS

    return [pos, max_num]

#finds max assuming there is no exception
def find_max(place, prob, prior_POS, table_prev):
    return [place, prob * table_prev[place][(prior_POS, place)]]

def createAbstractVector(removeStopWordsAbstracts, removeStopWordsQueries):
    for term in removeStopWordsAbstracts:
        for term in term:
            term = term.lower()
            if term in wordFreq:
                wordFreq[term] += 1
            else:
                wordFreq[term] = 1

#main method
def main():
    likelihood = {}
    print "Working..."
    count_table = {}
    word_count = 0
    
    #training file
    with open("WSJ_02-21.pos") as file:

        for line in file:
            array = line.split("\t")
            if len(array) >= 2:
                pos = array[1].replace("\n", "")
                value = array[0]

                if not pos in count_table:
                    count_table[pos]= 1

                elif pos in count_table:
                    count_table[pos] = count_table[pos] + 1

                word_count = word_count + 1

        for key, value in count_table.iteritems():
            likelihood[key] = float(count_table[key])/word_count

    num_terms = {}
    likelihood_terms = {}

    with open("WSJ_24.pos") as infile:
        for line in infile:
            seq = line.split("\t")
            if len(seq) >= 2:
                val = seq[0]
                pos = seq[1]
                pos = seq[1].replace("\n", "")

                if not val in num_terms:
                    num_terms[seq[0]] = {}
                    num_terms[seq[0]][pos]=1

                if val in num_terms:
                    if not pos in num_terms[seq[0]]:
                        num_terms[seq[0]][pos]=1
                    else:
                        num_terms[seq[0]][pos] = num_terms[seq[0]][pos] + 1

        for key, val in num_terms.iteritems():
            if len(seq[0]) == 1:
                likelihood_terms[key] = {}
                likelihood_terms[key][value.keys()[0]] = 1.0

            if len(val) > 1:
                likelihood_terms[key] = {}

                pos_sums = 0
                for key, val in value.iteritems():
                    pos_sums - pos_sums + val

                for key, val in value.iteritems():
                    likelihood_terms[key][key] = float(val)/pos_sums

    

    file = open("WSJ_02-21.pos", "r").read()
    table = {}
    lines = file.splitlines()
    num_lines = 0
    likelihood_table = {}

    for i in range(len(lines)):

        line = lines[i].split("\t")

        try:
            next_line = lines[i+1].split("\t")
        except:
            continue

        if len(line) < 2 or len(next_line) <2:
            continue

        next_line = next_line[1]
        both_lines = line[1], next_line

        if both_lines in table:
            table[both_lines] = table[both_lines] + 1

        else:
            table[both_lines] = 1

        num_lines = num_lines + 1


    for key, value in table.iteritems():
        likelihood_table[key] = float(table[key])/num_lines

    table_prev = {}

    for key, value in likelihood_table.iteritems():
        current_pos = key[1]

        if current_pos not in table_prev:
            table_prev[current_pos] = {}

            for key, value in likelihood_table.iteritems():
                    if key[1] == current_pos:
                        table_prev[current_pos][key] = value

    # Viterbi HMM POS Tagging
    # take a corpus in the format of the test corpus and produce results in the format of the training corpus
    results = []
    with open("WSJ_23.words", "r+") as file:
        start = True

        for line in file:

            word = line.rstrip()

            if start==True:
                most_likely_first = max(likelihood.iteritems(), key=operator.itemgetter(1))[0]
                results.append([word, most_likely_first])
                start = False

            else:
                try:
                    if len(likelihood_terms[word]) > 1:
                        prior_POS = results[len(results)-1][1]

                        max_val = 0
                        max_both_lines = []

                        for key, value in likelihood_terms[word].iteritems():
                            check_max = find_max(key, value, prior_POS, table_prev)

                            if check_max[1] > max_val:
                                max_val = check_max[1]
                                max_both_lines = check_max

                        result = [word, max_both_lines[0]]       
                        results.append(result)

                    elif len(likelihood_terms[word]) == 1:
                        results.append([word, likelihood_terms[word].keys()[0]])

                except:
                    prior_POS = results[len(results)-1][1]

                    max_val = 0
                    max_both_lines = []

                    for key, value in likelihood.iteritems():
                        check_max_exception = find_max_except(key, value, prior_POS, table_prev)

                        if check_max_exception[1] > max_val:
                            max_val = check_max_exception[1]
                            max_both_lines = check_max_exception

                    results.append([word, max_both_lines[0]])

        #write results to an output file            
        output_file(results)
        print "Done. Output is in the file submission.pos"


main()