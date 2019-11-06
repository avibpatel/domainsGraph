# Domains
Generates a figure that combines ConSurf, PSIPRED, DISOPRED and PFAM data into a single figure that can be easily digested.

An example of files needed and resulting output is provided in the TBP directory.

![Image of TBP](https://github.com/avibpatel/Domains/blob/master/TBP/TBP.png)

##Procedure

####Step 1:
Make a folder on your computer to compile and run domains.py.
Download Domains.py and copy it into your new folder 

####Step 2:
Obtain the sequence of your protein of intersest and save it as TBP.seq. 
You can obtain this by going to uniprot (https://www.uniprot.org/uniprot/P20226). 

`cat TBP.seq`

>\>sp|P20226|TBP_HUMAN TATA-box-binding protein OS=Homo sapiens OX=9606 GN=TBP PE=1 SV=2\
>MDQNNSLPPYAQGLASPQGAMTPGIPIFSPMMPYGTGLTPQPIQNTNSLSILEEQQRQQQ
>QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQAVAAAAVQQSTSQQATQGTSGQAPQ
>LFHSQTLTTAPLPGTTPLYPSPMTPMTPITPATPASESSGIVPQLQNIVSTVNLGCKLDL
>KTIALRARNAEYNPKRFAAVIMRIREPRTTALIFSSGKMVCTGAKSEEQSRLAARKYARV
>VQKLGFPAKFLDFKIQNMVGSCDVKFPIRLEGLVLTHQQFSSYEPELFPGLIYRMIKPRI
>VLLIFVSGKVVLTGAKVRAEIYEAFENIYPILKGFRKTT

####Step 3:
Using the downloaded sequence run: 
ConSurf (http://consurf.tau.ac.il/)
[Select: Amino-Acids, NO, NO, automatically]
[Input: Protein seqence (MDQNN....), Job title (TBP), User E-Mail (your.email@where.something)]

Download: `Amino Acid Conservation Scores, Confidence Intervals and Conservation Colors` and save at TBP.grades

>	 Amino Acid Conservation Scores
>	===============================
>
>- POS: The position of the AA in the SEQRES derived sequence.
>- SEQ: The SEQRES derived sequence in one letter code.
>- SCORE: The normalized conservation scores.
>- COLOR: The color scale representing the conservation scores (9 - conserved, 1 - variable).
>- CONFIDENCE INTERVAL: When using the bayesian method for calculating rates, a confidence interval is assigned to each of the inferred evolutionary conservation scores.
>- CONFIDENCE INTERVAL COLORS: When using the bayesian method for calculating rates. The color scale representing the lower and upper bounds of the confidence interval.
>- B/E: Burried (b) or Exposed (e) residue.
>- FUNCTION: functional (f) or structural (s) residue (f - highly conserved and exposed, s - highly conserved and burried).
>- MSA DATA: The number of aligned sequences having an amino acid (non-gapped) from the overall number of sequences at each position.
>- RESIDUE VARIETY: The residues variety at each position of the multiple sequence alignment.
>
> POS	 SEQ	SCORE		COLOR	CONFIDENCE INTERVAL	CONFIDENCE INTERVAL COLORS	B/E	FUNCTION	MSA DATA	RESIDUE VARIETY
    	    	(normalized)	        	               
>   1	   M	-0.797		  9	-0.926,-0.774			    9,9			  e	       f	   8/150	M
>   2	   D	 0.059		  5*	-0.510, 0.400			    7,3			  e	        	   9/150	E,D
>   3	   Q	 0.062		  5*	-0.510, 0.400			    7,3			  e	        	   9/150	V,E,Q
>   4	   N	 0.318		  3*	-0.262, 0.723			    6,1			  e	        	   9/150	E,D,N
>   5	   N	 0.599		  2*	-0.147, 1.246			    



PSIPRED 4.0 and DISOPRED3 (http://bioinf.cs.ucl.ac.uk/psipred/)
PFAM (https://pfam.xfam.org/search/sequence)




