''' A magyarlánc összetevős elemzőjének kimenetét IOBES címkekészletre alakító szkript (maxNP-re) '''

# magyarlanc_vertical_szegedteszt.txt
# magyarlanc_vertical_szegedteszt_IOBES.txt

nyitva = 0

with open("magyarlanc_vertical_szegedteszt.txt", "r", encoding='utf-8') as putin, \
        open("magyarlanc_vertical_szegedteszt_IOBES.txt", "a", encoding='utf-8') as outputyin,\
        open("log.txt", "a", encoding='utf-8') as log:
    for line in putin:
        if len(line.split("\t")) > 1:
            if line.split("\t")[1].find("(NP") == -1 and nyitva < 1:
                outputyin.write(line.split("\t")[0]+"\tO\n")

            elif nyitva > 0:
                nyitva = nyitva + line.split("\t")[1].count("(")
                nyitva = nyitva - line.split("\t")[1].count(")")
                if nyitva > 0:
                    outputyin.write(line.split("\t")[0] + "\tI-N_1\n")
                else:
                    outputyin.write(line.split("\t")[0] + "\tE-N_1\n")
                    nyitva = 0

            elif line.split("\t")[1].find("(NP") > -1 and nyitva == 0:
                nyitva = line.split("\t")[1].count("(", line.split("\t")[1].find("(NP"))
                nyitva = nyitva - line.split("\t")[1].count(")", line.split("\t")[1].find("(NP"))
                if nyitva > 0:
                    outputyin.write(line.split("\t")[0] + "\tB-N_1\n")
                else:
                    outputyin.write(line.split("\t")[0] + "\t1-N_1\n")
                    nyitva = 0
        else:
            if nyitva != 0:
                outputyin.write("\tATTENZIONE!! Gond van, a nyitott zárójelek száma: "+str(nyitva)+"\n")
            else:
                outputyin.write(line)
            nyitva = 0