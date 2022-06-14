from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.patheffects as PathEffects

### Inputs ###
protein = input("Whats the name of the protein: ")
seq = protein + '.seq' #input("Path to fasta file of protein seq: ")
grades = protein + '.grades' #input("Path to grades file from consurf: ") 
ss2 = protein + '.ss2' #input("Path to ss2 file from psipred: ")
comb = protein + '.comb' #input("Path to combs file from disopred3: ")
pfam = protein + '.txt' #input("Path to PFAM text file: ")
clr = input("Whats the color do you want the protein to be: ")
show = 'Y' #input("Would you like to include the aa seq and numbering(Y/N)")
frags = protein + '_fragments.txt'

### Setup ###
#(ypos,hieght)
consurf_pos = (1.2,.2)
ss_pos = (1.0,.2)
pfam_pos = (0,1)
charge_pos = (-.2,.2)
hydro_pos = (-.2,.2)
seq_pos = (1.0,.2)

### Sequence ###
sf = open(seq)
sl = sf.readlines()
pseq = ''

for lines in sl:
    line = lines.splitlines()
    if lines[0][0] != '>':
        pseq = pseq + line[0]

### PsiPred ###
sf = open(ss2)
sl = sf.readlines()
helix=[]
sheet=[]
coil=[]
ss=[]
psi=[]

c=0
for line in sl:
    ll=line.split()
    if len(ll) == 6:
        helix.append(float(ll[4]))
        sheet.append(float(ll[5]))
        coil.append(float(ll[3]))
        psi.append([float(ll[3]),float(ll[4]),float(ll[5])])
        c=c+1
aa=c

### Disopred ###
cf = open(comb)
cl = cf.readlines()
disorder=[]

c=1
for line in cl:
    ll=line.split()
    if ll[0] != '#':
        temp=str(c)+'_'+ll[1]
        disorder.append(float(ll[3]))
        c=c+1

### ConSurf ###
gf = open(grades)
gl = gf.readlines()

start = False
conscore=[]

for line in gl:
    ll=line.split()
    if len(ll) > 0 and ll[0] == '1':
        start = True
    if len(ll) == 0:
        start = False
    if start == True:  
        if ll[3][0].find('x') == -1:        
            conscore.append(ll[3][0])
        else: conscore.append('0')

### PFAM ###
pf = open(pfam)
pl = pf.readlines()

plist=[]
for line in pl:
    ll=line.split()
    if len(ll) > 0:
        if ll[0] == 'EMBOSS_001':  
            plist.append([ll[6],int(ll[3]),int(ll[4])])
    if ll[-1] == 'Show':  
        plist.append([ll[0],int(ll[-11]),int(ll[-10])])
        
### Fragments ###
try:
    ff = open(frags)
    fl = ff.readlines() 
    fragls=fl[0].split(',')
except:
    print('No fragments found.')
    fragls=[]

### Colors ###
# ConSurf
c9=(233/255,14/255,139/255)
c8=(238/255,104/255,165/255)
c7=(243/255,154/255,192/255)
c6=(248/255,203/255,223/255)
c5=(255/255,255/255,255/255)
c4=(185/255,228/255,250/255)
c3=(101/255,206/255,245/255)
c2=(28/255,187/255,238/255)
c1=(41/255,171/255,226/255)
c0=(255/255,255/255,0/255)
cl=[c0,c1,c2,c3,c4,c5,c6,c7,c8,c9]

# PsiPred
ph = (102/255,45/255,145/255)
ps = (0/255,104/255,55/255)
pc = (255/255,165/255,32/255)

# AA(hydrophobicity,pKa3,Lesk,MW)
# http://assets.geneious.com/manual/8.0/GeneiousManualsu41.html
# http://www.chem.ucalgary.ca/courses/351/Carey5th/Ch27/ch27-1-4-2.html
# http://www.bioinformatics.nl/~berndb/aacolour.html
# https://www.thermofisher.com/us/en/home/references/ambion-tech-support/rna-tools-and-calculators/proteins-and-amino-acids.html
aad={
    'F' : [1.000,7.0,'green',165.2], 
    'L' : [.943,7.0, 'green', 131.2],
    'I' : [.943,7.0, 'green', 131.2],
    'Y' : [.880,7.0, 'green', 181.2],
    'W' : [.878,7.0, 'green', 204.2],
    'V' : [.825,7.0, 'green', 117.1],
    'M' : [.738,7.0, 'green', 149.2],
    'P' : [.711,7.0, 'green', 115.1],
    'C' : [.680,7.0, 'green', 121.2],
    'A' : [.616,7.0, 'orange', 89.1],
    'G' : [.501,7.0, 'orange', 75.1], 
    'T' : [.450,7.0, 'orange', 119.1],
    'S' : [.359,7.0, 'orange', 105.1],
    'K' : [.283,10.79, 'blue', 146.2],
    'Q' : [.251,7.0, 'magenta', 146.2],
    'N' : [.236,7.0, 'magenta', 132.1],
    'H' : [.165,7.0, 'magenta', 155.2],
    'E' : [.043,4.25, 'red', 147.1],
    'D' : [.028,3.86, 'red', 133.1],
    'R' : [0.000,12.48, 'blue', 174.2]
}

