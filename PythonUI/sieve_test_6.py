from tkinter import *
from math import *
import datetime
import csv
import sys
import os.path

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.backends.backend_tkagg
import tkinter.filedialog as fdialog
import tkinter.messagebox as msgbox
import tkinter


sieveGui = Tk()
sieveGui.geometry('500x685')
sieveGui.title(' Sieve Test Program ')

#All the Gui label text.  Names can be changed easily by changing the names in this list. You can add a new label to a column by adding a string to the list here.
row0LabelText = ["    Test Name    ", "    Sieve Weight    ","    Results    ","    Sieve %    ","    Results    "]
column0TestText = ["Date","Time","Name","Source/Line","Comment","6","12","20","30","40","50","70","100","140","200","270","Pan","Combustibles","Test Weight","Total Weight","Difference"]
column3Text = ["AFS Fineness", "AFS_Clay", "Fines","Sieve Total"]
column3CoreSandTest=["          L O I             ","Core Tensile #1    ","Core Tensile #2    ","Core Tensile #3    ","Core Tensile Total"]


#Variables held for calculations
sieve1total = DoubleVar()
sieve2total = DoubleVar()
abstotal = DoubleVar()
differenceVar = DoubleVar()
combusts = DoubleVar()
tensileStrTotal = DoubleVar()
fines = DoubleVar()
fineness = DoubleVar()
afsClay = DoubleVar()
testWeight = 50.0

#Entry Variables
idate=StringVar()
itime=StringVar()
iname=StringVar()
isource=StringVar()
i6=StringVar()
i12=StringVar()
i20=StringVar()
i30=StringVar()
i40=StringVar()
i50=StringVar()
i70=StringVar()
i100=StringVar()
i140=StringVar()
i200=StringVar()
i270=StringVar()
ipan=StringVar()
icombust=StringVar()
icomm=StringVar()
sieve1 = StringVar()
sieve2 = StringVar()
sieve3 = StringVar()
sieve4 = StringVar()
sieve5 = StringVar()
sieve6 = StringVar()
sieve7 = StringVar()
sieve8 = StringVar()
sieve9 = StringVar()
sieve10 = StringVar()
sieve11 = StringVar()
sieve12 = StringVar()
iloi = StringVar()
ict1 = StringVar()
ict2 = StringVar()
ict3 = StringVar()


total = DoubleVar()
r1 = DoubleVar()
r2 = DoubleVar()
r3 = DoubleVar()
r4 = DoubleVar()
r5 = DoubleVar()
r6 = DoubleVar()
r7 = DoubleVar()
r8 = DoubleVar()
r9 = DoubleVar()
r10 = DoubleVar()
r11 = DoubleVar()
r12 = DoubleVar()
ctTotal = DoubleVar()

p1=DoubleVar()
p2=DoubleVar()
p3=DoubleVar()
p4=DoubleVar()
p5=DoubleVar()
p6=DoubleVar()
p7=DoubleVar()
p8=DoubleVar()
p9=DoubleVar()
p10=DoubleVar()

p11=DoubleVar()
p12=DoubleVar()


#Variables put in lists to make loops easier
sieve2Inputs = [sieve1,sieve2,sieve3,sieve4,sieve5,sieve6,sieve7,sieve8,sieve9,sieve10,sieve11,sieve12]
entryInputs = [idate,itime,iname,isource,icomm,i6,i12,i20,i30,i40,i50,i70,i100,i140,i200,i270,ipan,icombust]
ctInputs = [iloi,ict1,ict2,ict3]

#Percent values that will be multiplied
percents = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12]

#Results in furthest right column
results = [r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,ctTotal,fineness,afsClay,fines,total]

def reset():
    for x in percents:
        x = DoubleVar()
    sieve1total.set(0)
    sieve2total.set(0)
    tensileStrTotal.set(0)
    combusts.set(0)
    for x in results:
        x.set(0)

