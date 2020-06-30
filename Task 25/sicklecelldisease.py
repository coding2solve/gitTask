def translate(seq):
    

    I = ["ATT", "ATC", "ATA"]
    L = ["CTT", "CTC", "CTA", "CTG", "TTA", "TTG"]
    V = ["GTT","GTC", "GTA", "GTG"]
    F = ["TTT", "TTC"]
    M = ["ATG"]

    splitSq = [] 

   
    for i in range(0, len(seq), 3):  
        splitSq.append(seq[i : i + 3]) 


    if len(splitSq[len(splitSq) - 1]) < 3: #loop through to check if sequence is less than 3
        splitSq.pop(len(splitSq) - 1)  

    #check DNA codons to return the Amino Acid
    if splitSq == I:
        return "Isoleucise"


    elif splitSq == L:
        return "Leucine"


    elif splitSq == V:
        return "Valine"


    elif splitSq == F:
        return "Phenylalanine"


    elif splitSq == M:
        return "Methionine"


    else:

        return "X"  #output X


def mutate(): #this functions splits sequence in the dna.txt file to write its content into two different files 
    
    DNA_file = open("DNA.txt", "r+")#write DNA_file
    normal_DNA_file = open("normalDNA.txt", "w") #write normal DNA_file
    mutated_DNA_file = open("mutatedDNA.txt", "w") #write mutated DNA_file

    
    DNA_file_content = DNA_file.read() #read all contents in the DNA.txt file 

    
    
    normal_DNA = DNA_file_content.replace("a", "A") #change the lowercase "a"  to "A" 
    mutated_DNA = DNA_file_content.replace("a", "T") #change the lowercase "a" to "T"

    
    normal_DNA_file.write(normal_DNA) #write content of normal_DNA to txt file normalDNA.txt
    mutated_DNA_file.write(mutated_DNA)#write content of mutated_DNA to txt file mutatedDNA.txt

    DNA_file.close() #dna file closed
    normal_DNA_file.close() #normal dna file closed
    mutated_DNA_file.close()#mutated dna file closed


def txtTranslate(seq):  #textTranslate function
    
    return translate(seq)

mutate()#calling mutate functions 

#print ( "Your DNA is : " + str(translate("ATG"))) #prints the dnaa


normal_DNA_file = open("normalDNA.txt", "r")
mutated_DNA_file = open("mutatedDNA.txt", "r")

print(txtTranslate(normal_DNA_file.read()))
print(txtTranslate(mutated_DNA_file.read()))

normal_DNA_file.close() #normal dna file closed
mutated_DNA_file.close()#mutated dna file closed



print (translate("ATG")) #prints the dnaa


