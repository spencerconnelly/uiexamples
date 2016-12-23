from tkinter import *
import tkinter.font
import time
import datetime
import minimalmodbus
import serial
import threading

import modbus_tk
from modbus_tk import modbus_rtu
import modbus_tk.defines as cst

from pymodbus3.client.sync import ModbusSerialClient as pyRtu

#READS THE PLC
master = modbus_rtu.RtuMaster(serial.Serial(port='COM4',baudrate=9600,bytesize=8,parity='E',stopbits=1))

##pymc = pyRtu(method='rtu',port='com4',stopbits=1,bytesize=8,parity='E',baudrate=9600,timeout=100)
##pymc.connect()
##r = pymc.read_holding_registers(203,count=1,unit=1)
##print (r)  #if i type alot when they come back they will think im workign hard do you know what i mean?? XD EEH
##print (r.registers)


sandGui = Tk() #MAIN TKINTER WINDOW CONFIGURATION
fullscreen = False
guiFont = tkinter.font.Font(family = "helvetica",size = 12)
guiFontTitle = tkinter.font.Font(family = "helvetica",weight="bold",size = 11)
sandGui.title('Muller Sand')
w, h = sandGui.winfo_screenwidth(), sandGui.winfo_screenheight()
sandGui.geometry(str(w)+"x"+str(h))
sandGui.configure(background = 'white')



##instr = minimalmodbus.Instrument('COM4',1,mode='rtu')
##instr.serial.baudrate = 9600
##instr.serial.parity = serial.PARITY_EVEN



#-----------------------------------------------------VARIABLES---------------------------------------------------
faultCode = DoubleVar() #Current Fault Code
batchNum = DoubleVar() #Current Batch Number
sandTemp = DoubleVar() #Current Sand Temp
mullSetting = DoubleVar() #Mullor Setting
watSetting = DoubleVar() #Water Setting
newSandSetting =DoubleVar() #New Sand Setting
bondSetting = DoubleVar() #Bond Setting
retSandSetting = DoubleVar() #Return Sand Setting
trimCorr = DoubleVar() #Trim Correction
trimAim = DoubleVar() #Trim Water Aim
constBond = DoubleVar() #Constant Bond
constSand = DoubleVar() #Constant Sand
constWater = DoubleVar() #Constant Water
compactibility = DoubleVar() #Compactability
compSetLow = DoubleVar() #Comp Set Low
compSetHigh = DoubleVar() #Comp Set High
mullTime = DoubleVar() #Mulling Time
seRatio = DoubleVar() #S/M Ratio
totBatchTime = DoubleVar() #Total Batch Time 
flushWater = DoubleVar() #Flush Water
newSandWt = DoubleVar() #New Sand Wt
bondWeight =DoubleVar() #Bond Weight
retSandWeight = DoubleVar() #Return Sand Weight
trimTime = DoubleVar() #Trim Time
watUsed = DoubleVar() #Water Used

totWaterGals = DoubleVar() #H2O Total Gals.
totFlushGals = DoubleVar() #H2O Flush Gals.
compActive = DoubleVar() #Computer Active
temp1 = DoubleVar() #Temperature 1
temp2 = DoubleVar() #Temperature 2
temp3 = DoubleVar() #Temperature 3
tempAve = DoubleVar() #Average Temperature
firstFault = DoubleVar() #First Fault
retSand = DoubleVar() #Return Sand
dustScrew = DoubleVar() #Dust Screw



time1 = ''
date1 = ''
batchnum1=0



#--------------------------------------------------FUNCTIONS-----------------------------------------------------------

