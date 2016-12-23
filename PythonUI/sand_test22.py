from tkinter import*

# Sand Testing Program
# used in Sand Analysis of Molding Sand
# for the Alburtis and Forks Facilities.
# Current Version 0.2.0

# Definitions are as Follows:

# Sand Test Program 

from math import *
import sys
import datetime
import csv
import os.path

sandGui = Tk()
sandGui.geometry('400x650')
sandGui.title(' Sand Test Program ')

def quit():
    quit()

def hello():
    print ("hello!")

menubar = Menu(sandGui)

# create a pulldown menu, and add to it

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Sand_Test",command=hello)
filemenu.add_command(label="Seive_Test",command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=quit)
menubar.add_cascade(label="File",menu=filemenu)

#-------------------------------Definition ---------------------------------------------------


idate = StringVar() # In_Date
itime = StringVar() # In_Time
ijob = StringVar() # In_Job
iline = StringVar() # In_Line 
iident = StringVar() # In_Initials
itemp = StringVar() # In_Sand Temp
imoist = StringVar() # In_Moisture
icomp = StringVar() # In_Compactability
igrstr = StringVar() # In_Green Strengtht
ispec = StringVar()# In_Specimen Weight
iperm = StringVar()# In_Permeability
imbc = StringVar()# In_Methylene Blue Clay
icomm = StringVar()# In_Comment
odate = StringVar() # Out_Date
otime = StringVar() # Out_Time
ojob = StringVar() # Out_Job
oline = StringVar() # Out_Line 
oident = StringVar() # Out_Initials
otemp = StringVar() # Out_Sand Temp
omoist = StringVar() # Out_Moisture
ocomp = StringVar() # Out_Compactability
ogrstr = StringVar() # Out_Green Strengtht
ospec = StringVar()# Out_Specimen Weight
operm = StringVar()# Out_Permeability
ombc = StringVar()# Out_Methylene Blue Clay
ocomm = StringVar()# Out_Comment



#-----------------------Column 0 ------------------------------------------------------------
sandlabel1 =Label(text = ' Test Name ',fg='white',bg='blue').grid(row=0,column=0,sticky=W+E, pady=5) #Header

sandlabel2 =Label(text = ' Date ',fg='black',bg='orange').grid(row=1,column=0, sticky=W+E, pady=5)
sandlabel3 =Label(text = ' Time ',fg='black',bg='orange').grid(row=2,column=0,sticky=W+E, pady=5)
sandlabel4 =Label(text = ' Job ',fg='black',bg='orange').grid(row=3,column=0,sticky=W+E, pady=5)
sandlabel5 =Label(text = ' Line # ',fg='black',bg='orange').grid(row=4,column=0,sticky=W+E, pady=5)
sandlabel6 =Label(text = ' Initials.',fg='black',bg='orange').grid(row=5,column=0,sticky=W+E, pady=5)
sandlabel7 =Label(text = ' Sand Temp. ',fg='black',bg='orange').grid(row=6,column=0,sticky=W+E, pady=5)
sandlabel8 =Label(text = ' Moisture ',fg='black',bg='orange').grid(row=7,column=0,sticky=W+E, pady=5)
sandlabel9 =Label(text = ' Compactability ',fg='black',bg='orange').grid(row=8,column=0,sticky=W+E, pady=5)
sandlabel10 =Label(text = ' Green Strength ',fg='black',bg='orange').grid(row=9,column=0,sticky=W+E, pady=5)
sandlabel11 = Label(text = ' Specimen Weight ',fg='black',bg='orange').grid(row=10,column=0,sticky=W+E, pady=5)
sandlabel12 = Label(text = ' Permeability ',fg='black',bg='orange').grid(row=11,column=0,sticky=W+E, pady=5)
sandlabel13 = Label(text = ' Meth. Blue Clay ',fg='black',bg='orange').grid(row=12,column=0,sticky=W+E, pady=5)
sandlabel14 = Label(text = ' Comment ',fg='black',bg='orange').grid(row=13,column=0,sticky=W+E, pady=5)




