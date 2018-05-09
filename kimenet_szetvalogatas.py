'''A szkript a végig helyesen csonkolt és a csonkolási hibákat tartalmazó mondatokat
válogatja szét.
Bemenet: az adott elemző kimenete
Kimenet: két fájl a jól és hibásan csonkolt mondatokkal'''

def kiir(sentence_list, good, bad):
    matching = True
    gold_line = ''
    new_line = ''
    for i in sentence_list:
        if i[3]:
            if i[2][0] == 'O' or i[2][0] == 'I':
                new_line = new_line + i[0] + ' '
            elif i[2][0] == '1':
                new_line = new_line + '[' + i[0] + '] '
            elif i[2][0] == 'B':
                new_line = new_line + '[' + i[0] + ' '
            elif i[2][0] == 'E':
                new_line = new_line + i[0] + '] '

            if i[1][0] == 'O' or i[1][0] == 'I':
                gold_line = gold_line + i[0] + ' '
            elif i[1][0] == '1':
                gold_line = gold_line + '[' + i[0] + '] '
            elif i[1][0] == 'B':
                gold_line = gold_line + '[' + i[0] + ' '
            elif i[1][0] == 'E':
                gold_line = gold_line + i[0] + '] '

        else:
            matching = False
            if i[2][0] == 'O' or i[2][0] == 'I':
                new_line = new_line + i[0] + ' '
            elif i[2][0] == '1':
                new_line = new_line + '[' + i[0] + '] '
            elif i[2][0] == 'B':
                new_line = new_line + '[' + i[0] + ' '
            elif i[2][0] == 'E':
                new_line = new_line + i[0] + '] '

            if i[1][0] == 'O' or i[1][0] == 'I':
                gold_line = gold_line + i[0] + ' '
            elif i[1][0] == '1':
                gold_line = gold_line + '[' + i[0] + '] '
            elif i[1][0] == 'B':
                gold_line = gold_line + '[' + i[0] + ' '
            elif i[1][0] == 'E':
                gold_line = gold_line + i[0] + '] '

    new_line = new_line + '\n'
    gold_line = gold_line + '\n'

    if matching:
        with open(good, "a", encoding='utf-8') as ki:
            ki.write(new_line)
            print("Egy jo mondat kiirva:")
            print(new_line)
    else:
        with open(bad, "a", encoding='utf-8') as ki:
            ki.write(gold_line)
            ki.write(new_line)
            print("Egy rossz mondat kiirva:")
            print(gold_line)
            print(new_line)


with open("magyarlanc_demo.txt", "r", encoding='utf-8') as myfile:  # bemeneti fájl nevét behelyettesíteni
    sentence = []
    for line in myfile:
        if line == "\n":
            kiir(sentence, "01_jo.txt", "02_nemjo.txt")
            sentence = []
        elif line.split("\t")[1] == line.split("\t")[2][0:-1]:  # HunTag3-hoz és PurePOS-hoz 1 és 2 helyett 8 és 9
            sentence.append([line.split("\t")[0], line.split("\t")[1], line.split("\t")[2], True])
        else:
            sentence.append([line.split("\t")[0], line.split("\t")[1], line.split("\t")[2], False])