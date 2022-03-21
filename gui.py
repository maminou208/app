from PyQt5.QtWidgets import *
from PyQt5 import uic
import yagmail
from threading import *
import os
import sys
from time import *
from xlrd import open_workbook
import paho.mqtt.client as mqtt
import pickle


class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        self.wb1 = open_workbook('stats3G.xls').sheet_by_index(0)
        self.wb2 = open_workbook('stats3G.xls').sheet_by_index(0)
        self.wb3 = open_workbook('stats3G.xls').sheet_by_index(0)
        self.reemail = 'raniimmny@gmail.com'
        self.email = 'test12telecom@gmail.com'
        self.pasword = 'test@test@test'
        self.makeDataFile()
        self.makeDirs()
        self.message = self.getData()
        self.save_info('2g', self.wb1)
        self.save_info('3g', self.wb2)
        self.save_info('4g', self.wb3)
        self.thread()
        uic.loadUi('init.ui', self)
        self.show()
        self.update()
        self.update1.clicked.connect(self.changeData2G)
        self.update2.clicked.connect(self.changeData3G)
        self.update2.clicked.connect(self.changeData4G)
        # Psdrop 2g
        self.ps1c.clicked.connect(self.ps1c_stats)
        self.ps1m.clicked.connect(self.ps1m_stats)
        self.ps1n.clicked.connect(self.ps1n_stats)
        # Csdrop 2g
        self.csd1c.clicked.connect(self.csd1c_stats)
        self.csd1m.clicked.connect(self.csd1m_stats)
        self.csd1n.clicked.connect(self.csd1n_stats)
        # Disp 2g
        self.disc.clicked.connect(self.disc_stats)
        self.dism.clicked.connect(self.dism_stats)
        self.disn.clicked.connect(self.disn_stats)
        # Cssrcs 2g
        self.ccsc.clicked.connect(self.ccsc_stats)
        self.ccsm.clicked.connect(self.ccsm_stats)
        self.ccsn.clicked.connect(self.ccsn_stats)
        # glegt min all asami
        self.c1.clicked.connect(self.c1_stats)
        self.m1.clicked.connect(self.m1_stats)
        self.n1.clicked.connect(self.n1_stats)
        # 3g
        self.t3.clicked.connect(self.t3_stats)
        self.t2.clicked.connect(self.t2_stats)
        self.t1.clicked.connect(self.t1_stats)

        # 3g
        self.t4.clicked.connect(self.t4_stats)
        self.t5.clicked.connect(self.t5_stats)
        self.t6.clicked.connect(self.t6_stats)

        self.d1.clicked.connect(self.d1_stats)
        self.d2.clicked.connect(self.d2_stats)
        self.d3.clicked.connect(self.d3_stats)

        self.g1.clicked.connect(self.g1_stats)
        self.g2.clicked.connect(self.g2_stats)
        self.g3.clicked.connect(self.g3_stats)

        self.f1.clicked.connect(self.f1_stats)
        self.f2.clicked.connect(self.f2_stats)
        self.f3.clicked.connect(self.f3_stats)

        self.s1.clicked.connect(self.s1_stats)
        self.s2.clicked.connect(self.s2_stats)
        self.s3.clicked.connect(self.s3_stats)
        # APP 

        self.j1.clicked.connect(self.j1_stats)
        self.j2.clicked.connect(self.j2_stats)
        self.j3.clicked.connect(self.j3_stats)
        # APP 
        self.x1.clicked.connect(self.x1_stats)
        self.x2.clicked.connect(self.x2_stats)
        self.x3.clicked.connect(self.x3_stats)

        self.w1.clicked.connect(self.w1_stats)
        self.w2.clicked.connect(self.w2_stats)
        self.w3.clicked.connect(self.w3_stats)

        self.h1.clicked.connect(self.h1_stats)
        self.h2.clicked.connect(self.h2_stats)
        self.h3.clicked.connect(self.h3_stats)


    def thread(self):
        t1 = Thread(target=self.sendEmails)
        t1.start()

    def sendEmails(self):
        print('starting Thread Succesfully')
        while True:
            self.send_save_info('2g', self.wb1)
            self.send_save_info('3g', self.wb2)
            self.send_save_info('4g', self.wb3)
            # SE3a
            time.sleep(3600)


    def h3_stats(self):
        app2 = Ui2(self,os.path.join('4g','cps','mineur.dat'),self.message['4g']['cps'][-3],'cps')
        app2.exec_()

    def h2_stats(self):
        app2 = Ui2(self,os.path.join('4g','cps','majeur.dat'),self.message['4g']['cps'][-2],'cps')
        app2.exec_()

    def h1_stats(self):
        app2 = Ui2(self,os.path.join('4g','cps','critique.dat'),self.message['4g']['cps'][-1],'cps')
        app2.exec_()




    def w1_stats(self):
        app2 = Ui2(self,os.path.join('4g','ccs','critique.dat'),self.message['4g']['ccs'][-1],'ccs')
        app2.exec_()
    def w3_stats(self):
        app2 = Ui2(self,os.path.join('4g','ccs','mineur.dat'),self.message['4g']['ccs'][-3],'ccs')
        app2.exec_()
    def w2_stats(self):
        app2 = Ui2(self,os.path.join('4g','ccs','majeur.dat'),self.message['4g']['ccs'][-2],'ccs')
        app2.exec_()


    def x2_stats(self):
        app2 = Ui2(self,os.path.join('4g','av','majeur.dat'),self.message['4g']['av'][-2],'av')
        app2.exec_()

    def x3_stats(self):
        app2 = Ui2(self,os.path.join('4g','av','mineur.dat'),self.message['4g']['av'][-3],'av')
        app2.exec_()

    def x1_stats(self):
        app2 = Ui2(self,os.path.join('4g','av','critique.dat'),self.message['4g']['av'][-1],'av')
        app2.exec_()





    def j1_stats(self):
        app2 = Ui2(self,os.path.join('4g','dcs','critique.dat'),self.message['4g']['dcs'][-1],'dcs')
        app2.exec_()

    def j2_stats(self):
        app2 = Ui2(self,os.path.join('4g','dcs','majeur.dat'),self.message['4g']['dcs'][-2],'dcs')
        app2.exec_()

    def j3_stats(self):
        app2 = Ui2(self,os.path.join('4g','dcs','mineur.dat'),self.message['4g']['dcs'][-3],'dcs')
        app2.exec_()


    def s3_stats(self):
        app2 = Ui2(self,os.path.join('4g','dps','mineur.dat'),self.message['4g']['dps'][-3],'dps')
        app2.exec_()
    def s1_stats(self):
        app2 = Ui2(self,os.path.join('4g','dps','critique.dat'),self.message['4g']['dps'][-1],'dps')
        app2.exec_()
    def s2_stats(self):
        app2 = Ui2(self,os.path.join('4g','dps','majeur.dat'),self.message['4g']['dps'][-2],'dps')
        app2.exec_()



    def f3_stats(self):
        app2 = Ui2(self,os.path.join('3g','cps','mineur.dat'),self.message['3g']['cps'][-3],'cps')
        app2.exec_()

    def f2_stats(self):
        app2 = Ui2(self,os.path.join('3g','cps','majeur.dat'),self.message['3g']['cps'][-2],'cps')
        app2.exec_()

    def f1_stats(self):
        app2 = Ui2(self,os.path.join('3g','cps','critique.dat'),self.message['3g']['cps'][-1],'cps')
        app2.exec_()


    def g1_stats(self):
        app2 = Ui2(self,os.path.join('3g','ccs','critique.dat'),self.message['3g']['ccs'][-1],'ccs')
        app2.exec_()
    def g3_stats(self):
        app2 = Ui2(self,os.path.join('3g','ccs','mineur.dat'),self.message['3g']['ccs'][-3],'ccs')
        app2.exec_()
    def g2_stats(self):
        app2 = Ui2(self,os.path.join('3g','ccs','majeur.dat'),self.message['3g']['ccs'][-2],'ccs')
        app2.exec_()



    def d2_stats(self):
        app2 = Ui2(self,os.path.join('3g','av','majeur.dat'),self.message['3g']['av'][-2],'av')
        app2.exec_()

    def d3_stats(self):
        app2 = Ui2(self,os.path.join('3g','av','mineur.dat'),self.message['3g']['av'][-3],'av')
        app2.exec_()

    def d1_stats(self):
        app2 = Ui2(self,os.path.join('3g','av','critique.dat'),self.message['3g']['av'][-1],'av')
        app2.exec_()

    def t4_stats(self):
        app2 = Ui2(self,os.path.join('3g','dcs','critique.dat'),self.message['3g']['dcs'][-1],'dcs')
        app2.exec_()

    def t6_stats(self):
        app2 = Ui2(self,os.path.join('3g','dcs','majeur.dat'),self.message['3g']['dcs'][-2],'dcs')
        app2.exec_()

    def t5_stats(self):
        app2 = Ui2(self,os.path.join('3g','dcs','mineur.dat'),self.message['3g']['dcs'][-3],'dcs')
        app2.exec_()



    def t3_stats(self):
        app2 = Ui2(self,os.path.join('3g','dps','mineur.dat'),self.message['3g']['dps'][-3],'dps')
        app2.exec_()
    def t1_stats(self):
        app2 = Ui2(self,os.path.join('3g','dps','critique.dat'),self.message['3g']['dps'][-1],'dps')
        app2.exec_()
    def t2_stats(self):
        app2 = Ui2(self,os.path.join('3g','dps','majeur.dat'),self.message['3g']['dps'][-2],'dps')
        app2.exec_()


    def n1_stats(self):
        app2 = Ui2(self,os.path.join('2g','cps','mineur.dat'),self.message['2g']['cps'][-3],'cps')
        app2.exec_()

    def m1_stats(self):
        app2 = Ui2(self,os.path.join('2g','cps','majeur.dat'),self.message['2g']['cps'][-2],'cps')
        app2.exec_()

    def c1_stats(self):
        app2 = Ui2(self,os.path.join('2g','cps','critique.dat'),self.message['2g']['cps'][-1],'cps')
        app2.exec_()

    def ccsc_stats(self):
        app2 = Ui2(self,os.path.join('2g','ccs','critique.dat'),self.message['2g']['ccs'][-1],'ccs')
        app2.exec_()

    def ccsn_stats(self):
        app2 = Ui2(self,os.path.join('2g','ccs','mineur.dat'),self.message['2g']['ccs'][-3],'ccs')
        app2.exec_()


    def ccsm_stats(self):
        app2 = Ui2(self,os.path.join('2g','ccs','majeur.dat'),self.message['2g']['ccs'][-2],'ccs')
        app2.exec_()


    def dism_stats(self):
        app2 = Ui2(self,os.path.join('2g','av','majeur.dat'),self.message['2g']['av'][-2],'av')
        app2.exec_()

    def disn_stats(self):
        app2 = Ui2(self,os.path.join('2g','av','mineur.dat'),self.message['2g']['av'][-3],'av')
        app2.exec_()

    def disc_stats(self):
        app2 = Ui2(self,os.path.join('2g','av','critique.dat'),self.message['2g']['av'][-1],'av')
        app2.exec_()

    def csd1c_stats(self):
        app2 = Ui2(self,os.path.join('2g','dcs','critique.dat'),self.message['2g']['dcs'][-1],'dcs')
        app2.exec_()

    def csd1m_stats(self):
        app2 = Ui2(self,os.path.join('2g','dcs','majeur.dat'),self.message['2g']['dcs'][-2],'dcs')
        app2.exec_()

    def csd1n_stats(self):
        app2 = Ui2(self,os.path.join('2g','dcs','mineur.dat'),self.message['2g']['dcs'][-3],'dcs')
        app2.exec_()

    def ps1n_stats(self):
        app2 = Ui2(self,os.path.join('2g','dps','mineur.dat'),self.message['2g']['dps'][-3],'dps')
        app2.exec_()

    def ps1c_stats(self):
        app2 = Ui2(self,os.path.join('2g','dps','critique.dat'),self.message['2g']['dps'][-1],'dps')
        app2.exec_()

    def ps1m_stats(self):
        app2 = Ui2(self,os.path.join('2g','dps','majeur.dat'),self.message['2g']['dps'][-2],'dps')
        app2.exec_()



    def makeDirs(self):
        parentdirs = ['2g', '3g', '4g']
        parentydirs = ['dps', 'dcs', 'cps', 'ccs', 'av']
        for i in parentdirs:
            try:
                os.makedirs(i)
                for j in parentydirs:
                    os.makedirs(os.path.join(i, j))
            except:
                for j in parentydirs:
                    try:
                        os.makedirs(os.path.join(i, j))
                    except:
                        pass

    def send_save_info(self,res,sheet):
        psdrops = self.message[res]['dps'][0]
        csdrops = self.message[res]['dcs'][0]
        cssrpss = self.message[res]['cps'][0]
        cssrcss = self.message[res]['ccs'][0]
        avavg = self.message[res]['av'][0]

        self.message[res]['dcs'][-1]=0
        self.message[res]['dcs'][-2]=0
        self.message[res]['dcs'][-3]=0

        self.message[res]['dps'][-1]=0
        self.message[res]['dps'][-2]=0
        self.message[res]['dps'][-3]=0
        
        self.message[res]['ccs'][-1]=0
        self.message[res]['ccs'][-2]=0
        self.message[res]['ccs'][-3]=0

        self.message[res]['cps'][-1]=0
        self.message[res]['cps'][-2]=0
        self.message[res]['cps'][-3]=0


        self.message[res]['av'][-1]=0
        self.message[res]['av'][-2]=0
        self.message[res]['av'][-3]=0

        file1 = open(os.path.join(res,'dps','mineur.dat'),'wb')
        file2 = open(os.path.join(res,'dps','majeur.dat'),'wb')
        file3 = open(os.path.join(res,'dps','critique.dat'),'wb')
        file4 = open(os.path.join(res,'dcs','mineur.dat'),'wb')
        file5 = open(os.path.join(res,'dcs','majeur.dat'),'wb')
        file6 = open(os.path.join(res,'dcs','critique.dat'),'wb')
        file7 = open(os.path.join(res,'ccs','mineur.dat'),'wb')
        file8 = open(os.path.join(res,'ccs','majeur.dat'),'wb')
        file9 = open(os.path.join(res,'ccs','critique.dat'),'wb')
        file10 = open(os.path.join(res,'cps','mineur.dat'),'wb')
        file11 = open(os.path.join(res,'cps','majeur.dat'),'wb')
        file12 = open(os.path.join(res,'cps','critique.dat'),'wb')
    
        file13 = open(os.path.join(res,'av','mineur.dat'),'wb')
        file14 = open(os.path.join(res,'av','majeur.dat'),'wb')
        file15 = open(os.path.join(res,'av','critique.dat'),'wb')
    
        for i in range(sheet.nrows-1):
                e ={}
                e['nom'] = sheet.cell_value(i+1,2)
                e['id'] = sheet.cell_value(i+1,3)
                e['av'] = sheet.cell_value(i+1,6)
                e['dcs'] = sheet.cell_value(i+1,7)
                e['dps'] = sheet.cell_value(i+1,8)
                e['ccs'] = sheet.cell_value(i+1,9)
                e['cps'] = sheet.cell_value(i+1,10)
                problem = []
                # != str 3al #div 0
                # Drop cs
                if type(e['dcs'])!=str:
                    if e['dcs']>csdrops:
                        # Critique
                        self.message[res]['dcs'][-1]+=1
                        problem.append('csddrop')
                        pickle.dump(e,file6)
                    elif e['dcs']==csdrops:
                        # majeur
                        self.message[res]['dcs'][-2]+=1
                        pickle.dump(e,file5)
                    else:
                        # mineur
                        self.message[res]['dcs'][-3]+=1
                        pickle.dump(e,file4)
                # DROP PS
                if type(e['dps'])!=str:
                    if e['dps']>psdrops:
                        # Critique
                        self.message[res]['dps'][-1]+=1
                        problem.append('psdrop')
                        pickle.dump(e,file3)
                    elif e['dps']==psdrops:
                        # majeur
                        self.message[res]['dps'][-2]+=1
                        pickle.dump(e,file2)
                    else:
                        # mineur
                        self.message[res]['dps'][-3]+=1
                        pickle.dump(e,file1)
                # CSSR CS
                if type(e['ccs'])!=str:
                    if e['ccs']<cssrcss:
                        problem.append('ccs')
                        self.message[res]['ccs'][-1]+=1
                        # Critique
                        pickle.dump(e,file9)
                    elif e['ccs']==cssrcss:
                        # majeur
                        self.message[res]['ccs'][-2]+=1
                        pickle.dump(e,file8)
                    else:
                        # mineur
                        self.message[res]['ccs'][-3]+=1
                        pickle.dump(e,file7)
                # CSSR PS
                if type(e['cps'])!=str:
                    if e['cps']<cssrpss:
                        # Critique
                        problem.append('cps')
                        self.message[res]['cps'][-1]+=1
                        pickle.dump(e,file12)
                    elif e['cps']==cssrpss:
                        # majeur
                        self.message[res]['cps'][-2]+=1
                        pickle.dump(e,file11)
                    else:
                        # mineur
                        self.message[res]['cps'][-3]+=1
                        pickle.dump(e,file10)
                # Availibility
                if type(e['av'])!=str:
                    if e['av']<avavg:
                        problem.append('avg')
                        self.message[res]['av'][-1]+=1
                        # Critique
                        pickle.dump(e,file15)
                    elif e['av']==avavg:
                        # majeur
                        self.message[res]['av'][-2]+=1
                        pickle.dump(e,file14)
                    else:
                        # mineur
                        self.message[res]['av'][-3]+=1
                        pickle.dump(e,file13)
    
                if len(problem) >0:
                    yag = yagmail.SMTP(self.email, self.pasword)
                    mese = f"{e['nom']} et {e['id']} on des problemes "
                    for i in problem:
                        mese += f" {i} "
                    print(mese)
                    yag.send(self.reemail,res,mese)





    def save_info(self,res,sheet):
        psdrops = self.message[res]['dps'][0]
        csdrops = self.message[res]['dcs'][0]
        cssrpss = self.message[res]['cps'][0]
        cssrcss = self.message[res]['ccs'][0]
        avavg = self.message[res]['av'][0]

        self.message[res]['dcs'][-1]=0
        self.message[res]['dcs'][-2]=0
        self.message[res]['dcs'][-3]=0

        self.message[res]['dps'][-1]=0
        self.message[res]['dps'][-2]=0
        self.message[res]['dps'][-3]=0
        
        self.message[res]['ccs'][-1]=0
        self.message[res]['ccs'][-2]=0
        self.message[res]['ccs'][-3]=0

        self.message[res]['cps'][-1]=0
        self.message[res]['cps'][-2]=0
        self.message[res]['cps'][-3]=0


        self.message[res]['av'][-1]=0
        self.message[res]['av'][-2]=0
        self.message[res]['av'][-3]=0

        file1 = open(os.path.join(res,'dps','mineur.dat'),'wb')
        file2 = open(os.path.join(res,'dps','majeur.dat'),'wb')
        file3 = open(os.path.join(res,'dps','critique.dat'),'wb')
        file4 = open(os.path.join(res,'dcs','mineur.dat'),'wb')
        file5 = open(os.path.join(res,'dcs','majeur.dat'),'wb')
        file6 = open(os.path.join(res,'dcs','critique.dat'),'wb')
        file7 = open(os.path.join(res,'ccs','mineur.dat'),'wb')
        file8 = open(os.path.join(res,'ccs','majeur.dat'),'wb')
        file9 = open(os.path.join(res,'ccs','critique.dat'),'wb')
        file10 = open(os.path.join(res,'cps','mineur.dat'),'wb')
        file11 = open(os.path.join(res,'cps','majeur.dat'),'wb')
        file12 = open(os.path.join(res,'cps','critique.dat'),'wb')
    
        file13 = open(os.path.join(res,'av','mineur.dat'),'wb')
        file14 = open(os.path.join(res,'av','majeur.dat'),'wb')
        file15 = open(os.path.join(res,'av','critique.dat'),'wb')
    
        for i in range(sheet.nrows-1):
                e ={}
                e['nom'] = sheet.cell_value(i+1,2)
                e['id'] = sheet.cell_value(i+1,3)
                e['av'] = sheet.cell_value(i+1,6)
                e['dcs'] = sheet.cell_value(i+1,7)
                e['dps'] = sheet.cell_value(i+1,8)
                e['ccs'] = sheet.cell_value(i+1,9)
                e['cps'] = sheet.cell_value(i+1,10)
                # != str 3al #div 0
                # Drop cs
                if type(e['dcs'])!=str:
                    if e['dcs']>csdrops:
                        # Critique
                        self.message[res]['dcs'][-1]+=1
                        pickle.dump(e,file6)
                    elif e['dcs']==csdrops:
                        # majeur
                        self.message[res]['dcs'][-2]+=1
                        pickle.dump(e,file5)
                    else:
                        # mineur
                        self.message[res]['dcs'][-3]+=1
                        pickle.dump(e,file4)
                # DROP PS
                if type(e['dps'])!=str:
                    if e['dps']>psdrops:
                        # Critique
                        self.message[res]['dps'][-1]+=1
                        pickle.dump(e,file3)
                    elif e['dps']==psdrops:
                        # majeur
                        self.message[res]['dps'][-2]+=1
                        pickle.dump(e,file2)
                    else:
                        # mineur
                        self.message[res]['dps'][-3]+=1
                        pickle.dump(e,file1)
                # CSSR CS
                if type(e['ccs'])!=str:
                    if e['ccs']<cssrcss:
                        self.message[res]['ccs'][-1]+=1
                        # Critique
                        pickle.dump(e,file9)
                    elif e['ccs']==cssrcss:
                        # majeur
                        self.message[res]['ccs'][-2]+=1
                        pickle.dump(e,file8)
                    else:
                        # mineur
                        self.message[res]['ccs'][-3]+=1
                        pickle.dump(e,file7)
                # CSSR PS
                if type(e['cps'])!=str:
                    if e['cps']<cssrpss:
                        # Critique
                        self.message[res]['cps'][-1]+=1
                        pickle.dump(e,file12)
                    elif e['cps']==cssrpss:
                        # majeur
                        self.message[res]['cps'][-2]+=1
                        pickle.dump(e,file11)
                    else:
                        # mineur
                        self.message[res]['cps'][-3]+=1
                        pickle.dump(e,file10)
                # Availibility
                if type(e['av'])!=str:
                    if e['av']<avavg:
                        self.message[res]['av'][-1]+=1
                        # Critique
                        pickle.dump(e,file15)
                    elif e['av']==avavg:
                        # majeur
                        self.message[res]['av'][-2]+=1
                        pickle.dump(e,file14)
                    else:
                        # mineur
                        self.message[res]['av'][-3]+=1
                        pickle.dump(e,file13)
    
        file1.close()
        file2.close()
        file3.close()
        file4.close()
        file5.close()
        file6.close()
        file7.close()
        file8.close()
        file9.close()
        file10.close()
        file11.close()
        file12.close()
        file13.close()
        file14.close()
        file15.close()
        self.changeMainMessage(self.message)
    
    def update(self):
        self.dps1.setValue(self.message['2g']['dps'][0])
        self.dcs1.setValue(self.message['2g']['dcs'][0])
        self.cps1.setValue(self.message['2g']['cps'][0])
        self.ccs1.setValue(self.message['2g']['ccs'][0])
        self.av1.setValue(self.message['2g']['av'][0])
        self.dps2.setValue(self.message['3g']['dps'][0])
        self.dcs2.setValue(self.message['3g']['dcs'][0])
        self.cps2.setValue(self.message['3g']['cps'][0])
        self.ccs2.setValue(self.message['3g']['ccs'][0])
        self.av2.setValue(self.message['3g']['av'][0])
        self.dps3.setValue(self.message['4g']['dps'][0])
        self.dcs3.setValue(self.message['4g']['dcs'][0])
        self.cps3.setValue(self.message['4g']['cps'][0])
        self.ccs3.setValue(self.message['4g']['ccs'][0])
        self.av3.setValue(self.message['4g']['av'][0])
    def changeData4G(self):
        self.message['4g']['dps'][0]=self.dps3.value()
        self.message['4g']['dcs'][0]=self.dcs3.value()
        self.message['4g']['cps'][0]=self.cps3.value()
        self.message['4g']['ccs'][0]=self.ccs3.value()
        self.message['4g']['av'][0]=self.av3.value()
        self.changeMainMessage(self.message)
    def changeData3G(self):
        self.message['3g']['dps'][0]=self.dps2.value()
        self.message['3g']['dcs'][0]=self.dcs2.value()
        self.message['3g']['cps'][0]=self.cps2.value()
        self.message['3g']['ccs'][0]=self.ccs2.value()
        self.message['3g']['av'][0]=self.av2.value()
        self.changeMainMessage(self.message)
    def changeData2G(self):
        self.message['2g']['dps'][0]=self.dps1.value()
        self.message['2g']['dcs'][0]=self.dcs1.value()
        self.message['2g']['cps'][0]=self.cps1.value()
        self.message['2g']['ccs'][0]=self.ccs1.value()
        self.message['2g']['av'][0]=self.av1.value()
        self.changeMainMessage(self.message)

    def makeDataFile(self):
        if not(os.path.exists('data.dat')):
            msg = {}
            msg['2g']={
                'dps': [0.213,0,0,0],
                'dcs': [0.3,0,0,0],
                'cps': [0.2,0,0,0],
                'ccs': [83,0,0,0],
                'av': [93,0,0,0]
            }
            msg['3g']={
                'dps': [0.213,0,0,0],
                'dcs': [0.3,0,0,0],
                'cps': [0.2,0,0,0],
                'ccs': [83,0,0,0],
                'av': [93,0,0,0]
            }
            msg['4g']={
                'dps': [0.213,0,0,0],
                'dcs': [0.3,0,0,0],
                'cps': [0.2,0,0,0],
                'ccs': [83,0,0,0],
                'av': [93,0,0,0]
            }
            self.changeMainMessage(msg)        
    def getData(self):
        with open('data.dat','rb') as fileData:
            return(pickle.load(fileData))
    def changeMainMessage(self,new):
        with open('data.dat','wb') as fileData:
            pickle.dump(new,fileData)
        mqttc = mqtt.Client()
        mqttc.connect("test.mosquitto.org", 1883)
        mqttc.publish("tunisie/telecom", str(new),retain=True)
        mqttc.loop(2)




class Ui2(QDialog):
    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent)
        uic.loadUi("second.ui",self)
        self.file = args[0]
        self.rows = args[1]
        self.champ = args[2]
        self.t1.setRowCount(args[1])
        self.t1.setColumnWidth(1,250)
        self.t1.setColumnWidth(2,250)
        self.t1.setColumnWidth(3,250)
        self.dataShow()
    def dataShow(self):
        f1 = open(self.file,'rb')
        for i in range(self.rows):
            e = pickle.load(f1)
            self.t1.setItem(i,0,QTableWidgetItem(str(e['id'])))
            self.t1.setItem(i,1,QTableWidgetItem(str(e['nom'])))
            self.t1.setItem(i,2,QTableWidgetItem(str(e[self.champ])))
        f1.close()

app = QApplication(sys.argv)
UIWindow = Ui()
app.exec_()