sandlabel115 = Label(text = ' Test Normal ',fg='black',bg='green').grid(row=17,column=0,sticky=W+E, pady=5)#Status_Bar, Green
sandlabel116 = Label(text = ' Outside Control Range ',fg='black',bg='yellow').grid(row=18,column=0,sticky=W+E, pady=5)#Status_Bar, Yellow
sandlabel117 = Label(text = ' Outside Operating Range',fg='black',bg='red').grid(row=19,column=0,sticky=W+E, pady=5)#Status_Bar, Red

#----------------------------Column 1 -------------------------------------------------------------------------------

sandlabel80 =Label(text = ' Enter Value ',fg='white',bg='blue').grid(row=0,column=1,sticky=W+E, pady=5)#Header


date_entry = Entry(sandGui,width=10,textvariable=idate, bg='white').grid(row=1, column=1, sticky=W+E) # Date
time_entry = Entry(sandGui,width=10,textvariable=itime, bg='white').grid(row=2, column=1, sticky=W+E) # Time
job_entry = Entry(sandGui,width=10,textvariable=ijob, bg = 'white').grid(row=3, column=1, sticky=W+E) # job
line_entry = Entry(sandGui,width=10,textvariable=iline, bg='white').grid(row=4, column=1, sticky=W+E) # Line Number
ident_entry = Entry(sandGui,width=10,textvariable=iident, bg ='white').grid(row=5, column=1, sticky=W+E) # Initials
temp_entry = Entry(sandGui,width=10,textvariable=itemp, bg ='white').grid(row=6, column=1, sticky=W+E) # Sand Temperature
moist_entry = Entry(sandGui,width=10,textvariable=imoist, bg ='white').grid(row=7, column=1, sticky=W+E) # Moisture
comp_entry = Entry(sandGui,width=10,textvariable=icomp, bg = 'white').grid(row=8, column=1, sticky=W+E) # Compactability
grstr_entry = Entry(sandGui,width=10,textvariable=igrstr, bg = 'white').grid(row=9, column=1, sticky=W+E) # Green Strength
spec_entry = Entry(sandGui,width=10,textvariable=ispec, bg = 'white').grid(row=10, column=1, sticky=W+E) # Specimen Weight
perm_entry = Entry(sandGui,width=10,textvariable=iperm, bg='white').grid(row=11, column=1, sticky=W+E) # Permeability
mbc_entry = Entry(sandGui,width=10,textvariable=imbc, bg='white').grid(row=12, column=1, sticky=W+E) # Methylene Blue Clay
comm_entry = Entry(sandGui,width=10,textvariable=icomm, bg='white').grid(row=13, column=1, sticky=W+E) # Comments




#---------------------------------------------Column 3 --------------------------------------------------



#--------------------------------------------Column 4 Stuff---------------------------------------------------------------
sandlabel100 =Label(text = ' Test ',fg='white',bg='blue').grid(row=0,column=4,sticky=W+E, pady=5) #Header

