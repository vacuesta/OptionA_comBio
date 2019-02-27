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
  