def constWindow():
    constWind = Tk()
    for x in range(0,10):
        Grid.rowconfigure(constWind,x,weight=1)
    for y in range(0,6):
        Grid.columnconfigure(constWind,y,weight=1)
    constWind.configure(background = 'white')
    constWind.title('Variables')
    constWind.geometry('520x350')
    titlelabel=Label(constWind,text='                      VARIABLE                                                    VALUE                     ',font=guiFont,bg='systemhighlight',fg='black',borderwidth=2,relief="raised").grid(row=0,column=0,stick=N+S+E+W,pady=1,columnspan=3)
    emptylabel=Label(constWind).grid(row=2,column=0)
    constbondlabel =Label(constWind,text='CONSTANT BOND', font = guiFont, bg='gray',fg='black',borderwidth=2,relief=SOLID).grid(row=3,column=0,sticky=N+S+E+W,pady=1)
    constsandlabel =Label(constWind,text='CONSTANT SAND', font = guiFont, bg='orange',fg='black',borderwidth=2,relief=SOLID).grid(row=4,column=0,sticky=N+S+W+E,pady=2)
    constwaterlabel = Label(constWind,text='CONSTANT WATER', font = guiFont, bg='light blue',fg='black',borderwidth=2,relief=SOLID).grid(row=5,column=0,sticky=N+S+W+E,pady=2)
    mullorsettinglabel =Label(constWind,text='MULLOR SETTING', font = guiFont, bg='black',fg='white',borderwidth=2,relief=SOLID).grid(row=6,column=0,sticky=N+S+W+E,pady=2)
    dustscrewlabel = Label(constWind,text='DUST SCREW', font = guiFont, bg='black',fg='white',borderwidth=2,relief=SOLID).grid(row=7,column=0,sticky=N+S+W+E,pady=2)
    bondsettinglabel =Label(constWind,text='BOND SET', font = guiFont, bg='gray',fg='black',borderwidth=2,relief=SOLID).grid(row=8,column=0,sticky=N+S+W+E,pady=2)
    retsandwtlabel = Label(constWind,text = 'RETURN SAND WEIGHT',font=guiFont,bg='orange',fg='black',borderwidth=2,relief=SOLID).grid(row=9,column=0,sticky=N+S+E+W,pady=1)
    compsetlowlabel = Label(constWind,text = 'COMP SET LOW',font=guiFont,bg = 'mediumpurple4',fg='white',borderwidth=2,relief=SOLID).grid(row=10,column=0,sticky=N+S+E+W,pady=1)
    compsethighlabel=Label(constWind,text = 'COMP SET HIGH',font=guiFont,bg='mediumpurple4',fg='white',borderwidth=2,relief=SOLID).grid(row=11,column=0,sticky=N+S+E+W,pady=1)
    constbondentry =Entry(constWind,font=guiFont,justify=CENTER)
    constbondentry.grid(row=3,column=2)
    
    constsandentry =Entry(constWind,font=guiFont,justify=CENTER)
    constsandentry.grid(row=4,column=2)

    constwaterentry =Entry(constWind,font=guiFont,justify=CENTER)
    constwaterentry.grid(row=5,column=2)

    mullsettingentry =Entry(constWind,font=guiFont,justify=CENTER)
    mullsettingentry.grid(row=6,column=2)
    
    dustscrewentry =Entry(constWind,font=guiFont,justify=CENTER)
    dustscrewentry.grid(row=7,column=2)
    
    bondsetentry =Entry(constWind,font=guiFont,justify=CENTER)
    bondsetentry.grid(row=8,column=2)

    retsandwtentry = Entry(constWind,font=guiFont,justify = CENTER)
    retsandwtentry.grid(row=9,column=2)

    complowentry = Entry(constWind,font=guiFont,justify = CENTER)
    complowentry.grid(row=10,column=2)

    comphighentry = Entry(constWind,font=guiFont,justify = CENTER)
    comphighentry.grid(row=11,column=2)
        
    emptylabel=Label(constWind).grid(row=12,column=0)
    submitButton= Button(constWind,text="SUBMIT DATA",font=guiFontTitle,bg='orange',command=lambda: submitConstants(constbondentry.get(),constsandentry.get(),constwaterentry.get(),mullsettingentry.get(),dustscrewentry.get(),bondsetentry.get(),retsandwtentry.get(),complowentry.get(),comphighentry.get()))
    submitButton.grid(row=13,column=0,columnspan=3,sticky=N+S+E+W)
    constWind.mainloop()
    
def submitConstants(constbond,constsand,constwater,mullset,dustscrew,bondset,retsandwt,compsetlow,compsethigh):

    if isFloat(constbond):
        instr.write_register(203,float(constbond))
    if isFloat(constsand):
        instr.write_register(202,float(constsand))
    if isFloat(constwater):
        instr.write_register(204,float(constwater))
    if isFloat(mullset):
        instr.write_register(212,float(mullset))
    if isFloat(dustscrew):
        instr.write_register(235,float(dustscrew))
    if isFloat(bondset):
        instr.write_register(206,float(bondset))
    if isFloat(retsandwt):
        instr.write_register(225,float(retsandwt))
    if isFloat(compsetlow):
        instr.write_register(226,float(compsetlow))
    if isFloat(compsethigh):
        instr.write_register(227,float(compsethigh))
        