#Saves Data after submit button is pressed
def submit():
    reset()
    for x in sieve2Inputs:
        if isreal(x.get()):
            sieve2total.set(sieve2total.get() + float(x.get()))
        else:
            x.set("0")
    for x in entryInputs[5:17]:
        if isreal(x.get()):
            sieve1total.set(sieve1total.get() + float(x.get()))
        else:
            x.set("0")
            
    updatePercentResults(sieve1total.get(),sieve2total.get())
    totalLabel = Label(sieveGui,text = "%.2f"%abstotal.get(),bg = "black",fg = "white").grid(row = 20,sticky=W+E,column = 2,padx = 3) #displays total at bottom of screen

    testLabel = Label(sieveGui,text = "%.2f"%testWeight,bg="black",fg="white").grid(row = 19,sticky = W+E, column = 2,padx = 3)
    
    differenceVar.set(testWeight - abstotal.get())
    
    afsClay.set(2*differenceVar.get())
    diffLabel = Label(sieveGui,text = "%.2f"%differenceVar.get(),bg = "black",fg="white").grid(row=21,column = 2,padx=3,sticky=W+E)
    
    if isreal(icombust.get()):
        combusts.set(float(icombust.get()))
        combustLabel = Label(sieveGui,text = "%.2f"%combusts.get(), bg = "black",fg="white").grid(row=18,column=2,padx=3,sticky=W+E)
    else:
        combusts.set(0)
        combustLabel = Label(sieveGui,text = "0.00", bg = "black",fg="white").grid(row=18,column=2,padx=3,sticky=W+E)
    calcResults(sieve1total.get(),sieve2total.get())
    fineslabel = Label(text = "%.2f"%fines.get(),bg="black",fg="white").grid(row = 3, column  = 4, padx = 3,sticky=W+E)
    calcFineness()
    afslabel = Label(text = "%.2f"%afsClay.get(),bg = "black", fg="white").grid(row=2, column = 4, padx = 3,sticky=W+E)
    finenesslabel = Label(text = "%.2f"%fineness.get(),bg = "black", fg="white").grid(row=1, column = 4, padx = 3,sticky=W+E)
    coreTestCalc()
    writeFile()
    drawPlot()

def coreTestCalc():
    for x in ctInputs[1:4]:
        if isreal(x.get()):
            tensileStrTotal.set(tensileStrTotal.get() + float(x.get()))
        else:
            x.set("0")
    tensileStrTotal.set(tensileStrTotal.get()*2)
    tensileLabel = Label(sieveGui,text = "%.2f"%tensileStrTotal.get(),bg="black",fg="white").grid(row = 23, column = 4,padx=3, sticky=W+E)
        

    
#Calculates Percent weight in sieve compared to the total and updates labels
def updatePercentResults(total1,total2):
    for x in range(6,18):
        sieveLabel = Label(sieveGui, text = "", bg="black",fg = "white").grid(row = x, column = 2,padx = 3, sticky=W+E)
        sieveLabel = Label(sieveGui, text="",bg = "black",fg="white").grid(row=x,column=4,sticky=W+E,padx=3)
    if total2 == 0 and total1 != 0:
        abstotal.set(total1)
        for x in range(5,17):
            if(isreal(entryInputs[x].get())):
                percents[x-5].set((float(entryInputs[x].get())/float(total1))*100.0)
                sievelabel = Label(sieveGui, text = "%.2f" % percents[x-5].get(), bg = "black", fg = "white")
                sievelabel.grid(row = x+1, column = 2,padx = 3,sticky=W+E)
    elif total1 == 0 and total2 !=0:
        abstotal.set(total2)
        for x in range(0,12):
            if(isreal(sieve2Inputs[x].get())):
                percents[x].set((float(sieve2Inputs[x].get())/float(total2))*100.0) 
                sievelabel = Label(sieveGui, text = "%.2f" % percents[x].get(), bg = "black", fg = "white")
                sievelabel.grid(row = x+6, column = 2,padx = 3,sticky=W+E)
    elif total1 != 0 and total2 != 0:
        for x in percents:
            x.set(0)

