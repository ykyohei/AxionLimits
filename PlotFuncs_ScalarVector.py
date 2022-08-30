#================================PlotFuncs_ScalarVector.py==================================#
# Created by Ciaran O'Hare 2022

# Description:
# This file has some extra classes for dealing with the scalar and vector plots 
# only

#==============================================================================#

from PlotFuncs import *

def NaturalnessCorner(ax,scale,Lambda_min_TeV,dim,edgecolor='gold',facecolor='gold',
                      lw=3,path_effects=line_background(4,'k'),
                      nlevels=100,alpha=0.1,Lambda_max_TeV=1e20,
                      mass_label=5e-13,
                     text_label=r'Natural $d_e$ ($\Lambda = 10$ TeV)',
                     text_shift=[1,1],zorder=-100,
                     Shading=True,fs=25):
    m_vals = array([1e-30,1e30])
    d_natural = lambda m,Lambda : m/(scale*Lambda**dim)
    ax.plot(m_vals,d_natural(m_vals,Lambda_min_TeV*1e12),'-',lw=lw,color=edgecolor,path_effects=path_effects,zorder=zorder)
   
    if Shading:
        Lambda_vals = logspace(log10(Lambda_min_TeV),log10(Lambda_max_TeV),nlevels)
        for Lambda in Lambda_vals:
            ax.fill_between(m_vals,d_natural(m_vals,Lambda*1e12),y2=1e-100,color=facecolor,alpha=alpha,zorder=zorder,lw=0)
  
    trans_angle = plt.gca().transData.transform_angles(array((45.0,)),array([[0, 0]]))[0]
    ax.text(mass_label*text_shift[0],0.1*d_natural(mass_label,Lambda_min_TeV*1e12)*text_shift[1],text_label,fontsize=fs,color=edgecolor,rotation=trans_angle,path_effects=line_background(1,'k'),clip_on=True,zorder=zorder)
    return
    
def FuzzyDM(ax,edgecolor='#205e8a',facecolor='#205e8a',
                      lw=3,path_effects=line_background(0,'k'),
                      nlevels=100,alpha=0.05,m_max=5e-20,m_min=1e-24,
                      g_label=5e-13,fs=23,
                     text_label=r'{\bf Structure formation}',
                     text_shift=[1,1],zorder=-100):
    g_vals = array([1e-30,1e30])
    m_vals = logspace(log10(m_min),log10(m_max),nlevels)
    for m in m_vals:
        ax.fill_between(array([1e-30,m]),array([1e30,1e30]),y2=1e-30,color=facecolor,alpha=alpha,zorder=zorder,lw=0)
    ax.text(m_max*text_shift[0]*0.5,g_label*text_shift[1],text_label,fontsize=fs,color=edgecolor,rotation=90,path_effects=line_background(1,'k'),clip_on=True,zorder=zorder)
    return