### PLot ###
plt.figure(figsize=(aa/10,5))
plt.ylim((-.5,1.6))
plt.xlim((-25,aa+1))
plt.axis('off')

#consurf
count = 1 
for i in conscore:
    rect = plt.Rectangle((count,consurf_pos[0]),1,consurf_pos[1],alpha=1,fc=(cl[int(i)]))
    plt.gca().add_patch(rect)
    count = count + 1

#psipred 
count = 1 
for i in psi:
    rect = plt.Rectangle((count,ss_pos[0]),1,ss_pos[1],alpha=i[0],fc=pc)
    plt.gca().add_patch(rect)
    rect = plt.Rectangle((count,ss_pos[0]),1,ss_pos[1],alpha=i[1],fc=ph)
    plt.gca().add_patch(rect)
    rect = plt.Rectangle((count,ss_pos[0]),1,ss_pos[1],alpha=i[2],fc=ps)
    plt.gca().add_patch(rect)
    count = count + 1

#disopred
count = 1 
for i in disorder:
    rect = plt.Rectangle((count,ss_pos[0]),1,ss_pos[1],alpha=i,fc='white')
    plt.gca().add_patch(rect)
    count = count + 1

#pfam
count = 1
rect = plt.Rectangle((1,pfam_pos[0]),aa,pfam_pos[1],alpha=.5,fc=clr) 
plt.gca().add_patch(rect)
text = plt.text(-25,.25,protein,horizontalalignment='right',name='Myriad Pro',size='124',weight='1')
for i in plist:
    name=i[0]
    xpos=i[1]
    wide=i[2]-i[1]
    rect = plt.Rectangle((xpos,pfam_pos[0]),wide,pfam_pos[1],alpha=1,fc=clr)
    plt.gca().add_patch(rect)
    text = plt.text(xpos+(wide/2),.333,name,horizontalalignment='center',name='Myriad Pro',size='72',weight='1')
    #text.set_path_effects([PathEffects.withStroke(linewidth=2, foreground='white')])

#hydrophobicity & charge
count = 1
for i in pseq:
    if aad[i][1] > 7.00:
        rect = plt.Rectangle((count,charge_pos[0]),1,charge_pos[1],alpha=((aad[i][1]-7.00)/(12.48-7.00)),fc='blue')
    else: rect = plt.Rectangle((count,charge_pos[0]),1,charge_pos[1],alpha=((7.00-aad[i][1])/(7.00-3.86)),fc='red')
    plt.gca().add_patch(rect)
    if aad[i][0] > .5:
        rect = plt.Rectangle((count,hydro_pos[0]),1,hydro_pos[1],alpha=((aad[i][0]-.5)*2),fc='goldenrod')
    plt.gca().add_patch(rect)
    count = count + 1

'''
#MW
count = 1
for i in pseq:
    rect = plt.Rectangle((count,-.4),1,.2,alpha=((aad[i][3]-75.1)/(204.2-75.1)),fc='black')
    plt.gca().add_patch(rect)
    count = count + 1    
'''

#fragments
for i in fragls:
    nums=i.split('-')
    rect = plt.Rectangle((int(nums[0]),-.3),(int(nums[1])-int(nums[0])),.1,fc='black')
    plt.gca().add_patch(rect)    
    text = plt.text(int(nums[0]),-.65,str(nums[0]),horizontalalignment='left',name='Myriad Pro',size='48',weight='1')
    text = plt.text(int(nums[1]),-.65,str(nums[1]),horizontalalignment='right',name='Myriad Pro',size='48',weight='1')
text = plt.text(aa,1.5,str(aa),horizontalalignment='right',name='Myriad Pro',size='48',weight='1')

plt.savefig(protein + ".svg", transparent=True)
plt.savefig(protein + ".pdf", transparent=True)

#Seq
count = 1
if show == 'Y':
    for i in pseq:
        text = plt.text(count+.5,seq_pos[0]+.09,pseq[count-1],horizontalalignment='center',name='Myriad Pro',size='5',weight='1',color=aad[pseq[count-1]][2])
        text.set_path_effects([PathEffects.withStroke(linewidth=.3, foreground='white')])
        text = plt.text(count+.5,seq_pos[0]+.07,count,horizontalalignment='center',name='Myriad Pro',size='1.5',weight='1',color='black')
        text.set_path_effects([PathEffects.withStroke(linewidth=.15, foreground='white')])
        count = count + 1
    plt.savefig(protein + "_seq.svg", transparent=True)

#plt.show()
