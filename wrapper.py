
"""
Created on Mon Feb 25 20:42:36 2019

Here begins the python wrapper that will contain all the line commands
And the python scripts to be able to run previous steps.
The functions are done in order and will be called sequentially according to the mini project at the end

@author: vincentacuesta
"""
import os
from Bio import SeqIO
import datetime
from multiprocessing import Process
import sys


    

#you need to make a directory for everything that is being ran to be printed out
def make_dir():
    os.system('mkdir OptionA_Vincent_Acuesta')
    os.chdir('OptionA_Vincent_Acuesta')
    return

#step1 wget the .sra

def letsBegin():
    'begin the project by wget'
    input_path='wget ftp://ftp.ncbi.nlm.nih.gov/sra/sra-instant/reads/ByRun/sra/SRR/SRR818/SRR8185310/SRR8185310.sra'
    os.system(input_path)
    #this will write out our command into the log file
    with open('log.txt','w') as output:
        output.write(input_path) 
    return input_path

#step2 spades 
def run_spades():
    """
    Will contain the line command to run spades into a directory and to read a file to run spades
    
    """
    output_path='~/OptionA_Vincent_Acuesta'
    read_file='~OptionA_Vincent_Acuesta/SRR8185310'
    
    #this is what the spades command begins with 
    begin_command='spades.py'
    #this will be appended to the spades command
    begin_command+=' -k 55,77,99,127 -t 2 --only-assembler -s '+read_file+' -o '+output_path
    os.system(begin_command)
    #opens the log.txt file to be written into but now we are appending to it in order to do it 
    with open('log.txt','a') as output:
        output.write('The spades command '+begin_command) 
    #return afterwards
    return begin_command

#step3 from assignment
def step3():
    """
    This will read in a file to check a conditional of contigs that will be greater than a 1000
    
    """
    #initiate the empty list
    contigs=[]

    #handles the open of the file 
    handle=open('~/OptionA_Vincent_Acuesta/contigs.fasta')

    #the loop will read the open file and parse it to be read into record the list contigs[]
    for record in SeqIO.parse(handle, 'fasta'):
    #this will logically read it to follow this conditional
        if len(record)>1000:
            contigs.append(record)
    number = len(contigs)
            #prints out according to format asked in the problem
    print("This is the specific amount >1000 %d" % ( number))

    #writes the file 
    with open('log.txt','a') as output:
        output.write("This is the amount >1000 %d" % (number)) 
    SeqIO.write(contigs, '~/OptionA_Vincent_Acuesta/long_contigs.fasta', "fasta")
    return number

    
#step4 from assignment
def step4():
    """
    This will read in the outputted file from step 3 and that outputted file will be read into step 4.
    This will concatenate all the contigs from the previous file to be put into a long one. This will
    give you the number of the longest one which is over 2million
    
    """
    #in order to handle and parse the file
    from Bio import SeqIO

    #intitate a list to be read into 
    long_contigs=[]

    #keeps track of the total length to be counted
    total_length = 0

    hold = 0

    #this will read and handle the path file 
    handle=open('~/OptionA_Vincent_Acuesta/long_contigs.fasta')
    #parse and append the long contigs from the file in step 3 to a long contig 
    for record in SeqIO.parse(handle, 'fasta'):
        long_contigs.append(record)
        hold=(len(record))
        total_length += hold
   
    #will print out the total length of the string
    print(str(total_length))
   

    #writes the file 
    with open('log.txt','a') as output:
        output.write('The concatenation of all the contigs is' +str(total_length)) 
        
    return total_length

#step5 of the assignment to run prokka
def run_prokka():
    """
    Prokka to annotate the assembly. We will be utilizing the Escherichia database.
    
    """
    outpath_file ='~/OptionA_Vincent_Acuesta/Prokka_results'
    read_file = 'long_contigs.fasta'
    
    prokka_command='prokka --outdir '+outpath_file+' genus Escherichia --locustag ECOL '+read_file
    os.system(prokka_command)
    return prokka_command

#step6 you need to write the information from the .txt file of from the prokka output to the log
def step6():
    """
    After running prokka this will output a specific .txt file that you will need to be read into the log file
    This is what step6 will do. If you run prokka this will change by the date that you decide to run prokka
    there will be an import of datetime to make sure that the filename changes according to date.
    #read in file to use, and then parse through
   #cds and trna from the reference seek are on the document, its like 4000 something
   #save the cds and trna from the file we read in
   #once you have both of those then do math to find out the outputs
   
   
    """
    now = datetime.datetime.now()
    input = ('0'+ '%d' %now.month + '%d' %now.day + '%d' % now.year)
   
    #simple code to read information from the prokka file to the log file
    with open("~/OptionA_Vincent_Acuesta/Prokka_results/PROKKA_" + str(input) + ".txt") as f:
        with open("log.txt", "a") as f1:
            for line in f:
                f1.write(line)

    return 



