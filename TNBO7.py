filename = input("Insert file to transform: ")

f = open(filename,"r")

newfile = open(filename+"RW","w")

line = f.readline()
count = 0

while line:
    if "------------------------------------" in line:
        count += 1
        line = f.readline()
    if count == 2:
        lt = line.split(" ")
        lt = list(filter(None,lt))
        lt[-1] = lt[-1].strip()

        if len(lt[0]) == 2:
            newfile.write("   "+lt[0])
        else:
            newfile.write("    "+lt[0])

        for n in range(1,4):
            if "-" in lt[n]:
                newfile.write("  "+lt[n]+"000")
            else:
                newfile.write("   "+lt[n]+"000")

        newfile.write("\n")

    if count == 3:
        break

    line = f.readline()


f.close()
newfile.close()