#Checks that a string can be casted to a float
def isreal(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

#Calculates the results in the furthest right column and prints labels
def calcResults(total1,total2):
    for x in range(6,18):
        sievelabel = Label(sieveGui,text = "", bg="black",fg="white").grid(row=x,column=4,sticky = W+E)
    if (total2 != 0 and total1 == 0) or  (total1!=0 and total2==0):
        results[0].set(percents[0].get() * 3)
        results[1].set(percents[1].get() * 5)
        results[2].set(percents[2].get() * 10)
        results[3].set(percents[3].get() * 20)
        results[4].set(percents[4].get() * 30)
        results[5].set(percents[5].get() * 40)
        results[6].set(percents[6].get() * 50)
        results[7].set(percents[7].get() * 70)
        results[8].set(percents[8].get() * 100)
        results[9].set(percents[9].get() * 140)
        results[10].set(percents[10].get() * 200)
        results[11].set(percents[11].get() * 300)
    counter = 6
    for x in results:
        if x.get() != 0 and counter != 20:
            sievelabel = Label(sieveGui, text = "%.2f" % results[counter-6].get(),bg = "black", fg = "white").grid(row = counter,padx=3, column=4,sticky=W+E)
        counter+=1
    fines.set(percents[9].get() + percents[10].get() + percents[11].get())

def calcFineness():
    resultsTotal = 0
    for x in results:
        resultsTotal+=x.get()
    percentTotal = 0
    for x in percents:
        percentTotal += x.get()
    if percentTotal!=0:
        fineness.set(resultsTotal/percentTotal)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
def writeFile():
    fields = ['Date','Time','Technician Name','Line/Source','%6','%12','%20','%30','%40','%50','%70','%100','%140','%200','%270','%Pan','AFS Fineness','AFS_Clay','Fines','6 Results','12 Results','20 Results','30 Results','40 Results','50 Results','70 Results','100 Results','140 Results','200 Results','270 Results','Pan Results']
    if os.path.isfile('MetLabSieveReport.csv') == False:
        with open('MetLabSieveReport.csv','a') as csvfile:
            filewriter = csv.DictWriter(csvfile,fieldnames= fields)
            filewriter.writeheader()
            csvfile.close()
    csvfile =  open('MetLabSieveReport.csv','a')
    filewriter = csv.DictWriter(csvfile,fieldnames = fields)
    fields = {fields[0]:idate.get(),fields[1]:itime.get(),fields[2]:iname.get(),fields[3]:isource.get(),fields[4]:str(percents[0].get()),fields[5]:str(percents[1].get()),fields[6]:str(percents[2].get()),fields[7]:str(percents[3].get()),fields[8]:str(percents[4].get()),fields[9]:str(percents[5].get()),fields[10]:str(percents[6].get()),fields[11]:str(percents[7].get()),fields[12]:str(percents[8].get()),fields[13]:str(percents[9].get()),fields[14]:str(percents[10].get()),fields[15]:str(percents[11].get()),fields[16]:str(results[13].get()),fields[17]:str(results[14].get()),fields[18]:str(results[15].get()),fields[19]:str(results[0].get()),fields[20]:str(results[1].get()),fields[21]:str(results[2].get()),fields[22]:str(results[3].get()),fields[23]:str(results[4].get()),fields[24]:str(results[5].get()),fields[25]:str(results[6].get()),fields[26]:str(results[7].get()),fields[27]:str(results[8].get()),fields[28]:str(results[9].get()),fields[29]:str(results[10].get()),fields[30]:str(results[11].get())}
    filewriter.writerow(fields)
    csvfile.close()
        
def drawPlot():
    x = [10,20,30,40,50,60,70,80,90,100,110,120]
    y = [percents[0].get(),percents[1].get(),percents[2].get(),percents[3].get(),percents[4].get(),percents[5].get(),percents[6].get(),percents[7].get(),percents[8].get(),percents[9].get(),percents[10].get(),percents[11].get()]
    plt.plot(x, y)
    labels = ['6','12','20','30','40','50','70','100','140','200','270','PAN']
    plt.axis([0,120,0,60])
    plt.grid(True)
    plt.xticks(x,labels)
    plt.margins (0.2)
    plt.show()
            
#Instantiates row 0 column labels
counter = 0
for x in row0LabelText:
    sievelabel = Label(sieveGui,text = x,  bg = "blue", fg = "white")
    sievelabel.grid(row = 0,column = counter, sticky = W+E, pady=2)
    counter+=1

#Instantiates column 1 Test Labels
counter  = 1
for x in column0TestText:
    sievelabel = Label(sieveGui,text = x, bg = "orange", fg = "black")
    sievelabel.grid(row = counter, column = 0, pady = 2, sticky = W+ E)
    counter+=1

#Instantiates column 1 Entries
counter = 0
for x in entryInputs:
    ent = Entry(sieveGui,width = 8, textvariable = entryInputs[counter], bg = "white")
    if(counter<5):
        ent.grid(row = counter+1, column=1, sticky = W+E,columnspan = 2,padx = 3)
    else:
        ent.grid(row = counter+1, column=1, sticky = W+E,padx=3)
    counter += 1

#Instantiates column 2 Entries
for x in range(5,len(entryInputs)+3):
    sievelabel = Label(sieveGui,text = " ", bg = "black", fg = "white")
    sievelabel.grid(row = x+1, column  = 2, sticky = W + E,padx = 3)

#Instatiates column 3 Sieve %'s Labels and entries
    counter = 1
for x in column3Text:
    sievelabel = Label(sieveGui,text = x,bg = "orange")
    sievelabel.grid(column = 3, row = counter, sticky = W + E)
    counter += 1
counter = 6
for x in sieve2Inputs:
    sievelabel = Entry(sieveGui,textvariable = x, bg = "white", fg = "black")
    sievelabel.grid(row = counter, column  = 3, sticky = W + E)
    counter+=1

counter = 19
for x in column3CoreSandTest:
    sievelabel = Label(sieveGui,text = x, bg= "orange",fg="black").grid(row = counter, column = 3,sticky=W,pady=2)
    counter+=1
    
coreTestLabel = Label(sieveGui,text = "Core Tensile Test",bg = "blue", fg = "white").grid(column = 3, row = 18,sticky=W+E,columnspan=2)
    
#Instantiates column 4 Results and entries
for x in range(1,len(column0TestText)-3):
    if x==5:
        sievelabel = Label(sieveGui, text = "Core Sand Sieve",bg = "blue",fg="white")
        sievelabel.grid(row = x,column=3,sticky=W+E,columnspan = 2)
    else:
        sievelabel = Label(sieveGui, text = " ", bg = "black",fg = "white")
        sievelabel.grid(row = x, column = 4, sticky = W + E,padx = 3)

counter = 19
for x in ctInputs:
    ctEntry = Entry(sieveGui, textvariable = x).grid(row = counter,column = 4)
    counter+=1

tensileTotalLabel = Label(sieveGui,text="",bg="black",fg="white").grid(row=23,sticky=W+E,column=4)

#Submit Button layout at bottom of window
emptylabel=Label(sieveGui).grid(row=22)
emptylabel=Label(sieveGui).grid(row=23)
emptylabel=Label(sieveGui).grid(row=24)
emptylabel=Label(sieveGui).grid(row=25)

fileButton = Button(sieveGui, text = "FILE SIEVE",command = submit,bg="orange")
fileButton.grid(row = 26, column = 1,columnspan=3,sticky=W+E)


                    
sieveGui. mainloop()



