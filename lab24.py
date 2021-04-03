peptide = input()

masses = {
    'G': '57',
    'A': '71',
    'S': '87',
    'P': '97',
    'V': '99',
    'T': '101',
    'C': '103',
    'I': '113',
    'L': '113',
    'N': '114',
    'D': '115',
    'K': '128',
    'Q': '128',
    'E': '129',
    'M': '131',
    'H': '137',
    'F': '147',
    'R': '156',
    'Y': '163',
    'W': '186'
    }

def mass_list(string):
    string = str(string.upper())
    mass_ls = []
    for i in string:
        if i in masses:
            mass_ls.append(int(masses[i]))
    mass_ls = sorted(mass_ls)
    le_sum = sum(mass_ls)

    le_try = []

    for i,j in enumerate(mass_ls):
        if i > 0:
            le_try.append(mass_ls[i] + mass_ls[i-1])
    le_try.append(mass_ls[0]+mass_ls[len(mass_ls)-1])

    le_que = []

    for i,j in enumerate(le_try):
        if i > 0:
            le_que.append(le_try[i] + mass_ls[i-1])
    le_que.append(le_try[0]+mass_ls[len(mass_ls)-1])

    le_try += le_que
    mass_ls += le_try
    mass_ls.insert(0,0)
    mass_ls.append(le_sum)
    return sorted(mass_ls)

le_test = mass_list(peptide)
for i in le_test:
    print(i, end = " ")
