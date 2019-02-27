# OptionA_comBio
Mini Project

Overview:
Automate the process of taking in illumina reads through a wget file, spades to assemble the genome, prokka to annotate, then utilize bowtie2 to index the reads then tophat and cufflinks to map the reads. There are subsequent steps in the assignment to ask for specific outputs from the file such as reads that are '> 1000'. Everything will be written into a log file that is stated. The automation of this is done using a python wrapper that imports os module in order to call the command lines within the python script. 

Software Dependencies include:
  Linus/Unix
  Python 3+
  
Main Application Parameters:
  This is specified through the wrapper.py in that there are certain commands that have specific parameters that are stated 
  such as when running the spades command.
  
Importing
  Open the Terminal or a Command session:
  git clone https://github.com/vacuesta/OptionA_comBio.git
  
  
Script:
wrapper.py
  Contains all the functions that will be ran sequentially in accordance to the miniproject assignment. There is intensive documentation within the script. It starts with creating a directory then changing into that directory. A wget download will occur taking in a .sra from ncbi. It will go by fastq dump that .sra file in order to get the .fastq file. Then it will run spades for the assembly of the ecoli. After running spades there are subsequent steps that need to occur in the functions in the file that will see the contigs that are greater than 1000 then to concatenate all those together to see the longest sequence. That file will then be put into prokka for annotation. After annotation. The CDS and tRNA will then be compared. Since the amount is given in the miniproject doc, those variables are already declared and it is compared to the annotated file with the CDS and tRNA. After that bowtie2 is ran, following those 2 commands will be tophat to map the reads, then cufflinks will produce the .fpkm file. That final file will go through a parse into a csv with specific headings that are listed.


Input Data:
In order for everything to run consecutively, it needs to work within the directory that is made at the beginning for all of it to work, or else it won't be able to find any of the files. 

Output Data:
At the end this should give you a log.txt file with all the commands and outputs that were wanted in the miniproject such as the .csv file too. 