sandlabel101 =Label(text = ' Date ',fg='white',bg='brown').grid(row=1,column=4, sticky=W+E, pady=5)
sandlabel102 =Label(text = ' Time ',fg='white',bg='brown').grid(row=2,column=4,sticky=W+E, pady=5)
sandlabel103 =Label(text = ' Job ',fg='white',bg='brown').grid(row=3,column=4,sticky=W+E, pady=5)
sandlabel104 =Label(text = ' Sand Temp. ',fg='white',bg='brown').grid(row=4,column=4,sticky=W+E, pady=5)
sandlabel105 =Label(text = ' Moisture',fg='white',bg='brown').grid(row=5,column=4,sticky=W+E, pady=5)
sandlabel106 =Label(text = ' Compactability ',fg='white',bg='brown').grid(row=6,column=4,sticky=W+E, pady=5)
sandlabel107 =Label(text = ' Green Strength ',fg='white',bg='brown').grid(row=7,column=4,sticky=W+E, pady=5)
sandlabel108 =Label(text = ' Specimen Weight ',fg='white',bg='brown').grid(row=8,column=4,sticky=W+E, pady=5)
sandlabel109 =Label(text = ' Permeability ',fg='white',bg='brown').grid(row=9,column=4,sticky=W+E, pady=5)
sandlabel113 =Label(text = ' Meth. Blue Clay',fg='white',bg='brown').grid(row=10,column=4,sticky=W+E, pady=5)
sandlabel110 =Label(text = ' M.C.C ',fg='white',bg='brown').grid(row=11,column=4,sticky=W+E, pady=5)
sandlabel111 =Label(text = ' GS. M.C. ',fg='white',bg='brown').grid(row=12,column=4,sticky=W+E, pady=5)
sandlabel112 =Label(text = ' GS. C. C. ',fg='white',bg='brown').grid(row=13,column=4,sticky=W+E, pady=5)
sandlabel116 =Label(text = ' R-Factor ',fg='white',bg='brown').grid(row=14,column=4,sticky=W+E, pady=5)
sandlabel117 =Label(text = ' Available Bond ',fg='white',bg='brown').grid(row=15,column=4,sticky=W+E, pady=5)
sandlabel118 =Label(text = ' Working Bond ',fg='white',bg='brown').grid(row=16,column=4,sticky=W+E, pady=5)
sandlabel119 =Label(text = ' Mulling Efficiency ',fg='white',bg='brown').grid(row=17,column=4,sticky=W+E, pady=5)
sandlabel120 =Label(text = ' Green Str. Eff.',fg='white',bg='brown').grid(row=18,column=4,sticky=W+E, pady=5)
sandlabel121 =Label(text = ' Compact Eff. ',fg='white',bg='brown').grid(row=19,column=4,sticky=W+E, pady=5)
sandlabel122 =Label(text = ' % Moist / Clay ',fg='white',bg='brown').grid(row=20,column=4,sticky=W+E, pady=5)
sandlabel114 =Label(text = ' Initials ',fg='white',bg='brown').grid(row=21,column=4,sticky=W+E, pady=5)          
sandlabel115 =Label(text = ' comment ',fg='white',bg='brown').grid(row=22,column=4,sticky=W+E, pady=5)

#----------------------------------------------Column 5 --------------------------------------------------------------
           
sandlabel130 =Label(text = ' Final Results ',fg='white',bg='blue').grid(row=0,column=5,sticky=W+E, pady=5)#Header



#------------------------------------------------def Clear,------------------------------------------------------------------

def centery(*args):
    idate.set("")
    itime.set("")
    ijob.set("")
    iline.set("")
    iident.set("")
    itemp.set("")
    imoist.set("")
    icomp.set("")
    igrstr.set("")
    ispec.set("")
    iperm.set("")
    imbc.set("")
    icomm.set("")
    
#------------------------------------------------def Evaluate, Column 6 ------------------------------------------------------

