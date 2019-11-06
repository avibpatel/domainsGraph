# Domains
Generates a figure that combines ConSurf, PSIPRED, DISOPRED and PFAM data into a single figure that can be easily digested.

An example of files needed and resulting output is provided in the TBP directory.

![Image of TBP](https://github.com/avibpatel/Domains/blob/master/TBP/TBP.png)

## Procedure

#### Step 1:
- Make a folder on your computer to compile and run domains.py.
- Download Domains.py and copy it into your new folder 

#### Step 2:
- Obtain the sequence of your protein of intersest and save it as TBP.seq. 
- You can obtain this by going to uniprot (https://www.uniprot.org/uniprot/P20226). 

#### Step 3:
Use the downloaded fasta sequence run: 
- ConSurf (http://consurf.tau.ac.il/)
    - [Select: Amino-Acids, NO, NO, automatically]
    - [Input: Protein seqence (MDQNN....), Job title (TBP), User E-Mail (your.email@where.something)]
    - Download: `Amino Acid Conservation Scores, Confidence Intervals and Conservation Colors` and save at TBP.grades

- PSIPRED 4.0 and DISOPRED3 (http://bioinf.cs.ucl.ac.uk/psipred/)
    - [Select: PSIPRED 4.0 and DISOPRED3]
    - [Input: Protein seqence (MDQNN....), Job title (TBP), User E-Mail (your.email@where.something)]
    - Download: `SS2 Format Output` and `COMB NN Output` files and rename as TBP.ss2 and TBP.comb respectively
    
- PFAM (https://pfam.xfam.org/search/sequence)
    - [Input: Seqence (MDQNN....)}
    - Copy output table: `Significant Pfam-A Matches` and save as a text file called TBP.txt
    - Optional: Modify the PFAM file to custom define domains
        - Domains.py reads 
 
#### Step 4:
If you want mark certain regions of interst of the protein sequence  

    