class ScalarPhoton():
    def MICROSCOPE(ax,text_label=r'{\bf MICROSCOPE}',text_pos=[2e-16,0.5e-3],col='#84878c',text_col='k',fs=17.5,zorder=-1,text_on=True,Projection=False,edgealpha=1,lw=3):
        dat = loadtxt("limit_data/ScalarPhoton/MICROSCOPE.txt")
        FilledLimit(ax,dat,text_label,y2=1e20,text_pos=text_pos,text_col=text_col,col=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
    
    def EotWashEP(ax,text_label=r'{\bf E\"ot-Wash (EP)}',text_pos=[2e-24,0.5e-2],col='gray',text_col='k',fs=20,zorder=0.1,text_on=True,Projection=False,edgealpha=1,lw=3):
        dat = loadtxt("limit_data/ScalarPhoton/EotWashEP.txt")
        FilledLimit(ax,dat,text_label,y2=1e20,text_pos=text_pos,text_col=text_col,col=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
    
    def FifthForce(ax,text_label=r'{\bf Fifth force}',text_pos=[2e-21,1e2],rotation=-28,col='darkgray',text_col='k',fs=20,zorder=0.1,text_on=True,Projection=False,edgealpha=1,lw=3):
        dat = loadtxt("limit_data/ScalarPhoton/FifthForce.txt")
        FilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,col=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
    
    def GlobularClusters(ax,text_label=r'{\bf Globular clusters}',text_pos=[2e-24,4e9],col=[0.0, 0.66, 0.42],text_col='w',fs=27,zorder=1,text_on=True,Projection=False,edgealpha=1,lw=3):
        dat = loadtxt("limit_data/ScalarPhoton/GlobularClusters.txt")
        FilledLimit(ax,dat,text_label,y2=1e20,text_pos=text_pos,text_col=text_col,col=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
    
    def AURIGA(ax,text_label=r'{\bf AURIGA}',text_pos=[0.18e-11,0.1e-6],rotation=90,col='darkred',text_col='darkred',fs=17,zorder=0.0,text_on=True,Projection=False,edgealpha=1,lw=0):
        dat = loadtxt("limit_data/ScalarPhoton/AURIGA.txt")
        FilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,col=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return

    def DyDy(ax,text_label=r'{\bf Dy/Dy}',text_pos=[0.4e-22,0.2e-6],rotation=28,col='#a11a4e',text_col='w',fs=20,zorder=0.02,text_on=True,Projection=False,edgealpha=1,lw=2):
        dat = loadtxt("limit_data/ScalarPhoton/DyDy.txt")
        FilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,col=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
    
    def RbCs(ax,text_label=r'\center{{\bf SYRTE \newline Rb/Cs}}',text_pos=[0.2e-23,4e-7],rotation=-30,col='#c7345d',text_col='w',fs=17,zorder=0.01,text_on=True,Projection=False,edgealpha=1,lw=2):
        dat = loadtxt("limit_data/ScalarPhoton/RbCs.txt")
        FilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,col=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
    
    def BACON(ax,text_label=r'{\bf BACON}',text_pos=[0.1e-21,0.075e-7],rotation=26,col='#59042d',text_col='#59042d',fs=19,zorder=0.0,text_on=True,Projection=False,edgealpha=1,lw=2):
        dat = loadtxt("limit_data/ScalarPhoton/BACON.txt")
        FilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,col=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
    
    def SrSi(ax,text_label=r'{\bf Sr/Si}',text_pos=[0.3e-17,0.35e-3],rotation=13,col='#730f3a',text_col='w',fs=15,zorder=0.0,text_on=True,Projection=False,edgealpha=1,lw=2):
        dat = loadtxt("limit_data/ScalarPhoton/SrSi.txt")
        FilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,col=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
    
    def HQuartzSapphire(ax,text_label=r'\center{\bf H/Quartz/Sapphire}',text_pos=[0.7e-18,1e4],rotation=0,col='#a81313',text_col='w',fs=20,zorder=0.11,text_on=True,Projection=False,edgealpha=1,lw=3):
        dat = loadtxt("limit_data/ScalarPhoton/HQuartzSapphire.txt")
        FilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,col=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
    
    def I2(ax,text_label=r'{\bf I}$_2$',text_pos=[0.5e-12,1e6],rotation=0,col='#b52452',text_col='w',fs=25,zorder=0.13,text_on=True,Projection=False,edgealpha=1,lw=3):
        dat = loadtxt("limit_data/ScalarPhoton/I2.txt")
        FilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,col=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return

    def DAMNED(ax,text_label=r'{\bf DAMNED}',text_pos=[0.85e-10,0.7e4],rotation=90,col='#b5243f',text_col='w',fs=13,zorder=0.11,text_on=True,Projection=False,edgealpha=1,lw=3):
        dat = loadtxt("limit_data/ScalarPhoton/DAMNED.txt")
        FilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,col=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
    
    
    def GEO600(ax,text_label=r'{\bf GEO600}',text_pos=[4e-13,1e2],rotation=0,col='#b5260d',text_col='w',fs=20,zorder=0.11,text_on=True,Projection=False,edgealpha=1,lw=3):
        dat = loadtxt("limit_data/ScalarPhoton/GEO600.txt")
        FilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,col=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return

        
    def Holometer(ax,text_label=r'{\bf Holometer}',text_pos=[1.2e-10,0.2e9],rotation=0,col='#b53724',text_col='w',fs=18,zorder=0.17,text_on=True,Projection=False,edgealpha=1,lw=3):
        dat = loadtxt("limit_data/ScalarPhoton/Holometer.txt")
        FilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,col=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
    
            
    def DynamicDecoupling(ax,text_label=r'\center{\bf Dynamic \newline decoupling}',text_pos=[0.6e-13,0.25e9],rotation=-26,col='crimson',text_col='w',fs=12,zorder=0.14,text_on=True,Projection=False,edgealpha=1,lw=3):
        dat = loadtxt("limit_data/ScalarPhoton/DynamicDecoupling.txt")
        FilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,col=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return

        
    def CsCav(ax,text_label=r'{\bf Cs/Cav}',text_pos=[3e-8,0.2e7],rotation=55,col='red',text_col='w',fs=18,zorder=0.109,text_on=True,Projection=False,edgealpha=1,lw=3):
        dat = loadtxt("limit_data/ScalarPhoton/CsCav.txt")
        FilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,col=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
    
    # Projected
    def AEDGE(ax,text_label=r'{\bf AEDGE}',text_pos=[1e-16,0.1e-11],rotation=50,col='#eb4034',text_col='#eb4034',fs=20,zorder=-1.1,text_on=True,Projection=False,edgealpha=1,lw=3):
        dat = loadtxt("limit_data/ScalarPhoton/Projections/AEDGE.txt")
        UnfilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,linestyle='--',edgecolor=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
        
    def AION(ax,text_label=r'{\bf AION-km}',text_pos=[1e-14,6e-7],rotation=51,col='#eb4034',text_col='#eb4034',fs=18,zorder=-1.1,text_on=True,Projection=False,edgealpha=1,lw=3):
        dat = loadtxt("limit_data/ScalarPhoton/Projections/AION-km.txt")
        UnfilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,linestyle='--',edgecolor=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return

    def MAGIS(ax,text_label=r'{\bf MAGIS-km}',text_pos=[3e-16,0.14e-5],rotation=32,col='#eb4034',text_col='#eb4034',fs=17,zorder=-1.1,text_on=True,Projection=False,edgealpha=1,lw=3):
        dat = loadtxt("limit_data/ScalarPhoton/Projections/MAGIS-km.txt")
        UnfilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,linestyle='--',edgecolor=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
    
    def NuclearClock(ax,text_label=r'{\bf Nuclear clock}',text_pos=[2e-19,2e-12],rotation=28,col='#703e41',text_col='#703e41',fs=20,zorder=-1.1,text_on=True,Projection=False,edgealpha=1,lw=3):
        dat = loadtxt("limit_data/ScalarPhoton/Projections/NuclearClock.txt")
        UnfilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,linestyle='--',edgecolor=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
    
    def DUAL(ax,text_label=r'{\bf DUAL}',text_pos=[0.5e-11,1e-6],rotation=0,col='#a10649',text_col='#a10649',fs=15,zorder=0,text_on=True,Projection=False,edgealpha=1,lw=1.5):
        dat = loadtxt("limit_data/ScalarPhoton/Projections/DUAL.txt")
        UnfilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,linestyle='--',edgecolor=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
    
    def Resonators(ax,text_label=r'{\bf Resonators}',ms=7,alpha=0.75,text_pos=[0.1e-9,0.9e-4],rotation=23,rotation2=45,col='#690c43',text_col='#690c43',fs=25,fs2=13,zorder=0,text_on=True,Projection=False,edgealpha=1,lw=0):
        dat = loadtxt("limit_data/ScalarPhoton/Projections/Resonator-Sapphire.txt")
        plt.plot(dat[:,0],dat[:,1],'o',ms=ms,mfc=col,mew=lw,mec='k',alpha=alpha)
        dat = loadtxt("limit_data/ScalarPhoton/Projections/Resonator-Pillar.txt")
        plt.plot(dat[:,0],dat[:,1],'o',ms=ms,mfc=col,mew=lw,mec='k',alpha=alpha)
        dat = loadtxt("limit_data/ScalarPhoton/Projections/Resonator-Quartz.txt")
        plt.plot(dat[:,0],dat[:,1],'o',ms=ms,mfc=col,mew=lw,mec='k',alpha=alpha)
        dat = loadtxt("limit_data/ScalarPhoton/Projections/Resonator-Helium.txt")
        plt.plot(dat[:,0],dat[:,1],'o',ms=ms,mfc=col,mew=lw,mec='k',alpha=alpha)

        ax.text(6.5e-11,1.2e-2,'Helium',rotation=rotation2,fontsize=fs2,color=text_col,alpha=alpha)
        ax.text(4e-10,2e-2,'Sapphire',rotation=rotation2,fontsize=fs2,color=text_col,alpha=alpha)
        ax.text(4e-9,0.7e-1,'Pillar',rotation=rotation2,fontsize=fs2,color=text_col,alpha=alpha)
        ax.text(4.5e-8,0.8e-1,'Quartz',rotation=rotation2,fontsize=fs2,color=text_col,alpha=alpha)
        plt.text(text_pos[0],text_pos[1],text_label,rotation=rotation,color=text_col,fontsize=fs)

        return

class ScalarElectron():
    
    def MICROSCOPE(ax,text_label=r'{\bf MICROSCOPE}',text_pos=[2e-24,6e-3],col='#84878c',text_col='k',fs=20,zorder=0.0,text_on=True,Projection=False,edgealpha=1,lw=3):
        dat = loadtxt("limit_data/ScalarElectron/MICROSCOPE.txt")
        FilledLimit(ax,dat,text_label,y2=1e20,text_pos=text_pos,text_col=text_col,col=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
    
    def EotWashEP(ax,text_label=r'{\bf E\"ot-Wash (EP)}',text_pos=[2e-24,0.8e-1],col='gray',text_col='k',fs=20,zorder=0.1,text_on=True,Projection=False,edgealpha=1,lw=3):
        dat = loadtxt("limit_data/ScalarElectron/EotWashEP.txt")
        FilledLimit(ax,dat,text_label,y2=1e20,text_pos=text_pos,text_col=text_col,col=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
        
    def FifthForce(ax,text_label=r'{\bf Fifth force}',text_pos=[2e-21,4e2],rotation=-28,col='darkgray',text_col='k',fs=20,zorder=0.101,text_on=True,Projection=False,edgealpha=1,lw=3):
        dat = loadtxt("limit_data/ScalarElectron/FifthForce.txt")
        FilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,col=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
    
    def RedGiants(ax,text_label=r'{\bf Red giants}',text_pos=[2e-24,7e7],col=[0.0, 0.66, 0.42],text_col='w',fs=30,zorder=2,text_on=True,Projection=False,edgealpha=1,lw=3):
        dat = loadtxt("limit_data/ScalarElectron/RedGiants.txt")
        FilledLimit(ax,dat,text_label,y2=1e20,text_pos=text_pos,text_col=text_col,col=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return

    def HSi(ax,text_label=r'{\bf H/Si}',text_pos=[1e-20,2e-4],rotation=23,col='#730f3a',text_col='w',fs=20,zorder=-0.1,text_on=True,Projection=False,edgealpha=1,lw=2):
        dat = loadtxt("limit_data/ScalarElectron/HSi.txt")
        FilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,col=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
    
    def AURIGA(ax,text_label=r'{\bf AURIGA}',text_pos=[0.8e-11,0.01e-2],rotation=-90,col='darkred',text_col='darkred',fs=17,zorder=0.01,text_on=True,Projection=False,edgealpha=1,lw=0):
        dat = loadtxt("limit_data/ScalarElectron/AURIGA.txt")
        FilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,col=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
    
    def I2(ax,text_label=r'{\bf I}$_2$',text_pos=[0.4e-12,2.5e6],rotation=20,col='#b52452',text_col='w',fs=21,zorder=0.11,text_on=True,Projection=False,edgealpha=1,lw=3):
        dat = loadtxt("limit_data/ScalarElectron/I2.txt")
        FilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,col=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
    
    def GEO600(ax,text_label=r'{\bf GEO600}',text_pos=[4e-13,1e2],rotation=0,col='#b5260d',text_col='w',fs=20,zorder=0.109,text_on=True,Projection=False,edgealpha=1,lw=3):
        dat = loadtxt("limit_data/ScalarElectron/GEO600.txt")
        FilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,col=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
    
    def HQuartzSapphire(ax,text_label=r'\center{{\bf H/Quartz/Sapphire}}',text_pos=[0.8e-18,1e4],rotation=0,col='#a81313',text_col='w',fs=20,zorder=0.11,text_on=True,Projection=False,edgealpha=1,lw=3):
        dat = loadtxt("limit_data/ScalarElectron/HQuartzSapphire.txt")
        FilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,col=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
    
    def DAMNED(ax,text_label=r'{\bf DAMNED}',text_pos=[4.6e-11,1.6e4],rotation=90,col='#b5243f',text_col='w',fs=13.5,zorder=0.12,text_on=True,Projection=False,edgealpha=1,lw=3):
        dat = loadtxt("limit_data/ScalarElectron/DAMNED.txt")
        FilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,col=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
    
    def CsCav(ax,text_label=r'{\bf Cs/Cav}',text_pos=[3e-9,0.08e7],rotation=21,col='red',text_col='w',fs=18,zorder=0.11,text_on=True,Projection=False,edgealpha=1,lw=3):
        dat = loadtxt("limit_data/ScalarElectron/CsCav.txt")
        FilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,col=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return

    def Holometer(ax,text_label=r'{\bf Holometer}',text_pos=[1.3e-9,3e4],rotation=0,col='#b53724',text_col='#b53724',fs=15,zorder=0.15,text_on=True,Projection=False,edgealpha=1,lw=3):
        dat = loadtxt("limit_data/ScalarElectron/Holometer.txt")
        FilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,col=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
    
    # Projections
    def AEDGE(ax,text_label=r'{\bf AEDGE}',text_pos=[1e-16,0.1e-11],rotation=51,col='#eb4034',text_col='#eb4034',fs=20,zorder=0,text_on=True,Projection=False,edgealpha=1,lw=3):
        dat = loadtxt("limit_data/ScalarElectron/Projections/AEDGE.txt")
        UnfilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,linestyle='--',edgecolor=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
    
    def AION(ax,text_label=r'{\bf AION-km}',text_pos=[1e-14,0.1e-5],rotation=52,col='#eb4034',text_col='#eb4034',fs=20,zorder=0,text_on=True,Projection=False,edgealpha=1,lw=3):
        dat = loadtxt("limit_data/ScalarElectron/Projections/AION-km.txt")
        UnfilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,linestyle='--',edgecolor=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return

    def MAGIS(ax,text_label=r'{\bf MAGIS-km}',text_pos=[3e-16,0.2e-6],rotation=36,col='#eb4034',text_col='#eb4034',fs=20,zorder=0,text_on=True,Projection=False,edgealpha=1,lw=3):
        dat = loadtxt("limit_data/ScalarElectron/Projections/MAGIS-km.txt")
        UnfilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,linestyle='--',edgecolor=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return    
   
        
    def DUAL(ax,text_label=r'{\bf DUAL}',text_pos=[3e-11,0.1e-4],rotation=0,col='#eb4034',text_col='#eb4034',fs=15,zorder=0,text_on=True,Projection=False,edgealpha=1,lw=1.5):
        dat = loadtxt("limit_data/ScalarElectron/Projections/DUAL.txt")
        UnfilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,linestyle='--',edgecolor=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
    
    def Resonators(ax,text_label=r'{\bf Resonators}',ms=7,alpha=0.75,text_pos=[0.1e-9,0.9e-4],rotation=23,rotation2=45,col='#690c43',text_col='#690c43',fs=25,fs2=13,zorder=0,text_on=True,Projection=False,edgealpha=1,lw=0):
        dat = loadtxt("limit_data/ScalarElectron/Projections/Resonator-Sapphire.txt")
        plt.plot(dat[:,0],dat[:,1],'o',ms=ms,mfc=col,mew=lw,mec='k',alpha=alpha)
        dat = loadtxt("limit_data/ScalarElectron/Projections/Resonator-Pillar.txt")
        plt.plot(dat[:,0],dat[:,1],'o',ms=ms,mfc=col,mew=lw,mec='k',alpha=alpha)
        dat = loadtxt("limit_data/ScalarElectron/Projections/Resonator-Quartz.txt")
        plt.plot(dat[:,0],dat[:,1],'o',ms=ms,mfc=col,mew=lw,mec='k',alpha=alpha)
        dat = loadtxt("limit_data/ScalarElectron/Projections/Resonator-Helium.txt")
        plt.plot(dat[:,0],dat[:,1],'o',ms=ms,mfc=col,mew=lw,mec='k',alpha=alpha)

        ax.text(5e-11,5e-3,'Helium',rotation=rotation2,fontsize=fs2,color=text_col,alpha=alpha)
        ax.text(3e-10,1e-2,'Sapphire',rotation=rotation2,fontsize=fs2,color=text_col,alpha=alpha)
        ax.text(3.5e-9,0.6e-1,'Pillar',rotation=rotation2,fontsize=fs2,color=text_col,alpha=alpha)
        ax.text(4e-8,0.7e-1,'Quartz',rotation=rotation2,fontsize=fs2,color=text_col,alpha=alpha)
        plt.text(text_pos[0],text_pos[1],text_label,rotation=rotation,color=text_col,fontsize=fs)

        return
    
    def OpticalMW(ax,text_label=r'{\bf Optical-MW clock}',text_pos=[3e-22,7e-8],rotation=29,col='#703e41',text_col='#703e41',fs=20,zorder=0,text_on=True,Projection=False,edgealpha=1,lw=3):
        dat = loadtxt("limit_data/ScalarElectron/Projections/OpticalMW.txt")
        UnfilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,linestyle='--',edgecolor=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
    
    def SrOH(ax,text_label=r'{\bf SrOH}',text_pos=[3e-22,20e-10],rotation=30,col='#703e41',text_col='#703e41',fs=20,zorder=0,text_on=True,Projection=False,edgealpha=1,lw=3):
        dat = loadtxt("limit_data/ScalarElectron/Projections/SrOH.txt")
        UnfilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,linestyle='--',edgecolor=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
    
    def CavityCavity(ax,text_label=r'{\bf Cavity}',text_pos=[5e-13,2e-4],rotation=25,col='#703e41',text_col='#703e41',fs=13,zorder=0,text_on=True,Projection=False,edgealpha=1,lw=3):
        dat = loadtxt("limit_data/ScalarElectron/Projections/CavityCavity.txt")
        UnfilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,linestyle='--',edgecolor=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return

class VectorBL():
    def MICROSCOPE(ax,text_label=r'{\bf MICROSCOPE}',text_pos=[1.5e-22,2e-24],col='#84878c',text_col='k',fs=17,zorder=0.1,text_on=True,Projection=False,edgealpha=1,lw=3):
        dat = loadtxt("limit_data/VectorB-L/MICROSCOPE.txt")
        FilledLimit(ax,dat,text_label,y2=1e20,text_pos=text_pos,text_col=text_col,col=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
    
    def EotWashEP(ax,text_label=r'{\bf E\"ot-Wash (EP)}',rotation=15,text_pos=[0.1e-8,0.5e-21],col='gray',text_col='k',fs=18,zorder=0.1,text_on=True,Projection=False,edgealpha=1,lw=3):
        dat = loadtxt("limit_data/VectorB-L/EotWashEP.txt")
        FilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,col=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
    
    def InverseSquareLaw(ax,text_label=r'{\bf Fifth force}',rotation=61,text_pos=[3.5e-4,0.7e-19],col='darkgray',text_col='k',fs=18,zorder=0.1,text_on=True,Projection=False,edgealpha=1,lw=3):
        dat = loadtxt("limit_data/VectorB-L/InverseSquareLaw.txt")
        FilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,col=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
    
    def Casimir(ax,text_label=r'{\bf Casimir}',rotation=60,text_pos=[3e-2,0.7e-14],col='silver',text_col='k',fs=18,zorder=0.1,text_on=True,Projection=False,edgealpha=1,lw=3):
        dat = loadtxt("limit_data/VectorB-L/Casimir.txt")
        FilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,col=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
     
    def DMStability(ax,text_label=r'{\bf DM decays}',text_pos=[1e1,5e-16],rotation=-24,col='royalblue',text_col='w',fs=20,zorder=0.0,text_on=True,Projection=False,edgealpha=1,lw=3):
        dat = loadtxt("limit_data/VectorB-L/DMStability.txt")
        FilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,col=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
    
    def Sun(ax,text_label=r'{\bf Sun}',text_pos=[0.6e2,2e-14],rotation=-45,col='forestgreen',text_col='w',fs=20,zorder=0.2,text_on=True,Projection=False,edgealpha=1,lw=3):
        dat = loadtxt("limit_data/VectorB-L/Sun.txt")
        FilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,col=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
    
    def HorizontalBranch(ax,text_label=r'{\bf HB}',text_pos=[6e2,1.5e-14],rotation=-45,col=[0.0, 0.66, 0.42],text_col='w',fs=20,zorder=0.19,text_on=True,Projection=False,edgealpha=1,lw=3):
        dat = loadtxt("limit_data/VectorB-L/HorizontalBranch.txt")
        FilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,col=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
    
    def EotWashDM(ax,text_label=r'{\bf E\"ot-Wash (DM)}',text_pos=[0.6e-17,3e-23],rotation=90,col='darkred',text_col='w',fs=20,zorder=0.2,text_on=True,Projection=False,edgealpha=1,lw=3):
        dat = loadtxt("limit_data/VectorB-L/EotWashDM.txt")
        FilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,col=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
        
    def LIGO(ax,text_label='',text_pos=[1e-13,3e-20],rotation=90,col='crimson',text_col='w',fs=17,zorder=0.21,text_on=True,Projection=False,edgealpha=1,lw=3):
        dat = loadtxt("limit_data/VectorB-L/LIGO-O1.txt")
        FilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,col=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
    
    def LIGOVirgo(ax,text_label=r'{\bf LIGO/Virgo (DM)}',text_pos=[0.5e-12,2e-21],rotation=90,col='crimson',text_col='w',fs=20,zorder=0.2,text_on=True,Projection=False,edgealpha=1,lw=3):
        dat = loadtxt("limit_data/VectorB-L/LIGOVirgo.txt")
        FilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,col=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
    
    def MAGIS(ax,text_label=r'{\bf MAGIS-100}',text_pos=[1e-20,3e-27],rotation=0,col='#a10649',text_col='#a10649',fs=21,zorder=0.0,text_on=True,Projection=False,edgealpha=1,lw=3):
        dat = loadtxt("limit_data/VectorB-L/Projections/MAGIS100-Initial.txt")
        UnfilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,edgecolor=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        dat = loadtxt("limit_data/VectorB-L/Projections/MAGIS100-Upgrade.txt")
        UnfilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,edgecolor=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        
        plt.text(3e-19,0.6e-26,'Initial',color=text_col,fontsize=fs*0.75,ha='center')
        plt.text(3e-19,2.3e-28,'Upgrade',color=text_col,fontsize=fs*0.75,ha='center')
        return
    
    def OptomechanicalMembranes(ax,text_label=r'{\bf \noindent Optomechanical \newline \indent membranes}',text_pos=[0.3e-11,0.4e-25],rotation=55,col='#961c06',text_col='#961c06',fs=15,zorder=0.25,text_on=True,Projection=False,edgealpha=1,lw=1.2):
        dat = loadtxt("limit_data/VectorB-L/Projections/OptomechanicalMembranes.txt")
        UnfilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,edgecolor=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return

    def LISA(ax,text_label=r'{\bf LISA}',text_pos=[4e-17,0.8e-25],rotation=50,col='darkred',text_col='darkred',fs=15,zorder=0.25,text_on=True,Projection=False,edgealpha=1,lw=2):
        dat = loadtxt("limit_data/VectorB-L/Projections/LISA.txt")
        UnfilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,edgecolor=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
    
    def SKA(ax,text_label=r'{\bf SKA}',text_pos=[3e-22,5e-26],rotation=60,col='green',text_col='green',fs=15,zorder=-1,text_on=True,Projection=False,edgealpha=1,lw=2):
        dat = loadtxt("limit_data/VectorB-L/Projections/SKA.txt")
        UnfilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,edgecolor=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
    
    def TorsionBalance(ax,text_label=r'{\bf Torsion balance (future)}',text_pos=[1e-14,3e-29],rotation=63,col='gray',text_col='gray',fs=15,zorder=0.0,text_on=True,Projection=False,edgealpha=1,lw=2):
        dat = loadtxt("limit_data/VectorB-L/Projections/TorsionBalance.txt")
        UnfilledLimit(ax,dat,text_label,y2=1e20,rotation=rotation,text_pos=text_pos,text_col=text_col,edgecolor=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return
