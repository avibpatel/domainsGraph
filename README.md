# domainsGraph
Generates a single figure that combines ConSurf, PSIPRED, DISOPRED and PFAM data.

An example of files needed and resulting outputs are provided in the TBP directory.

![Image of Demo](https://github.com/avibpatel/Domains/blob/master/Figures/Demo.png)

## Procedure
Example for human TBP (TATA-box binding protein)

#### Step 1:
- Make a folder on your computer to compile and run domains.py.
- Download domainsGraph.py and copy it into your new folder 

#### Step 2:
- Obtain the sequence of your protein of interest and save it as [TBP.seq](https://github.com/avibpatel/domainsGraph/blob/master/TBP/TBP.seq). 
    - You can obtain this by searching uniprot (https://www.uniprot.org/uniprot/P20226) 

#### Step 3:
Use the downloaded fasta sequence to run: 
- ConSurf (http://consurf.tau.ac.il/)
    - [Select: Amino-Acids, NO, NO, automatically]
    - [Input: Protein seqence (MDQNN....), Job title (TBP), User E-Mail (your.email@some.where)]
    - Download: `Amino Acid Conservation Scores, Confidence Intervals and Conservation Colors` and save at [TBP.grades](https://github.com/avibpatel/domainsGraph/blob/master/TBP/TBP.grades)

- PSIPRED 4.0 and DISOPRED3 (http://bioinf.cs.ucl.ac.uk/psipred/)
    - [Select: PSIPRED 4.0 and DISOPRED3]
    - [Input: Protein seqence (MDQNN....), Job title (TBP), User E-Mail (your.email@some.where)]
    - Download: `SS2 Format Output` and `COMB NN Output` files and rename as [TBP.ss2](https://github.com/avibpatel/domainsGraph/blob/master/TBP/TBP.ss2) and [TBP.comb](https://github.com/avibpatel/domainsGraph/blob/master/TBP/TBP.comb) respectively
    
- PFAM (https://pfam.xfam.org/search/sequence) or (https://www.ebi.ac.uk/Tools/pfa/pfamscan/)
    - [Input: Seqence (MDQNN....) and Output Format > Plain Text]
    - Copy output table: `Significant Pfam-A Matches` and save as a text file called [TBP.txt](https://github.com/avibpatel/domainsGraph/blob/master/TBP/TBP.txt) or download Tool Output `pfamscan-*.output` and save as a text file called TBP.txt
    - Optional: Modify the PFAM file to custom define domains
        - xfam: First column defines domain name and columns 5 and 6 define the limits of that domain.
        - scan: Seventh column defines domain name and columns 4 and 5 define the limits of that domain. 
 
#### Step 4:
- Fragments (Optional: If you want to mark modeled regions)
    - Create a file named [TBP_fragements.txt](https://github.com/avibpatel/domainsGraph/blob/master/TBP/TBP_fragments.txt)
    - List regions you have modeled: `155-333` (from PDB 1CDW)
        - If you have multiple fragment add the ranges in new lines

- Run Domains.py 
    - Open a terminal and navigate to the directory that contains all of the downloaded files
        - You should have the following files: TBP.seq, TBP.grades, TBP.ss2, TBP.comb, TBP.txt, TBP_fragemnts.txt
        - All files should have the same name. You will provide this name (TBP in this case) to Domains.py.  
    - Run Domains.py:

C:\Users\Github_demo\TBP> `py .\Domains.py`

What is the name of the protein: `TBP`

What color do you want the protein to be: `red`

   - There should be 3 new files in your directory: `TBP.pdf`, `TBP.svg` and `TBP_seq.svg`
       - All files are editable in illustrator or any vector art programs. 
       - TBP.pdf is the smallest and easiiest file to work with if you do not plan on editing the figure
       - TBP.svg is the more easily editable version 
       - TBP_seq.svg contains the sequence of TBP embeded into the figure. This can be useful for model building... or showing a zoomed in view of a specific part of your protein. 
       
## Citations

- Consurf (http://consurf.tau.ac.il/credits.php)
- PSIPRED & DISOPRED (http://bioinfadmin.cs.ucl.ac.uk/UCL-CS_Bioinformatics_PSIPRED_citation.html) 
- PFAM (https://pfam.xfam.org/)

    