def evaluate(*args):
    now = datetime.datetime.now()
    odate = idate.get()
    sandlabel171 = Label(sandGui,text = odate,fg='black',bg='white').grid(row=1,column=5,sticky=W+E, pady=5) # Final Result, Date
    otime = str(itime.get())
    sandlabel172 = Label(sandGui,text = otime,fg='black',bg='white').grid(row=2,column=5,sticky=W+E, pady=5) # Time
    ojob = str(ijob.get())
    sandlabel173 = Label(sandGui,text = ojob,fg='black',bg='white').grid(row=3,column=5,sticky=W+E, pady=5) # Job
    oline = str(iline.get())
    oident = str(iident.get())
    sandlabel184 = Label(sandGui,text = oident,fg='black',bg='white').grid(row=21,column=5,sticky=W+E, pady=5) # Initials
    
    otemp = float(itemp.get())
    # Sand Temperature
    if (otemp >= 90.0) and (otemp <=130.0): sandlabel274 = Label(text = otemp,fg='black',bg='green').grid(row=4,column=5,sticky=W+E, pady=5)
    elif (otemp >= 70.0) and (otemp <=155.0): sandlabel274 = Label(text=otemp,fg='black',bg='yellow').grid(row=4,column=5,sticky=W+E, pady=5)
    else: sandlabel274 = Label(text=otemp,fg='black',bg='red').grid(row=4,column=5,sticky=W+E, pady=5)
    
    omoist = float(imoist.get())
    # Moisture
    if (omoist >= 2.8) and (omoist <=3.4): sandlabel275 = Label(text=omoist,fg='black',bg='green').grid(row=5,column=5,sticky=W+E, pady=5)
    elif (omoist >= 2.0) and (omoist <=5.0): sandlabel275 = Label(text=omoist,fg='black',bg='yellow').grid(row=5,column=5,sticky=W+E, pady=5)
    else: sandlabel275 = Label(text=omoist,fg='black',bg='red').grid(row=5,column=5,sticky=W+E, pady=5)
    
    ocomp = float(icomp.get())
    # Compactability
    if (ocomp >= 35.0) and (ocomp <=42.0): sandlabel276 = Label(text = ocomp,fg='black',bg='green').grid(row=6,column=5,sticky=W+E, pady=5)
    elif (ocomp >= 28.0) and (ocomp <=52.0): sandlabel276 = Label(text = ocomp,fg='black',bg='yellow').grid(row=6,column=5,sticky=W+E, pady=5)
    else: sandlabel276 = Label(text = ocomp,fg='black',bg='red').grid(row=6,column=5,sticky=W+E, pady=5)
    
    ogrstr = float(igrstr.get())
    # Green Strength
    if (ogrstr >= 23.0) and (ogrstr <=33.0): sandlabel276 = Label(text= ogrstr,fg='black',bg='green').grid(row=7,column=5,sticky=W+E, pady=5)
    elif (ogrstr >= 18.0) and (ogrstr <=38.0): sandlabel276 = Label(text= ogrstr,fg='black',bg='yellow').grid(row=7,column=5,sticky=W+E, pady=5)
    else: sandlabel276 = Label(text= ogrstr,fg='black',bg='red').grid(row=7,column=5,sticky=W+E, pady=5)
    
    ospec = float(ispec.get())
    # Specimen Weight
    if (ospec>= 140.0) and (ospec <=150.0): sandlabel276 = Label(text = ospec,fg='black',bg='green').grid(row=8,column=5,sticky=W+E, pady=5)
    elif (ospec >= 139.0) and (ospec <=160.0): sandlabel276 = Label(text = ospec,fg='black',bg='yellow').grid(row=8,column=5,sticky=W+E, pady=5)
    else: sandlabel276 = Label(text = ospec,fg='black',bg='red').grid(row=8,column=5,sticky=W+E, pady=5)
    
    operm = float(iperm.get())
   # Permeability
    if (operm>= 60.0) and (operm <=90.0): sandlabel276 = Label(text= operm,fg='black',bg='green').grid(row=9,column=5,sticky=W+E, pady=5)
    elif (operm >= 30.0) and (operm <=100.0): sandlabel276 = Label(text= operm,fg='black',bg='yellow').grid(row=9,column=5,sticky=W+E, pady=5)
    else: sandlabel276 = Label(text= operm,fg='black',bg='red').grid(row=9,column=5,sticky=W+E, pady=5)
    
    ombc = float(imbc.get())
    # MBC
    if (ombc>= 8.5) and (ombc <=10.5): sandlabel276 = Label(text= ombc,fg='black',bg='green').grid(row=10,column=5,sticky=W+E, pady=5)
    elif (ombc >= 7.0) and (ombc <=14.0): sandlabel276 = Label(text= ombc,fg='black',bg='yellow').grid(row=10,column=5,sticky=W+E, pady=5)
    else: sandlabel276 = Label(text= ombc,fg='black',bg='red').grid(row=10,column=5,sticky=W+E, pady=5)
    
    ocomm = str(icomm.get())
    sandlabel185 = Label(sandGui,text = ocomm,fg='black',bg='white').grid(row=22,column=5,sticky=W+E, pady=5) # Comment
    
    MCC = omoist * exp(2.1463 - ( .3807 * log (ocomp)))
   
    sandlabel180 = Label(sandGui,text =round(MCC, 2),fg='black',bg='white').grid(row=11,column=5,sticky=W+E, pady=5) # MCC, test status
    
    GSMC = exp((log((ogrstr) * omoist * .4343 * log (ocomp)) - .81238)/ 2.0875)
    
    sandlabel181 = Label(sandGui,text = round(GSMC,2),fg='black',bg='white').grid(row=12,column=5,sticky=W+E, pady=5) # GSMC, test status
    
    GSCC = exp(((log(ogrstr) + log(.4343 * log(ocomp))) - log(exp(2.1463 - .3807 * log(ocomp))) - .81075)/ 1.0875)
   
    sandlabel182 = Label(sandGui,text = round(GSCC,2),fg='black',bg='white').grid(row=13,column=5,sticky=W+E, pady=5) # GSCC, test status

    Rfac = (ombc/omoist)
    
    sandlabel186 = Label(sandGui,text = round(Rfac,2) ,fg='black',bg='white').grid(row=14,column=5,sticky=W+E, pady=5) # R-Factor, test status

    Ab = (1.316 * omoist) + (.105 * ogrstr)
    
    sandlabel187 = Label(sandGui,text = round(Ab,2),fg='black',bg='white').grid(row=15,column=5,sticky=W+E, pady=5) # Available Bond, test status

    Wkb = (15.29 * ogrstr)/(129.7 - ocomp)
    
    sandsandlabel188 = Label(sandGui,text = round(Wkb,2),fg='black',bg='white').grid(row=16,column=5,sticky=W+E, pady=5) # Working Bond, test status
       
    Me = (100 * Wkb)/Ab
    
    sandlabel189 = Label(sandGui,text = round(Me,2),fg='black',bg='white').grid(row=17,column=5,sticky=W+E, pady=5) # Mulling Efficiency, test status

    Gse = ogrstr /(exp(2.0879 * log(ombc) + .8125 - log(ombc / (exp(2.5195 - .3807 * log(ocomp))))- log(.4343 * log(ocomp))))*100
    
    sandlabel190 = Label(sandGui,text = round(Gse,2),fg='black',bg='white').grid(row=18,column=5,sticky=W+E, pady=5) # Green Strength Efficiency, test status

    Ce = 100 * ombc/exp(2.0879 * log(ombc + .8125 - log(ombc/exp(2.5195 - .3807 * log (ocomp))) - log(.4343 * log(ocomp))))
    
    sandlabel191 = Label(sandGui,text = round(Ce,2),fg='black',bg='white').grid(row=19,column=5,sticky=W+E, pady=5) # Compactability Efficiency, test status

    Cm = (1 / Rfac) * 100   
    
    sandlabel192 = Label(sandGui,text = round(Cm,2),fg='black',bg='white').grid(row=20,column=5,sticky=W+E, pady=5) # % Moisture / Clay, test status

    omcc = round(MCC,2)
    ogsmc = round(GSMC,2)
    ogscc = round(GSCC,2)
    orfac = round(Rfac,2)
    oab = round(Ab,2)
    owkb = round(Wkb,2)
    ome = round(Me,2)
    ogse = round(Gse,2)
    oce = round(Ce,2)
    ocm = round(Cm,2)
    
    

