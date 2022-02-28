dna = "GTAT" 
compliment = []
def DNA_strand(dna):
    for i in dna:
        if i == "A":
            compliment.append("T")
        if i == "T":
            compliment.append("A")
        if i == "C":
            compliment.append("G")
        if i == "G":
            compliment.append("C")
        x = "".join(compliment)
    print(x)
DNA_strand(dna)