"""
at the bottom is what needs to be out of the function for step 7
"""
prokka_input = open("~/OptionA_Vincent_Acuesta/Prokka_results/PROKKA_" + str(input) + ".txt")
values_dict = {}
tRNA = 89
CDS = 4140
hold_tRNA = int(values_dict["tRNA"])
hold_CDS = int(values_dict["CDS"])

#split at the colon in the file
for line in prokka_input:
    a, b = line.strip().split(':')
    values_dict[a.strip()] = b.strip()
    
#step7 of the assignment
def step7(c, d, cx, cy):
    """
    This will be involved with comparing between the annotated prokka .txt file and the refseq to compare the 
    amount between the CDS and the tRNAs
    
    """

    tRNA = 89
    CDS = 4140
    #holds the command to do the today's date
    now = datetime.datetime.now()

    #holds to do the dynamically changing date
    input = ('0'+ '%d' %now.month + '%d' %now.day + '%d' % now.year)

    #gives the file name .txt with the today's date
    prokka_input = open("~/OptionA_Vincent_Acuesta/Prokka_results/PROKKA_" + str(input) + ".txt")


    #works to split the values at the colon and will map these values from the text file which makes this easier
    #the file contains the label and then the colon then the value 'var: value' 
    #Creates a dictionary with the input values 
    #in order to map certain things from the txt file
    values_dict = {}

    #will hold the values from the annotation into int values
    hold_tRNA = int(values_dict["tRNA"])
    hold_CDS = int(values_dict["CDS"])

    #split at the colon in the file
    for line in prokka_input:
        a, b = line.strip().split(':')
        values_dict[a.strip()] = b.strip()
        
        
    #initializes variables for the dif between cds and trna and to store the term less or additional
    #initialize empty
    cds_a = ""
    trna_a = ""
    
    #Holders to count 
    diffc = 0
    diffd = 0
 
#condition to see if the difference between annotation in Prokka or Refseq will either higher or lower when compard
    if c >= cx:
        diffc = c - cx
        #because we made the cds_a above this will fill it with less with the condition is true
        cds_a = "less"
    elif c < cx:
        diffc = cx - c
        #same as stated above
        cds_a = "additional"
    if d >= cy:
        diffd = d - cy
        trna_a = "less"
    elif d < cy:
        diffd = cy - d
        trna_a = "additional"
    return(diffc, diffd, cds_a, trna_a)
    
#step 8 will consis of bowtie2, tophat and cufflinks commands
def get_file ():
    """
    we need the file that is going to run bowtie
    
    """
    input_path= 'wget ftp://ftp.ncbi.nlm.nih.gov/genomes/archive/old_refseq/Bacteria/Escherichia_coli_K_12_substr__MG1655_uid57779/NC_000913.fna '
    os.system(input_path)
    with open('log.txt','a') as output:
        output.write(input_path) 
    return input_path

def build_bowtie():
    """
    this is the first command to build bowtie
    """
    input_this='bowtie2-build NC_000913.fna EcoliK12'
    os.system(input_this)
    return input_this

def run_bowtie():
    
    """
    the last command to run of bowtie2 before you are able to run tophat and this will map 
    the reads and get the index for then tophat to run over the file
    """
    input_this='bowtie2 --quiet -x EcoliK12 -U SRR8185310.fastq -S K12map.sam'
    os.system(input_this)
    return input_this

def run_tophat():
    """
    now that we have the index that was ran through bowtie we can now run tophat through the command
    
    """
    input_this='tophat --no-novel-juncs -o ~/OptionA_Vincent_Acuesta EcoliK12 SRR1411276_1.fastq'
    os.system(input_this)
    return input_this

def run_cufflinks():
    """
    
    this is what we are going to run after tophat for summarize reads and expression
    quanitfication
    """
    input_this='cufflinks -p 2 accepted_hits.bam'
    os.system(input_this)
    return input_this
    
    

make_dir()
letsBegin()
run_spades()
step3()
step4()
run_prokka()
step6()
step7()
CDS_dif, tRNA_dif, CDS_la, tRNA_la = step7(CDS, tRNA, hold_CDS, hold_tRNA)

with open('log.txt','w') as output:
   output.write('These are the differences in CDS and tRNA respectively'+ CDS_dif, CDS_la,+'and'+ tRNA_dif, tRNA_la) 
print("Computing and comparing the 2, Prokka has", CDS_dif, CDS_la, "CDS and", tRNA_dif, tRNA_la, "tRNA than the RefSeq.")

get_file()
build_bowtie()
run_bowtie()
run_tophat()
run_cufflinks()

 
    
    