#----------------------------------------define print function and csv printout--------------------------------------------------------------------------
    writeFile()
    idate.set("")
    itime.set("")
    ijob.set("")
    iline.set("")
    iident.set("")
    itemp.set("")
    imoist.set("")
    icomp.set("")
    igrstr.set("")
    ispec.set("")
    iperm.set("")
    imbc.set("")
    icomm.set("")


#File Writing Function -- called in evaluate
def writeFile():
    fields = ['Date','Time','Job','Temp','Moisture','Comp. Str', 'Green Str.','Spec. Weight','Comment']
    if os.path.isfile('MetLabSieveReport.csv') == False:
        with open('MetLabSandReport.csv','a') as csvfile:
            filewriter = csv.DictWriter(csvfile,fieldnames= fields)
            filewriter.writeheader()
            csvfile.close()
    csvfile =  open('MetLabSandReport.csv','a')
    filewriter = csv.DictWriter(csvfile,fieldnames = fields)
    fields = {fields[0]:idate.get(),fields[1]:itime.get(),fields[2]:ijob.get(),fields[3]:itemp.get(),fields[4]:imoist.get(),fields[5]:icomp.get(),fields[6]:igrstr.get(),fields[7]:ispec.get(),fields[8]:icomm.get()}
    filewriter.writerow(fields)
    csvfile.close()

  #---------------------------Control Buttons Column 7 ----------------------------------------------------------------------------------------------