def isFloat(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
    
def enterexitFS():
    global fullscreen
    if fullscreen == False:
        sandGui.call("wm", "attributes", ".", "-fullscreen", "true")
        fullscreen = True
    else:
        sandGui.call("wm", "attributes", ".", "-fullscreen", "False")
        fullscreen = False

#this method reads all the PLC registers and stores the values in  variables that are displayed on the tkinter screen
def getRegisters():  ##NEEDS TO BE MULTITHREADED
    while(sandGui.state() == 'normal'):
        start = time.time()
        sandTempReg=master.execute(1,cst.READ_HOLDING_REGISTERS,21,1)[0]
        compActiveReg=master.execute(1,cst.READ_HOLDING_REGISTERS,200,1)[0]
        newSandSetReg=master.execute(1,cst.READ_HOLDING_REGISTERS,201,1)[0]
        constSandReg=master.execute(1,cst.READ_HOLDING_REGISTERS,202,1)[0]
        constBondReg=master.execute(1,cst.READ_HOLDING_REGISTERS,203,1)[0]
        constWaterReg=master.execute(1,cst.READ_HOLDING_REGISTERS,204,1)[0]
        bondSetReg=master.execute(1,cst.READ_HOLDING_REGISTERS,206,1)[0]
        newSandWtReg=master.execute(1,cst.READ_HOLDING_REGISTERS,209,1)[0]
        watSetReg=master.execute(1,cst.READ_HOLDING_REGISTERS,211,1)[0]
        mullSetReg=master.execute(1,cst.READ_HOLDING_REGISTERS,212,1)[0]
        temp1Reg=master.execute(1,cst.READ_HOLDING_REGISTERS,213,1)[0]
        temp2Reg=master.execute(1,cst.READ_HOLDING_REGISTERS,214,1)[0]
        temp3Reg=master.execute(1,cst.READ_HOLDING_REGISTERS,215,1)[0]
        faultCodeReg=master.execute(1,cst.READ_HOLDING_REGISTERS,216,1)[0]
        retSandSetReg=master.execute(1,cst.READ_HOLDING_REGISTERS,299,1)[0]
        compactReg=master.execute(1,cst.READ_HOLDING_REGISTERS,224,1)[0]
        compSetLowReg=master.execute(1,cst.READ_HOLDING_REGISTERS,301,1)[0]
        compSetHighReg=master.execute(1,cst.READ_HOLDING_REGISTERS,303,1)[0]
        mullTimeReg=master.execute(1,cst.READ_HOLDING_REGISTERS,219,1)[0]
        totBatchTimeReg=master.execute(1,cst.READ_HOLDING_REGISTERS,218,1)[0]
        flushWaterReg=master.execute(1,cst.READ_HOLDING_REGISTERS,221,1)[0]
        bondWeightReg=master.execute(1,cst.READ_HOLDING_REGISTERS,222,1)[0]
        retSandWeightReg=master.execute(1,cst.READ_HOLDING_REGISTERS,223,1)[0]
        batchNumReg=master.execute(1,cst.READ_HOLDING_REGISTERS,217,1)[0]
        totWaterGalsReg=master.execute(1,cst.READ_HOLDING_REGISTERS,229,1)[0]
        totFlushGalsReg=master.execute(1,cst.READ_HOLDING_REGISTERS,231,1)[0]
        dustScrewReg=master.execute(1,cst.READ_HOLDING_REGISTERS,235,1)[0]
        retSandReg=master.execute(1,cst.READ_HOLDING_REGISTERS,239,1)[0]
        print(time.time() - start)
        print(sandTempReg)
        print(compActiveReg)
        print(newSandSetReg)
        print(constSandReg)
        print(constBondReg)
        print(constWaterReg)
        print(constBondReg)
        print(constWaterReg)
        print(bondSetReg)
        print(newSandWtReg)
        print(watSetReg)
        print(mullSetReg)
        print(temp1Reg)
        print(temp2Reg)
        print(temp3Reg)
        print(faultCodeReg)
        print(retSandSetReg)
        print(compactReg)
        print(compSetLowReg)
        print(compSetHighReg)
        print(mullTimeReg)
        print(totBatchTimeReg)
        print(flushWaterReg)
        print(bondWeightReg)
        print(retSandWeightReg)
        print(batchNumReg)
        print(totWaterGalsReg)
        print(totFlushGalsReg)
        print(dustScrewReg)
        print(retSandReg)
    ##    if faultCode.get() != faultCodeReg :
    ##        faultCode.set(instr.faultCodeReg )
    ##    if batchNum.get() != batchNumReg :
    ##        batchNum.set(batchNumReg )
    ##    if sandTemp.get() != sandTempReg :
    ##        sandTemp.set(sandTempReg)
    ##    if mullSetting.get() != mullSetReg  :
    ##        mullSetting.set(mullSetReg )
    ##    if watSetting.get() != watSetReg :
    ##        watSetting.set(watSetReg )
    ##    if newSandSetting.get() != newSandSetReg :
    ##        newSandSetting.set(newSandSetReg )
    ##    if bondSetting.get() != bondSetReg :
    ##        bondSetting.set(bondSetReg )
    ##    if retSandSetting.get() != retSandSetReg :
    ##        retSandSetting.set(retSandSetReg )
    ##    if compactibility.get() != compactReg :
    ##        compactibility.set(compactReg )
    ##    if compSetLow.get() != compSetLowReg :
    ##        compSetLow.set(compSetLowReg )
    ##    if compSetHigh.get() != compSetHighReg :
    ##        compSetHigh.set(compSetHighReg)
    ##    if mullTime.get() != mullTimeReg:
    ##        mullTime.set(mullTimeReg )
    ##    if totBatchTime.get() !=totBatchTimeReg :
    ##        totBatchTime.set(totBatchTimeReg )
    ##    if flushWater.get() != flushWaterReg:
    ##        flushWater.set(flushWaterReg)
    ##    if newSandWt.get() != newSandWtReg :
    ##        newSandWt.set(newSandWtReg )
    ##    if bondWeight.get() != bondWeightReg :
    ##        bondWeight.set(bondWeightReg)
    ##    if retSandWeight.get() != retSandWeightReg :
    ##        retSandWeight.set(retSandWeightReg )
    ##    if totWaterGals.get() != totWaterGalsReg :
    ##        totWaterGals.set(totWaterGalsReg )
    ##    if totFlushGals.get() !=totFlushGalsReg :
    ##        totFlushGals.set(totFlushGalsReg )
    ##    if compActive.get() != compActiveReg :
    ##        compActive.set(compActiveReg )
    ##    if temp1.get() != temp1Reg :
    ##        temp1.set(temp1Reg )
    ##    if temp2.get() != temp2Reg :
    ##        temp2.set(temp2Reg )
    ##    if temp3.get() != temp3Reg :
    ##        temp3.set(temp3Reg )
    ##    if retSand.get() != retSandReg :
    ##        retSand.set(retSandReg )
    ##    if dustScrew.get() !=dustScrewReg :
    ##        dustScrew.set(dustScrewReg )
    ##    if constBond.get() != constBondReg :
    ##        constBond.set(constBondReg )
    ##    if constSand.get() !=constSandReg :
    ##        constSand.set(constSandReg )
    ##    if constWater.get() !=constWaterReg:
    ##        constWater.set(constWaterReg)
    




#This function updates the screen and variables every 400ms.  
def update():
    
    global time1
    global date1
    global regVariables
    global regOutputLabels
    global faultCode
    
##    faultCode2 = instr.read_register(216) 
##    if faultCode.get() != faultCode2:
##        faultCode.set(faultCode2)
##        faultcodelabel.configure(text='FAULT CODE:  '+"%.0f"%faultCode.get())
    time2 = time.strftime('%H:%M:%S')
    date2 = datetime.date.today()
    if time2 != time1:
        time1 = time2
        timeTitle.configure(text = time2)
    if date2 != date1:
        date1 = date2
        dateTitle.configure(text = date2)
    counter = 0
    regThread.join()  #BOTTLENECKS HERE
    for x in regVariables:
        if str(x.get()) != regOutputLabels[counter].cget('text'):
            regOutputLabels[counter].configure(text = str(x.get()))
        counter = counter + 1
    sandGui.after(1000 , update)
    


#-----------------------------------------------------TKINTER LABELS AND ENTRIES---------------------------------------------------

fsButton = Button(text = "±",font=guiFontTitle,bg = "orange",command=enterexitFS).grid(columnspan = 3,row=0, column=5,sticky=N+S+E+W)
changeButton = Button(text = "Change Constants", font = guiFontTitle,bg="orange",command=constWindow).grid(row=0,column=4,sticky=N+S+E+W)

dateTitle = Label(text = str(datetime.date.today()),font = guiFontTitle,bg = "systemhighlight",fg = "white",borderwidth=2,relief=SOLID )
dateTitle.grid(row = 0,column = 0,sticky=N+S+E+W)


for x in range(0,30):  #Configures the rows and columns to be expandable
    Grid.rowconfigure(sandGui,x,weight=1)
for y in range(0,9):
    Grid.columnconfigure(sandGui,y,weight=1)

emptylabel1 = Label(text="   ").grid(row=1,column=0)
batchdisplaylabel = Label(text='BATCH #', font = guiFont,bg='black',fg='white',borderwidth=2,relief=SOLID).grid(row=2,column=0,sticky=N+S+E+W,pady=2)
tempdisplaylabel = Label(text='TEMP SAND', font = guiFont, bg='peru',fg='black',borderwidth=2,relief=SOLID).grid(row=3,column=0,sticky=N+S+W+E,pady=2)
mullisettdisplaylabel = Label(text='MULLOR SETTING', font = guiFont, bg='black',fg='white',borderwidth=2,relief=SOLID).grid(row=4,column=0,sticky=N+S+W+E,pady=2)
watersettdisplaylabel = Label(text='WATER SETTING', font = guiFont, bg='light blue',fg='black',borderwidth=2,relief=SOLID).grid(row=5,column=0,sticky=N+S+W+E,pady=2)
newsanddisplaylabel = Label(text='NEW SAND SET', font = guiFont, bg='orange',fg='black',borderwidth=2,relief=SOLID).grid(row=6,column=0,sticky=N+S+W+E,pady=2)
bondsetdisplaylabel = Label(text='BOND SET', font = guiFont, bg='gray',fg='black',borderwidth=2,relief=SOLID).grid(row=7,column=0,sticky=N+S+W+E,pady=2)
returnsandsetdisplaylabel = Label(text='RETURN SAND SET', font = guiFont, bg='orange',fg='black',borderwidth=2,relief=SOLID).grid(row=8,column=0,sticky=N+S+W+E,pady=2)
trimcorrdisplaylabel = Label(text='TRIM CORRECTION', font = guiFont, bg='light blue',fg='black',borderwidth=2,relief=SOLID).grid(row=9,column=0,sticky=N+S+W+E,pady=2)
trimaimdisplaylabel = Label(text='TRIM WATER AIM', font = guiFont, bg='light blue',fg='black',borderwidth=2,relief=SOLID).grid(row=10,column=0,sticky=N+S+W+E,pady=2)
constbonddisplaylabel = Label(text='CONSTANT BOND', font = guiFont, bg='gray',fg='black',borderwidth=2,relief=SOLID).grid(row=11,column=0,sticky=N+S+W+E,pady=2)
constsanddisplaylabel = Label(text='CONSTANT SAND', font = guiFont, bg='orange',fg='black',borderwidth=2,relief=SOLID).grid(row=12,column=0,sticky=N+S+W+E,pady=2)
constwaterdisplaylabel = Label(text='CONSTANT WATER', font = guiFont, bg='light blue',fg='black',borderwidth=2,relief=SOLID).grid(row=13,column=0,sticky=N+S+W+E,pady=2)
compactabilitydisplaylabel = Label(text='COMPACTABILITY', font = guiFont, bg='mediumpurple4',fg='white',borderwidth=2,relief=SOLID).grid(row=14,column=0,sticky=N+S+W+E,pady=2)
compsetlowdisplaylabel = Label(text='COMP SET LOW', font = guiFont, bg='mediumpurple4',fg='white',borderwidth=2,relief=SOLID).grid(row=16,column=0,sticky=N+S+W+E,pady=2)
compsethighdisplaylabel = Label(text='COMP SET HIGH', font = guiFont, bg='mediumpurple4',fg='white',borderwidth=2,relief=SOLID).grid(row=15,column=0,sticky=N+S+W+E,pady=2)
totbatchtimedisplaylabel = Label(text='TOTAL BATCH TIME', font = guiFont, bg='black',fg='white',borderwidth=2,relief=SOLID).grid(row=2,column=4,sticky=N+S+W+E,pady=2)
mulltimedisplaylabel = Label(text='MULLING TIME', font = guiFont, bg='black',fg='white',borderwidth=2,relief=SOLID).grid(row=17,column=0,sticky=N+S+W+E,pady=2)
flushwatdisplaylabel = Label(text='FLUSH WATER', font = guiFont, bg='light blue',fg='black',borderwidth=2,relief=SOLID).grid(row=2+1,column=4,sticky=N+S+W+E,pady=2)
newsandwtdisplaylabel = Label(text='NEW SAND WT', font = guiFont, bg='orange',fg='black',borderwidth=2,relief=SOLID).grid(row=3+1,column=4,sticky=N+S+W+E,pady=2)
bondwtdisplaylabel = Label(text='BOND WEIGHT', font = guiFont, bg='gray',fg='black',borderwidth=2,relief=SOLID).grid(row=4+1,column=4,sticky=N+S+W+E,pady=2)
retsandwtdisplaylabel = Label(text='RETURN SAND WEIGHT', font = guiFont, bg='orange',fg='black',borderwidth=2,relief=SOLID).grid(row=5+1,column=4,sticky=N+S+W+E,pady=2)
trimdisplaylabel = Label(text='TRIM TIME', font = guiFont, bg='light blue',fg='black',borderwidth=2,relief=SOLID).grid(row=6+1,column=4,sticky=N+S+W+E,pady=2)
watusedisplaylabel = Label(text='WATER USED', font = guiFont, bg='light blue',fg='black',borderwidth=2,relief=SOLID).grid(row=8,column=4,sticky=N+S+W+E,pady=2)

totwaterdisplaylabel = Label(text='H2O TOTAL GALS',borderwidth=2,font = guiFont, bg='light blue',fg='black',relief=SOLID).grid(row=9,column=4,sticky=N+S+W+E,pady=2)

totflushdisplaylabel = Label(text='H2O FLUSH GALS', font = guiFont, bg='light blue',fg='black',borderwidth=2,relief=SOLID).grid(row=10,column=4,sticky=N+S+W+E,pady=2)
compactivedisplaylabel = Label(text='COMPUTER ACTIVE', font = guiFont, bg='black',fg='white',borderwidth=2,relief=SOLID).grid(row=11,column=4,sticky=N+S+W+E,pady=2)
temp1displaylabel = Label(text='TEMP 1', font = guiFont, bg='peru',fg='black',borderwidth=2,relief=SOLID).grid(row=12,column=4,sticky=N+S+W+E,pady=2)
temp2displaylabel = Label(text='TEMP 2', font = guiFont, bg='peru',fg='black',borderwidth=2,relief=SOLID).grid(row=13,column=4,sticky=N+S+W+E,pady=2)
temp3displaylabel = Label(text='TEMP 3', font = guiFont, bg='peru',fg='black',borderwidth=2,relief=SOLID).grid(row=14,column=4,sticky=N+S+W+E,pady=2)
tempavedisplaylabel = Label(text='AVE TEMP', font = guiFont, bg='peru',fg='black',borderwidth=2,relief=SOLID).grid(row=15,column=4,sticky=N+S+W+E,pady=2)
firstfaultdisplaylabel = Label(text='FIRST FAULT', font = guiFont, bg='black',fg='white').grid(row=16,column=4,sticky=N+S+W+E,pady=2)
retsanddisplaylabel = Label(text='RETURN SAND', font = guiFont, bg='orange',fg='black',borderwidth=2,relief=SOLID).grid(row=17,column=4,sticky=N+S+W+E,pady=2)
dustscrewdisplaylabel = Label(text='DUST SCREW', font = guiFont, bg='black',fg='white',borderwidth=2,relief=SOLID).grid(row=18,column=4,sticky=N+S+W+E,pady=2)
seratiodisplaylabel = Label(text = 'S/M RATIO',font = guiFont,bg = 'orange',fg='black',borderwidth=2,relief=SOLID).grid(row=18,column=0,sticky=N+S+E+W,pady=2)

timeTitle = Label(text =time.strftime("%H:%M"),font = guiFontTitle,bg = "systemhighlight",fg = "white",borderwidth=2,relief=SOLID )
timeTitle.grid(row = 0,column = 1,sticky=N+S+E+W)

statuslabel = Label(text = "ALL SYSTEMS NORMAL", font = guiFontTitle, bg = "light green",borderwidth=2,relief=SOLID)
statuslabel.grid(row=1,column=0,columnspan=8,sticky=N+W+S+E,pady=5)

faultcodelabel = Label(text='FAULT CODE:  '+"%.0f"%faultCode.get(), font = guiFontTitle, bg='systemhighlight',fg='white',borderwidth=2,relief=SOLID)
faultcodelabel.grid(row=0,column=2,sticky=N+S+W+E)

batchNumOutput = Label(text = "%.0f"%batchNum.get(),bg='black',fg='white',font=guiFont,borderwidth=2,relief=SOLID)
batchNumOutput.grid(column = 2,row = 2,sticky=N+S+E+W,pady=2)

sandTempOutput = Label(text = "0.0",bg='peru',fg='black',font=guiFont,borderwidth=2,relief=SOLID)
sandTempOutput.grid(column = 2,row = 3,sticky=N+S+E+W,pady=2)

mullSettingOutput = Label(text = "%.0f"%mullSetting.get(),bg='black',fg='white',font=guiFont,borderwidth=2,relief=SOLID)
mullSettingOutput.grid(column = 2,row = 4,sticky=N+S+E+W,pady=2)

watSettingOutput = Label(text = "%.0f"%watSetting.get(),bg='light blue',fg='black',font=guiFont,borderwidth=2,relief=SOLID)
watSettingOutput.grid(column = 2,row = 5,sticky=N+S+E+W,pady=2)

newSandSettingOutput = Label(text = "%.0f"%newSandSetting.get(),bg='orange',fg='black',font=guiFont,borderwidth=2,relief=SOLID)
newSandSettingOutput.grid(column = 2,row = 6,sticky=N+S+E+W,pady=2)

bondSettingOutput = Label(text = "%.0f"%bondSetting.get(),bg='gray',fg='black',font=guiFont,borderwidth=2,relief=SOLID)
bondSettingOutput.grid(column = 2,row = 7,sticky = N+S+E+W,pady=2)

retSandSettingOutput = Label(text = "%.0f"%retSandSetting.get(),bg='orange',fg='black',font=guiFont,borderwidth=2,relief=SOLID)
retSandSettingOutput.grid(column = 2,row = 8,sticky = N+S+E+W,pady=2)

trimCorrOutput = Label(text = "%.0f"%trimCorr.get(),bg='light blue',fg='black',font=guiFont,borderwidth=2,relief=SOLID)
trimCorrOutput.grid(column = 2,row = 9,sticky = N+S+E+W,pady=2)

trimWatAimOutput = Label(text = "%.0f"%trimAim.get(),bg='light blue',fg='black',font=guiFont,borderwidth=2,relief=SOLID)
trimWatAimOutput.grid(column = 2,row = 10,sticky = N+S+E+W,pady=2)

constBondOutput = Label(text = "%.0f"%constBond.get(),bg='gray',fg='black',font=guiFont,borderwidth=2,relief=SOLID)
constBondOutput.grid(column = 2,row = 11,sticky = N+S+E+W,pady=2)

constSandOutput = Label(text = "%.0f"%constSand.get(),bg='orange',fg='black',font=guiFont,borderwidth=2,relief=SOLID)
constSandOutput.grid(column = 2,row = 12,sticky = N+S+E+W,pady=2)

constWaterOutput = Label(text = "%.0f"%constWater.get(),bg='light blue',fg='black',font=guiFont,borderwidth=2,relief=SOLID)
constWaterOutput.grid(column = 2,row = 13,sticky = N+S+E+W,pady=2)

compactibilityOutput = Label(text = "%.0f"%compactibility.get(),bg='mediumpurple4',fg='white',font=guiFont,borderwidth=2,relief=SOLID)
compactibilityOutput.grid(column = 2,row = 14,sticky = N+S+E+W,pady=2)

compSetLowOutput = Label(text = "%.0f"%compSetLow.get(),bg='mediumpurple4',fg='white',font=guiFont,borderwidth=2,relief=SOLID)
compSetLowOutput.grid(column = 2,row = 16,sticky = N+S+E+W,pady=2)

compSetHighOutput = Label(text = "%.0f"%compSetHigh.get(),bg='mediumpurple4',fg='white',font=guiFont,borderwidth=2,relief=SOLID)
compSetHighOutput.grid(column = 2,row = 15,sticky = N+S+E+W,pady=2)

mullTimeOutput = Label(text = "%.0f"%mullTime.get(),bg='black',fg='white',font=guiFont,borderwidth=2,relief=SOLID)
mullTimeOutput.grid(column = 2,row = 17,sticky = N+S+E+W,pady=2)

seRatioOutput = Label(text = "%.0f"%seRatio.get(),bg='orange',fg='black',font=guiFont,borderwidth=2,relief=SOLID)
seRatioOutput.grid(column = 2,row = 18,sticky = N+S+E+W,pady=2)

totBatchTimeOutput = Label(text = "%.0f"%totBatchTime.get(),bg='black',fg='white',font=guiFont,borderwidth=2,relief=SOLID)
totBatchTimeOutput.grid(column = 6,row = 2,sticky = N+S+E+W,pady=2,columnspan=2)

flushWaterOutput = Label(text = "%.0f"%flushWater.get(),bg='light blue',fg='black',font=guiFont,borderwidth=2,relief=SOLID)
flushWaterOutput.grid(column = 6,row = 3,sticky = N+S+E+W,pady=2,columnspan=2)

newSandWtOutput = Label(text = "%.0f"%newSandWt.get(),bg='orange',fg='black',font=guiFont,borderwidth=2,relief=SOLID)
newSandWtOutput.grid(column = 6,row = 4,sticky = N+S+E+W,pady=2,columnspan=2)

bondWeightOutput = Label(text = "%.0f"%bondWeight.get(),bg='gray',fg='black',font=guiFont,borderwidth=2,relief=SOLID)
bondWeightOutput.grid(column = 6,row = 5,sticky = N+S+E+W,pady=2,columnspan=2)

retSandWeightOutput = Label(text = "%.0f"%retSandWeight.get(),bg='orange',fg='black',font=guiFont,borderwidth=2,relief=SOLID)
retSandWeightOutput.grid(column = 6,row = 6,sticky = N+S+E+W,pady=2,columnspan=2)

trimTimeOutput = Label(text = "%.0f"%trimTime.get(),bg='light blue',fg='black',font=guiFont,borderwidth=2,relief=SOLID)
trimTimeOutput.grid(column = 6,row = 7,sticky = N+S+E+W,pady=2,columnspan=2)

waterUsedOutput = Label(text = "%.0f"%watUsed.get(),bg='light blue',fg='black',font=guiFont,borderwidth=2,relief=SOLID)
waterUsedOutput.grid(column = 6,row = 8,sticky = N+S+E+W,pady=2,columnspan=2)

totWaterGalsOutput = Label(text = "%.0f"%totWaterGals.get(),bg='light blue',fg='black',font=guiFont,borderwidth=2,relief=SOLID)
totWaterGalsOutput.grid(column = 6,row = 9,sticky = N+S+E+W,pady=2,columnspan=2)

totFlushGalsOutput= Label(text = "%.0f"%totFlushGals.get(),bg='light blue',fg='black',font=guiFont,borderwidth=2,relief=SOLID)
totFlushGalsOutput.grid(column = 6,row = 10,sticky = N+S+E+W,pady=2,columnspan=2)

compActiveOutput= Label(text = "%.0f"%compActive.get(),bg='black',fg='white',font=guiFont,borderwidth=2,relief=SOLID)
compActiveOutput.grid(column = 6,row = 11,sticky = N+S+E+W,pady=2,columnspan=2)

temp1Output= Label(text = "%.0f"%temp1.get(),bg='peru',fg='black',font=guiFont,borderwidth=2,relief=SOLID)
temp1Output.grid(column = 6,row = 12,sticky = N+S+E+W,pady=2,columnspan=2)

temp2Output= Label(text = "%.0f"%temp2.get(),bg='peru',fg='black',font=guiFont,borderwidth=2,relief=SOLID)
temp2Output.grid(column = 6,row = 13,sticky = N+S+E+W,pady=2,columnspan=2)

temp3Output= Label(text = "%.0f"%temp3.get(),bg='peru',fg='black',font=guiFont,borderwidth=2,relief=SOLID)
temp3Output.grid(column = 6,row = 14,sticky = N+S+E+W,pady=2,columnspan=2)

aveTempOutput= Label(text = "%.0f"%tempAve.get(),bg='peru',fg='black',font=guiFont,borderwidth=2,relief=SOLID)
aveTempOutput.grid(column = 6,row = 15,sticky = N+S+E+W,pady=2,columnspan=2)

firstFaultOutput= Label(text = "%.0f"%firstFault.get(),bg='black',fg='white',font=guiFont,borderwidth=2,relief=SOLID)
firstFaultOutput.grid(column = 6,row = 16,sticky = N+S+E+W,pady=2,columnspan=2)

retSandOutput= Label(text = "%.0f"%retSand.get(),bg='orange',fg='black',font=guiFont,borderwidth=2,relief=SOLID)
retSandOutput.grid(column = 6,row = 17,sticky = N+S+E+W,pady=2,columnspan=2)

dustScrewOutput= Label(text = "%.0f"%dustScrew.get(),bg='black',fg='white',font=guiFont,borderwidth=2,relief=SOLID)
dustScrewOutput.grid(column = 6,row = 18,sticky = N+S+E+W,pady=2,columnspan=2)

regVariables=[batchNum,sandTemp,mullSetting,watSetting,newSandSetting,bondSetting,retSandSetting,compactibility,compSetLow,compSetHigh,mullTime,totBatchTime,flushWater,newSandWt,bondWeight,retSandWeight,totWaterGals,totFlushGals,compActive,temp1,temp2,temp3,retSand,dustScrew,constBond,constSand,constWater]
regOutputLabels=[batchNumOutput,sandTempOutput,mullSettingOutput,watSettingOutput,newSandSettingOutput,bondSettingOutput,retSandSettingOutput,compactibilityOutput,compSetLowOutput,compSetHighOutput,mullTimeOutput,totBatchTimeOutput,flushWaterOutput,newSandWtOutput,bondWeightOutput,retSandWeightOutput,totWaterGalsOutput,totFlushGalsOutput,compActiveOutput,temp1Output,temp2Output,temp3Output,retSandOutput,dustScrewOutput,constBondOutput,constSandOutput,constWaterOutput]

#THREADING
regThread = threading.Thread(target=getRegisters)
updateThread=threading.Thread(target=update)
updateThread.start()
regThread.start()

updateThread.join()
regThread.join()
sandGui.mainloop()

