import collections


def ClumpFinder():
    ##Opening the file and reading the data

    with open('w1_4_data_set0.txt', 'r') as in_file:
        line = 1
        genome = ""
        k = 0
        l = 0
        t = 0
        ##Copying the data to a variable
        for i in range(2):
            if (line == 1):
                genome = str(in_file.readline())

            elif (line == 2):
                in_line2 = (in_file.readline()).split()
                in_line2 = list(map(int, in_line2))

                k = in_line2[0]
                l = in_line2[1]
                t = in_line2[2]
            line += 1

    ##Printing the contents of the file
    print(genome)

    ##Printing the requirements
    print(k)
    print(l)
    print(t)

    ##Finding the clumps:

    clumps = []
    for j in range(len(genome)):
        kstr = genome[j: j + l]
        if (len(kstr) == l):
            patterns = collections.defaultdict(list)

            for i in range(len(kstr) - k + 1):
                c = kstr[i:i + k]
                if c not in clumps and c in patterns:
                    patterns[c] += 1
                    if patterns[c] == t:
                        clumps.append(c)

                else:
                    patterns[c] = 1

    print(clumps)

##Running the program
ClumpFinder()

##Comments regarding the program:
## This program is not so efficient for very large datasets. The running time is very high. 
## Verdict: Better algorithms can be developed