# Control Definitions, buttons

calcbutton = Button(sandGui, text ="Calc",command=evaluate,fg='white', bg='blue').grid(row=17,column=1, sticky=W+E,columnspan=2) # Calculate

clrbutton = Button(sandGui, text ="Clear",command=centery,fg='white',bg='blue').grid(row=19, column=1, sticky=W+E,columnspan=2) # Clear Entry
qbutton = Button(sandGui, text = "Quit",command=quit, fg="white", bg="blue").grid(row=21, column=7, sticky=W+E) # Quit Program


editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=hello)
editmenu.add_command(label="Copy", command=hello)
editmenu.add_command(label="Paste", command=hello)
menubar.add_cascade(label="Edit", menu=editmenu)

testmenu = Menu(menubar, tearoff=0)
testmenu.add_command(label="File_Sand", command=evaluate)
menubar.add_cascade(label="Test",menu=testmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=hello)
menubar.add_cascade(label="Help",menu=helpmenu)

         




# Display the menu

sandGui.config(menu=menubar)

sandGui.mainloop() # for windows users

#---------------------------------------------------------------------------------------------

# Sand System Status Codes as of 04-15-2014
# Control Range ( Normal Operation ) := Display Green
# Control Range Deviation ( Outside of Control Range ) := Display Yellow
# Operating Range Deviation ( Outside of Operating Range ) := Display RED



#idate  Input_Date
#itime  Input_Time
#ijob   Input_Job
#iline  Input_Line 
#iident Input_Initials
#itemp  Input_Sand Temp
#imoist Input_Moisture
#icomp  Input_Compactability
#igrstr Input_Green Strengtht
#ispec  Input_Specimen Weight
#iperm  Input_Permeability
#imbc   Input_Methylene Blue Clay
#icomm  Input_Comment
#odate  Output_Date
#otime  Output_Time
#ojob   Output_Job
#oline  Output_Line 
#oident Output_Initials
#otemp  Output_Sand Temp
#omoist Output_Moisture
#ocomp  Output_Compactability
#ogrstr Output_Green Strengtht
#ospec  Output_Specimen Weight
#operm  Output_Permeability
#ombc   Output_Methylene Blue Clay
#ocomm  Output_Comment

# MBC = Methylene Blue Clay
# Comp = Compactability
# GrStr = Green Strength
# Moist = Moisture content of the test Sand
# Temp = Sand Temperature
# MCC = Moisture Compactability Clay
# GSMC = Green Strength Moisture Clay
# GSCC = Green Strength Compactability Clay
# Gse = Green Strength Efficiency
# Perm = Permeability
# SpecWt = Specimen Weight
# Rfac = Return Factor 
# Ab = Available Bond
# Wkb = Working Bond
# Me = Mulling Efficiency
# Cm = Compactability vs. Moisture
# Ce = Compactability Efficiency

# def_Control_Range
# Comp 37 - 43 
# MBC  8.5 - 10.5
# GrStr 23 - 33
# Moist 2.8 - 3.4
# Temp 90 -13
# Perm 30 - 100
# SpecWt 140 - 160
#

# def_Operating_Range
# Comp 28 - 52
# MBC  7.0 - 14.0
# GrStr 18 - 38
# Moist 2.0 - 5.0
# Temp  70 - 155
# Perm  30 - 100
# SpecWt 140 - 160
#



                     
                     
    
