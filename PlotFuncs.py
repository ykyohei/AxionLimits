#================================PlotFuncs.py==================================#
# Created by Ciaran O'Hare 2020

# Description:
# This file has many functions which are used throughout the project, but are
# all focused around the bullshit that goes into making the plots

#==============================================================================#

from numpy import *
from numpy.random import *
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.gridspec as gridspec
from matplotlib.colors import ListedColormap
from matplotlib import colors
import matplotlib.ticker as mticker
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.cm as cm
from scipy.stats import norm
import matplotlib.patheffects as pe

pltdir = 'plots/'
pltdir_png = pltdir+'plots_png/'

txt_off = True
def switch_label(label, txt_off=txt_off):
    if txt_off:
        return ''
    else:
        return label

#==============================================================================#
def col_alpha(col,alpha=0.1):
    rgb = colors.colorConverter.to_rgb(col)
    bg_rgb = [1,1,1]
    return [alpha * c1 + (1 - alpha) * c2
            for (c1, c2) in zip(rgb, bg_rgb)]
#==============================================================================#



def FilledLimit(ax,dat,text_label='',col='ForestGreen',edgecolor='k',zorder=1,\
                    lw=2,y2=1e0,edgealpha=0.6,text_on=False,text_pos=[0,0],\
                    ha='left',va='top',clip_on=True,fs=15,text_col='k',rotation=0,facealpha=1):
    plt.plot(dat[:,0],dat[:,1],'-',color=edgecolor,alpha=edgealpha,zorder=zorder,lw=lw)
    plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,alpha=facealpha,zorder=zorder)
    if text_on:
        plt.text(text_pos[0],text_pos[1],text_label,fontsize=fs,color=text_col,\
            ha=ha,va=va,clip_on=clip_on,rotation=rotation,rotation_mode='anchor')
    return

def UnfilledLimit(ax,dat,text_label='',col='ForestGreen',edgecolor='k',zorder=1,\
                    lw=2,y2=1e0,edgealpha=0.6,text_on=False,text_pos=[0,0],\
                    ha='left',va='top',clip_on=True,fs=15,text_col='k',rotation=0,facealpha=1,\
                     linestyle='--'):
    plt.plot(dat[:,0],dat[:,1],linestyle=linestyle,color=edgecolor,alpha=edgealpha,zorder=zorder,lw=lw)
    if text_on:
        plt.text(text_pos[0],text_pos[1],text_label,fontsize=fs,color=text_col,\
            ha=ha,va=va,clip_on=clip_on,rotation=rotation,rotation_mode='anchor')
    return

# Black hole superradiance constraints on the axion mass
# can be used for any coupling
def BlackHoleSpins(ax,C,label_position,whichfile='Mehta',fs=20,col='k',alpha=0.4,\
                   PlotLine=True,rotation=90,linecolor='k',facecolor='k',text_col='k',text_on=True,zorder=0.1):
    y2 = ax.get_ylim()[-1]

    # arxiv: 2009.07206
    # BH = loadtxt("limit_data/BlackHoleSpins.txt")
    # if PlotLine:
    #     plt.plot(BH[:,0],BH[:,1],color=col,lw=3,alpha=min(alpha*2,1),zorder=0)
    # plt.fill_between(BH[:,0],BH[:,1],y2=0,edgecolor=None,facecolor=col,zorder=0,alpha=alpha)
    # if text_on:
    #     plt.text(label_position[0],label_position[1],r'{\bf Black hole spins}',fontsize=fs,color=text_col,\
    #          rotation=rotation,ha='center',rotation_mode='anchor')

    # arxiv: 2011.11646
    dat = loadtxt('limit_data/fa/BlackHoleSpins_'+whichfile+'.txt')
    dat[:,1] = dat[:,1]*C
    plt.fill_between(dat[:,0],dat[:,1],y2=0,lw=3,alpha=alpha,color=facecolor,zorder=zorder)
    if PlotLine:
        plt.plot(dat[:,0],dat[:,1],'-',lw=3,alpha=0.7,color=linecolor,zorder=zorder)
    if text_on:
        plt.text(label_position[0],label_position[1],r'{\bf Black hole spins}',fontsize=fs,color=text_col,\
            rotation=rotation,ha='center',rotation_mode='anchor')

    return

def UpperFrequencyAxis(ax,N_Hz=1,tickdir='out',xtick_rotation=0,labelsize=25,xlabel=r"$\nu_a$ [Hz]",lfs=40,tick_pad=8,tfs=25,xlabel_pad=10):
    m_min,m_max = ax.get_xlim()
    ax2 = ax.twiny()
    ax2.set_xlim([m_min*241.8*1e12/N_Hz,m_max*241.8*1e12/N_Hz])
    ax2.set_xlabel(xlabel,fontsize=lfs,labelpad=xlabel_pad)
    ax2.set_xscale('log')
    plt.xticks(rotation=xtick_rotation)
    ax2.tick_params(labelsize=tfs)
    ax2.tick_params(which='major',direction=tickdir,width=2.5,length=13,pad=tick_pad)
    ax2.tick_params(which='minor',direction=tickdir,width=1,length=10)
    locmaj = mpl.ticker.LogLocator(base=10.0, subs=(1.0, ), numticks=50)
    locmin = mpl.ticker.LogLocator(base=10.0, subs=arange(2, 10)*.1,numticks=100)
    ax2.xaxis.set_major_locator(locmaj)
    ax2.xaxis.set_minor_locator(locmin)
    ax2.xaxis.set_minor_formatter(mpl.ticker.NullFormatter())
    plt.sca(ax)

def AlternativeCouplingAxis(ax,scale=1,tickdir='out',labelsize=25,ylabel=r"$g_\gamma$ [GeV$^{-1}$]",lfs=40,tick_pad=8,tfs=25,ylabel_pad=60):
    g_min,g_max = ax.get_ylim()
    ax3 = ax.twinx()
    ax3.set_ylim([g_min*scale,g_max*scale])
    ax3.set_ylabel(ylabel,fontsize=lfs,labelpad=ylabel_pad,rotation=-90)
    ax3.set_yscale('log')
    ax3.tick_params(labelsize=tfs)
    ax3.tick_params(which='major',direction=tickdir,width=2.5,length=13,pad=tick_pad)
    ax3.tick_params(which='minor',direction=tickdir,width=1,length=10)
    locmaj = mpl.ticker.LogLocator(base=10.0, subs=(1.0, ), numticks=50)
    locmin = mpl.ticker.LogLocator(base=10.0, subs=arange(2, 10)*.1,numticks=100)
    ax3.yaxis.set_major_locator(locmaj)
    ax3.yaxis.set_minor_locator(locmin)
    ax3.yaxis.set_minor_formatter(mpl.ticker.NullFormatter())
    plt.sca(ax)

def FigSetup(xlab=r'$m_a$ [eV]',ylab='',\
                 g_min = 1.0e-19,g_max = 1.0e-6,\
                 m_min = 1.0e-12,m_max = 1.0e7,\
                 lw=2.5,lfs=45,tfs=25,tickdir='out',\
                 Grid=False,Shape='Rectangular',\
                 mathpazo=False,TopAndRightTicks=False,\
                xtick_rotation=20.0,tick_pad=8,x_labelpad=10,y_labelpad=10,\
             FrequencyAxis=False,N_Hz=1,upper_xlabel=r"$\nu_a$ [Hz]",**freq_kwargs):

    plt.rcParams['axes.linewidth'] = lw
    #plt.rc('text', usetex=True)
    plt.rc('font', family='serif',size=tfs)

    if mathpazo:
            plt.rcParams.update({
        "text.usetex": True,
        "font.family": "serif",
        "font.serif": ["Palatino"],
            })

    if Shape=='Wide':
        fig = plt.figure(figsize=(16.5,5))
    elif Shape=='Rectangular':
        fig = plt.figure(figsize=(16.5,11))
    elif Shape=='Square':
        fig = plt.figure(figsize=(14.2,14))

    ax = fig.add_subplot(111)

    ax.set_xlabel(xlab,fontsize=lfs,labelpad=x_labelpad)
    ax.set_ylabel(ylab,fontsize=lfs,labelpad=y_labelpad)

    ax.tick_params(which='major',direction=tickdir,width=2.5,length=13,right=TopAndRightTicks,top=TopAndRightTicks,pad=tick_pad)
    ax.tick_params(which='minor',direction=tickdir,width=1,length=10,right=TopAndRightTicks,top=TopAndRightTicks)

    ax.set_yscale('log')
    ax.set_xscale('log')
    ax.set_xlim([m_min,m_max])
    ax.set_ylim([g_min,g_max])

    locmaj = mpl.ticker.LogLocator(base=10.0, subs=(1.0, ), numticks=50)
    locmin = mpl.ticker.LogLocator(base=10.0, subs=arange(2, 10)*.1,numticks=100)
    ax.xaxis.set_major_locator(locmaj)
    ax.xaxis.set_minor_locator(locmin)
    ax.xaxis.set_minor_formatter(mpl.ticker.NullFormatter())

    locmaj = mpl.ticker.LogLocator(base=10.0, subs=(1.0, ), numticks=100)
    locmin = mpl.ticker.LogLocator(base=10.0, subs=arange(2, 10)*.1,numticks=100)
    ax.yaxis.set_major_locator(locmaj)
    ax.yaxis.set_minor_locator(locmin)
    ax.yaxis.set_minor_formatter(mpl.ticker.NullFormatter())

    plt.xticks(rotation=xtick_rotation)

    if Grid:
        ax.grid(zorder=0)

    if FrequencyAxis:
        UpperFrequencyAxis(ax,N_Hz=N_Hz,tickdir='out',\
                           xtick_rotation=xtick_rotation,\
                           xlabel=upper_xlabel,\
                           lfs=lfs/1.3,tfs=tfs,tick_pad=tick_pad-2,**freq_kwargs)

    return fig,ax


#==============================================================================#
class AxionPhoton():
    def QCDAxion(ax,C_logwidth=10,KSVZ_on=True,DFSZ_on=True,cmap='YlOrBr',fs=18,RescaleByMass=False,text_on=True,thick_lines=False,C_center=1,C_width=0.8,KSVZ_label_mass=1e-8,DFSZ_label_mass=5e-8,vmax=0.9):
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
        else:
            rs1 = 0.0
            rs2 = 1.0

        ## QCD Axion band:
        g_min,g_max = ax.get_ylim()
        m_min,m_max = ax.get_xlim()

        # Mass-coupling relation
        def g_x(C_ag,m_a):
            return 2e-10*C_ag*m_a
        KSVZ = 1.92
        DFSZ = 0.75

        if rs1==0:
            # Plot Band
            n = 200
            g = logspace(log10(g_min),log10(g_max),n)
            m = logspace(log10(m_min),log10(m_max),n)
            QCD = zeros(shape=(n,n))
            for i in range(0,n):
                QCD[:,i] = norm.pdf(log10(g)-log10(g_x(C_center,m[i])),0.0,C_width)
            cols = cm.get_cmap(cmap)

            cols.set_under('w') # Set lowest color to white
            vmin = amax(QCD)/(C_logwidth/4.6)
            plt.contourf(m, g, QCD, 50,cmap=cols,vmin=vmin,vmax=vmax,zorder=0)
            plt.contourf(m, g, QCD, 50,cmap=cols,vmin=vmin,vmax=vmax,zorder=0)
            plt.contourf(m, g, QCD, 50,cmap=cols,vmin=vmin,vmax=vmax,zorder=0)

            # QCD Axion models
            rot = 45.0
            trans_angle = plt.gca().transData.transform_angles(array((rot,)),array([[0, 0]]))[0]
            m2 = array([1e-9,5e-8])
            if KSVZ_on:
                if thick_lines:
                    plt.plot(m,g_x(KSVZ,m),'-',linewidth=5,color='k',zorder=0)
                    plt.plot(m,g_x(KSVZ,m),'-',linewidth=3,color=cols(0.7),zorder=0)
                else:
                    plt.plot(m,g_x(KSVZ,m),'-',linewidth=2,color=cols(1.0),zorder=0)
                if text_on:
                    plt.text(KSVZ_label_mass,g_x(KSVZ,KSVZ_label_mass)*1.05,r'{\bf KSVZ}',fontsize=fs,rotation=trans_angle,color=cols(1.0),ha='left',va='bottom',rotation_mode='anchor',clip_on=True)
            if DFSZ_on:
                if thick_lines:
                    plt.plot(m,g_x(DFSZ,m),'-',linewidth=5,color='k',zorder=0)
                    plt.plot(m,g_x(DFSZ,m),'-',linewidth=3,color=cols(0.7),zorder=0)
                else:
                    plt.plot(m,g_x(DFSZ,m),'-',linewidth=2,color=cols(1.0),zorder=0)
                if text_on:
                    plt.text(DFSZ_label_mass,g_x(DFSZ,DFSZ_label_mass)/1.5,r'{\bf DFSZ}',fontsize=fs,rotation=trans_angle,color=cols(1.0),ha='left',va='top',rotation_mode='anchor',clip_on=True)
        else:
            C_min,C_max = ax.get_ylim()
            n = 200
            C = logspace(log10(C_min),log10(C_max),n)
            m = logspace(log10(m_min),log10(m_max),n)
            QCD = zeros(shape=(n,n))
            for i in range(0,n):
                QCD[:,i] = norm.pdf(log10(C),0.0,0.8)
            cols = cm.get_cmap(cmap)
            cols.set_under('w') # Set lowest color to white
            vmin = amax(QCD)/(C_logwidth/2)
            plt.contourf(m, C, QCD, 50,cmap=cols,vmin=vmin,vmax=0.9,zorder=0)
            plt.contourf(m, C, QCD, 50,cmap=cols,vmin=vmin,vmax=0.9,zorder=0)
            plt.contourf(m, C, QCD, 50,cmap=cols,vmin=vmin,vmax=0.9,zorder=0)
            if DFSZ_on:
                if thick_lines:
                    plt.plot([m_min,m_max],[0.75,0.75],'-',lw=5,color='k')
                    plt.plot([m_min,m_max],[0.75,0.75],'-',lw=3,color='k')
                else:
                    plt.plot([m_min,m_max],[0.75,0.75],'-',lw=2,color='k')
                if text_on:
                    plt.text(DFSZ_label_mass,0.75/3,r'{\bf DFSZ II}',fontsize=fs,color='k',clip_on=True)

            if KSVZ_on:
                if thick_lines:
                    plt.plot([m_min,m_max],[1.92,1.92],'-',lw=5,color='k')
                    plt.plot([m_min,m_max],[1.92,1.92],'-',lw=3,color='k')
                else:
                    plt.plot([m_min,m_max],[1.92,1.92],'-',lw=2,color='k')
                if text_on:
                    plt.text(KSVZ_label_mass,0.75/3,r'{\bf KSVZ}',fontsize=fs,color='k',clip_on=True)
        return

    def ADMX(ax,col=[0.8, 0.0, 0.0],projection=False,fs=15,RescaleByMass=False,text_on=True,text_shift=[1,1],zorder=0.1):
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
        else:
            rs1 = 0.0
            rs2 = 1.0
        # 2018: arXiv[1804.05750]
        # 2019: arXiv[1910.08638]
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/AxionPhoton/ADMX.txt")
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=zorder)
        dat = loadtxt("limit_data/AxionPhoton/ADMX2018.txt")
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=zorder)
        dat = loadtxt("limit_data/AxionPhoton/ADMX2019_1.txt")
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=zorder)
        dat = loadtxt("limit_data/AxionPhoton/ADMX2019_2.txt")
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=zorder)
        dat = loadtxt("limit_data/AxionPhoton/ADMX2021.txt")
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=zorder)
        dat = loadtxt("limit_data/AxionPhoton/ADMX_Sidecar.txt")
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=zorder)


        if projection:
            # ADMX arXiv[1804.05750]
            dat = loadtxt("limit_data/AxionPhoton/Projections/ADMX_Projected.txt")
            plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),'-',linewidth=1.5,color=col,zorder=0)
            plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=0,alpha=0.1)
            if text_on:
                if rs1==0:
                    plt.text(1e-5*text_shift[0],2.3e-16*text_shift[1],switch_label(r'{\bf ADMX}'),fontsize=20,color=col,rotation=0,ha='left',va='top',clip_on=True)
                    plt.plot([3e-5,2e-5],[3e-16,0.6e-15],'k-',lw=1.5)
                else:
                    plt.text(0.9e-6*text_shift[0],0.15*text_shift[1],switch_label(r'{\bf ADMX}'),fontsize=fs,color=col,rotation=0,ha='left',va='top',clip_on=True)
        else:
            if text_on:
                if rs1==0:
                    plt.text(0.85e-6*text_shift[0],1e-13*text_shift[1],switch_label(r'{\bf ADMX}'),fontsize=fs,color=col,rotation=90,ha='left',va='top',clip_on=True)
                else:
                    plt.gcf().text(0.39*text_shift[0],0.5*text_shift[1],switch_label(r'{\bf ADMX}'),rotation=90,color=col)
        return

    def RBF_UF(ax,col ='darkred',fs=13,RescaleByMass=False,text_on=True,text_shift=[1,1],zorder=0.1):
        # UF: Phys. Rev. D42, 1297 (1990).
        # RBF: Phys. Rev. Lett. 59, 839 (1987).
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
        else:
            rs1 = 0.0
            rs2 = 1.0
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/AxionPhoton/RBF_UF_Haloscopes.txt")
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=zorder)

        if text_on:
            if rs1==0:
                plt.text(text_shift[0]*0.37e-5,text_shift[1]*0.8e-11,switch_label(r'{\bf RBF+UF}'),fontsize=fs,color='w',rotation=-90,ha='left',va='top',clip_on=True)
            else:
                plt.text(text_shift[0]*0.7e-5,text_shift[1]*4e3,switch_label(r'{\bf RBF}'),fontsize=fs,color='w',rotation=0,ha='center',va='top',clip_on=True)
                plt.text(text_shift[0]*0.7e-5,text_shift[1]*1e3,switch_label(r'{\bf UF}'),fontsize=fs,color='w',rotation=0,ha='center',va='top',clip_on=True)

        return

    def HAYSTAC(ax,col=[0.88, 0.07, 0.37],fs=13,RescaleByMass=False,projection=True,text_on=True,text_shift=[1,1]):
        # HAYSTAC arXiv:[1803.03690] and [2008.01853]
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
            zo = 3
        else:
            rs1 = 0.0
            rs2 = 1.0
            zo = 0
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/AxionPhoton/HAYSTAC.txt")
        dat2 = loadtxt("limit_data/AxionPhoton/HAYSTAC_2020.txt")

        if rs1==0:
            plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color=col,zorder=zo,lw=2)
            plt.plot([dat2[0,0],dat2[0,0]],[dat2[0,1]/(rs1*2e-10*dat2[0,0]+rs2),y2/(rs1*2e-10*dat2[0,0]+rs2)],color=col,zorder=zo,lw=2)

            if text_on:
                if projection==False:
                    plt.text(text_shift[0]*2.1e-5,text_shift[0]*5e-13,switch_label(r'{\bf HAYSTAC}'),fontsize=fs,color=col,rotation=-90,ha='left',va='top',clip_on=True)
        else:
            plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color='k',zorder=zo,lw=4)
            plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color=col,zorder=zo,lw=3)
            plt.plot(dat[0,0],dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),'.',markersize=15,color=col,markeredgecolor='k',zorder=zo)

            plt.plot([dat2[0,0],dat2[0,0]],[dat2[0,1]/(rs1*2e-10*dat2[0,0]+rs2),y2/(rs1*2e-10*dat2[0,0]+rs2)],color='k',zorder=zo,lw=4)
            plt.plot([dat2[0,0],dat2[0,0]],[dat2[0,1]/(rs1*2e-10*dat2[0,0]+rs2),y2/(rs1*2e-10*dat2[0,0]+rs2)],color=col,zorder=zo,lw=3)
            plt.text(text_shift[0]*dat2[0,0]*1.1,text_shift[1]*y2*1.2,switch_label(r'{\bf HAYSTAC}'),fontsize=fs,color=col,rotation=40,ha='left',rotation_mode='anchor')
            plt.plot(dat2[0,0],dat2[0,1]/(rs1*2e-10*dat2[0,0]+rs2),'.',markersize=15,color=col,markeredgecolor='k',zorder=zo)
        return

    def TASEH(ax,col=[0.88, 0.07, 0.24],fs=13,RescaleByMass=False,projection=True,text_on=True,text_shift=[1,1]):
        # TASEH https://arxiv.org/pdf/2205.05574.pdf
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
            zo = 3
        else:
            rs1 = 0.0
            rs2 = 1.0
            zo = 0
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/AxionPhoton/TASEH.txt")

        if rs1==0:
            plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color=col,zorder=zo,lw=2)
        return

    def CAPP(ax,col=[1, 0.1, 0.37],fs=15,RescaleByMass=False,text_on=True,text_shift=[1,1]):
        y2 = ax.get_ylim()[1]
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
            zo = 3
        else:
            rs1 = 0.0
            rs2 = 1.0
            zo = 0
        dat = loadtxt("limit_data/AxionPhoton/CAPP-1.txt")
        dat2 = loadtxt("limit_data/AxionPhoton/CAPP-2.txt")
        dat3 = loadtxt("limit_data/AxionPhoton/CAPP-3.txt")
        dat4 = loadtxt("limit_data/AxionPhoton/CAPP-4.txt")
        if rs1==0:
            plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color=col,zorder=zo,lw=3)
            plt.fill_between(dat2[:,0],dat2[:,1]/(rs1*2e-10*dat2[0,0]+rs2),y2=y2,color=col,zorder=zo)
            plt.fill_between(dat3[:,0],dat3[:,1]/(rs1*2e-10*dat3[0,0]+rs2),y2=y2,color=col,zorder=zo)
            plt.fill_between(dat4[:,0],dat4[:,1]/(rs1*2e-10*dat4[0,0]+rs2),y2=y2,color=col,zorder=zo)

            if text_on:
                plt.text(text_shift[0]*0.8e-5,text_shift[1]*0.1e-13,switch_label(r'{\bf CAPP}'),fontsize=fs,color=col,rotation=90,ha='center',va='top',clip_on=True)
        else:
            plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color='k',zorder=zo,lw=4)
            plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color=col,zorder=zo,lw=3)
            if text_on:
                plt.text(text_shift[0]*dat[0,0]*1.1,text_shift[1]*y2*1.8,switch_label(r'{\bf CAPP}'),fontsize=fs,color=col,rotation=40,ha='left',va='top',rotation_mode='anchor')
            plt.plot(dat[0,0],dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),'.',markersize=15,color=col,markeredgecolor='k',zorder=zo)
            imin = argmin(dat2[:,1])
            plt.plot(dat2[imin,0],dat2[imin,1]/(rs1*2e-10*dat2[0,0]+rs2),'.',markersize=15,color=col,markeredgecolor='k',zorder=zo)
            imin = argmin(dat3[:,1])
            plt.plot(dat3[imin,0],dat3[imin,1]/(rs1*2e-10*dat3[0,0]+rs2),'.',markersize=15,color=col,markeredgecolor='k',zorder=zo)
            plt.fill_between(dat2[:,0],dat2[:,1]/(rs1*2e-10*dat2[0,0]+rs2),y2=y2,color=col)
            plt.fill_between(dat3[:,0],dat3[:,1]/(rs1*2e-10*dat3[0,0]+rs2),y2=y2,color=col)
            plt.fill_between(dat4[:,0],dat4[:,1]/(rs1*2e-10*dat4[0,0]+rs2),y2=y2,color=col)

        return

    def QUAX(ax,col='crimson',fs=13,RescaleByMass=False,text_on=True,text_shift=[1,1],projection=False):
        # QUAX1 arXiv:[1903.06547]
        # QUAX2 arXiv:[2012.09498]
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
            zo = 3
        else:
            rs1 = 0.0
            rs2 = 1.0
            zo = 0
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/AxionPhoton/QUAX.txt")
        dat2 = loadtxt("limit_data/AxionPhoton/QUAX2.txt")

        if rs1==0:
            plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color=col,lw=2,zorder=zo)
            plt.plot([dat2[0,0],dat2[0,0]],[dat2[0,1]/(rs1*2e-10*dat2[0,0]+rs2),y2/(rs1*2e-10*dat2[0,0]+rs2)],color=col,lw=2,zorder=zo)

            if text_on:
                plt.text(text_shift[0]*6.3e-5,text_shift[1]*0.05e-11,switch_label(r'{\bf QUAX}'),fontsize=fs,color=col,rotation=-90,ha='center',va='top',clip_on=True)
        else:
            plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color='k',lw=4,zorder=zo)
            plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color=col,lw=3,zorder=zo)
            plt.plot([dat2[0,0],dat2[0,0]],[dat2[0,1]/(rs1*2e-10*dat2[0,0]+rs2),y2/(rs1*2e-10*dat2[0,0]+rs2)],color='k',lw=4,zorder=zo)
            plt.plot([dat2[0,0],dat2[0,0]],[dat2[0,1]/(rs1*2e-10*dat2[0,0]+rs2),y2/(rs1*2e-10*dat2[0,0]+rs2)],color=col,lw=3,zorder=zo)
            if text_on:
                plt.text(text_shift[0]*dat2[0,0]*1.2,text_shift[1]*y2*1.2,switch_label(r'{\bf QUAX}'),fontsize=fs,color=col,rotation=40,ha='left',rotation_mode='anchor')
            plt.plot(dat[0,0],dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),'.',markersize=15,color=col,markeredgecolor='k',zorder=zo)
            plt.plot(dat2[0,0],dat2[0,1]/(rs1*2e-10*dat2[0,0]+rs2),'.',markersize=15,color=col,markeredgecolor='k',zorder=zo)

        if projection==True:
            dat = loadtxt("limit_data/AxionPhoton/Projections/QUAX2005.txt")
            plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),'-',linewidth=1.5,color=col,zorder=0)
            plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=0,alpha=0.2)
            if rs1==1.0:
                plt.text(2.5e-5,0.8e-1,r'{\bf QUAX}',color=col,fontsize=18)
                plt.plot([4.0e-5,4.0e-5],[2.2e-1,2.1e0],'k-',lw=1.5)
        return

    def ABRACADABRA(ax,col=[0.83, 0.07, 0.37],fs=15,projection=False,RescaleByMass=False,text_on=True,lw=1,text_shift=[1,1],edgealpha=1):
        # ABRACADABRA arXiv:[1810.12257]
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
        else:
            rs1 = 0.0
            rs2 = 1.0
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/AxionPhoton/ABRACADABRA.txt")
        n = shape(dat)[0]
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=2)
        x = dat[arange(0,n,20),0]
        y = dat[arange(0,n,20),1]
        y[-1] = y2
        plt.plot(x,y/(rs1*2e-10*x+rs2),'k-',lw=lw,zorder=2.01,alpha=edgealpha)


        dat = loadtxt("limit_data/AxionPhoton/ABRACADABRA_run2.txt")
        n = shape(dat)[0]
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=2.02)
        x = dat[arange(0,n,1),0]
        y = dat[arange(0,n,1),1]
        y[-1] = y2
        plt.plot(x,y/(rs1*2e-10*x+rs2),'k-',lw=lw,zorder=2.02,alpha=edgealpha)


        if text_on:
            if rs1==0:
                plt.text(text_shift[0]*1.5e-9,text_shift[1]*3e-8,r'{\bf ABRA}',fontsize=fs,color='w',rotation=0,ha='center',va='top',zorder=10,clip_on=True)
                plt.text(text_shift[0]*1.5e-9,text_shift[1]*1e-8,r'10 cm',fontsize=fs,color='w',rotation=0,ha='center',va='top',zorder=10,clip_on=True)

        if projection:
            dat = loadtxt("limit_data/AxionPhoton/Projections/ABRACADABRA.txt")
            plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),'-',linewidth=1.5,color=col,zorder=0)
            plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=0,alpha=0.1)
            if text_on:
                if rs1==0:
                    plt.text(text_shift[0]*5e-12,text_shift[1]*4e-18,r'{\bf ABRACADABRA}',fontsize=fs-1,color=col,rotation=13,ha='left',va='top',clip_on=True)
                else:
                    plt.text(text_shift[0]*1.3e-9,text_shift[1]*1.0e2,r'{\bf ABRACADABRA}',fontsize=fs-1,color=col,rotation=0,ha='left',va='top',clip_on=True)
                    plt.plot([dat[-1,0],dat[-1,0]],[dat[-1,1]/(rs1*2e-10*dat[-1,0]+rs2),1e6],lw=1.5,color=col,zorder=0)
        return

    def DMRadio(ax,col=[0.83, 0.07, 0.37],fs=23,text_on=True,RescaleByMass=False,lw=2,text_shift=[1,1],linestyle='-',rotation=90):
        y2 = ax.get_ylim()[1]
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
        else:
            rs1 = 0.0
            rs2 = 1.0
        dat = loadtxt('limit_data/AxionPhoton/Projections/DMRadio.txt')
        plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),linestyle=linestyle,linewidth=2,color=col,zorder=0)
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=0,alpha=0.1)
        if text_on:
            if rs1==0:
                plt.text(text_shift[0]*2e-10,text_shift[1]*0.05e-16,r'{\bf DM-Radio}',color='crimson',fontsize=20,rotation=rotation,clip_on=True)
            else:
                plt.text(text_shift[0]*5e-9,text_shift[1]*4.0e-1,r'{\bf DM-Radio}',fontsize=fs-1,color=col,rotation=0,ha='left',va='top',clip_on=True)
        return


    def SRF(ax,col=[0.83, 0.07, 0.37],fs=20,text_on=True,RescaleByMass=False,lw=2,text_shift=[1,1],linestyle='-',rotation=-40):
        y2 = ax.get_ylim()[1]
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
        else:
            rs1 = 0.0
            rs2 = 1.0
        dat = loadtxt('limit_data/AxionPhoton/Projections/SRF.txt')
        plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),linestyle=linestyle,linewidth=2,color=col,zorder=0.0)
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=0.0,alpha=0.1)
        if text_on:
            if rs1==0:
                plt.text(text_shift[0]*1.5e-11,text_shift[1]*0.7e-18,r'{\bf SRF-m$^3$}',color='crimson',fontsize=20,rotation=rotation,clip_on=True)
            else:
                plt.text(text_shift[0]*5e-9,text_shift[1]*4.0e-1,r'{\bf SRF-m$^3$}',fontsize=fs-1,color=col,rotation=0,ha='left',va='top',clip_on=True)
        return

    def WISPLC(ax,col=[0.8, 0.07, 0.37],fs=15,text_on=True,RescaleByMass=False,lw=2,text_shift=[1,1],linestyle='-',rotation=14):
        y2 = ax.get_ylim()[1]
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
        else:
            rs1 = 0.0
            rs2 = 1.0
        dat = loadtxt('limit_data/AxionPhoton/Projections/WISPLC.txt')
        plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),linestyle=linestyle,linewidth=2,color=col,zorder=0)
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=0,alpha=0.1)
        if text_on:
            if rs1==0:
                plt.text(text_shift[0]*2e-11,text_shift[1]*8e-16,r'{\bf WISPLC}',color='crimson',fontsize=fs,rotation=rotation,clip_on=True)
            else:
                plt.text(text_shift[0]*1.5e-9,text_shift[1]*1.5e4,r'{\bf WISPLC}',fontsize=fs+1,color=col,rotation=-14,ha='left',va='top',clip_on=True)
        return

    def ORGAN(ax,col=[0.8, 0.0, 0.0],projection=False,fs=15,RescaleByMass=False,text_on=True,text_shift=[1,1],lw=0.5):
        # ORGAN arXiv[1706.00209]
        y2 = ax.get_ylim()[1]
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
            zo = 6
        else:
            rs1 = 0.0
            rs2 = 1.0
            zo = 0
        dat = loadtxt("limit_data/AxionPhoton/ORGAN.txt")
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=col,facecolor=col,zorder=0.1,lw=1)

        dat2 = loadtxt("limit_data/AxionPhoton/ORGAN-1a.txt")
        plt.fill_between(dat2[:,0],dat2[:,1]/(rs1*2e-10*dat2[:,0]+rs2),y2=y2,edgecolor='k',facecolor=col,zorder=0.1,lw=lw)

        if projection:
            dat = loadtxt("limit_data/AxionPhoton/Projections/ORGAN_Projected.txt")
            plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),'-',linewidth=1.5,color=col,zorder=0)
            plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=0,alpha=0.2)
            if text_on:
                if rs1==0:
                    plt.text(text_shift[0]*5e-4,text_shift[1]*1.15e-14,switch_label(r'{\bf ORGAN}'),fontsize=18,color=col,rotation=0,ha='left',va='top',clip_on=True)
                    plt.plot([5e-4,1.5e-4],[1.3e-14,6e-13],'k-',lw=1.5)
                else:
                    plt.text(text_shift[0]*1.2e-4,text_shift[1]*1e3,switch_label(r'{\bf ORGAN}'),fontsize=18,color='darkred',rotation=-90,ha='left',va='top',clip_on=True)

        else:
            if RescaleByMass:
                plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color='k',lw=4,zorder=zo)
            plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color=col,lw=1,zorder=zo)
            if RescaleByMass:
                plt.plot(dat[0,0],dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),'.',markersize=15,color=col,markeredgecolor='k',zorder=zo)
            if text_on:
                if rs1==0:
                    plt.text(text_shift[0]*110e-6,text_shift[1]*1e-11,switch_label(r'{\bf ORGAN}'),fontsize=fs,color=col,rotation=-90,ha='left',va='top',clip_on=True)
                else:
                    plt.text(text_shift[0]*dat[0,0]*1.1,text_shift[1]*y2*1.2,switch_label(r'{\bf ORGAN}'),fontsize=fs-3,color=col,rotation=40,ha='left',rotation_mode='anchor')
                    plt.text(text_shift[0]*6e-5,text_shift[1]*1e2,switch_label(r'{\bf ORGAN}'),fontsize=fs-6,color=col,rotation=90,ha='left',rotation_mode='anchor')
        return

    def RADES(ax,col='blueviolet',fs=15,RescaleByMass=False,text_on=True,text_shift=[1,1]):
        # RADES 2104.13798
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
            zo = 6
        else:
            rs1 = 0.0
            rs2 = 1.0
            zo = 0
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/AxionPhoton/RADES.txt")

        if rs1==0:
            plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color=col,lw=2,zorder=zo)
        else:
            plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color='k',lw=4,zorder=zo)
            plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color=col,lw=3,zorder=zo)
            if text_on:
                plt.text(text_shift[0]*dat[0,0]*0.88,text_shift[1]*y2*1.2,r'{\bf RADES}',fontsize=fs,color=col,rotation=40,ha='left',rotation_mode='anchor')
            plt.plot(dat[0,0],dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),'.',markersize=15,color=col,markeredgecolor='k',zorder=zo)

        return

    def GrAHal(ax,col='#b53e5a',fs=15,RescaleByMass=False,text_on=True,text_shift=[1,1]):
        # Grenoble haloscope  2110.14406
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
            zo = 6
        else:
            rs1 = 0.0
            rs2 = 1.0
            zo = 0
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/AxionPhoton/GrAHal.txt")

        if rs1==0:
            plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color=col,lw=2,zorder=zo)
        else:
            plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color='k',lw=4,zorder=zo)
            plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color=col,lw=3,zorder=zo)
            if text_on:
                plt.text(text_shift[0]*dat[0,0]*0.88,text_shift[1]*y2*1.2,r'{\bf GrAHal}',fontsize=fs,color=col,rotation=40,ha='left',rotation_mode='anchor')
            plt.plot(dat[0,0],dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),'.',markersize=15,color=col,markeredgecolor='k',zorder=zo)

        return

    def MADMAX(ax,col='darkred',fs=18,RescaleByMass=False,text_on=True,text_shift=[1,1]):
        # MADMAX arXiv[2003.10894]
        y2 = ax.get_ylim()[1]
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
        else:
            rs1 = 0.0
            rs2 = 1.0
        dat = loadtxt("limit_data/AxionPhoton/Projections/MADMAX.txt")
        plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),'-',linewidth=1.5,color=col,zorder=0)
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=0,alpha=0.2)
        if text_on:
            if rs1==0:
                plt.text(text_shift[0]*1.5e-4,text_shift[1]*3.5e-15,r'{\bf MADMAX}',fontsize=18,color=col,rotation=0,ha='left',va='top',clip_on=True)
                plt.plot([3e-4,1.3e-4],[4.5e-15,2.6e-14],'k-',lw=1.5)
            else:
                plt.text(text_shift[0]*5e-5,text_shift[1]*3.5e0,r'{\bf MADMAX}',fontsize=14,color=col,rotation=0,ha='left',va='top',clip_on=True)

        return

    def ALPHA(ax,col='darkred',fs=18,RescaleByMass=False,text_on=True,text_shift=[1,1]):
        # Plasma Haloscope arXiv[1904.11872]
        y2 = ax.get_ylim()[1]
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
        else:
            rs1 = 0.0
            rs2 = 1.0
        dat = loadtxt("limit_data/AxionPhoton/Projections/ALPHA.txt")
        plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),'-',linewidth=2,color=col,zorder=0)
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=0,alpha=0.2)
        if text_on:
            if rs1==0:
                plt.text(text_shift[0]*1.5e-4,text_shift[1]*1e-15,r'{\bf ALPHA}',fontsize=18,color=col,rotation=0,ha='left',va='top',clip_on=True)
                plt.plot([1.3e-4,0.5e-4],[1e-15,0.7e-14],'k-',lw=1.5)
            else:
                plt.text(text_shift[0]*2.3e-4,text_shift[1]*5e-1,r'{\bf ALPHA}',fontsize=fs,color=col,rotation=0,ha='center',va='top',clip_on=True)
                #plt.text(2.3e-4,2e-1,r'{\bf haloscope}',fontsize=fs,color=col,rotation=0,ha='center',va='top')
        return

    def FLASH(ax,col='darkred',fs=15,RescaleByMass=False,text_on=True,text_shift=[1,1]):
        # FLASH https://indico.cern.ch/event/1115163/
        y2 = ax.get_ylim()[1]
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
        else:
            rs1 = 0.0
            rs2 = 1.0
        dat = loadtxt("limit_data/AxionPhoton/Projections/FLASH.txt")
        plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),'-',linewidth=1.5,color=col,zorder=0)
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,facecolor=col,zorder=0,alpha=0.3)
        if text_on:
            if rs1==0:
                plt.text(text_shift[0]*2.5e-6,text_shift[1]*0.45e-16,r'{\bf FLASH}',fontsize=20,color=col,rotation=0,ha='left',va='top',clip_on=True)
                plt.plot([1.2e-6,2.5e-6],[5e-16,0.6e-16],'k-',lw=1.5)
            else:
                plt.text(text_shift[0]*3e-7,text_shift[1]*3e0,r'{\bf FLASH}',rotation=90,fontsize=fs,color=col,ha='left',va='top',rotation_mode='anchor',clip_on=True)
        return

    def CADEx(ax,col='firebrick',fs=15,RescaleByMass=False,text_on=True,text_shift=[1,1]):
        y2 = ax.get_ylim()[1]
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
        else:
            rs1 = 0.0
            rs2 = 1.0
        dat = loadtxt("limit_data/AxionPhoton/Projections/CADEx.txt")
        plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),'-',linewidth=1.5,color=col,zorder=0)
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,facecolor=col,zorder=0,alpha=0.1)
        if text_on:
            if rs1==0:
                plt.text(text_shift[0]*1.1e-3,text_shift[1]*0.35e-13,r'{\bf CADEx}',fontsize=18,color=col,rotation=0,ha='left',va='top',clip_on=True)
                plt.plot([1.3e-3,0.4e-3],[0.45e-13,2e-12],'k-',lw=1.5)
            else:
                plt.text(text_shift[0]*5e-4,text_shift[1]*1e2,r'{\bf CADEx}',fontsize=fs,rotation=-90,color=col,clip_on=True)

        return

    def BRASS(ax,col='darkred',fs=15,RescaleByMass=False,text_on=True,text_shift=[1,1]):
        # BRASS http://www.iexp.uni-hamburg.de/groups/astroparticle/brass/brassweb.htm
        y2 = ax.get_ylim()[1]
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
        else:
            rs1 = 0.0
            rs2 = 1.0
        dat = loadtxt("limit_data/AxionPhoton/Projections/BRASS.txt")
        plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),'-',linewidth=1.5,color=col,zorder=0)
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,facecolor=col,zorder=0,alpha=0.1)
        if text_on:
            if rs1==0:
                plt.text(text_shift[0]*2.4e-3,text_shift[1]*0.98e-13,r'{\bf BRASS}',fontsize=18,color=col,rotation=0,ha='left',va='top',clip_on=True)
                plt.plot([2.1e-3,0.7e-3],[0.95e-13,1.9e-12],'k-',lw=1.5)
            else:
                plt.text(text_shift[0]*0.45e-3,text_shift[1]*1e1,r'{\bf BRASS}',fontsize=20,rotation=9,color=col,clip_on=True)

        return

    def BREAD(ax,col='firebrick',fs=15,RescaleByMass=False,text_on=True,text_shift=[1,1]):
        y2 = ax.get_ylim()[1]
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
        else:
            rs1 = 0.0
            rs2 = 1.0
        dat = loadtxt("limit_data/AxionPhoton/Projections/BREAD.txt")
        plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),'-',linewidth=1.5,color=col,zorder=0)
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,facecolor=col,zorder=0,alpha=0.1)
        if text_on:
            if rs1==0:
                plt.text(text_shift[0]*7e-3,text_shift[1]*2.5e-13,r'{\bf BREAD}',fontsize=18,color=col,rotation=0,ha='left',va='top',clip_on=True)
                plt.plot([5.5e-3,3e-3],[1.9e-13,2.9e-13],'k-',lw=1.5)
            else:
                plt.text(text_shift[0]*2e-3,text_shift[1]*1e-1,r'{\bf BREAD}',fontsize=18,rotation=0,color=col,clip_on=True)

        return

    def TOORAD(ax,col=[0.8, 0.1, 0.2],fs=15,RescaleByMass=False,text_on=True,text_shift=[1,0.5]):
        # TOORAD arXiv[1807.08810]
        y2 = ax.get_ylim()[1]
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
        else:
            rs1 = 0.0
            rs2 = 1.0
        dat = loadtxt("limit_data/AxionPhoton/Projections/TOORAD.txt")
        dat[:,0] *= 1e-3
        plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),'-',linewidth=1.5,color=col,zorder=0)
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,facecolor=col,zorder=0,alpha=0.1)
        if text_on:
            if rs1==0:
                plt.text(text_shift[0]*0.7e-2,text_shift[1]*3e-11,r'{\bf TOO}',fontsize=12,ha='center',color=col,clip_on=True)
                plt.text(text_shift[0]*0.7e-2,text_shift[1]*1.5e-11,r'{\bf RAD}',fontsize=12,ha='center',color=col,clip_on=True)
            else:
                #plt.text((1-0.05)*text_shift[0]*0.25e-2,(1+0.05)*text_shift[1]*0.3e2,r'{\bf TOORAD}',fontsize=18,rotation=-21,color='k',clip_on=True)
                plt.text(text_shift[0]*0.25e-2,text_shift[1]*0.3e2,r'{\bf TOORAD}',fontsize=18,rotation=-21,color=col,clip_on=True,path_effects=line_background(1,'k'))
        return

    def LAMPOST(ax,col=[0.8, 0.1, 0.2],fs=15,RescaleByMass=False,text_on=True,text_shift=[1,1],rotation=55):
        # LAMPOST arXiv[1803.11455]
        y2 = ax.get_ylim()[1]
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
        else:
            rs1 = 0.0
            rs2 = 1.0
        dat = loadtxt("limit_data/AxionPhoton/Projections/LAMPOST.txt",delimiter=',')
        plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),'-',linewidth=1.5,color=col,zorder=0)
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,facecolor=col,zorder=0,alpha=0.1)
        if text_on:
            if rs1==0:
                plt.text(text_shift[0]*1.55e-1,text_shift[1]*3.5e-11,r'{\bf LAMPOST}',rotation=rotation,fontsize=fs,color=col,ha='left',va='top',clip_on=True)
            else:
                plt.text(text_shift[0]*0.9e-1,text_shift[1]*1.9e-1,r'{\bf LAMPOST}',rotation=0,fontsize=fs,color=col,ha='left',va='top',clip_on=True)

        return

    # Low mass ALP haloscopes
    def DANCE(ax,col=[0.8, 0.1, 0.2],fs=14,text_on=True,text_pos=[1.5e-12,1.7e-13]):
        # DANCE arXiv[1911.05196]
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/AxionPhoton/Projections/DANCE.txt")
        plt.plot(dat[:,0],dat[:,1],'-',linewidth=1.5,color=col,zorder=0)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,facecolor=col,zorder=0,alpha=0.1)
        if text_on:
            plt.text(text_pos[0],text_pos[1],r'{\bf DANCE}',rotation=50,fontsize=fs,color=col,ha='left',va='top',clip_on=True)
        return

    def aLIGO(ax,col=[0.8, 0.1, 0.2],fs=15,text_on=True,text_pos=[0.2e-9,0.35e-13]):
        # aLIGO arXiv[1903.02017]
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/AxionPhoton/Projections/aLIGO.txt")
        plt.plot(dat[:,0],dat[:,1],'-',linewidth=1.5,color=col,zorder=0)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,facecolor=col,zorder=0,alpha=0.1)
        if text_on:
            plt.text(text_pos[0],text_pos[1],r'{\bf aLIGO}',rotation=0,fontsize=fs,color=col,ha='left',va='top',clip_on=True)
        return

    def ADBC(ax,col=[0.8, 0.1, 0.2],fs=15,text_on=True,text_pos=[1.3e-11,1.65e-12],rotation=26):
        # ADBC arXiv[1809.01656]
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/AxionPhoton/Projections/ADBC.txt")
        plt.plot(dat[:,0],dat[:,1],'-',linewidth=1.5,color=col,zorder=0)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,facecolor=col,zorder=0,alpha=0.1)
        if text_on:
            plt.text(text_pos[0],text_pos[1],r'{\bf ADBC}',rotation=rotation,fontsize=fs,color=col,ha='left',va='top',clip_on=True)
        return

    def SHAFT(ax,col='red',fs=16,text_on=True,lw=1,text_pos=[0.8e-10,3e-10],rotation=0,zorder=1.8,edgealpha=1):
        # SHAFT arXiv:[2003.03348]
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/AxionPhoton/SHAFT.txt")
        n = shape(dat)[0]
        x = dat[arange(0,n,2),0]
        y = dat[arange(0,n,2),1]
        y[-1] = y2
        plt.plot(x,y,'k-',lw=lw,zorder=1.81,alpha=edgealpha)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=zorder)
        if text_on:
            plt.text(text_pos[0],text_pos[1],r'{\bf SHAFT}',fontsize=fs,color='w',rotation=rotation,ha='center',va='top',clip_on=True)
        return

    def UPLOAD(ax,col='tomato',fs=16,text_on=False):
        # UPLOAD arXiv:[1912.07751]
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/AxionPhoton/UPLOAD.txt")
        n = shape(dat)[0]
        x = dat[arange(0,n,2),0]
        y = dat[arange(0,n,2),1]
        y[-1] = y2
        plt.plot(x,y,'k-',lw=1,zorder=10,alpha=0.9)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=1.8)
        #if text_on:

        #    plt.text(0.8e-9,3e-8,r'{\bf UPLOAD}',fontsize=fs,color='w',rotation=-90,ha='center',va='top',zorder=9,clip_on=True)
        return


    def BASE(ax,col='crimson',fs=15,RescaleByMass=False,text_on=True,text_shift=[1,1],zorder=1.9,lw=2.5,arrow_on=True):
        # BASE https://inspirehep.net/literature/1843024
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
            zo = zorder
        else:
            rs1 = 0.0
            rs2 = 1.0
            zo = zorder
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/AxionPhoton/BASE.txt")

        if arrow_on:
            fig = plt.gcf()
            plt.arrow(0.265, 0.535, 0, 0.035, transform=fig.transFigure,figure=fig,
              length_includes_head=True,lw=1,
              head_width=0.007, head_length=0.016, overhang=0.13,
              edgecolor='crimson',facecolor='crimson',clip_on=True)

        if rs1==0:
            plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color=col,lw=lw,zorder=zo)
            if text_on:
                plt.text(text_shift[0]*3e-9,text_shift[1]*1.e-12,r'{\bf BASE}',fontsize=fs,color=col,rotation=90,ha='center',va='top',clip_on=True)
        else:
            plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color='k',lw=lw+2,zorder=zo)
            plt.plot([dat[0,0],dat[0,0]],[dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),y2/(rs1*2e-10*dat[0,0]+rs2)],color=col,lw=lw+1,zorder=zo)
            if text_on:
                plt.text(text_shift[0]*dat[0,0]*1.2,text_shift[1]*y2*1.2,r'{\bf BASE}',fontsize=fs,color=col,rotation=40,ha='left',rotation_mode='anchor')
            plt.plot(dat[0,0],dat[0,1]/(rs1*2e-10*dat[0,0]+rs2),'.',markersize=15,color=col,markeredgecolor='k',zorder=zo)

        return

    def ADMX_SLIC(ax,col='crimson',fs=12,RescaleByMass=False,text_on=True,text_shift=[1,1],zorder=0.005):
        # ADMX SLIC https://arxiv.org/pdf/1911.05772.pdf
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
            zo = zorder
        else:
            rs1 = 0.0
            rs2 = 1.0
            zo = zorder
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/AxionPhoton/ADMX_SLIC.txt")
        x = mean(dat[:,0])
        y = amin(dat[:,1])
        if rs1==0:
            plt.plot([x,x],[y/(rs1*2e-10*x+rs2),y2/(rs1*2e-10*x+rs2)],color=col,lw=2,zorder=zorder)
            if text_on:
                plt.text(text_shift[0]*2.4e-7,text_shift[1]*0.4e-11,switch_label(r'{\bf ADMX SLIC}'),fontsize=fs,color=col,rotation=-90,ha='center',va='top',clip_on=True)
        else:
            plt.plot([x,x],[y/(rs1*2e-10*x+rs2),y2/(rs1*2e-10*x+rs2)],color='k',lw=4,zorder=zorder)
            plt.plot([x,x],[y/(rs1*2e-10*x+rs2),y2/(rs1*2e-10*x+rs2)],color=col,lw=3,zorder=zorder)
            if text_on:
                plt.text(text_shift[0]*x,text_shift[1]*y2*1.2,switch_label(r'{\bf ADMX SLIC}'),fontsize=fs,color=col,rotation=40,ha='left',rotation_mode='anchor')
            plt.plot(x,y/(rs1*2e-10*x+rs2),'.',markersize=15,color=col,markeredgecolor='k',zorder=zorder)

        return

    def ALPS(ax,projection=True,col=[0.8, 0.25, 0.33],fs=15,lw=2,RescaleByMass=False,text_on=True,lw_proj=1.5,lsty_proj='-',col_proj='k',text_shift_x=1,text_shift_y=1,block=True):
        # ALPS-I arXiv:[1004.1313]
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
        else:
            rs1 = 0.0
            rs2 = 1.0

        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/AxionPhoton/ALPS.txt")

        plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),'k-',lw=lw,zorder=1.53,alpha=1)
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=1.53,lw=0.01)
        if rs1==0:
            if text_on: plt.text(1e-5*text_shift_x,8e-8*text_shift_y,r'{\bf ALPS-I}',fontsize=20,color='w',clip_on=True)
        if projection:
            dat = loadtxt("limit_data/AxionPhoton/Projections/ALPS-II.txt")
            if block:
                mask = dat[:,0]<0.85e-6
                dat[mask,0] = nan
            plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),linestyle=lsty_proj,lw=lw_proj,zorder=1.5,color=col_proj,alpha=0.5)
            if RescaleByMass:
                plt.text(9e-4*text_shift_x,2.5e3*text_shift_y,r'{\bf ALPS-II}',fontsize=20,color='k',rotation=20,alpha=0.5,clip_on=True)
            else:
                if text_on: plt.text(1.5e-3*text_shift_x,3e-9*text_shift_y,r'{\bf ALPS-II}',rotation=60,fontsize=18,color='w',zorder=10,clip_on=True)
        return

    def SAPPHIRES(ax,text_label=r'{\bf SAPPHIRES}',rotation=-57,text_pos=[1.4e-2,2e-1],col=[0.8, 0.2, 0.25],text_col='w',fs=15,zorder=1.6,text_on=True,edgealpha=1,lw=2):
        # SAPPHIRES arXiv:[2105.01224]
        dat = loadtxt("limit_data/AxionPhoton/SAPPHIRES.txt")
        FilledLimit(ax,dat,text_label,text_pos=text_pos,col=col,text_col=text_col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw,rotation=rotation)
        return


    def OSQAR(ax,text_label=r'{\bf OSQAR}',text_pos=[1e-5,3e-8],col=[0.6, 0.2, 0.25],text_col='w',fs=17,zorder=1.52,text_on=True,edgealpha=1,lw=2):
        # OSQAR arXiv:[]
        dat = loadtxt("limit_data/AxionPhoton/OSQAR.txt")
        FilledLimit(ax,dat,text_label,text_pos=text_pos,col=col,text_col=text_col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return

    def PVLAS(ax,text_label=r'{\bf PVLAS}',text_pos=[2e-3,9e-8],col=[0.4, 0.2, 0.2],text_col='w',fs=17,zorder=1.51,text_on=True,edgealpha=1,rotation=45,lw=2):
        # PVLAS arXiv:[]
        dat = loadtxt("limit_data/AxionPhoton/PVLAS.txt")
        FilledLimit(ax,dat,text_label,text_pos=text_pos,col=col,text_col=text_col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,rotation=rotation,lw=lw)
        return

    def CROWS(ax,text_label=r'{\bf CROWS}',text_pos=[1e-7,2.5e-7],col=[0.7, 0.2, 0.2],text_col='w',fs=17,zorder=1.54,text_on=True,edgealpha=1,lw=2):
        # CROWS arXiv:[1310.8098]
        dat = loadtxt("limit_data/AxionPhoton/CROWS.txt")
        FilledLimit(ax,dat,text_label,text_pos=text_pos,col=col,text_col=text_col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return

    def Helioscopes(ax,col=[0.5, 0.0, 0.13],fs=25,projection=False,RescaleByMass=False,text_on=True):
        # CAST arXiv:[1705.02290]
        y2 = ax.get_ylim()[1]
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
        else:
            rs1 = 0.0
            rs2 = 1.0
        dat = loadtxt("limit_data/AxionPhoton/CAST_highm.txt")
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor='k',facecolor=col,zorder=1.49,lw=0.1)
        plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),'k-',lw=1.5,zorder=1.49,alpha=1)

        mf = dat[-3,0]
        gf = dat[-3,1]
        dat = loadtxt("limit_data/AxionPhoton/CAST.txt")
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor='none',facecolor=col,zorder=1.5,lw=0.1)
        plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),'k-',lw=1.5,zorder=1.5,alpha=1)

        gi = 10.0**interp(log10(mf),log10(dat[:,0]),log10(dat[:,1]))/(rs1*2e-10*mf+rs2)
        plt.plot([mf,mf],[gf,gi],'k-',lw=1.5,zorder=1.5)
        if text_on==True:
            if rs1==0:
                plt.text(1e-1,1.5e-9,r'{\bf CAST}',fontsize=fs+4,color='w',rotation=0,ha='center',va='top',clip_on=True)
            else:
                plt.text(4e-2,5e3,r'{\bf CAST}',fontsize=fs+4,color='w',rotation=0,ha='center',va='top',clip_on=True)

        if projection:
            # IAXO arXiv[1212.4633]
            IAXO_col = 'purple'
            IAXO = loadtxt("limit_data/AxionPhoton/Projections/IAXO.txt")
            plt.plot(IAXO[:,0],IAXO[:,1]/(rs1*2e-10*IAXO[:,0]+rs2),'--',linewidth=2.5,color=IAXO_col,zorder=0.001)
            plt.fill_between(IAXO[:,0],IAXO[:,1]/(rs1*2e-10*IAXO[:,0]+rs2),y2=y2,edgecolor=None,facecolor=IAXO_col,zorder=0,alpha=0.3)
            if text_on==True:
                if rs1==0:
                    plt.text(1e-2,3.3e-13,r'{\bf IAXO}',fontsize=23,color='purple',rotation=0,clip_on=True)
                    plt.plot([3e-3,0.8e-2],[4.0e-12,6e-13],'k-',lw=1.5)
                else:
                    plt.text(0.7e-2,0.12e1,r'{\bf IAXO}',fontsize=fs,color=IAXO_col,rotation=-18,clip_on=True)
        return

    def FermiSNe(ax,text_label=switch_label(r'{\bf Fermi-SNe}'),text_pos=[1.2e-12,0.45e-10],col='ForestGreen',text_col='w',fs=12,zorder=0.265,text_on=True,edgealpha=1,lw=2):
        # Fermi extragalactic SN gamma rays arXiv:[2006.06722]
        dat = loadtxt("limit_data/AxionPhoton/SNe-gamma.txt")
        FilledLimit(ax,dat,text_label,text_pos=text_pos,col=col,text_col=text_col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return

    def DSNALP(ax,text_label=switch_label(r'{\bf DSNALP}'),text_pos=[1.2e-12,1.2e-10],col=[0.0, 0.62, 0.3],text_col='w',fs=12,zorder=0.27,text_on=True,edgealpha=1,lw=2):
        # Diffuse SN ALP background arXiv:[2008.11741]
        dat = loadtxt("limit_data/AxionPhoton/DSNALP.txt")
        FilledLimit(ax,dat,text_label,text_pos=text_pos,col=col,text_col=text_col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return

    def SN1987A_gamma(ax,text_label=switch_label(r'{\bf SN1987A}'),text_pos=[6e-11,0.4e-11],col='#067034',text_col='#067034',fs=15,zorder=0.21,text_on=True,edgealpha=1,lw=2):
        # SN1987 gamma rays arXiv:[1410.3747]
        dat = loadtxt("limit_data/AxionPhoton/SN1987A_gamma.txt")
        FilledLimit(ax,dat,text_label,text_pos=text_pos,col=col,text_col=text_col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return

    def Hydra(ax,text_label=switch_label(r'{\bf Hydra}'),text_pos=[1.2e-12,2e-11],col=[0.24, 0.71, 0.54],text_col='w',fs=13,zorder=0.23,text_on=True,edgealpha=1,lw=2):
        # HYDRA-A arXiv:[1304.0989]
        dat = loadtxt("limit_data/AxionPhoton/Chandra_HYDRA_A.txt")
        FilledLimit(ax,dat,text_label,text_pos=text_pos,col=col,text_col=text_col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return

    def M87(ax,text_label=switch_label(r'\quad {\bf M87}'),text_pos=[1.4e-12,4e-12],col='seagreen',text_col='w',fs=15,zorder=0.219,text_on=True,edgealpha=1,lw=2):
        # M87 Limits from arXiv:[1703.07354]
        dat = loadtxt("limit_data/AxionPhoton/Chandra_M87.txt")
        FilledLimit(ax,dat,text_label,text_pos=text_pos,col=col,text_col=text_col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return

    def HESS(ax,text_label=switch_label(r'{\bf HESS}'),text_pos=[1.4e-8,1.6e-11],col='#2a5736',text_col='#2a5736',fs=14,zorder=0.255,text_on=True,edgealpha=1,lw=2):
        # HESS arXiv:[1304.0700]
        dat = loadtxt("limit_data/AxionPhoton/HESS.txt")
        FilledLimit(ax,dat,text_label,text_pos=text_pos,col=col,text_col=text_col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return

    def Mrk421(ax,text_label=switch_label(r'{\bf Mrk 421}'),text_pos=[3e-9,6e-11],col=[0.4, 0.6, 0.1],text_col='w',fs=12,zorder=0.26,text_on=True,edgealpha=1,lw=2):
        # Mrk 421 arXiv:[2008.09464]
        dat = loadtxt("limit_data/AxionPhoton/Mrk421.txt")
        FilledLimit(ax,dat,text_label,text_pos=text_pos,col=col,text_col=text_col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return

    def NGC1275(ax,text_label=switch_label(r'{\bf Chandra}'),text_pos=[1e-11,1.5e-12],col= [0.0, 0.3, 0.24],text_col=[0.0, 0.3, 0.24],fs=15,zorder=0.1,text_on=True,edgealpha=1,lw=2):
        dat = loadtxt("limit_data/AxionPhoton/Chandra_NGC1275.txt")
        FilledLimit(ax,dat,text_label,text_pos=text_pos,col=col,text_col=text_col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return

    def H1821643(ax,text_label=switch_label(r'{\bf Chandra}'), text_pos=[1e-11,1.5e-12],col= [0.0, 0.3, 0.24],text_col=[0.0, 0.3, 0.24],fs=15,zorder=0.1,text_on=True,edgealpha=1,lw=2):
        dat = loadtxt("limit_data/AxionPhoton/Chandra_H1821643.txt")
        FilledLimit(ax,dat,text_label,text_pos=text_pos,col=col,text_col=text_col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return

    def Fermi(ax,text_label=switch_label(r'{\bf Fermi}'),text_pos=[4.02e-10,1.2e-11],col=[0.0, 0.42, 0.24],text_col='w',fs=15,zorder=0.24,text_on=True,edgealpha=1,lw=2):
        # Fermi NGC1275 arXiv:[1603.06978]
        Fermi1 = loadtxt("limit_data/AxionPhoton/Fermi1.txt")
        Fermi2 = loadtxt("limit_data/AxionPhoton/Fermi2.txt")
        plt.fill_between(Fermi1[:,0],Fermi1[:,1],y2=1e0,edgecolor=col,facecolor=col,zorder=zorder,lw=0.001)
        plt.fill(Fermi2[:,0],1.01*Fermi2[:,1],edgecolor=col,facecolor=col,lw=0.001,zorder=zorder)
        Fermi1 = loadtxt("limit_data/AxionPhoton/Fermi_bound.txt")
        Fermi2 = loadtxt("limit_data/AxionPhoton/Fermi_hole.txt")
        plt.plot(Fermi1[:,0],Fermi1[:,1],'k-',alpha=edgealpha,lw=lw,zorder=zorder)
        plt.plot(Fermi2[:,0],Fermi2[:,1],'k-',alpha=edgealpha,lw=lw,zorder=zorder)
        if text_on:
            plt.text(text_pos[0],text_pos[1],text_label,fontsize=fs,color=text_col,ha='left',va='top',clip_on=True)
        return

    def MWDPolarisation(ax,text_shift=[1,1],col='#32a852',text_col='#32a852',fs=14,zorder=0.01,projection=False,text_on=True,edgealpha=1,lw=2):
        # Upper limit on the axion-photon coupling from magnetic white dwarf polarization arXiv:[2203.04319]
        dat = loadtxt("limit_data/AxionPhoton/MWDPolarisation.txt")
        FilledLimit(ax,dat,col=col,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)

        if text_on:
            if projection==False:
                plt.text(text_shift[0]*2.3e-8,text_shift[1]*0.28e-11,switch_label(r'{\bf MWD}'),fontsize=fs,color=text_col,rotation=0,ha='center',clip_on=True)
                plt.text(text_shift[0]*2.3e-8,text_shift[1]*0.13e-11,switch_label(r'{\bf Polarisation}'),fontsize=fs,color=text_col,rotation=0,ha='center',clip_on=True)
            else:
                plt.text(text_shift[0]*5e-8,text_shift[1]*0.7e-11,switch_label(r'{\bf MWD Pol.}'),fontsize=13,color='w',rotation=0,ha='center',clip_on=True)
        return

    def HAWC(ax,text_label=switch_label(r'{\bf HAWC}'),text_pos=[0.9e-7,2.5e-11],col='#2b5e4e',text_col='#2b5e4e',fs=14,zorder=0.25,text_on=True,Projection=False,edgealpha=1,lw=2):
        # HAWC TeV Blazars arXiv:[2203.04332]
        dat = loadtxt("limit_data/AxionPhoton/HAWC.txt")
        FilledLimit(ax,dat,text_label,text_pos=text_pos,text_col=text_col,col=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return


    def MWDXrays(ax,text_label=switch_label(r'{\bf MWD X-rays}'),text_pos=[1.5e-7,1.3e-10],col='#59c275',text_col='#59c275',fs=14,zorder=0.1,text_on=True,Projection=False,edgealpha=1,lw=2):
        # Magnetic white dwarf chandra x-rays arXiv:[2104.12772]
        dat = loadtxt("limit_data/AxionPhoton/MWDXrays.txt")
        FilledLimit(ax,dat,text_label,text_pos=text_pos,text_col=text_col,col=col,fs=fs,zorder=zorder,text_on=text_on,edgealpha=edgealpha,lw=lw)
        return


    def StarClusters(ax,text_pos=[2.2e-11,2.7e-11],col= [0.2, 0.54, 0.01],text_col='w',fs=13,zorder=0.22,rotation=45,text_on=True,edgealpha=1,lw=2):
        # Xray super star clusters arXiv:[2008.03305]
        dat = loadtxt("limit_data/AxionPhoton/Xray-SuperStarClusters.txt")
        FilledLimit(ax,dat,col=col,text_col=text_col,fs=fs,zorder=zorder,text_on=False,edgealpha=edgealpha,lw=lw)
        if text_on:
            plt.text(text_pos[0],text_pos[1],switch_label(r'{\bf Star}'),fontsize=fs,color=text_col,ha='left',va='top',rotation=rotation,clip_on=True)
            plt.text(0.88*text_pos[0],text_pos[1],switch_label(r'{\bf clusters}'),fontsize=fs,color=text_col,ha='left',va='top',rotation=rotation,clip_on=True)
        return

    def Fermi_GalacticSN(ax,text_label=r'{\bf Fermi SN}',text_pos=[1e-9,5e-13],col=[0.0, 0.42, 0.24],text_col=[0.0, 0.42, 0.24],fs=15,zorder=0.0,text_on=True,rotation=43,lw=1.5,facealpha=0.05,edgealpha=0.6):
        # Fermi nearby SN prospects arXiv:[1609.02350]
        dat = loadtxt("limit_data/AxionPhoton/Projections/FermiSN.txt")
        FilledLimit(ax,dat,text_label,text_pos=text_pos,col=col,text_col=text_col,fs=fs,zorder=zorder,text_on=text_on,lw=lw,rotation=rotation,facealpha=facealpha,edgealpha=edgealpha)
        return

    def MUSE(ax,text_label=switch_label(r'{\bf MUSE}'),text_pos=[1.5,0.7e-12],col=[0.09, 0.45, 0.27],text_col=[0.09, 0.45, 0.27],fs=15,zorder=0.01,text_on=True,lw=0):
        # Telescopes (MUSE) [2009.01310]
        dat = loadtxt("limit_data/AxionPhoton/Telescopes_MUSE.txt")
        FilledLimit(ax,dat,text_label,text_pos=text_pos,col=col,edgecolor=col,text_col=text_col,fs=fs,zorder=zorder,text_on=text_on,rotation=90,lw=lw,edgealpha=0)
        return

    def VIMOS(ax,text_label=switch_label(r'{\bf VIMOS}'),text_pos=[12,0.4e-11],col=[0.09, 0.6, 0.27],text_col=[0.09, 0.6, 0.27],fs=15,zorder=0.01,text_on=True,lw=0):
        # Telescopes (VIMOS) [astro-ph/0611502]
        dat = loadtxt("limit_data/AxionPhoton/Telescopes_VIMOS.txt")
        FilledLimit(ax,dat,text_label,text_pos=text_pos,col=col,edgecolor=col,text_col=text_col,fs=fs,zorder=zorder,text_on=text_on,rotation=-90,lw=lw,edgealpha=0)
        return

    def SolarBasin(ax,text_label=switch_label(r'{\bf Solar basin}'),rotation=98,text_pos=[0.45e4,0.18e-11],col=[0.03, 0.42, 0.29],text_col='w',fs=13,zorder=0.01,text_on=True,lw=1.5,edgecolor='k'):
        dat = loadtxt("limit_data/AxionPhoton/SolarBasin.txt")
        FilledLimit(ax,dat,text_label,text_pos=text_pos,col=col,edgecolor=edgecolor,text_col=text_col,fs=fs,zorder=zorder,text_on=text_on,rotation=rotation,lw=lw,edgealpha=1)
        return

    def LeoT(ax,text_label=switch_label(r'{\bf Leo T}'),text_pos=[2.3e2,0.25e-13],col='#036b3e',text_col='w',fs=16,zorder=0.00003,text_on=True,rotation=-46,edgealpha=1,lw=2):
        # anomalous gas heating in Leo T dwarf
        dat = loadtxt("limit_data/AxionPhoton/LeoT.txt")
        FilledLimit(ax,dat,text_label,text_pos=text_pos,col=col,text_col=text_col,fs=fs,zorder=zorder,text_on=text_on,rotation=rotation,edgealpha=edgealpha,lw=lw)
        return


    def THESEUS(ax,text_label=r'{\bf THESEUS}',text_pos=[8e2,0.8e-17],col=[0.03, 0.57, 0.82],edgecolor=[0.03, 0.57, 0.82],text_col=[0.03, 0.57, 0.82],fs=17,zorder=0.00001,text_on=True,lw=2,facealpha=0.1):
        # THESEUS 2008.08306
        dat = loadtxt("limit_data/AxionPhoton/Projections/THESEUS.txt")
        FilledLimit(ax,dat,text_label,text_pos=text_pos,col=col,text_col=text_col,edgecolor=edgecolor,edgealpha=1,fs=fs,zorder=zorder,text_on=text_on,lw=lw,ha='right',facealpha=facealpha)
        plt.plot([8e2,1.4e3],[0.8e-17,1.3e-17],'k-',lw=2.5)
        plt.plot([8e2,1.4e3],[0.8e-17,1.3e-17],'-',lw=2,color=col)
        return

    def eROSITA(ax,text_label=r'{\bf eROSITA}',text_pos=[2e3,0.3e-18],col=[0.03, 0.57, 0.82],edgecolor=[0.03, 0.57, 0.82],text_col=[0.03, 0.57, 0.82],fs=17,zorder=0.00001,text_on=True,lw=2,facealpha=0.1):
        # eROSITA 2103.13241
        dat = loadtxt("limit_data/AxionPhoton/Projections/eROSITA.txt")
        FilledLimit(ax,dat,text_label,text_pos=text_pos,col=col,text_col=text_col,edgecolor=edgecolor,edgealpha=1,fs=fs,zorder=zorder,text_on=text_on,lw=lw,ha='right',facealpha=facealpha)
        plt.plot([2.1e3,3.5e3],[0.3e-18,0.4e-18],'-',lw=2.5,color=col)
        plt.plot([2.1e3,3.5e3],[0.3e-18,0.4e-18],'-',lw=2,color=col)
        return

    def XMMNewton(ax,text_label=r'{\bf XMM-Newton}',text_pos=[1e3,1.8e-18],col='#3b4ba1',edgecolor='k',text_col='#3b4ba1',fs=17,zorder=0.00001,text_on=True,lw=0.5,facealpha=1):
        dat = loadtxt("limit_data/AxionPhoton/XMM-Newton.txt")
        FilledLimit(ax,dat,text_label,text_pos=text_pos,col=col,text_col=text_col,edgecolor=edgecolor,edgealpha=1,fs=fs,zorder=zorder,text_on=text_on,lw=lw,ha='right',facealpha=facealpha)
        plt.plot([1.2e3,6e3],[1.3e-18,2e-18],'-',lw=2,color=col,path_effects=line_background(3,'k'))
        return

    def COBEFIRAS(ax,text_label=switch_label(r'{\bf COBE/FIRAS}'),text_pos=[0.45e2,4e-13],col='#234f8c',text_col='w',fs=13,zorder=0.0001,text_on=True,rotation=-46,lw=1.5,edgealpha=1):
        # anomalous gas heating in Leo T dwarf
        dat = loadtxt("limit_data/AxionPhoton/COBE-FIRAS.txt")
        FilledLimit(ax,dat,text_label,text_pos=text_pos,col=col,text_col=text_col,fs=fs,zorder=zorder,text_on=text_on,rotation=rotation,edgealpha=edgealpha,lw=lw)
        return

    def Cosmology(ax,fs=30,text_on=True,edgealpha=1,lw=1.5):
        ## Cosmology constraints see arXiv:[1210.3196] for summary
        # Xray Background
        dat = loadtxt("limit_data/AxionPhoton/XRAY.txt")
        FilledLimit(ax,dat,r'{\bf X-rays}',y2=1e-10,text_pos=[1e4,0.8e-16],col=[0.03, 0.57, 0.82],text_col='w',fs=fs,zorder=0.00002,text_on=text_on,rotation=-50,ha='left',va='top',edgealpha=edgealpha,lw=lw)

        # Ionisation fraction
        dat = loadtxt("limit_data/AxionPhoton/x_ion.txt")
        FilledLimit(ax,dat,'',col=[0.27, 0.51, 0.71],text_col='k',fs=fs,zorder=0.001,text_on=False,edgealpha=edgealpha,lw=lw)
        if text_on:
            plt.text(100.5744*0.93,4.0e-11,switch_label(r'{\bf Ionisation}'),fontsize=fs-9,color='w',rotation=-90,ha='left',va='top',clip_on=True)
            plt.text(40*0.93,3.7720e-11,switch_label(r'{\bf fraction}'),fontsize=fs-9,color='w',rotation=-90,ha='left',va='top',clip_on=True)

        # BBN+N_eff arXiv:[2002.08370]
        dat = loadtxt("limit_data/AxionPhoton/BBN_Neff.txt")
        FilledLimit(ax,dat,switch_label(r'{\bf BBN}+$N_{\rm eff}$'),text_pos=[2.5e5,2e-11],col=[0.27, 0.51, 0.71],text_col='w',fs=fs,zorder=0.001,text_on=text_on,rotation=-55,ha='left',va='top',edgealpha=edgealpha,lw=lw)

        # Extragalactic background light
        EBL = loadtxt("limit_data/AxionPhoton/EBL.txt")
        #EBL2 = loadtxt("limit_data/AxionPhoton/EBL2.txt")
        FilledLimit(ax,EBL,switch_label(r'{\bf EBL}'),text_pos=[5e4,5e-14],col=[0.0, 0.2, 0.6],text_col='w',fs=fs+5,zorder=0.001,text_on=text_on,rotation=-55,ha='left',va='top',edgealpha=edgealpha,lw=lw)
        #FilledLimit(ax,EBL2,'',col=[0.0, 0.2, 0.6],text_on=False,zorder=0.001,edgealpha=edgealpha,lw=lw)

        # Spectral distortions of CMB
        AxionPhoton.COBEFIRAS(ax,text_on=text_on,edgealpha=edgealpha,lw=lw)

        return

    def GlobularClusters(ax,text_label=switch_label(r'{\bf Globular clusters}'),text_pos=[1.4e0,1.1e-10],col=[0.0, 0.66, 0.42],text_col='w',fs=23,zorder=0.05,text_on=True,lw=1.5,edgealpha=1):
        # Globular clusters arXiv:[1406.6053]
        dat = loadtxt("limit_data/AxionPhoton/GlobularClusters.txt")
        FilledLimit(ax,dat,text_label,text_pos=text_pos,col=col,text_col=text_col,fs=fs,zorder=zorder,text_on=text_on,lw=lw,va='center',edgealpha=edgealpha)
        return

    def GlobularClusters_R2(ax,text_label=switch_label(r'{\bf Globular clusters ($R_2$)}'),text_pos=[1e-3,5e-11],col=[0.0, 0.66, 0.42],text_col='w',fs=23,zorder=0.01,text_on=True,lw=1.5,edgealpha=1):
        # R2 parameter https://arxiv.org/pdf/2207.03102.pdf
        dat = loadtxt("limit_data/AxionPhoton/GlobularClusters-R2.txt")
        FilledLimit(ax,dat,text_label,text_pos=text_pos,col=col,text_col=text_col,fs=fs,zorder=zorder,text_on=text_on,lw=lw,va='center',edgealpha=edgealpha)
        return

    def WhiteDwarfs(ax,text_label=switch_label(r'\noindent {\bf White}\newline  {\bf dwarfs}'),text_pos=[1.3e6,4e-8],col='#2ec763',text_col='w',fs=18,zorder=0.04,text_on=True,lw=1.5,rotation=87,edgealpha=1):
        dat = loadtxt("limit_data/AxionPhoton/WhiteDwarfs.txt")
        FilledLimit(ax,dat,text_label,text_pos=text_pos,col=col,text_col=text_col,fs=fs,zorder=zorder,text_on=text_on,lw=lw,va='center',rotation=rotation,edgealpha=edgealpha)
        return

    def SolarNu(ax,text_label=switch_label(r'{\bf Solar} $\nu$'),text_pos=[1e1,2e-9],col='seagreen',text_col='w',fs=33,zorder=1,text_on=True,lw=1.5,edgealpha=1):
        # Solar neutrino B8 bound arXiv:[1501.01639]
        dat = loadtxt("limit_data/AxionPhoton/SolarNu.txt")
        FilledLimit(ax,dat,text_label,text_pos=text_pos,col=col,text_col=text_col,fs=fs,zorder=zorder,text_on=text_on,lw=lw,va='center',edgealpha=edgealpha)
        return

    def DiffuseGammaRays(ax,text_label=r'{Diffuse}-$\gamma$',text_pos=[1e5,1e-10],col='#1e7ac7',text_col='w',fs=21,zorder=0.03,text_on=True,lw=1.5,rotation=0):
        # https://arxiv.org/pdf/2109.03244.pdf
        dat = loadtxt("limit_data/AxionPhoton/DiffuseGammaRays.txt")
        plt.fill(dat[:,0],dat[:,1],edgecolor=None,facecolor=col,zorder=zorder)
        plt.plot(dat[:,0],dat[:,1],lw=2,color='k',alpha=0.5,zorder=zorder)

        if text_on:
            plt.text(text_pos[0],text_pos[1],text_label,fontsize=fs,color=text_col,rotation=rotation,ha='left',va='top',clip_on=True)
        return

    def SN1987A_HeavyALP_gamma(ax,text_label=switch_label(r'{\bf SN1987A} ($\gamma$)'),text_pos=[0.8e5,2.0e-10],col='#067034',text_col='w',fs=18,zorder=0.03,text_on=True,lw=1.5,rotation=-25.5,edgealpha=1):
        # https://arxiv.org/pdf/2109.03244.pdf
        dat = loadtxt("limit_data/AxionPhoton/SN1987A_HeavyALP_gamma.txt")
        plt.fill(dat[:,0],dat[:,1],edgecolor=None,facecolor=col,zorder=zorder)
        plt.plot(dat[:,0],dat[:,1],lw=lw,color='k',alpha=edgealpha,zorder=zorder)

        if text_on:
            plt.text(text_pos[0],text_pos[1],text_label,fontsize=fs,color=text_col,rotation=rotation,ha='left',va='top',clip_on=True)
        return

    def SN1987A_HeavyALP_nu(ax,text_shift=[1,1],col='darkgreen',text_col='w',fs=17,zorder=0.03,text_on=True,lw=1.5,rotation=0,ha='center',edgealpha=1):
        # https://arxiv.org/pdf/2109.03244.pdf
        dat = loadtxt("limit_data/AxionPhoton/SN1987A_HeavyALP_nu.txt")
        plt.fill(dat[:,0],dat[:,1],edgecolor=None,facecolor=col,zorder=zorder)
        plt.plot(dat[:,0],dat[:,1],lw=lw,color='k',alpha=edgealpha,zorder=zorder)

        if text_on:
            plt.text(text_shift[0]*1.8e6,text_shift[1]*5e-9,switch_label(r'{\bf SN1987A}'),fontsize=fs,color='w',rotation=0,ha='center',va='top',clip_on=True)
            plt.text(text_shift[0]*1.8e6,text_shift[1]*2e-9,switch_label(r'($\nu$)'),fontsize=fs,color='w',rotation=0,ha='center',va='top',clip_on=True)
        return

    def NeutronStars(ax,col='#52a178',fs=14,RescaleByMass=False,text_on=True,text_shift=[1,1],lw=1,text_col='#52a178',xskip=8,edgealpha=1):
        # Neutron stars: Green Bank arXiv:[2004.00011]
        # Jansky VLA: 2008.01877, 2008.11188
        # Battye et al. []

        y2 = ax.get_ylim()[1]
        if RescaleByMass:
            rs1 = 1.0
            rs2 = 0.0
        else:
            rs1 = 0.0
            rs2 = 1.0
        # dat = loadtxt('limit_data/AxionPhoton/NeutronStars_GreenBank.txt')
        # plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=0.1)
        # plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),'k-',alpha=0.5,lw=0.5,zorder=0)
        #
        # dat = loadtxt('limit_data/AxionPhoton/NeutronStars_VLA.txt')
        # plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=0.1)
        # plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),'k-',alpha=0.5,lw=0.5,zorder=0)
        #
        # dat = loadtxt('limit_data/AxionPhoton/NeutronStars_Battye.txt')
        # plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=0.1)
        # plt.plot(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),'k-',alpha=0.5,lw=0.5,zorder=0)

        dat = loadtxt('limit_data/AxionPhoton/NeutronStars_BreakthroughListen.txt')
        plt.fill_between(dat[:,0],dat[:,1]/(rs1*2e-10*dat[:,0]+rs2),y2=y2,edgecolor=None,facecolor=col,zorder=0.1)
        plt.plot(dat[0::xskip,0],dat[0::xskip,1]/(rs1*2e-10*dat[0::xskip,0]+rs2),'k-',alpha=edgealpha,lw=lw,zorder=0.1)

        if text_on:
            if rs1==0:
                plt.text(text_shift[0]*1e-5,text_shift[1]*0.62e-10,switch_label(r'{\bf Neutron stars}'),fontsize=fs,color=text_col,ha='left',va='bottom')
            else:
                plt.text(text_shift[0]*1e-7,text_shift[1]*4e3, switch_label(r'{\bf Neutron}'),fontsize=fs,color=col,ha='center')
                plt.text(text_shift[0]*1e-7,text_shift[1]*1e3,r'{\bf stars}',fontsize=fs,color=col,ha='center')
                plt.plot([3.5e-7*text_shift[0],2e-5],[6e3*text_shift[1],8e3],lw=1.5,color=col,path_effects=line_background(2,'w'))
        return

    def Haloscopes(ax,projection=False,fs=20,text_on=True,BASE_arrow_on=True):
        AxionPhoton.ADMX(ax,projection=projection,fs=fs,text_on=text_on)
        AxionPhoton.HAYSTAC(ax,projection=projection,text_on=text_on)
        #AxionPhoton.ABRACADABRA(ax,fs=fs,projection=False,text_on=text_on)
        #AxionPhoton.SHAFT(ax,text_on=text_on)
        AxionPhoton.ORGAN(ax,projection=projection,text_on=text_on,lw=0)
        AxionPhoton.UPLOAD(ax,text_on=text_on)
        AxionPhoton.TASEH(ax,text_on=False)

        if projection:
            AxionPhoton.CAPP(ax,fs=fs-4,text_on=False)
            AxionPhoton.RBF_UF(ax,fs=fs-2,text_on=False)
            AxionPhoton.DMRadio(ax,text_on=text_on)
            AxionPhoton.SRF(ax,text_on=text_on)
            AxionPhoton.ALPHA(ax,text_on=text_on)
            AxionPhoton.MADMAX(ax,text_on=text_on)
            AxionPhoton.FLASH(ax,text_on=text_on)
            AxionPhoton.TOORAD(ax,text_on=text_on)
            AxionPhoton.BRASS(ax,text_on=text_on)
            AxionPhoton.BREAD(ax,text_on=text_on)
            AxionPhoton.CADEx(ax,text_on=text_on)
            AxionPhoton.ADBC(ax,text_on=text_on)
            AxionPhoton.DANCE(ax,text_on=text_on)
            AxionPhoton.aLIGO(ax,text_on=text_on)
            AxionPhoton.WISPLC(ax,text_on=text_on)
            AxionPhoton.LAMPOST(ax)

            AxionPhoton.ADMX(ax,text_on=False,col='darkred')
            AxionPhoton.CAPP(ax,text_on=False,col='darkred')
            AxionPhoton.ORGAN(ax,text_on=False,col='darkred',lw=0)
            AxionPhoton.HAYSTAC(ax,text_on=False,col='darkred')
            AxionPhoton.RBF_UF(ax,text_on=False,col='darkred')
            AxionPhoton.QUAX(ax,text_on=False,col='darkred')
            plt.text(0.5e-5,0.45e-12,r'{\bf Haloscopes}',color='w',rotation=90,fontsize=15)
        else:
            AxionPhoton.RBF_UF(ax,fs=fs-2,text_on=text_on)
            AxionPhoton.CAPP(ax,fs=fs-4,text_on=text_on)
            AxionPhoton.QUAX(ax,text_on=text_on)
            #AxionPhoton.BASE(ax,text_on=text_on,arrow_on=BASE_arrow_on)
            AxionPhoton.ADMX_SLIC(ax,fs=fs-8,text_on=text_on)
            #AxionPhoton.RADES(ax,text_on=False)
            #AxionPhoton.GrAHal(ax,text_on=False)
        return

    def HaloscopesUniform(ax,projection=False,fs=20,text_on=True,col='darkred'):
        AxionPhoton.ADMX(ax,projection=projection,fs=fs,text_on=text_on,col=col)
        AxionPhoton.RBF_UF(ax,fs=fs-2,text_on=text_on,col=col)
        AxionPhoton.HAYSTAC(ax,projection=projection,text_on=text_on,col=col)
        AxionPhoton.ABRACADABRA(ax,fs=fs,projection=False,text_on=text_on,col=col,lw=0.75)
        AxionPhoton.SHAFT(ax,text_on=text_on,col=col,lw=0.75)
        AxionPhoton.CAPP(ax,fs=fs-4,text_on=text_on,col=col)
        AxionPhoton.ORGAN(ax,projection=projection,text_on=text_on,col=col,lw=0)
        AxionPhoton.UPLOAD(ax,text_on=text_on,col=col)
        AxionPhoton.QUAX(ax,text_on=text_on,col=col)
        AxionPhoton.BASE(ax,text_on=text_on,col=col,arrow_on=False)
        AxionPhoton.ADMX_SLIC(ax,fs=fs-8,text_on=text_on,col=col)
        AxionPhoton.RADES(ax,text_on=text_on,col=col)
        AxionPhoton.GrAHal(ax,text_on=text_on,col=col)
        return

    def LSW(ax,projection=False,text_on=True):
        AxionPhoton.ALPS(ax,projection=projection,text_on=text_on)
        AxionPhoton.PVLAS(ax,text_on=text_on)
        AxionPhoton.OSQAR(ax,text_on=text_on)
        AxionPhoton.CROWS(ax,text_on=text_on)
        return

    def LowMassAstroBounds(ax,projection=False,text_on=True,edgealpha=1,lw=1,GalacticSN=False):
        """
        AxionPhoton.FermiSNe(ax,text_on=text_on,edgealpha=edgealpha,lw=lw)
        AxionPhoton.DSNALP(ax,text_on=text_on,edgealpha=edgealpha,lw=lw)
        AxionPhoton.Hydra(ax,text_on=text_on,edgealpha=edgealpha,lw=lw)
        AxionPhoton.M87(ax,text_on=text_on,edgealpha=edgealpha,lw=lw)
        AxionPhoton.Mrk421(ax,text_on=text_on,edgealpha=edgealpha,lw=lw)
        AxionPhoton.Fermi(ax,text_on=text_on,edgealpha=edgealpha,lw=lw)
        AxionPhoton.StarClusters(ax,text_on=text_on,edgealpha=edgealpha,lw=lw)
        """
        if projection:
            #AxionPhoton.NGC1275(ax,text_on=False,edgealpha=edgealpha,lw=lw)
            AxionPhoton.SN1987A_gamma(ax,text_on=False,edgealpha=edgealpha,lw=lw)
            if GalacticSN:
                AxionPhoton.Fermi_GalacticSN(ax,text_on=text_on,lw=lw)
            AxionPhoton.MWDXrays(ax,text_on=text_on,edgealpha=edgealpha,lw=lw)
            AxionPhoton.MWDPolarisation(ax,text_on=text_on,projection=True,edgealpha=edgealpha,lw=lw)
            AxionPhoton.HESS(ax,text_on=False,edgealpha=edgealpha,lw=lw)
            AxionPhoton.HAWC(ax,text_on=False,edgealpha=edgealpha,lw=lw)
        else:
            
            AxionPhoton.NGC1275(ax,text_on=text_on,edgealpha=edgealpha,lw=lw)
            AxionPhoton.SN1987A_gamma(ax,text_on=text_on,edgealpha=edgealpha,lw=lw)
            AxionPhoton.HESS(ax,text_on=text_on,edgealpha=edgealpha,lw=lw)
            AxionPhoton.HAWC(ax,text_on=text_on,edgealpha=edgealpha,lw=lw)
            AxionPhoton.MWDXrays(ax,text_on=text_on,edgealpha=edgealpha,lw=lw)
            AxionPhoton.MWDPolarisation(ax,text_on=text_on,edgealpha=edgealpha,lw=lw)
        
        return

    def StellarBounds(ax,text_on=True):
        AxionPhoton.GlobularClusters(ax,text_on=text_on)
        AxionPhoton.SolarNu(ax,text_on=text_on)
        AxionPhoton.WhiteDwarfs(ax,text_on=text_on)
        return

    def ALPdecay(ax,projection=False,text_on=True):
        AxionPhoton.SN1987A_HeavyALP_gamma(ax,text_on=text_on)
        AxionPhoton.SN1987A_HeavyALP_nu(ax,text_on=text_on)
        AxionPhoton.MUSE(ax,text_on=text_on)
        AxionPhoton.VIMOS(ax,text_on=text_on)
        AxionPhoton.XMMNewton(ax,text_on=text_on)
        AxionPhoton.LeoT(ax,text_on=text_on)

        if projection:
            AxionPhoton.THESEUS(ax,text_on=text_on)
            AxionPhoton.eROSITA(ax,text_on=text_on)
        return
#==============================================================================#


#==============================================================================#
class AxionElectron():
    def QCDAxion(ax,text_on=True,C_logwidth=10,KSVZ_on=True,DFSZ_on=True,Hadronic_on=True,fs=25,DFSZ_col='goldenrod',KSVZ_col='brown',Hadronic_col='gold',DFSZ_label_mass=1e-4,KSVZ_label_mass=0.8e-1,Hadronic_label_mass=5e-3):
        ## QCD Axion band:
        g_min,g_max = ax.get_ylim()
        m_min,m_max = ax.get_xlim()

        # Mass-coupling relation
        def g_x(C_ae,m_a):
            return 8.943e-11*C_ae*m_a
        DFSZ_u = 1.0/3.0
        DFSZ_l = 2.0e-5
        KSVZ = 2e-4
        Had_u = 5e-3
        Had_l = 1.5e-4

        # QCD Axion models
        n = 200
        m = logspace(log10(m_min),log10(m_max),n)
        rot = 45.0
        trans_angle = plt.gca().transData.transform_angles(array((rot,)),array([[0, 0]]))[0]
        if DFSZ_on:
            col = DFSZ_col
            plt.fill_between(m,g_x(DFSZ_l,m),y2=g_x(DFSZ_u,m),facecolor=col,zorder=0,alpha=0.5)
            plt.plot(m,g_x(DFSZ_l,m),'k-',lw=3.5,zorder=0)
            plt.plot(m,g_x(DFSZ_u,m),'k-',lw=3.5,zorder=0)
            plt.plot(m,g_x(DFSZ_l,m),'-',lw=2,zorder=0,color=col)
            plt.plot(m,g_x(DFSZ_u,m),'-',lw=2,zorder=0,color=col)
            if text_on:
                plt.text(DFSZ_label_mass,g_x(DFSZ_u,DFSZ_label_mass)/1.5,r'{\bf DFSZ}',fontsize=fs,rotation=trans_angle,color='k',ha='left',va='top',rotation_mode='anchor',clip_on=True)
        if KSVZ_on:
            col = KSVZ_col
            plt.plot(m,g_x(KSVZ,m),'k-',lw=3.5,zorder=0.02)
            plt.plot(m,g_x(KSVZ,m),'-',lw=2,zorder=0.02,color=col)
            if text_on:
                plt.text(KSVZ_label_mass,g_x(KSVZ,KSVZ_label_mass)*2.7,r'{\bf KSVZ}',fontsize=fs,rotation=trans_angle,color=col,ha='left',va='top',rotation_mode='anchor',clip_on=True)
        if Hadronic_on:
            col = Hadronic_col
            plt.fill_between(m,g_x(Had_l,m),y2=g_x(Had_u,m),facecolor=col,zorder=0.01,alpha=0.6)
            plt.plot(m,g_x(Had_l,m),'k-',lw=3.5,zorder=0.01)
            plt.plot(m,g_x(Had_u,m),'k-',lw=3.5,zorder=0.01)
            plt.plot(m,g_x(Had_l,m),'-',lw=2,zorder=0.01,color=col)
            plt.plot(m,g_x(Had_u,m),'-',lw=2,zorder=0.01,color=col)
            if text_on:
                plt.text(Hadronic_label_mass,g_x(Had_u,Hadronic_label_mass)/1.5,r'{\bf Hadronic models}',fontsize=fs-5,rotation=trans_angle,color='k',ha='left',va='top',rotation_mode='anchor',clip_on=True)

        return

    def XENON1T(ax,col='crimson',fs=19,text_on=True,zorder=0.51,lw=2,text_shift=[1,1],**kwargs):
        # XENON1T S2 analysis arXiv:[1907.11485]
        dat = loadtxt("limit_data/AxionElectron/XENON1T_DM_S2.txt")
        plt.plot(dat[:,0],dat[:,1],'k-',alpha=1,zorder=zorder,lw=lw)
        plt.fill_between(dat[:,0],dat[:,1],y2=1e0,edgecolor=None,facecolor=col,zorder=zorder)

        # XENON1T S1+S2 analysis arXiv:[2006.09721]
        dat = loadtxt("limit_data/AxionElectron/XENON1T_DM_S1S2.txt")
        plt.plot(dat[:,0],dat[:,1],'k-',alpha=1,zorder=zorder,lw=lw)
        plt.fill_between(dat[:,0],dat[:,1],y2=1e0,edgecolor=None,facecolor=col,zorder=zorder)

        # XENON1T Single electron analysis arXiv:[2112.12116]
        dat = loadtxt("limit_data/AxionElectron/XENON1T_DM_SE.txt")
        plt.plot(dat[:,0],dat[:,1],'k-',alpha=1,zorder=zorder,lw=lw)
        plt.fill_between(dat[:,0],dat[:,1],y2=1e0,edgecolor=None,facecolor=col,zorder=zorder)

        if text_on:
            plt.text(text_shift[0]*1.2e2,text_shift[1]*4e-14,r'{\bf XENON1T}',fontsize=fs,color=col,ha='center',va='top',clip_on=True,**kwargs)
            #plt.text(text_shift[0]*1.2e2,text_shift[1]*2.5e-14,r'(DM)',fontsize=fs,color=col,ha='center',va='top',clip_on=True,**kwargs)
        return

    def XENONnT(ax,col='crimson',fs=19,text_on=True,zorder=0.51,lw=2,text_shift=[1,1],**kwargs):
        # XENONnT ALP DM
        dat = loadtxt("limit_data/AxionElectron/XENONnT.txt")
        plt.plot(dat[:,0],dat[:,1],'k-',alpha=1,zorder=zorder,lw=lw)
        plt.fill_between(dat[:,0],dat[:,1],y2=1e0,edgecolor=None,facecolor=col,zorder=zorder)

        if text_on:
            plt.text(text_shift[0]*8e2,text_shift[1]*0.85e-14,r'{\bf XENONnT}',fontsize=fs,color=col,ha='center',va='top',clip_on=True,**kwargs)

    def XENONnT_Solar(ax,col='indianred',fs=30,text_on=True,zorder=0.52,lw=2,text_shift=[1,1],**kwargs):
        # Solar axions
        dat = loadtxt("limit_data/AxionElectron/XENONnT_Solar.txt")
        plt.plot(dat[:,0],dat[:,1],'k-',alpha=1,zorder=zorder,lw=lw)
        plt.fill_between(dat[:,0],dat[:,1],y2=1e0,edgecolor=None,facecolor=col,zorder=zorder)
        if text_on:
            plt.text(text_shift[0]*0.2e-8,text_shift[1]*4e-12,r'{\bf XENONnT} (Solar axions)',fontsize=fs,color='w',alpha=0.8,ha='left',va='top',clip_on=True,**kwargs)
        return

    def SolarBasin(ax,col='royalblue',fs=20,text_on=True,lw=2,text_shift=[1,1],zorder=0.6,**kwargs):
        # Solar axion basin arXiv:[2006.12431]
        dat = loadtxt("limit_data/AxionElectron/XENON1T_S2_SolarAxionBasin.txt")
        plt.plot(dat[:,0],dat[:,1],'k-',alpha=1,zorder=zorder,lw=lw)
        plt.fill_between(dat[:,0],dat[:,1],y2=1e0,edgecolor=None,facecolor=col,zorder=zorder)
        if text_on:
            plt.text(text_shift[0]*3e3,text_shift[1]*2e-11,r'{\bf XENON1T}',fontsize=fs,color='k',ha='center',va='top',clip_on=True,**kwargs)
            plt.text(text_shift[0]*3e3,text_shift[1]*1.3e-11,r'(Solar axion',fontsize=fs,color='k',ha='center',va='top',clip_on=True,**kwargs)
            plt.text(text_shift[0]*3e3,text_shift[1]*0.8e-11,r' basin)',fontsize=fs,color='k',ha='center',va='top',clip_on=True,**kwargs)
        return

    def LUX(ax,col='indianred',fs=30,text_on=True,lw=2,text_pos=[0.2e-8,7e-12],zorder=0.52,**kwargs):
        # LUX arXiv:[1704.02297]
        dat = loadtxt("limit_data/AxionElectron/LUX.txt")
        plt.plot(dat[:,0],dat[:,1],'k-',alpha=1,zorder=zorder,lw=lw)
        plt.fill_between(dat[:,0],dat[:,1],y2=1e0,edgecolor=None,facecolor=col,zorder=zorder)
        if text_on:
            plt.text(text_pos[0],text_pos[1],r'{\bf LUX} (Solar axions)',fontsize=fs,color='w',alpha=0.8,ha='left',va='top',clip_on=True,**kwargs)
        return

    def PandaX(ax,col='firebrick',fs=20,text_on=True,lw=2,text_pos=[1.2e3,4.5e-13],zorder=0.53,rotation=20,**kwargs):
        dat = loadtxt("limit_data/AxionElectron/PandaX.txt")
        plt.plot(dat[:,0],dat[:,1],'k-',alpha=1,zorder=zorder,lw=lw)
        plt.fill_between(dat[:,0],dat[:,1],y2=1e0,edgecolor=None,facecolor=col,zorder=zorder)
        if text_on:
            plt.text(text_pos[0],text_pos[1],r'{\bf PandaX}',fontsize=fs-2,color='w',ha='left',va='top',rotation=rotation,clip_on=True,**kwargs)
        return

    def GERDA(ax,col='#d13617',fs=22,text_on=True,text_pos=[1.6e5,1.9e-11],zorder=0.52,lw=2,text_col='w',**kwargs):
        dat = loadtxt("limit_data/AxionElectron/GERDA.txt")
        plt.plot(dat[:,0],dat[:,1],'k-',alpha=1,zorder=zorder,lw=lw)
        plt.fill_between(dat[:,0],dat[:,1],y2=1e0,edgecolor=None,facecolor=col,zorder=zorder)
        if text_on:
            plt.text(text_pos[0],text_pos[1],r'{\bf GERDA}',fontsize=fs,color=text_col,ha='left',va='top',clip_on=True,**kwargs)
        return

    def EDELWEISS(ax,col='darkred',projection=False,fs=15,text_col='darkred',text_on=True,text_pos=[9e0,7e-13],zorder=0.57,lw=2,rotation=0,**kwargs):
        # EDELWEISS arXiv:[1808.02340]
        dat = loadtxt("limit_data/AxionElectron/EDELWEISS.txt")
        plt.plot(dat[:,0],dat[:,1],'k-',alpha=1,zorder=zorder,lw=lw)
        plt.fill_between(dat[:,0],dat[:,1],y2=1e0,edgecolor=None,facecolor=col,zorder=zorder)
        if projection:
            dat = loadtxt("limit_data/AxionElectron/Projections/EDELWEISS.txt")
            plt.plot(dat[:,0],dat[:,1],'--',color=col,zorder=zorder,lw=lw)
        if text_on:
            plt.text(text_pos[0],text_pos[1],r'{\bf EDELWEISS}',fontsize=fs,color=text_col,ha='left',va='top',clip_on=True,rotation=rotation,**kwargs)
        return

    def SuperCDMS(ax,col='maroon',fs=20,text_on=True,text_pos=[5e1,2.7e-11],text_col='w',zorder=0.58,rotation=-84,lw=2,**kwargs):
        # SuperCDMS arXiv:[1911.11905]
        dat = loadtxt("limit_data/AxionElectron/SuperCDMS.txt")
        plt.fill_between(dat[:,0],dat[:,1],y2=1e0,edgecolor=None,facecolor=col,zorder=zorder)
        plt.plot(dat[:,0],dat[:,1],'-',color='k',alpha=1,zorder=zorder,lw=lw)
        if text_on:
            plt.text(text_pos[0],text_pos[1],r'{\bf SuperCDMS}',fontsize=fs-1,color=text_col,ha='left',va='top',alpha=1.0,rotation=rotation,clip_on=True,**kwargs)
        return

    def DARWIN(ax,col='brown',fs=20,text_on=True,text_pos=[0.3e3,2e-14],zorder=0.1,lw=3,**kwargs):
        # DARWIN arXiv:[1606.07001]
        dat = loadtxt("limit_data/AxionElectron/Projections/DARWIN.txt")
        plt.plot(dat[:,0],dat[:,1],'--',color=col,alpha=1.0,zorder=zorder,lw=lw)
        if text_on:
            plt.text(text_pos[0],text_pos[1],r'{\bf DARWIN}',fontsize=fs,color=col,ha='left',va='top',clip_on=True,**kwargs)
        return

    def LZ(ax,col='crimson',fs=20,text_on=True,text_pos=[2.3e3,0.8e-14],lw=3,zorder=0.1,**kwargs):
        # DARWIN arXiv:[2102.11740]
        dat = loadtxt("limit_data/AxionElectron/Projections/LZ.txt")
        plt.plot(dat[:,0],dat[:,1],'--',color=col,alpha=1.0,zorder=zorder,lw=lw)
        if text_on:
            plt.text(text_pos[0],text_pos[1],r'{\bf LZ}',fontsize=fs,color=col,ha='left',va='top',clip_on=True,**kwargs)
        return

    def Semiconductors(ax,col='purple',fs=15,text_on=True,text_pos=[1e0,2.5e-12],lw=2.5,rotation=-80,zorder=0.51,**kwargs):
        # ALP Absorption with semiconductors arXiv:[1608.02123]
        dat = loadtxt("limit_data/AxionElectron/Projections/SemiconductorAbsorption.txt")
        plt.plot(dat[:,0],dat[:,1],'--',color=col,alpha=1.0,zorder=zorder,lw=lw)
        if text_on:
            plt.text(text_pos[0],text_pos[1],r'{\bf Semiconductors}',fontsize=fs,color=col,ha='left',va='top',rotation=rotation,clip_on=True,**kwargs)
        return

    def Magnon(ax,col='rebeccapurple',fs=20,text_on=True,text_pos=[2e-6,1e-14],lw=3,zorder=0.51,**kwargs):
        # Axion-magnon conversion arXiv:[2005.10256]
        dat = loadtxt("limit_data/AxionElectron/Projections/Magnon.txt")
        plt.fill_between(dat[:,0],dat[:,1],y2=1e0,color=col,alpha=0.4,zorder=zorder)
        plt.plot(dat[:,0],dat[:,1],'--',color=col,alpha=1.0,zorder=zorder,lw=lw)
        if text_on:
            plt.text(text_pos[0],text_pos[1],r'{\bf Magnons \newline (YIT, NiSP$_3$)}',fontsize=fs,color=col,ha='left',va='top',clip_on=True,**kwargs)
        return

    def MagnonScan(ax,col='mediumvioletred',fs=20,text_on=True,text_shift=[1,1],lw=3,zorder=0.5,**kwargs):
        # Axion-magnon conversion arXiv:[2005.10256 and 2001.10666]
        dat = loadtxt("limit_data/AxionElectron/Projections/MagnonScan.txt")
        plt.fill_between(dat[:,0],dat[:,1],y2=1e0,color=col,alpha=0.4,zorder=zorder)
        plt.plot(dat[:,0],dat[:,1],'--',color=col,alpha=1.0,zorder=zorder,lw=lw)
        if text_on:
            plt.text(text_shift[0]*1.2e-5,text_shift[1]*0.5e-13,r'{\bf Magnons}',fontsize=fs-1,color=col,ha='center',va='top',clip_on=True,**kwargs)
            plt.text(text_shift[0]*1.2e-5,text_shift[1]*0.7*0.5e-13,r'{\bf (Scanning)}',fontsize=fs-1,color=col,ha='center',va='top',clip_on=True,**kwargs)
        return

    def QUAX(ax,col='maroon',fs=17,text_on=True,text_pos=[50e-6,0.9e-10],lw=3,zorder=10.0,text_rot=-90,**kwargs):
        # QUAX https://inspirehep.net/literature/1777123
        dat = loadtxt("limit_data/AxionElectron/QUAX.txt")
        plt.fill_between(dat[:,0],dat[:,1],y2=1e0,color=col,alpha=0.4,zorder=zorder)
        plt.plot(dat[:,0],dat[:,1],'-',color=col,alpha=1.0,zorder=zorder,lw=lw)
        if text_on:
            plt.text(text_pos[0],text_pos[1],r'{\bf QUAX}',fontsize=fs,color=col,rotation=text_rot,ha='left',va='top',clip_on=True,**kwargs)
        return

    def RedGiants(ax,col=[0.0, 0.66, 0.42],text_pos=[0.2e-8,2e-13],text_on=True,zorder=0.5,fs=30,lw=2,**kwargs):
        # Red Giants arXiv:[2007.03694]
        dat = loadtxt("limit_data/AxionElectron/RedGiants_HighMass.txt")
        plt.plot(dat[:,0],dat[:,1],color='k',alpha=1,zorder=zorder,lw=lw)
        plt.fill_between(dat[:,0],dat[:,1],y2=1e0,edgecolor=None,facecolor=col,zorder=zorder)
        if text_on: plt.text(text_pos[0],text_pos[1],r'{\bf Red giants} ($\omega$Cen)',fontsize=fs,color='w',clip_on=True,**kwargs)
        return

    def Xrays(ax,col='green',text_shift=[1,1],text_on=True,zorder=0.5,fs=20,rotation=-80,alpha=0.8,**kwargs):
        dat = loadtxt("limit_data/AxionElectron/Xray_1loop.txt")
        plt.plot(dat[:,0],dat[:,1],'--',color='k',zorder=zorder,lw=2,alpha=alpha)
        plt.fill_between(dat[:,0],dat[:,1],y2=1e0,edgecolor=None,facecolor=col,zorder=zorder,alpha=alpha)
        if text_on:
            plt.text(3.3e4*text_shift[0],4e-15*text_shift[1],r'{\bf X-rays}',fontsize=fs,color='w',clip_on=True,rotation=rotation,**kwargs)
            plt.text(1.32e4*text_shift[0],1.2e-15*text_shift[1],r'(EM anomaly-free ALP)',fontsize=fs*0.85,color='w',clip_on=True,rotation=rotation,**kwargs)

            return

    def SolarNu(ax,col='seagreen',text_pos=[0.2e-8,3.8e-11],text_on=True,zorder=0.7,fs=30,lw=2,**kwargs):
        # Solar neutrinos arXiv:[0807.2926]
        dat = loadtxt("limit_data/AxionElectron/SolarNu.txt")
        plt.plot(dat[:,0],dat[:,1],color='k',alpha=1,zorder=zorder,lw=lw)
        plt.fill_between(dat[:,0],dat[:,1],y2=1e0,edgecolor=None,facecolor=col,zorder=zorder)
        if text_on: plt.text(text_pos[0],text_pos[1],r'{\bf Solar} $\nu$',fontsize=fs,color='w',clip_on=True,**kwargs)
        return

    def WhiteDwarfHint(ax,col='k',text_pos=[1e-7,1e-13],facealpha=0.3,zorder=1.0,text_on=True,fs=20,**kwargs):
        # White dwarf hint arXiv:[1708.02111]
        dat = loadtxt("limit_data/AxionElectron/WDhint.txt")
        plt.fill_between(dat[:,0],dat[:,1],color=col,edgecolor=None,lw=0.001,zorder=zorder,alpha=facealpha)
        if text_on: plt.text(text_pos[0],text_pos[1],r'{\bf White dwarf hint}',fontsize=fs,clip_on=True,**kwargs)
        return

    def StellarBounds(ax,fs=30,Hint=True,text_on=True):
        AxionElectron.RedGiants(ax,text_on=text_on)
        AxionElectron.SolarNu(ax,text_on=text_on)
        if Hint:
            AxionElectron.WhiteDwarfHint(ax,text_on=text_on)
        return

    def UndergroundDetectors(ax,projection=False,fs=20,text_on=True):
        AxionElectron.XENONnT_Solar(ax,fs=fs+10,text_on=text_on)
        AxionElectron.PandaX(ax,fs=fs,text_on=text_on)
        AxionElectron.XENON1T(ax,fs=fs-2,text_on=text_on)
        AxionElectron.XENONnT(ax,fs=fs-2,text_on=text_on)
        AxionElectron.SolarBasin(ax,fs=fs-2,text_on=text_on)
        AxionElectron.SuperCDMS(ax,fs=fs,text_on=text_on)
        AxionElectron.EDELWEISS(ax,fs=fs-5,projection=projection,text_on=text_on)
        if projection:
            AxionElectron.DARWIN(ax,fs=fs,text_on=text_on)
            AxionElectron.LZ(ax,fs=fs,text_on=text_on)
            AxionElectron.Semiconductors(ax,fs=fs-5,text_on=text_on)
        return

    def Haloscopes(ax,projection=False,fs=20,text_on=True):
        if projection:
            AxionElectron.Magnon(ax,fs=fs,text_on=text_on)
            AxionElectron.MagnonScan(ax,fs=fs,text_on=text_on)
        return
#==============================================================================#


#==============================================================================#
class AxionNeutron():
    # Warning: often couplings are actually given as g_an/2 m_n (this is what is in the limit_data files)
    # But we are using the dimensionless coupling, so will multiply by the neutron mass
    # this makes essentially no observable difference to the plot but it useful to remember.
    m_n = 0.93957

    def QCDAxion(ax,C_logwidth=10,KSVZ_on=True,DFSZ_on=True,
                      cmap='YlOrBr',fs=25,Mpl_lab=False,DFSZ_label_mass=1e-8,KSVZ_label_mass=1e-7):
        ## QCD Axion band:
        g_min,g_max = ax.get_ylim()
        m_min,m_max = ax.get_xlim()

        # Mass-coupling relation
        def g_x(C_ae,m_a):
            return 1.644e-7*C_ae*m_a
        DFSZ_l = 0.16
        DFSZ_u = 0.26
        KSVZ = 0.02

        if Mpl_lab:
            plt.plot([3.5e-13,3.5e-13],[g_min,g_max],'k--',lw=3)
            plt.text(3.5e-13/4,5e-16,r'$f_a\sim M_{\rm Pl}$',fontsize=fs,rotation=90)

        m_vals = array([1e-10,1e-2])
        g_QCD_upper = 1.644e-7*0.26*m_vals
        for i in logspace(1,8,40):
            ax.fill_between(m_vals,g_QCD_upper/i,y2=g_QCD_upper,color='orange',\
                            alpha=0.01,zorder=-100,lw=3)

        # QCD Axion models
        n = 200
        m = logspace(log10(m_min),log10(m_max),n)
        rot = 45.0
        trans_angle = plt.gca().transData.transform_angles(array((rot,)),array([[0, 0]]))[0]
        if KSVZ_on:
            col = 'goldenrod'
            plt.plot(m,g_x(KSVZ,m),'k-',lw=3.5,zorder=0)
            plt.plot(m,g_x(KSVZ,m),'-',lw=2,zorder=0,color=col)
            plt.text(KSVZ_label_mass,g_x(KSVZ,KSVZ_label_mass)/2,r'{\bf KSVZ}',fontsize=fs,rotation=trans_angle,color='k',ha='left',va='top',rotation_mode='anchor',clip_on=True)

        if DFSZ_on:
            col = 'goldenrod'
            #plt.fill_between(m,g_x(DFSZ_u,m),y2=1e-99,facecolor=col,zorder=0,alpha=0.5)
            plt.plot(m,g_x(DFSZ_u,m),'k-',lw=3.5,zorder=0)
            plt.plot(m,g_x(DFSZ_u,m),'-',lw=2,zorder=0,color=col)
            plt.text(DFSZ_label_mass,g_x(DFSZ_l,DFSZ_label_mass)*10,r'{\bf DFSZ}',fontsize=fs,rotation=trans_angle,color='k',ha='left',va='top',rotation_mode='anchor',clip_on=True)
        return

    def OldComagnetometers(ax,col=[0.75, 0.2, 0.2],fs=20,projection=True):
        # Old comagnetometer data arXiv:[1907.03767]
        y2 = ax.get_ylim()[1]
        zo = 0.3
        dat = loadtxt("limit_data/AxionNeutron/OldComagnetometers.txt")
        dat[:,1] *= 2*AxionNeutron.m_n
        plt.plot(dat[:,0],dat[:,1],'-',color='k',alpha=1,zorder=zo,lw=2.5)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=zo,alpha=1.0)
        plt.text(2e-20*(1-0.07),3e-5*(1+0.07),r'{\bf Old comagnetometers}',fontsize=fs,color='k',ha='center',va='top',rotation=-10,clip_on=True)
        plt.text(2e-20,3e-5,r'{\bf Old comagnetometers}',fontsize=fs,color='w',ha='center',va='top',rotation=-10,clip_on=True)
        if projection:
            dat = loadtxt("limit_data/AxionNeutron/Projections/FutureComagnetometers.txt")
            dat[:,1] *= 2*AxionNeutron.m_n
            plt.plot(dat[:,0],dat[:,1],'--',color=col,alpha=1.0,zorder=1,lw=3)
            plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=0,alpha=0.5)
            plt.text(5e-18,2*0.5e-12,r'{\bf Future comagnetometers}',fontsize=fs-1,color=col,ha='left',va='top',clip_on=True)
        return

    def UltracoldNeutronsAndMercury(ax,col=[0.5, 0.0, 0.13],fs=20,projection=True):
        # arXiv:[1902.04644]
        StochasticCorrection = 18.0 #<---- From 1905.13650
        y2 = ax.get_ylim()[1]
        zo = 1
        dat = loadtxt("limit_data/AxionNeutron/UltracoldNeutronsAndMercury.txt")
        dat[:,1] *= 2*AxionNeutron.m_n
        plt.plot(dat[:,0],StochasticCorrection*dat[:,1],'-',color='k',alpha=1,zorder=zo,lw=3)
        plt.fill_between(dat[:,0],StochasticCorrection*dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=zo)
        plt.text(0.5e-19*(1-0.07),2*StochasticCorrection*2.5e-5*(1+0.07),r'$\nu_n/\nu_{\rm Hg}$',fontsize=fs,color='k',ha='left',va='top',clip_on=True)
        plt.text(0.5e-19,2*StochasticCorrection*2.5e-5,r'$\nu_n/\nu_{\rm Hg}$',fontsize=fs,color='w',ha='left',va='top',clip_on=True)
        return


    def NASDUCK(ax,col=[0.77, 0.1, 0.13],fs=20,projection=True):
        y2 = ax.get_ylim()[1]
        zo = 1
        dat = loadtxt("limit_data/AxionNeutron/NASDUCK.txt")
        dat[:,1] *= 2*AxionNeutron.m_n
        plt.plot(dat[:,0],dat[:,1],'-',color='k',alpha=1,zorder=zo,lw=3)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=zo)
        plt.text((1-0.07)*1.5e-14,(1+0.07)*5e-5,r'{\bf NASDUCK}',fontsize=fs,color='k',ha='left',va='top',clip_on=True)
        plt.text(1.5e-14,5e-5,r'{\bf NASDUCK}',fontsize=fs,color='w',ha='left',va='top',clip_on=True)
        return



    class CASPEr():
        def ZULF(ax,col=[0.6, 0.1, 0.1],fs=20,projection=True):
            # arXiv:[1902.04644]
            StochasticCorrection = 18.0 #<---- From 1905.13650
            y2 = ax.get_ylim()[1]
            zo = 1
            dat = loadtxt("limit_data/AxionNeutron/CASPEr_ZULF.txt")
            dat[:,1] *= 2*AxionNeutron.m_n
            plt.plot(dat[:,0],StochasticCorrection*dat[:,1],'-',color='k',alpha=1.0,zorder=zo,lw=0.5)
            plt.plot(dat[0:2,0],StochasticCorrection*dat[0:2,1],'k-',lw=2.5)
            plt.fill_between(dat[:,0],StochasticCorrection*dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=zo,alpha=1.0)
            plt.text(0.3e-16*(1-0.05),(1+0.07)*StochasticCorrection*0.95e-5,r'{\bf CASPEr-ZULF}',fontsize=fs-4,color='k',ha='left',va='top',rotation=40,rotation_mode='anchor',clip_on=True)
            plt.text(0.3e-16,StochasticCorrection*0.95e-5,r'{\bf CASPEr-ZULF}',fontsize=fs-4,color='w',ha='left',va='top',rotation=40,rotation_mode='anchor',clip_on=True)
            if projection:
                dat = loadtxt("limit_data/AxionNeutron/Projections/CASPEr_ZULF.txt")
                dat[:,1] *= 2*AxionNeutron.m_n
                plt.plot(dat[:,0],dat[:,1],'--',color=col,alpha=1.0,zorder=0.1,lw=3)
                plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=0.0,alpha=0.3)
                plt.text(1e-22,2*8e-11,r'{\bf CASPEr-ZULF} (projected)',fontsize=fs,color=col,ha='left',va='top',clip_on=True)
            return

        def Comagnetometer(ax,col='darkred',fs=20,projection=True):
            # arXiv:[1901.10843]
            y2 = ax.get_ylim()[1]
            zo = 1.5
            dat = loadtxt("limit_data/AxionNeutron/CASPEr_Comagnetometer.txt")
            dat[:,1] *= 2*AxionNeutron.m_n
            plt.plot(dat[:,0],dat[:,1],'-',color='k',alpha=0.8,zorder=zo,lw=1.5)
            plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=zo,alpha=1.0)
            plt.text(1e-21*(1-0.05),(1+0.07)*1.5*5e-3,r'{\bf CASPEr-comag.}',fontsize=fs-1,color='k',ha='left',va='top',clip_on=True)
            plt.text(1e-21,1.5*5e-3,r'{\bf CASPEr-comag.}',fontsize=fs-1,color='w',ha='left',va='top',clip_on=True)
            return

        def wind(ax,col='red',fs=20,projection=True):
            # arXiv:[1711.08999]
            y2 = ax.get_ylim()[1]
            zo = -1
            dat = loadtxt("limit_data/AxionNeutron/Projections/CASPEr_wind.txt")
            dat[:,1] *= 2*AxionNeutron.m_n
            plt.plot(dat[:,0],dat[:,1],'--',color=col,alpha=1.0,zorder=zo,lw=3)
            plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=zo,alpha=0.3)
            plt.text(1.4e-9,2*1.1e-11,r'{\bf CASPEr}-wind',fontsize=fs,color=col,ha='left',va='top',rotation=27,clip_on=True)
            return

    def LabExperiments(ax,projection=True,fs=20):
        y2 = ax.get_ylim()[1]

        # Long range spin dependent forces K-3He arXiv:[0809.4700]
        zo = 0.2
        col = [0.4, 0.2, 0.2]
        dat = loadtxt("limit_data/AxionNeutron/K-3He_Comagnetometer.txt")
        plt.plot(dat[:,0],dat[:,1],'-',color='k',alpha=1,zorder=zo,lw=3)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=zo)
        plt.text((1-0.07)*5.0e-12,(1+0.07)*2.2e-4,r'{\bf K-}$^3${\bf He comagnetometer}',fontsize=fs,color='k',ha='left',va='top',clip_on=True)
        plt.text(5.0e-12,2.2e-4,r'{\bf K-}$^3${\bf He comagnetometer}',fontsize=fs,color='w',ha='left',va='top',clip_on=True)

        # Torsion balance test of gravitational inverse square law: hep-ph/0611184
        # reinterpreted in: hep-ph/0611223
        zo = 0.21
        col = [0.2, 0.25, 0.25]
        dat = loadtxt("limit_data/AxionNeutron/TorsionBalance.txt")
        plt.fill_between(dat[:,0],dat[:,1]*11500,y2=y2,edgecolor=None,facecolor=col,zorder=zo)
        plt.plot(dat[:,0],dat[:,1]*11500,'-',color='k',alpha=1,zorder=zo,lw=3)
        plt.text((1-0.07)*1e-8,(1+0.07)*3e-3,r'{\bf Torsion balance}',fontsize=fs*1.1,color='k',ha='left',va='top',clip_on=True)
        plt.text(1e-8,3e-3,r'{\bf Torsion balance}',fontsize=fs*1.1,color='w',ha='left',va='top',clip_on=True)


        # SNO, axion-induced dissociation of deuterons  arXiv:[2004.02733]
        zo = 0.03
        col = 'darkred'
        dat = loadtxt("limit_data/AxionNeutron/SNO.txt")
        dat[:,1] *= 2*AxionNeutron.m_n
        plt.plot(dat[:,0],dat[:,1],'-',color='k',alpha=1,zorder=zo,lw=3)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=zo)
        plt.text((1-0.07)*0.8e-2,(1+0.07)*3*1.6e-4,r'{\bf SNO}',fontsize=fs+6,color='k',ha='right',va='top',clip_on=True)
        plt.text(0.8e-2,3*1.6e-4,r'{\bf SNO}',fontsize=fs+6,color='w',ha='right',va='top',clip_on=True)

        if projection:
            # Proton storage ring arXiv:[2005.11867]
            zo = -1
            col = 'crimson'
            dat = loadtxt("limit_data/AxionNeutron/Projections/StorageRing.txt")
            dat[:,1] *= 2*AxionNeutron.m_n
            plt.plot(dat[:,0],dat[:,1],'--',color=col,alpha=1.0,zorder=zo,lw=3)
            plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=zo,alpha=0.2)
            plt.text(1.3e-22,2*3e-13,r'{\bf Proton Storage Ring}',fontsize=18,color=col,ha='left',va='top',clip_on=True)


    def Haloscopes(ax,projection=True,fs=20):
        AxionNeutron.OldComagnetometers(ax,projection=projection,fs=fs)
        AxionNeutron.NASDUCK(ax,fs=fs)
        AxionNeutron.CASPEr.ZULF(ax,projection=projection,fs=fs)
        AxionNeutron.CASPEr.Comagnetometer(ax,projection=projection,fs=fs)
        AxionNeutron.UltracoldNeutronsAndMercury(ax,projection=projection,fs=fs+5)
        if projection:
            AxionNeutron.CASPEr.wind(ax,fs=fs)
        return

    def StellarBounds(ax,fs=30):
        y2 = ax.get_ylim()[1]

        # Stellar physics constraints
        # SN1987A cooling nucleon-nucleon Bremsstrahlung arXiv:[1906.11844]
        SN = loadtxt("limit_data/AxionNeutron/SN1987A.txt")
        SN[:,1] *= 2*AxionNeutron.m_n
        plt.fill_between(SN[:,0],SN[:,1],y2=y2,edgecolor=None,facecolor='#067034',zorder=0.02)
        plt.plot(SN[:,0],SN[:,1],'k-',alpha=1,lw=2.5,zorder=0.02)
        plt.text((1-0.05)*0.8e-2,(1+0.05)*2*2e-8,r'{\bf SN1987A}',fontsize=fs,color='k',ha='right',va='top',clip_on=True)
        plt.text(0.8e-2,2*2e-8,r'{\bf SN1987A}',fontsize=fs,color='w',ha='right',va='top',clip_on=True)

        #  https://arxiv.org/pdf/2111.09892.pdf
        SN = loadtxt("limit_data/AxionNeutron/NeutronStars.txt")
        SN[:,1] *= 2*AxionNeutron.m_n
        plt.fill_between(SN[:,0],SN[:,1],y2=y2,edgecolor=None,facecolor='DarkGreen',zorder=0.01)
        plt.plot(SN[:,0],SN[:,1],'k-',alpha=1,lw=2.5,zorder=0.01)
        plt.text((1-0.05)*0.8e-2,(1+0.05)*9e-6,r'{\bf Neutron star cooling}',fontsize=fs-6,color='k',ha='right',va='top',clip_on=True)
        plt.text(0.8e-2,9e-6,r'{\bf Neutron star cooling}',fontsize=fs-6,color='w',ha='right',va='top',clip_on=True)
#==============================================================================#


#==============================================================================#
class AxionProton():
    m_p = 0.93828

    def QCDAxion(ax,C_logwidth=10,KSVZ_on=True,DFSZ_on=True,
                      cmap='YlOrBr',fs=25,Mpl_lab=False,DFSZ_label_mass=1e-8,KSVZ_label_mass=1e-7):
        ## QCD Axion band:
        g_min,g_max = ax.get_ylim()
        m_min,m_max = ax.get_xlim()

        # Mass-coupling relation
        def g_x(C_ae,m_a):
            return 1.64e-7*C_ae*m_a
        DFSZ_l = 0.2
        DFSZ_u = 0.6
        KSVZ = 0.46

        if Mpl_lab:
            plt.plot([3.5e-13,3.5e-13],[g_min,g_max],'k--',lw=3)
            plt.text(3.5e-13/4,5e-16,r'$f_a\sim M_{\rm Pl}$',fontsize=fs,rotation=90)

        # QCD Axion models
        n = 200
        m = logspace(log10(m_min),log10(m_max),n)
        rot = 45.0
        trans_angle = plt.gca().transData.transform_angles(array((rot,)),array([[0, 0]]))[0]
        if KSVZ_on:
            col = 'goldenrod'
            plt.plot(m,g_x(KSVZ,m),'k-',lw=3.5,zorder=0)
            plt.plot(m,g_x(KSVZ,m),'-',lw=2,zorder=0,color=col)
            plt.text(KSVZ_label_mass,g_x(KSVZ,KSVZ_label_mass)*6,r'{\bf KSVZ}',fontsize=fs,rotation=trans_angle,color='k',ha='left',va='top',rotation_mode='anchor',clip_on=True)

        if DFSZ_on:
            col = 'goldenrod'
            plt.fill_between(m,g_x(DFSZ_l,m),y2=g_x(DFSZ_u,m),facecolor=col,zorder=0,alpha=0.5)
            plt.text(DFSZ_label_mass,g_x(DFSZ_l,DFSZ_label_mass)/2,r'{\bf DFSZ models}',fontsize=fs,rotation=trans_angle,color='k',ha='left',va='top',rotation_mode='anchor',clip_on=True)
        return

    def NASDUCK(ax,col=[0.77, 0.1, 0.13],fs=20,projection=True):
        y2 = ax.get_ylim()[1]
        zo = 1
        dat = loadtxt("limit_data/AxionProton/NASDUCK.txt")
        dat[:,1] *= 2*AxionProton.m_p
        plt.plot(dat[:,0],dat[:,1],'-',color='k',alpha=1,zorder=zo,lw=3)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=zo)
        plt.text((1-0.07)*1.5e-14,(1+0.07)*5e-5,r'{\bf NASDUCK}',fontsize=fs,color='k',ha='left',va='top')
        plt.text(1.5e-14,5e-5,r'{\bf NASDUCK}',fontsize=fs,color='w',ha='left',va='top')
        return



    class CASPEr():
        def ZULF(ax,col=[0.6, 0.1, 0.1],fs=20,projection=True):
            # arXiv:[1902.04644]
            StochasticCorrection = 18.0 #<---- From 1905.13650
            y2 = ax.get_ylim()[1]
            zo = 1
            dat = loadtxt("limit_data/AxionNeutron/CASPEr_ZULF.txt")
            dat[:,1] *= 2*AxionProton.m_p
            plt.plot(dat[:,0],StochasticCorrection*dat[:,1],'-',color='k',alpha=1.0,zorder=zo,lw=0.5)
            plt.plot(dat[0:2,0],StochasticCorrection*dat[0:2,1],'k-',lw=2.5)
            plt.fill_between(dat[:,0],StochasticCorrection*dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=zo,alpha=1.0)
            plt.text(0.3e-16*(1-0.05),(1+0.07)*StochasticCorrection*0.95e-5,r'{\bf CASPEr-ZULF}',fontsize=fs-4,color='k',ha='left',va='top',rotation=40,rotation_mode='anchor')
            plt.text(0.3e-16,StochasticCorrection*0.95e-5,r'{\bf CASPEr-ZULF}',fontsize=fs-4,color='w',ha='left',va='top',rotation=40,rotation_mode='anchor')
            if projection:
                dat = loadtxt("limit_data/AxionNeutron/Projections/CASPEr_ZULF.txt")
                dat[:,1] *= 2*AxionProton.m_p
                plt.plot(dat[:,0],dat[:,1],'--',color=col,alpha=1.0,zorder=0.1,lw=3)
                plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=0.0,alpha=0.3)
                plt.text(1e-22,2*8e-11,r'{\bf CASPEr-ZULF} (projected)',fontsize=fs,color=col,ha='left',va='top')
            return

        def Comagnetometer(ax,col='darkred',fs=20,projection=True):
            # arXiv:[1901.10843]
            y2 = ax.get_ylim()[1]
            zo = 1.5
            dat = loadtxt("limit_data/AxionNeutron/CASPEr_Comagnetometer.txt")
            dat[:,1] *= 2*AxionProton.m_p
            plt.plot(dat[:,0],dat[:,1],'-',color='k',alpha=0.8,zorder=zo,lw=1.5)
            plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=zo,alpha=1.0)
            plt.text(1e-21*(1-0.05),(1+0.07)*1.5*5e-3,r'{\bf CASPEr-comag.}',fontsize=fs-1,color='k',ha='left',va='top')
            plt.text(1e-21,1.5*5e-3,r'{\bf CASPEr-comag.}',fontsize=fs-1,color='w',ha='left',va='top')
            return

        def wind(ax,col='red',fs=20,projection=True):
            # arXiv:[1711.08999]
            y2 = ax.get_ylim()[1]
            zo = -1
            dat = loadtxt("limit_data/AxionNeutron/Projections/CASPEr_wind.txt")
            dat[:,1] *= 2*AxionNeutron.m_n
            plt.plot(dat[:,0],dat[:,1],'--',color=col,alpha=1.0,zorder=zo,lw=3)
            plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=zo,alpha=0.3)
            plt.text(1.4e-9,2*1.1e-11,r'{\bf CASPEr}-wind',fontsize=fs,color=col,ha='left',va='top',rotation=27)
            return

    def LabExperiments(ax,projection=True,fs=20):
        y2 = ax.get_ylim()[1]

        # Torsion balance test of gravitational inverse square law: hep-ph/0611184
        # reinterpreted in: hep-ph/0611223
        zo = 0.21
        col = [0.2, 0.25, 0.25]
        dat = loadtxt("limit_data/AxionNeutron/TorsionBalance.txt")
        plt.fill_between(dat[:,0],dat[:,1]*11500,y2=y2,edgecolor=None,facecolor=col,zorder=zo)
        plt.plot(dat[:,0],dat[:,1]*11500,'-',color='k',alpha=1,zorder=zo,lw=3)
        plt.text((1-0.07)*1e-8,(1+0.07)*3e-3,r'{\bf Torsion balance}',fontsize=fs*1.1,color='k',ha='left',va='top')
        plt.text(1e-8,3e-3,r'{\bf Torsion balance}',fontsize=fs*1.1,color='w',ha='left',va='top')

        # Torsion balance test of gravitational inverse square law: hep-ph/0611184
        # reinterpreted in: hep-ph/0611223
        zo = 0.21
        col = [0.2, 0.25, 0.25]
        dat = loadtxt("limit_data/AxionNeutron/TorsionBalance.txt")
        plt.fill_between(dat[:,0],dat[:,1]*11500,y2=y2,edgecolor=None,facecolor=col,zorder=zo)
        plt.plot(dat[:,0],dat[:,1]*11500,'-',color='k',alpha=1,zorder=zo,lw=3)
        plt.text((1-0.07)*1e-8,(1+0.07)*3e-3,r'{\bf Torsion balance}',fontsize=fs*1.1,color='k',ha='left',va='top')
        plt.text(1e-8,3e-3,r'{\bf Torsion balance}',fontsize=fs*1.1,color='w',ha='left',va='top')

        # SNO, axion-induced dissociation of deuterons  arXiv:[2004.02733]
        zo = 0.03
        col = 'darkred'
        dat = loadtxt("limit_data/AxionNeutron/SNO.txt")
        dat[:,1] *= 2*AxionProton.m_p
        plt.plot(dat[:,0],dat[:,1],'-',color='k',alpha=1,zorder=zo,lw=3)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=zo)
        plt.text((1-0.07)*0.8e-2,(1+0.07)*3*1.6e-4,r'{\bf SNO}',fontsize=fs+6,color='k',ha='right',va='top')
        plt.text(0.8e-2,3*1.6e-4,r'{\bf SNO}',fontsize=fs+6,color='w',ha='right',va='top')

        if projection:
            # Proton storage ring arXiv:[2005.11867]
            zo = -1
            col = 'crimson'
            dat = loadtxt("limit_data/AxionNeutron/Projections/StorageRing.txt")
            dat[:,1] *= 2*AxionProton.m_p
            plt.plot(dat[:,0],dat[:,1],'--',color=col,alpha=1.0,zorder=zo,lw=3)
            plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=zo,alpha=0.2)
            plt.text(1.3e-22,2*3e-13,r'{\bf Proton Storage Ring}',fontsize=18,color=col,ha='left',va='top')

    def Haloscopes(ax,projection=True,fs=20):
        AxionNeutron.NASDUCK(ax,fs=fs)
        AxionNeutron.CASPEr.ZULF(ax,projection=projection,fs=fs)
        AxionNeutron.CASPEr.Comagnetometer(ax,projection=projection,fs=fs)
        if projection:
            AxionNeutron.CASPEr.wind(ax,fs=fs)
        return

    def StellarBounds(ax,fs=30):
        y2 = ax.get_ylim()[1]

        # Stellar physics constraints
        # SN1987A cooling nucleon-nucleon Bremsstrahlung arXiv:[1906.11844]
        SN = loadtxt("limit_data/AxionProton/SN1987A.txt")
        SN[:,1] *= 2*AxionNeutron.m_n
        plt.fill_between(SN[:,0],SN[:,1],y2=y2,edgecolor=None,facecolor='#067034',zorder=0.01)
        plt.plot(SN[:,0],SN[:,1],'k-',alpha=1,lw=2.5,zorder=0.01)
        plt.text((1-0.05)*0.8e-2,(1+0.05)*1.3e-5,r'{\bf SN1987A}',fontsize=fs,color='k',ha='right',va='top')
        plt.text(0.8e-2,1.3e-5,r'{\bf SN1987A}',fontsize=fs,color='w',ha='right',va='top')

        # Cooling of HESS J1731-347 arXiv:[1806.07991]
        SN = loadtxt("limit_data/AxionProton/NeutronStars.txt")
        SN[:,1] *= 2*AxionNeutron.m_n
        plt.fill_between(SN[:,0],SN[:,1],y2=y2,edgecolor=None,facecolor='DarkGreen',zorder=0.02)
        plt.plot(SN[:,0],SN[:,1],'k-',alpha=1,lw=2.5,zorder=0.02)
        plt.text((1-0.05)*0.8e-2,(1+0.05)*1.9e-8,r'{\bf Neutron star cooling}',fontsize=fs-6,color='k',ha='right',va='top')
        plt.text(0.8e-2,1.9e-8,r'{\bf Neutron star cooling}',fontsize=fs-6,color='w',ha='right',va='top')
#==============================================================================#


#==============================================================================#
class AxionEDM():
    def QCDAxion(ax,shading_on=True,C_logwidth=10,C_width=0.4,
                      cmap='YlOrBr',fs=28,QCD_label_mass=1e-6,\
                 text_on=True,text_col='gold',alpha=0.5,rot=45.0,zorder=-100):
        ## QCD Axion band:
        g_min,g_max = ax.get_ylim()
        m_min,m_max = ax.get_xlim()

        # Mass-coupling relation
        def g_x(C,m_a):
            return 6.4e-10*C*m_a


        if shading_on:
            n = 200
            g = logspace(log10(g_min),log10(g_max),n)
            m = logspace(log10(m_min),log10(m_max),n)
            QCD = zeros(shape=(n,n))
            for i in range(0,n):
                QCD[:,i] = norm.pdf(log10(g)-log10(g_x(1,m[i])),0.0,C_width)
            cols = cm.get_cmap(cmap)

            cols.set_under('w') # Set lowest color to white
            vmin = amax(QCD)/(C_logwidth/8)
            plt.contourf(m, g, QCD, 50,cmap=cols,vmin=vmin,vmax=1.3,zorder=zorder)
            plt.contourf(m, g, QCD, 50,cmap=cols,vmin=vmin,vmax=1.3,zorder=zorder)
            plt.contourf(m, g, QCD, 50,cmap=cols,vmin=vmin,vmax=1.3,zorder=zorder)
        else:
            n = 200
            col ='goldenrod'
            m = logspace(log10(m_min),log10(m_max),n)
            plt.fill_between(m,g_x(1-0.4,m),y2=g_x(1+0.4,m),facecolor=col,zorder=0,alpha=alpha)

        if text_on:
            trans_angle = plt.gca().transData.transform_angles(array((rot,)),array([[0, 0]]))[0]
            plt.text(QCD_label_mass,g_x(1-0.4,QCD_label_mass)/1.4,r'{\bf QCD axion}',\
             fontsize=fs,rotation=trans_angle+1,color=text_col,ha='left',va='top',rotation_mode='anchor',clip_on=True,
             path_effects=line_background(1.4,'k'))
        return

    def nEDM(ax,text_pos=[5e-20,1e-18],col='darkred',text_col='w',text_rot=0,fs=30,zorder=-1):
        dat = loadtxt('limit_data/AxionEDM/nEDM.txt')
        plt.plot(dat[:,0],dat[:,1],color='k',lw=3,alpha=1,zorder=zorder)
        plt.fill_between(dat[:,0],dat[:,1],y2=1e0,color=col,zorder=zorder,alpha=1)
        plt.text(text_pos[0],text_pos[1],r'{\bf nEDM}',color=text_col,rotation=text_rot,fontsize=fs,clip_on=True)
        return

    def BeamEDM(ax,text_pos=[6e-18,2e-15],col='#822f2b',text_col='w',text_rot=30,fs=22,zorder=-1):
        dat = loadtxt('limit_data/AxionEDM/BeamEDM.txt')
        plt.fill_between(dat[:,0],dat[:,1],y2=1e0,color=col,zorder=zorder,alpha=1)
        plt.plot(dat[:,0],dat[:,1],color='k',lw=1.5,alpha=1,zorder=zorder)
        plt.text(text_pos[0],text_pos[1],r'{\bf Beam EDM}',color=text_col,rotation=text_rot,fontsize=fs,clip_on=True)
        return

    def HfF(ax,text_pos=[0.7e-19,1.5e-14],col='#a3435e',text_col='w',text_rot=30,fs=22,zorder=-1):
        dat = loadtxt('limit_data/AxionEDM/HfF.txt')
        plt.fill_between(dat[:,0],dat[:,1],y2=1e0,color=col,zorder=zorder,alpha=1)
        plt.plot(dat[:,0],dat[:,1],color='k',lw=1.5,alpha=1,zorder=zorder)
        plt.text(text_pos[0],text_pos[1],r'{\bf HfF}$^+$',color=text_col,rotation=text_rot,fontsize=fs,clip_on=True)
        return

    def SN1987A(ax,text_pos=[2e-10,0.9e-8],col='#067034',text_col='w',text_rot=0,fs=33,zorder=1):
        dat = loadtxt('limit_data/AxionEDM/SN1987A.txt')
        plt.plot(dat[:,0],dat[:,1],color='k',lw=3,alpha=1,zorder=zorder)
        plt.fill_between(dat[:,0],dat[:,1],y2=1e0,color=col,zorder=zorder,alpha=1)
        plt.text(text_pos[0],text_pos[1],r'{\bf SN1987A}',color=text_col,rotation=text_rot,fontsize=fs,ha='right',clip_on=True)
        return


    def PlanckBAO(ax,text_pos=[3e-10,0.5e-9],col='#1a6e7a',text_col='w',text_rot=0,fs=26,zorder=0.8):
        dat = loadtxt('limit_data/AxionEDM/PlanckBAO.txt')
        plt.plot(dat[:,0],dat[:,1],color='k',lw=3,alpha=1,zorder=zorder)
        plt.fill_between(dat[:,0],dat[:,1],y2=1e0,color=col,zorder=zorder,alpha=1)
        plt.text(text_pos[0],text_pos[1],r'{\bf Planck+BAO}',color=text_col,rotation=text_rot,fontsize=fs,ha='right',clip_on=True)
        return

    def CASPEr(ax,text_pos=[130e-9,1e-3],col='crimson',text_col='w',fs=20,zorder=30,projection=False,text_on=True):
        dat = loadtxt('limit_data/AxionEDM/CASPEr-electric.txt')
        plt.plot(dat[:,0],dat[:,1],'-',color=col,zorder=13,lw=4)
        if text_on:
            plt.text(text_pos[0],text_pos[1],r'{\bf CASPEr-electric}',color=text_col,fontsize=fs,ha='right',zorder=zorder)
        if projection:
            dat = loadtxt('limit_data/AxionEDM/Projections/CASPEr-electric-PhaseI.txt')
            plt.plot(dat[:,0],dat[:,1],'--',color=col,zorder=-10,lw=3)
            plt.fill_between(dat[:,0],dat[:,1],y2=1e0,color=col,lw=4,alpha=0.05,zorder=-10)

            dat = loadtxt('limit_data/AxionEDM/Projections/CASPEr-electric-PhaseII.txt')
            plt.plot(dat[:,0],dat[:,1],'--',color=col,zorder=-10,lw=3)
            plt.fill_between(dat[:,0],dat[:,1],y2=1e0,color=col,lw=4,alpha=0.05,zorder=-10)

            dat = loadtxt('limit_data/AxionEDM/Projections/CASPEr-electric-PhaseIII.txt')
            plt.plot(dat[:,0],dat[:,1],'--',color=col,zorder=-10,lw=3)
            plt.fill_between(dat[:,0],dat[:,1],y2=1e0,color=col,lw=4,alpha=0.05,zorder=-10)
            if text_on:
                plt.text(0.5e-12,0.2e-13,r'{\bf CASPEr-electric}',rotation=37,fontsize=25,color=col,clip_on=True)
                plt.text(0.7e-10,0.08e-11,'phase I',rotation=38,fontsize=20,color=col,clip_on=True)
                plt.text(1.5e-8,3e-15,'phase II',rotation=49,fontsize=20,color=col,clip_on=True)
                plt.text(7e-8,0.3e-15,'phase III',rotation=49,fontsize=20,color=col,clip_on=True)
        return

#==============================================================================#


#==============================================================================#
class Axion_fa():
    def QCDAxion(ax,shading_on=True,C_logwidth=10,C_width=0.4,
                      linecolor='gold',fs=28,QCD_label_mass=1e-7,\
                 text_on=True,text_col='gold',alpha=0.5,rot=45.0,zorder=-100):
        ## QCD Axion band:
        g_min,g_max = ax.get_ylim()
        m_min,m_max = ax.get_xlim()

        # Mass-coupling relation
        def f_a(C,m_a):
            return C*(1/1e12)*(m_a/5.7e-6)
        plt.plot([m_min,m_max],[f_a(1,m_min),f_a(1,m_max)],'-',lw=5,path_effects=line_background(6,'k'),color=linecolor,zorder=zorder)

        if text_on:
            trans_angle = plt.gca().transData.transform_angles(array((rot,)),array([[0, 0]]))[0]
            plt.text(QCD_label_mass,f_a(1-0.4,QCD_label_mass)/1.4,r'{\bf QCD axion}',\
                 fontsize=fs,rotation=trans_angle+1,color=text_col,ha='left',va='top',rotation_mode='anchor',clip_on=True,
                 path_effects=line_background(1.4,'k'))
        return

    def nEDM(ax,text_pos=[3e-20,0.2e-13],col='darkred',text_col='w',text_rot=0,fs=28,zorder=-1):
        # Already accounts for stochastic correction
        dat = loadtxt('limit_data/fa/nEDM.txt')
        plt.plot(dat[:,0],dat[:,1],color='k',lw=3,alpha=1,zorder=zorder)
        plt.fill_between(dat[:,0],dat[:,1],y2=1e0,color=col,zorder=zorder,alpha=1)
        plt.text(text_pos[0],text_pos[1],r'{\bf nEDM}',color=text_col,rotation=text_rot,fontsize=fs,clip_on=True)
        return

    def BeamEDM(ax,text_pos=[6e-18,6e-13],col='#822f2b',text_col='w',text_rot=40,fs=22,zorder=-1):
        dat = loadtxt('limit_data/fa/BeamEDM.txt')
        plt.fill_between(dat[:,0],dat[:,1],y2=1e0,color=col,zorder=zorder,alpha=1)
        plt.plot(dat[:,0],dat[:,1],color='k',lw=1.5,alpha=1,zorder=zorder)
        plt.text(text_pos[0],text_pos[1],r'{\bf Beam EDM}',color=text_col,rotation=text_rot,fontsize=fs,clip_on=True)
        return

    def HfF(ax,text_pos=[0.7e-19,4e-12],col='#a3435e',text_col='w',text_rot=40,fs=22,zorder=-1):
        dat = loadtxt('limit_data/fa/HfF.txt')
        plt.fill_between(dat[:,0],dat[:,1],y2=1e0,color=col,zorder=zorder,alpha=1)
        plt.plot(dat[:,0],dat[:,1],color='k',lw=1.5,alpha=1,zorder=zorder)
        plt.text(text_pos[0],text_pos[1],r'{\bf HfF}$^+$',color=text_col,rotation=text_rot,fontsize=fs,clip_on=True)
        return

    def SolarCore(ax,text_pos=[1e-15,0.15e-14],col='#0d4dba',text_col='w',text_rot=41,fs=30,zorder=-5):
        dat = loadtxt('limit_data/fa/SolarCore.txt')
        plt.plot(dat[:,0],dat[:,1],color='k',lw=3,alpha=1,zorder=zorder)
        plt.fill_between(dat[:,0],dat[:,1],y2=1e0,color=col,zorder=zorder,alpha=1)
        plt.text(text_pos[0],text_pos[1],r'{\bf Solar core}',color=text_col,rotation=text_rot,fontsize=fs,clip_on=True)
        return


    def GW170817(ax,text_pos=[7e-16,2e-17],zo=-7,linespacing_y=0.65,col=col_alpha('teal',0.4),text_col='teal',text_rot=0,fs=23):
        dat = loadtxt('limit_data/fa/GW170817.txt')
        plt.plot(dat[:,0],dat[:,1],color='k',lw=3,alpha=1,zorder=zo)
        plt.fill_between(dat[:,0],dat[:,1],color=col,zorder=zo,alpha=1)

        plt.text(text_pos[0],text_pos[1],r'{\bf GW170817}',color=text_col,rotation=text_rot,fontsize=fs,ha='center',clip_on=True)
        return


    def Pulsars(ax,text_pos=[3e-15,0.11e-16],linespacing_y=0.65,col='#05526e',text_col='#05526e',text_rot=0,fs=21,zo=-6.9):
        dat = loadtxt('limit_data/fa/Pulsar.txt')
        plt.plot(dat[:,0],dat[:,1],color='k',lw=3,alpha=1,zorder=zo)
        plt.fill_between(dat[:,0],dat[:,1],color=col,zorder=zo,alpha=1)

        plt.text(text_pos[0],text_pos[1]*(1-linespacing_y),r'{\bf Pulsars}',color=text_col,rotation=text_rot,fontsize=fs,ha='center',clip_on=True)
        return


    def BBN(ax,text_pos=[1.7e-17,0.8e-16],col='navy',text_col='w',text_rot=15,fs=20,zorder=-6):
        dat = loadtxt('limit_data/fa/BBN.txt')
        plt.plot(dat[:,0],dat[:,1],color='k',lw=3,alpha=1,zorder=zorder)
        plt.fill_between(dat[:,0],dat[:,1],y2=1e0,color=col,zorder=zorder,alpha=1)
        plt.text(text_pos[0],text_pos[1],r'{\bf BBN}',color=text_col,rotation=text_rot,fontsize=fs,clip_on=True)
        return

    def SN1987A(ax,text_pos=[7e-3,0.4e-5],col='#067034',text_col='w',text_rot=0,fs=33,zorder=1):
        dat = loadtxt('limit_data/fa/SN1987A.txt')
        plt.plot(dat[:,0],dat[:,1],color='k',lw=3,alpha=1,zorder=zorder)
        plt.fill_between(dat[:,0],dat[:,1],y2=1e0,color=col,zorder=zorder,alpha=1)
        plt.text(text_pos[0],text_pos[1],r'{\bf SN1987A}',color=text_col,rotation=text_rot,fontsize=fs,ha='right',clip_on=True)
        return

    def NeutronStars(ax,text_pos=[0.5e-3,0.4e-12],col='#1f6ff0',text_col='#1f6ff0',text_rot=41,fs=29,zorder=-10):
        dat = loadtxt('limit_data/fa/Projections/NeutronStars.txt')
        plt.plot(dat[:,0],dat[:,1],'--',color=col,lw=3,alpha=1,zorder=zorder)
        plt.fill_between(dat[:,0],dat[:,1],y2=1e0,color=col,zorder=zorder,alpha=0.1)
        plt.text(text_pos[0],text_pos[1],r'{\bf Neutron stars}',color=text_col,rotation=text_rot,fontsize=fs,ha='right',clip_on=True)
        return

    def Inspirals(ax,text_pos=[1e-16,2e-14],col='#b9befa',text_col='#b9befa',text_rot=0,fs=23,zorder=-10):
        dat = loadtxt('limit_data/fa/Projections/NSBH-Inspiral.txt')
        plt.plot(dat[:,0],dat[:,1],'--',color=col,lw=3,alpha=1,zorder=zorder)
        plt.fill_between(dat[:,0],dat[:,1],y2=1e-99,color=col,zorder=zorder,alpha=0.2)

        dat = loadtxt('limit_data/fa/Projections/NSNS-Inspiral.txt')
        plt.plot(dat[:,0],dat[:,1],'--',color=col,lw=3,alpha=1,zorder=zorder)
        plt.fill_between(dat[:,0],dat[:,1],y2=1e-99,color=col,zorder=zorder,alpha=0.2)

        plt.text(text_pos[0],text_pos[1],r'{\bf Inspirals}',color=text_col,rotation=text_rot,fontsize=fs,clip_on=True)
        return

    def StorageRingEDM(ax,text_pos=[1e-11,1.5e-13],col='crimson',alpha=0.4,zorder=-10,text_rot=41,fs=20):
        dat = loadtxt('limit_data/fa/Projections/StorageRingEDM.txt')
        plt.plot(dat[:,0],dat[:,1],'--',lw=3,color=col,zorder=zorder,alpha=0.4)
        plt.fill_between(dat[:,0],dat[:,1],y2=1e0,color=col,alpha=0.1,zorder=zorder)
        plt.text(text_pos[0],text_pos[1],r'{\bf Storage ring}',color=col,alpha=0.4,fontsize=fs,rotation=text_rot,clip_on=True)
        return

    def CASPEr(ax,text_pos=[4e-11,1e-19],col='crimson',alpha=0.1,zorder=-10,text_rot=57,fs=23):
        dat = loadtxt('limit_data/fa/Projections/CASPEr-electric-PhaseIII.txt')
        plt.plot(dat[:,0],dat[:,1],'--',lw=3,color=col,zorder=-1,alpha=1)
        plt.fill_between(dat[:,0],dat[:,1],y2=1e0,color=col,alpha=alpha,zorder=zorder)
        plt.text(text_pos[0],text_pos[1],r'{\bf CASPEr-electric}',color=col,alpha=1,fontsize=fs,rotation=text_rot,clip_on=True)
        return

    def PiezoaxionicEffect(ax,text_pos=[7.6e-10,0.4e-14],col='darkred',alpha=0.4,zorder=-10,text_rot=90,fs=20):
        dat = loadtxt('limit_data/fa/Projections/PiezoaxionicEffect1.txt')
        plt.plot(dat[:,0],dat[:,1],'--',lw=1.5,color=col,zorder=zorder,alpha=0.4)
        plt.fill_between(dat[:,0],dat[:,1],y2=1e0,color=col,alpha=0.1,zorder=zorder)
        dat = loadtxt('limit_data/fa/Projections/PiezoaxionicEffect64.txt')
        plt.plot(dat[:,0],dat[:,1],'--',lw=1.5,color=col,zorder=zorder,alpha=0.4)
        plt.fill_between(dat[:,0],dat[:,1],y2=1e0,color=col,alpha=0.1,zorder=zorder)
        plt.text(text_pos[0],text_pos[1],r'{\bf Piezoaxionic}',color=col,alpha=0.6,fontsize=fs,rotation=text_rot,clip_on=True)
        return
#==============================================================================#


class DarkPhoton():
    def FigSetup(xlab=r'Dark photon mass [eV]',ylab='Kinetic mixing',\
             chi_min = 1.0e-18,chi_max = 1.0e0,\
             m_min = 3e-18,m_max = 1e5,\
             lw=2.5,lfs=40,tfs=25,tickdir='out',\
             Grid=False,Shape='Rectangular',mathpazo=True,\
             TopAndRightTicks=False,FrequencyAxis=True,FrequencyLabels=True,UnitAxis=True,f_rescale=1,\
            tick_rotation = 20,width=20,height=10,upper_tickdir='out'):

        plt.rcParams['axes.linewidth'] = lw
        plt.rc('text', usetex=True)
        plt.rc('font', family='serif',size=tfs)

        if mathpazo:
            plt.rcParams.update({"text.usetex": True,"font.family": "serif","font.serif": ["Palatino"],})


        if Shape=='Wide':
            fig = plt.figure(figsize=(16.5,5))
        elif Shape=='Rectangular':
            fig = plt.figure(figsize=(16.5,11))
        elif Shape=='Custom':
            fig = plt.figure(figsize=(width,height))

        ax = fig.add_subplot(111)

        ax.set_xlabel(xlab,fontsize=lfs)
        ax.set_ylabel(ylab,fontsize=lfs)

        ax.tick_params(which='major',direction=tickdir,width=2.5,length=13,right=TopAndRightTicks,top=TopAndRightTicks,pad=7)
        ax.tick_params(which='minor',direction=tickdir,width=1,length=10,right=TopAndRightTicks,top=TopAndRightTicks)


        ax.set_yscale('log')
        ax.set_xscale('log')
        ax.set_xlim([m_min,m_max])
        ax.set_ylim([chi_min,chi_max])

        locmaj = mpl.ticker.LogLocator(base=10.0, subs=(1.0, ), numticks=50)
        locmin = mpl.ticker.LogLocator(base=10.0, subs=arange(2, 10)*.1,numticks=100)
        ax.xaxis.set_major_locator(locmaj)
        ax.xaxis.set_minor_locator(locmin)
        ax.xaxis.set_minor_formatter(mpl.ticker.NullFormatter())

        locmaj = mpl.ticker.LogLocator(base=10.0, subs=(1.0, ), numticks=100)
        locmin = mpl.ticker.LogLocator(base=10.0, subs=arange(2, 10)*.1,numticks=100)
        ax.yaxis.set_major_locator(locmaj)
        ax.yaxis.set_minor_locator(locmin)
        ax.yaxis.set_minor_formatter(mpl.ticker.NullFormatter())

        if Shape=='Rectangular':
            plt.xticks(rotation=tick_rotation)

        if Grid:
            ax.grid(zorder=0)

        if FrequencyAxis:
            ax2 = ax.twiny()



            ax2.set_xscale('log')
            ax2.tick_params(which='major',direction=upper_tickdir,width=2.5,length=13,pad=7)
            ax2.tick_params(which='minor',direction=upper_tickdir,width=1,length=10)
            locmaj = mpl.ticker.LogLocator(base=10.0, subs=(1.0, ), numticks=50)
            locmin = mpl.ticker.LogLocator(base=10.0, subs=arange(2, 10)*.1,numticks=100)
            ax2.xaxis.set_major_locator(locmaj)
            ax2.xaxis.set_minor_locator(locmin)
            ax2.xaxis.set_minor_formatter(mpl.ticker.NullFormatter())

            if FrequencyLabels:
                ax2.set_xticks([1e-3,1e0,1e3,1e6,1e9,1e12,1*241.8*1e12,1000*241.8*1e12])
                ax2.set_xticklabels(['mHz','Hz','kHz','MHz','GHz','THz','eV','keV'])
            ax2.set_xlim([m_min*241.8*1e12/f_rescale,m_max*241.8*1e12/f_rescale])

            plt.sca(ax)
        return fig,ax


    def Haloscopes(ax,col=[0.75, 0.2, 0.2],fs=17,projection=True,text_on=True):
        y2 = ax.get_ylim()[1]
        zo = 0.3

        HAYSTAC_col = 'indianred'
        CAPP_col = 'crimson'
        QUAX_col = 'r'
        ADMX_col = 'firebrick'

        # ADMX
        costh = sqrt(0.019)
        B = 7.6
        dat = loadtxt("limit_data/AxionPhoton/ADMX.txt")
        dat[:,1] = 1e-9*dat[:,1]*(B/(1.444e-3*costh*dat[:,0]))
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor='none',facecolor=ADMX_col,zorder=0.1,lw=3)

        B = 6.8
        dat = loadtxt("limit_data/AxionPhoton/ADMX2018.txt")
        dat[:,1] = 1e-9*dat[:,1]*(B/(1.444e-3*costh*dat[:,0]))
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor='none',facecolor=ADMX_col,zorder=0.1)

        B = 7.6
        dat = loadtxt("limit_data/AxionPhoton/ADMX2019_1.txt")
        dat[:,1] = 1e-9*dat[:,1]*(B/(1.444e-3*costh*dat[:,0]))
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor='none',facecolor=ADMX_col,zorder=0.1)

        B = 7.6
        dat = loadtxt("limit_data/AxionPhoton/ADMX2019_2.txt")
        dat[:,1] = 1e-9*dat[:,1]*(B/(1.444e-3*costh*dat[:,0]))
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor='none',facecolor=ADMX_col,zorder=0.1)

        B = 7.6
        dat = loadtxt("limit_data/AxionPhoton/ADMX2021.txt")
        dat[:,1] = 1e-9*dat[:,1]*(B/(1.444e-3*costh*dat[:,0]))
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor='none',facecolor=ADMX_col,zorder=0.1)

    #     B = 3.11
    #     dat = loadtxt("limit_data/AxionPhoton/ADMX_Sidecar_AC.txt")
    #     dat[:,1] = 1e-9*dat[:,1]*(B/(1.444e-3*costh*dat[:,0]))
    #     plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=ADMX_col,facecolor=ADMX_col,zorder=0.1)

    #     B = 5.0
    #     dat = loadtxt("limit_data/AxionPhoton/ADMX_SLIC.txt")
    #     dat[:,1] = 1e-9*dat[:,1]*(B/(1.444e-3*costh*dat[:,0]))
    #     plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=ADMX_col,facecolor=ADMX_col,zorder=100)



        B = 9
        dat = loadtxt("limit_data/AxionPhoton/HAYSTAC_highres.txt")
        dat[:,1] = 1e-9*dat[:,1]*(B/(1.444e-3*costh*dat[:,0]))
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor='none',facecolor=HAYSTAC_col,zorder=0.1)
        dat = loadtxt("limit_data/AxionPhoton/HAYSTAC_2020_highres.txt")
        dat[:,1] = 1e-9*dat[:,1]*(B/(1.444e-3*costh*dat[:,0]))
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor='none',facecolor=HAYSTAC_col,zorder=0.1)


        # CAPP
        B = 7.3
        dat = loadtxt("limit_data/AxionPhoton/CAPP-1.txt")
        dat[:,1] = 1e-9*dat[:,1]*(B/(1.444e-3*costh*dat[:,0]))
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor='none',facecolor=CAPP_col,zorder=0.1)

        B = 7.8
        dat = loadtxt("limit_data/AxionPhoton/CAPP-2.txt")
        dat[:,1] = 1e-9*dat[:,1]*(B/(1.444e-3*costh*dat[:,0]))
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor='none',facecolor=CAPP_col,zorder=0.1)

        B = 7.9
        dat = loadtxt("limit_data/AxionPhoton/CAPP-3.txt")
        dat[:,1] = 1e-9*dat[:,1]*(B/(1.444e-3*costh*dat[:,0]))
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor='none',facecolor=CAPP_col,zorder=0.1)

        # CAPP-3 [KSVZ]
        dat_min = dat[argmin(dat[:,1]),:]
        dat_min[1] = dat_min[1]*costh/sqrt(0.2)
        plt.plot([dat_min[0],dat_min[0]],[1e-10,dat_min[1]],'-',color=CAPP_col,lw=1.5,zorder=0.1)


        B = 8.1
        costh = sqrt(0.03)
        dat = loadtxt("limit_data/AxionPhoton/QUAX.txt")
        dat[:,1] = 1e-9*dat[:,1]*(B/(1.444e-3*0.023*dat[:,0]))
        plt.fill_between([dat[0,0],dat[0,0]],[y2,dat[0,1]],y2=y2,color=QUAX_col,zorder=0.1)


        if text_on:
            plt.text(1.4e-6,0.5e-14,switch_label(r'{\bf ADMX}'),fontsize=fs,color=ADMX_col,rotation=90,rotation_mode='anchor',ha='center',va='center')
            plt.text(0.8e-5,0.1e-13,switch_label(r'{\bf CAPP}'),fontsize=fs-2,color=CAPP_col,rotation=90,rotation_mode='anchor',ha='center',va='center')
            plt.text(0.19e-4,3e-15,switch_label(r'{\bf HAYSTAC}'),fontsize=fs-5,color=HAYSTAC_col,rotation=90,rotation_mode='anchor',ha='center',va='center')
            plt.text(0.47e-4,3e-12,switch_label(r'{\bf QUAX}'),fontsize=fs-8,color=QUAX_col,rotation=-90,rotation_mode='anchor',ha='center',va='center')

        return


    def StellarBounds(ax,fs=19,text_on=True):
        y2 = ax.get_ylim()[1]
        # Stellar physics constraints

        # Globular clusters
        HB_col = [0.01, 0.75, 0.24]
        HB = loadtxt("limit_data/DarkPhoton/RG.txt")
        plt.plot(HB[:,0],HB[:,1],color='k',alpha=0.5,zorder=0.9,lw=2)
        plt.fill_between(HB[:,0],HB[:,1],y2=y2,edgecolor=None,facecolor=HB_col,zorder=0.9)

        # Globular clusters
        HB_col = 'DarkGreen'
        HB = loadtxt("limit_data/DarkPhoton/HB.txt")
        plt.plot(HB[:,0],HB[:,1],color='k',alpha=0.5,zorder=0.95,lw=2)
        plt.fill_between(HB[:,0],HB[:,1],y2=y2,edgecolor=None,facecolor=HB_col,zorder=0.95)

        # Solar bound
        Solar_col = 'ForestGreen'
        Solar = loadtxt("limit_data/DarkPhoton/Solar.txt")
        plt.plot(Solar[:,0],Solar[:,1],color='k',alpha=0.5,zorder=1.02,lw=2)
        plt.fill_between(Solar[:,0],Solar[:,1],y2=y2,edgecolor=None,facecolor=Solar_col,zorder=1.02)

        Solar = loadtxt("limit_data/DarkPhoton/Solar-Global.txt")
        plt.plot(Solar[:,0],Solar[:,1]/Solar[:,0],color='k',alpha=0.5,zorder=1.021,lw=2)
        plt.fill_between(Solar[:,0],Solar[:,1]/Solar[:,0],y2=y2,edgecolor=None,facecolor=Solar_col,zorder=1.021)

        if text_on:
            plt.text(0.8e2*(1-0.01),1.5e-14*(1+0.05),r'{\bf Solar}',fontsize=fs,color='k',rotation=-41,rotation_mode='anchor',ha='center',va='center')
            plt.text(1e3*(1-0.01),0.7e-14*(1+0.05),r'{\bf HB}',fontsize=fs,color='k',rotation=-38,rotation_mode='anchor',ha='center',va='center')
            plt.text(0.8e4*(1-0.01),0.7e-14*(1+0.05),r'{\bf RG}',fontsize=fs,color='k',rotation=-37,rotation_mode='anchor',ha='center',va='center')
            plt.text(0.8e2,1.5e-14,r'{\bf Solar}',fontsize=fs,color='w',rotation=-41,rotation_mode='anchor',ha='center',va='center')
            plt.text(1e3,0.7e-14,r'{\bf HB}',fontsize=fs,color='w',rotation=-38,rotation_mode='anchor',ha='center',va='center')
            plt.text(0.8e4,0.7e-14,r'{\bf RG}',fontsize=fs,color='w',rotation=-37,rotation_mode='anchor',ha='center',va='center')
        return


    def Xenon(ax,col='crimson',fs=23,text_on=True):
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/DarkPhoton/Xenon1T.txt")
        dat[:,1] = dat[:,1]*sqrt(0.3/0.45)

        plt.plot(1e3*dat[:,0],dat[:,1],color='k',alpha=0.5,zorder=0.5,lw=2)
        plt.fill_between(1e3*dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=0.5)

        dat = loadtxt("limit_data/DarkPhoton/Xenon1T_S1S2.txt")
        dat[:,1] = dat[:,1]*sqrt(0.3/0.45)

        plt.plot(dat[:,0],dat[:,1],color='k',alpha=0.5,zorder=0.5,lw=2)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=0.5)


        dat = loadtxt("limit_data/DarkPhoton/XENON1T_SE.txt")
        dat[:,1] = dat[:,1]*sqrt(0.3/0.45)
        plt.plot(dat[:,0],dat[:,1],color='k',alpha=0.5,zorder=0.5,lw=2)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=0.5)


        dat = loadtxt("limit_data/DarkPhoton/XENON1T_Solar_S2.txt")
        plt.plot(dat[:,0],dat[:,1],color='k',alpha=0.5,zorder=0.5,lw=2)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=0.5)


        dat = loadtxt("limit_data/DarkPhoton/XENONnT.txt")
        plt.plot(dat[:,0],dat[:,1],color='k',alpha=0.5,zorder=0.5,lw=2)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=0.5)

        if text_on:
            plt.text(8e2,2.5e-17,r'{\bf XENON}',fontsize=fs,color=col,rotation=0,rotation_mode='anchor',ha='center',va='center')

        return





    def DAMIC(ax,col='salmon',fs=21,text_on=True):
        m1,y1 = loadtxt("limit_data/DarkPhoton/DM_combined.txt",unpack=True)
        dat = loadtxt("limit_data/DarkPhoton/DAMIC.txt")
        dat[:,1] = dat[:,1]*sqrt(0.3/0.45)

        y2 = interp(dat[:,0],m1,y1)
        dat[0,1] = y2[0]
        dat[-1,1] = y2[-1]
        plt.plot(dat[:,0],dat[:,1],color='k',alpha=1,zorder=1.001,lw=2)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=1.001)
        if text_on:
            plt.text(6e-1,1.3e-14,r'{\bf DAMIC}',fontsize=fs,color=col,rotation=0,rotation_mode='anchor',ha='center',va='center')
            plt.plot([5e0,1e1],[3e-14,6e-14],'-',lw=2.5,color=col)
        return

    def MuDHI(ax,col='#a82844',fs=15,text_on=True):
        m1,y1 = loadtxt("limit_data/DarkPhoton/DM_combined.txt",unpack=True)
        dat = loadtxt("limit_data/DarkPhoton/MuDHI.txt")

        y2 = interp(dat[:,0],m1,y1)
        dat[dat[:,1]>y2,1] = y2[dat[:,1]>y2]
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=10)
        plt.plot(dat[::2,0],dat[::2,1],color='k',alpha=1,zorder=10,lw=1.2)

        if text_on:
            plt.text(0.42e-2,1.8e-11,r'{\bf MuDHI}',fontsize=fs,color=col,rotation=0,rotation_mode='anchor',ha='center',va='center')
            plt.plot([2.8e-2,1.5e0],[2e-11,4e-11],'-',lw=2,color=col,path_effects=line_background(1,'k'))
        return


    def FUNK(ax,col='red',fs=21,text_on=True):
        m1,y1 = loadtxt("limit_data/DarkPhoton/DM_combined.txt",unpack=True)
        dat = loadtxt("limit_data/DarkPhoton/FUNK.txt")
        dat[:,1] = dat[:,1]*sqrt(0.3/0.45)*sqrt(2/3/0.27)

        y2 = interp(dat[:,0],m1,y1)
        #dat[0,1] = y2[0]
        dat[dat[:,1]>y2,1] = y2[dat[:,1]>y2]
        plt.plot(dat[:,0],dat[:,1],color='k',alpha=1,zorder=1.3,lw=2)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=1.3)
        if text_on:
            plt.text(2.6e-1,1e-13,r'{\bf FUNK}',fontsize=fs,color=col,rotation=0,rotation_mode='anchor',ha='center',va='center')
            plt.plot([9e-1,3e0],[3e-13,1e-12],'-',lw=2.5,color=col)
        return

    def SENSEI(ax,col='firebrick',fs=21,text_on=True):
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/DarkPhoton/SENSEI.txt")
        dat[:,1] = dat[:,1]*sqrt(0.3/0.45)

        plt.plot(dat[:,0],dat[:,1],color='k',alpha=1,zorder=1,lw=2)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=1)
        if text_on:
            plt.text(1.7e0,1e-15,r'{\bf SENSEI}',fontsize=fs,color=col,rotation=0,rotation_mode='anchor',ha='center',va='center')
            plt.plot([7e0,1e1],[3e-15,9e-15],'-',lw=2.5,color=col)
        return

    def SuperCDMS(ax,col=[0.4,0,0],fs=18,text_on=True):
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/DarkPhoton/SuperCDMS.txt")
        dat[:,1] = dat[:,1]*sqrt(0.3/0.45)
        plt.plot(dat[:,0],dat[:,1],color='k',alpha=0.5,zorder=0.6,lw=2)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=0.6)

        if text_on:
            plt.text(0.5e1,1.5e-16,r'{\bf SuperCDMS}',fontsize=fs,color=col,rotation=0,rotation_mode='anchor',ha='center',va='center')
            plt.plot([5e1,0.8e2],[3e-16,9e-16],'-',lw=2.5,color=col)
        return

    def Nanowire(ax,col='pink',fs=22,text_on=True):
        m1,y1 = loadtxt("limit_data/DarkPhoton/DM_combined.txt",unpack=True)
        dat = loadtxt("limit_data/DarkPhoton/WSi_Nanowire.txt")
        dat[:,1] = dat[:,1]*sqrt(0.3/0.45)
        y2 = interp(dat[:,0],m1,y1)
        dat[0,1] = y2[0]/1.1
        dat[-1,1] = y2[-1]/1.1
        plt.plot(dat[:,0],dat[:,1],color='k',alpha=1,zorder=1.3,lw=2)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=1.3)
        if text_on:
            plt.text(5e-4,1e-10,r'{\bf WSi Nanowire}',fontsize=fs,color=col,rotation=0,rotation_mode='anchor',ha='center',va='center')
            plt.plot([9e-3,3e-3],[3e-10,9e-10],'-',lw=2.5,color=col)
        return

    def LAMPOST(ax,col='red',fs=15,text_on=True):
        m1,y1 = loadtxt("limit_data/DarkPhoton/DM_combined.txt",unpack=True)
        dat = loadtxt("limit_data/DarkPhoton/LAMPOST.txt")
        dat[:,1] = dat[:,1]*sqrt(0.4/0.45)*sqrt(2/3/0.27)

        y2 = interp(dat[:,0],m1,y1)
        dat[0,1] = y2[0]/1.1
        dat[-1,1] = y2[-1]/1.1
        plt.plot(dat[:,0],dat[:,1],color=col,alpha=1,zorder=0,lw=2)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=0)
        if text_on:
            plt.text(0.3e-1,5e-13,r'{\bf LAMPOST}',fontsize=fs,color=col,rotation=0,rotation_mode='anchor',ha='center',va='center')
            plt.plot([3e-1,0.6e0],[6e-13,1e-12],'-',lw=1.5,color=col)
        return

    def Tokyo(ax,col='darkred',fs=15,text_on=True):
        m1,y1 = loadtxt("limit_data/DarkPhoton/DM_combined.txt",unpack=True)
        dat = loadtxt("limit_data/DarkPhoton/Tokyo-Dish.txt")
        dat[:,1] = dat[:,1]*sqrt(2/3/0.6)
        y2 = interp(dat[:,0],m1,y1)
        dat[0,1] = y2[0]
        dat[-1,1] = y2[-1]
        plt.plot(dat[:,0],dat[:,1],color='k',alpha=1,zorder=1.4,lw=2)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=1.4)


        dat = loadtxt("limit_data/DarkPhoton/Tokyo-Knirck.txt")
        dat[:,1] = dat[:,1]*sqrt(1/3/0.175)
        plt.fill_between(dat[:,0],dat[:,1],y2=1e0,edgecolor='k',facecolor=col,zorder=1.09)

        dat = loadtxt("limit_data/DarkPhoton/Tokyo-Tomita.txt")
        plt.plot([dat[1,0],dat[1,0]],[dat[1,1],1e0],'-',color=col,lw=3,zorder=0.2)
        if text_on:
            plt.text(2.3e-4,2.5e-10,r'{\bf Tokyo-3}',fontsize=fs,color=col,rotation=-90,rotation_mode='anchor',ha='center',va='center')
            plt.text(0.45e-3,3e-8,r'{\bf Tokyo-2}',fontsize=fs-2,color='k',rotation=90,rotation_mode='anchor',ha='center',va='center')
            plt.text(0.2e-1,4e-12,r'{\bf Tokyo-1}',fontsize=fs+4,color=col,rotation=0,rotation_mode='anchor',ha='center',va='center')
            plt.plot([2.05e-1,4e0],[5e-12,8e-12],'-',lw=2.5,color=col)
        return

    def FAST(ax,col='tomato',fs=10,text_on=True,lw=1.5,edge_on=False,zorder=0.11):
        m1,y1 = loadtxt("limit_data/DarkPhoton/DM_combined.txt",unpack=True)
        dat = loadtxt("limit_data/DarkPhoton/FAST.txt")
        dat[:,1] = dat[:,1]*sqrt(2/3/0.6)
        y2 = interp(dat[:,0],m1,y1)
        dat[0,1] = y2[0]/1.1
        dat[-1,1] = y2[-1]/1.1
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=zorder)
        if edge_on:
            plt.plot(dat[:,0],dat[:,1],color='k',alpha=1,zorder=zorder,lw=lw)

        if text_on:
            plt.text(7e-6,4e-12,r'{\bf FAST}',fontsize=fs,color=col,rotation=-90,rotation_mode='anchor',ha='center',va='center')
        return

    def Jupiter(ax,col='Green',fs=15,text_on=True):
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/DarkPhoton/Jupiter.txt")
        plt.plot(dat[:,0],dat[:,1],color='k',alpha=1,zorder=2,lw=2)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=2)
        if text_on:
            plt.text(0.1e-14*(1-0.02),4.5e-1*(1+0.07),r'{\bf Jupiter}',fontsize=fs,color='k',rotation=0,rotation_mode='anchor',ha='center',va='center')
            plt.text(0.1e-14,4.5e-1,r'{\bf Jupiter}',fontsize=fs,color='w',rotation=0,rotation_mode='anchor',ha='center',va='center')
        return

    def Earth(ax,col='DarkGreen',fs=17,text_on=True):
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/DarkPhoton/Earth.txt")
        plt.plot(dat[:,0],dat[:,1],color='k',alpha=1,zorder=1.9,lw=2)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=1.9)
        if text_on:
            plt.text(0.4e-13*(1-0.01),2e-1*(1+0.05),r'{\bf Earth}',fontsize=fs,color='k',rotation=0,rotation_mode='anchor',ha='center',va='center')
            plt.text(0.4e-13,2e-1,r'{\bf Earth}',fontsize=fs,color='w',rotation=0,rotation_mode='anchor',ha='center',va='center')
        return


    def Crab(ax,col=[0.1,0.4,0.1],fs=17,text_on=True):
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/DarkPhoton/Crab.txt")
        plt.plot(dat[:,0],dat[:,1],color='k',alpha=1,zorder=1.09999,lw=2)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=1.09999)

    #     dat = loadtxt("limit_data/DarkPhoton/Crab_2.txt")
    #     plt.plot(dat[:,0],dat[:,1],color='k',alpha=1,zorder=1.9,lw=2)
    #     plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=1.9)
        if text_on:
            plt.text(0.5e-6*(1-0.02),3e-1*(1+0.07),r'{\bf Crab}',fontsize=fs,color='k',rotation=0,rotation_mode='anchor',ha='center',va='center')
            plt.text(0.5e-6,3e-1,r'{\bf Crab}',fontsize=fs,color='w',rotation=0,rotation_mode='anchor',ha='center',va='center')

            plt.text(0.8e-6*(1-0.02),0.9e-1*(1+0.07),r'{\bf nebula}',fontsize=fs,color='k',rotation=0,rotation_mode='anchor',ha='center',va='center')
            plt.text(0.8e-6,0.9e-1,r'{\bf nebula}',fontsize=fs,color='w',rotation=0,rotation_mode='anchor',ha='center',va='center')

        return


    def SHUKET(ax,col='maroon',fs=13,text_on=True,edge_on=False,lw=0.8):
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/DarkPhoton/SHUKET.txt")
        dat[:,1] = dat[:,1]*sqrt(0.3/0.45)*sqrt(1/3/0.038)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=0.2)
        if edge_on:
            plt.plot(dat[:,0],dat[:,1],'k-',lw=lw,zorder=0.2)
        if text_on:
            plt.text(3.5e-5,0.13e-12,r'{\bf SHUKET}',fontsize=fs,color=col,rotation=-90,rotation_mode='anchor',ha='center',va='center')
        return

    def DarkEfield(ax,col='darkred',fs=17,text_on=True,edge_on=False,lw=0.8):
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/DarkPhoton/DarkEfield.txt")
        dat[:,1] = dat[:,1]*sqrt(1.64/5) # convert from 5 sigma CL to 95%
        dat[:,1] = dat[:,1]*sqrt(0.3/0.45)*sqrt(1/3/0.129)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=0.2)
        if edge_on:
            plt.plot(dat[:,0],dat[:,1],'k-',lw=lw,zorder=0.2)
        if text_on:
            plt.text(0.8e-7/1.2,0.2e-12,r'{\bf Dark}',fontsize=fs,color=col,rotation=90,rotation_mode='anchor',ha='center',va='center')
            plt.text(2e-7/1.2,0.2e-12,r'{\bf E-field}',fontsize=fs,color=col,rotation=90,rotation_mode='anchor',ha='center',va='center')
        return

    def ORPHEUS(ax,col='darkred',fs=10,text_on=True,edge_on=False,lw=0.8):
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/DarkPhoton/ORPHEUS.txt")
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor='k',facecolor=col,zorder=0.1,lw=0)
        if edge_on:
            plt.plot(dat[:,0],dat[:,1],'k-',lw=lw,zorder=0.2)
        if text_on:
            plt.text(6.5e-5,1e-13,r'{\bf ORPHEUS}',color=col,rotation=-90,fontsize=fs)
        return

    def WISPDMX(ax,col='crimson',fs=12,text_on=True,edge_on=False,lw=0.8):
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/DarkPhoton/WISPDMX.txt")
        dat[:,1] = dat[:,1]*sqrt(0.3/0.45)*sqrt(1/3/0.23)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=0.201)
        if edge_on:
            plt.plot(dat[:,0],dat[:,1],color='k',alpha=1,zorder=0.202,lw=lw)

        if text_on:
            plt.text(9e-7,4.1e-12/1.2,r'{\bf WISP}',fontsize=fs,color='w',rotation=0,rotation_mode='anchor',ha='center',va='center')
            plt.text(9e-7,1.8e-12/1.2,r'{\bf DMX}',fontsize=fs,color='w',rotation=0,rotation_mode='anchor',ha='center',va='center')

        return

    def DOSUE(ax,col='red',fs=9,text_on=True,edge_on=False,lw=0.8):
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/DarkPhoton/DOSUE-RR.txt")
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=0.201)
        if edge_on:
            plt.plot(dat[:,0],dat[:,1],color='k',alpha=1,zorder=0.202,lw=lw)

        if text_on:
            plt.text(90e-6,0.26e-10,r'{\bf DOSUE-RR}',fontsize=fs,color=col,rotation=-90,rotation_mode='anchor',ha='center',va='center')
        return


    def SQuAD(ax,col=[0.7,0,0],fs=12,text_on=True,lw=0.5,point_on=False,ms=10):
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/DarkPhoton/SQuAD.txt")
        dat[:,1] = dat[:,1]*sqrt(0.4/0.45)*sqrt(1/3/0.019)
        plt.plot([dat[0,0],dat[0,0]],[y2,dat[0,1]],lw=lw,color=col,alpha=1,zorder=0.2)
        if point_on:
            plt.plot(dat[0,0],dat[0,1],'o',mfc=col,mec='k',mew=lw+1,zorder=0.2,markersize=ms)
        if text_on:
            plt.text(36e-6,0.25e-14,r'{\bf SQuAD}',fontsize=fs,color=col,rotation=-90,rotation_mode='anchor',ha='center',va='center')
        return


    def DMPathfinder(ax,col='pink',fs=13,text_on=True):
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/DarkPhoton/DM-Pathfinder.txt")
        dat[:,1] = dat[:,1]*sqrt(1/0.075)
        plt.plot([dat[0,0],dat[0,0]],[y2,dat[0,1]],lw=2,color=col,alpha=1,zorder=0.6)
        if text_on:
            plt.text(2.1e-9,0.5e-8/1.9,r'{\bf DM}',fontsize=fs,color=col,rotation=0,rotation_mode='anchor',ha='center',va='center')
            plt.text(2.1e-9,0.2e-8/1.9,r'{\bf Pathfinder}',fontsize=fs,color=col,rotation=0,rotation_mode='anchor',ha='center',va='center')

        return

    def DarkMatter(ax,Witte_col='royalblue',Caputo_col='dodgerblue',Arias_col='navy',fs=20,projection=True,text_on=True):
        y2 = ax.get_ylim()[1]
        zo = 0.3
        pek=[pe.Stroke(linewidth=7, foreground='k'), pe.Normal()]

        # Combined limits
        dat = loadtxt("limit_data/DarkPhoton/DM_combined.txt")
        plt.plot(dat[:,0],dat[:,1],'-',color='w',alpha=1,zorder=zo+0.1,lw=2.5,path_effects=pek)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor='lightgray',zorder=zo,alpha=1.0)
        plt.plot([1e-16,dat[0,0]],[dat[0,1],dat[0,1]],'--',color='w',alpha=1,zorder=zo+0.1,lw=2.5,path_effects=pek)
        plt.fill_between([1e-16,dat[0,0]],[dat[0,1],dat[0,1]],y2=y2,edgecolor=None,facecolor='lightgray',zorder=zo+0.1,alpha=1.0)
        plt.plot(dat[40:,0],dat[40:,1],'--',color='w',alpha=1,lw=2.5,zorder=1000,solid_capstyle='round')

        # Individual limits
        dat2 = loadtxt("limit_data/DarkPhoton/Cosmology_Witte_inhomogeneous.txt")
        dat4 = loadtxt("limit_data/DarkPhoton/Cosmology_Caputo_HeII.txt",delimiter=',')
        dat5 = loadtxt("limit_data/DarkPhoton/Cosmology_Arias.txt")

        plt.fill_between(dat2[:,0],dat2[:,1],y2=y2,edgecolor='k',facecolor=Witte_col,zorder=0.305,alpha=0.8)
        plt.fill_between(dat4[:,0],dat4[:,1],y2=y2,edgecolor='k',facecolor=Caputo_col,zorder=0.305,alpha=0.8)
        plt.fill_between(dat5[:,0],dat5[:,1],y2=y2,edgecolor='k',facecolor=Arias_col,zorder=0.306,alpha=1)

        if text_on:
            plt.gcf().text(0.295,0.42-0.04,r'{\bf DPDM} HeII',fontsize=15,color='w',ha='center')
            plt.gcf().text(0.295,0.4-0.04,r'Reionisation',fontsize=15,color='w',ha='center')
            plt.gcf().text(0.295,0.38-0.04,r'(Caputo et al.)',fontsize=13,color='w',ha='center')

            plt.gcf().text(0.365,0.37,r'{\bf DPDM}',fontsize=17,color='w',ha='center')
            plt.gcf().text(0.365,0.35,r'(Witte et al.)',fontsize=13,color='w',ha='center')

            plt.gcf().text(0.49,0.48,r'{\bf DPDM}',fontsize=18,color='w',ha='center')
            plt.gcf().text(0.49,0.46,r'(Arias et al.)',fontsize=16,color='w',ha='center')

        return

    def COBEFIRAS(ax,col=[0.1,0.2,0.5],text_on=True):
        y2 = ax.get_ylim()[1]
        dat3 = loadtxt("limit_data/DarkPhoton/COBEFIRAS.txt",delimiter=',')
        plt.fill_between(dat3[:,0],dat3[:,1],y2=y2,edgecolor='k',facecolor=col,zorder=0.5,alpha=1)
        if text_on:
            plt.gcf().text(0.29,0.70,r'{\bf COBE/FIRAS}',fontsize=22,color='w',ha='center')
            plt.gcf().text(0.29,0.67,r'$\gamma \rightarrow X$',fontsize=22,color='w',ha='center')
        return


    def LSW(ax,text_on=True):
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/DarkPhoton/SPring-8.txt")
        plt.plot(dat[:,0],dat[:,1],color='k',alpha=1,zorder=1.1001,lw=2)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=[0.45, 0.05, 0.1],zorder=1.1001)

        dat = loadtxt("limit_data/DarkPhoton/ALPS.txt")
        plt.plot(dat[:,0],dat[:,1],color='k',alpha=1,zorder=1.091,lw=2)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=[0.55, 0.0, 0.16],zorder=1.091)

        dat = loadtxt("limit_data/DarkPhoton/LSW_UWA.txt")
        plt.plot(dat[:,0],dat[:,1],color='k',alpha=1,zorder=1.09,lw=2)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=[0.6, 0.0, 0.2],zorder=1.09)

        dat = loadtxt("limit_data/DarkPhoton/LSW_ADMX.txt")
        plt.plot(dat[:,0],dat[:,1],color='k',alpha=1,zorder=1.089,lw=2)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=[0.65, 0.1, 0.24],zorder=1.089)

    #     dat = loadtxt("limit_data/DarkPhoton/LSW_CERN.txt")
    #     plt.plot(dat[:,0],dat[:,1],color='k',alpha=1,zorder=1.089,lw=2)
    #     plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=[0.65, 0.15, 0.2],zorder=1.089)

        dat = loadtxt("limit_data/DarkPhoton/CROWS.txt")
        plt.plot(dat[:,0],dat[:,1],color='k',alpha=1,zorder=1.08,lw=2)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=[0.7, 0.2, 0.2],zorder=1.08)

        if text_on:
            plt.text(0.4e-6,0.15e-3,r'{\bf LSW-ADMX}',fontsize=17,color='w',rotation=-58,rotation_mode='anchor',ha='center',va='center')
            plt.text(1e-5,5e-5,r'{\bf LSW-UWA}',fontsize=14,color='w',rotation=-56,rotation_mode='anchor',ha='center',va='center')

            plt.text(0.55e0*(1-0.02),0.9e-4*(1+0.08),r'{\bf LSW-SPring-8}',fontsize=13,color='k',rotation=0,rotation_mode='anchor',ha='center',va='center')
            plt.text(0.55e0,0.9e-4,r'{\bf LSW-SPring-8}',fontsize=13,color='w',rotation=0,rotation_mode='anchor',ha='center',va='center')


            plt.text(1.2e-4*(1-0.02),0.9e-5*(1+0.08),r'{\bf ALPS}',fontsize=25,color='k',rotation=-56,rotation_mode='anchor',ha='center',va='center')
            plt.text(1.2e-4,0.9e-5,r'{\bf ALPS}',fontsize=25,color='w',rotation=-56,rotation_mode='anchor',ha='center',va='center')

            plt.text(0.75e-7*(1-0.01),9.9e-5*(1+0.05),r'{\bf CROWS}',fontsize=24,color='k',rotation=-56,rotation_mode='anchor',ha='center',va='center')
            plt.text(0.75e-7,9.9e-5,r'{\bf CROWS}',fontsize=24,color='w',rotation=-56,rotation_mode='anchor',ha='center',va='center')
        return

    def Coulomb(ax,text_on=True):
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/DarkPhoton/Cavendish.txt")
        plt.plot(dat[:,0],dat[:,1],color='k',alpha=1,zorder=1.07,lw=2)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=[0.7,0,0],zorder=1.07)

        dat = loadtxt("limit_data/DarkPhoton/PlimptonLawton.txt")
        plt.plot(dat[:,0],dat[:,1],color='k',alpha=1,zorder=1.071,lw=2)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor='crimson',zorder=1.071)

        dat = loadtxt("limit_data/DarkPhoton/Spectroscopy.txt")
        plt.plot(dat[:,0],dat[:,1],color='k',alpha=1,zorder=1.11,lw=2)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=[0.4, 0.0, 0.13],zorder=1.11)

        dat = loadtxt("limit_data/DarkPhoton/AFM.txt")
        plt.plot(dat[:,0],dat[:,1],color='k',alpha=1,zorder=1.5,lw=2)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=[0.4, 0.2, 0.2],zorder=1.5)
        if text_on:
            plt.text(2.5e-10*(1-0.02),0.35e-1*(1+0.08),r'{\bf Plimpton-Lawton}',fontsize=15,color='k',rotation=-38,rotation_mode='anchor',ha='center',va='center')
            plt.text(2.5e-10,0.35e-1,r'{\bf Plimpton-Lawton}',fontsize=15,color='w',rotation=-38,rotation_mode='anchor',ha='center',va='center')

            plt.text(3e1*(1-0.02),3e-1*(1+0.08),r'{\bf AFM}',fontsize=20,color='k',rotation=0,rotation_mode='anchor',ha='center',va='center')
            plt.text(3e1,3e-1,r'{\bf AFM}',fontsize=20,color='w',rotation=0,rotation_mode='anchor',ha='center',va='center')

            plt.text(0.5e-8*(1-0.02),4e-6*(1+0.08),r'{\bf Cavendish-Coulomb}',fontsize=23,color='k',rotation=-38,rotation_mode='anchor',ha='center',va='center')
            plt.text(0.5e-8,4e-6,r'{\bf Cavendish-Coulomb}',fontsize=23,color='w',rotation=-38,rotation_mode='anchor',ha='center',va='center')

            plt.text(0.2e2*(1-0.01),1e-3*(1+0.08),r'{\bf Spectroscopy}',fontsize=23,color='k',rotation=-34,rotation_mode='anchor',ha='center',va='center')
            plt.text(0.2e2,1e-3,r'{\bf Spectroscopy}',fontsize=23,color='w',rotation=-34,rotation_mode='anchor',ha='center',va='center')

        return

    def NeutronStarCooling(ax,col='#004d00',fs=18,text_on=True):
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/DarkPhoton/NeutronStarCooling.txt")
        plt.plot(dat[:,0],dat[:,1],color='k',alpha=1,zorder=1.1001,lw=2)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=1.1001)

        if text_on:
            plt.text(0.9e4*(1-0.03),0.4e-6*(1+0.05),r'{\bf Neutron stars}',fontsize=fs,color='k',rotation=-43,rotation_mode='anchor',ha='center',va='center')
            plt.text(0.9e4,0.4e-6,r'{\bf Neutron stars}',fontsize=fs,color='w',rotation=-43,rotation_mode='anchor',ha='center',va='center')
        return

    def CAST(ax,col='maroon',fs=27,text_on=True):
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/DarkPhoton/CAST.txt")
        plt.plot(dat[:,0],dat[:,1],color='k',alpha=1,zorder=1.1,lw=2)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=1.1)
        if text_on:
            plt.text(4e-3*(1-0.01),0.8e-6*(1+0.08),r'{\bf CAST}',fontsize=fs,color='k',rotation=-59,rotation_mode='anchor',ha='center',va='center')
            plt.text(4e-3,0.8e-6,r'{\bf CAST}',fontsize=fs,color='w',rotation=-59,rotation_mode='anchor',ha='center',va='center')
        return

    def SHIPS(ax,col='indianred',fs=20,text_on=True):
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/DarkPhoton/SHIPS.txt")
        dat[:,1] = dat[:,1]/dat[:,0]
        plt.plot(dat[:,0],dat[:,1],color='k',alpha=1,zorder=1.09,lw=2)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=1.09)
        if text_on:
            plt.text(0.6e-1*(1-0.05),0.08e-8*(1+0.1),r'{\bf SHIPS}',fontsize=fs,color='k',rotation=-32,rotation_mode='anchor',ha='center',va='center')
            plt.text(0.6e-1,0.08e-8,r'{\bf SHIPS}',fontsize=fs,color='w',rotation=-32,rotation_mode='anchor',ha='center',va='center')
        return

    def TEXONO(ax,col=[0.5, 0.0, 0.13],fs=15,text_on=True):
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/DarkPhoton/TEXONO.txt")
        plt.plot(dat[:,0],dat[:,1],color='k',alpha=1,zorder=1.101,lw=2)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=1.101)
        if text_on:
            plt.text(0.25e2*(1-0.01),0.1e-4*(1+0.08),r'{\bf TEXONO}',fontsize=fs,color='k',rotation=0,rotation_mode='anchor',ha='center',va='center')
            plt.text(0.25e2,0.1e-4,r'{\bf TEXONO}',fontsize=fs,color='w',rotation=0,rotation_mode='anchor',ha='center',va='center')
        return

    def IGM(ax,col='seagreen',fs=18,text_on=True):
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/DarkPhoton/IGM.txt")
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=0.49)
        plt.plot(dat[:,0],dat[:,1],color='k',alpha=0.6,zorder=0.49,lw=2)

        if text_on:
            plt.text(4e-12*(1-0.05),0.03e-7*(1+0.07),r'{\bf IGM}',fontsize=fs,color='k',rotation=-39,rotation_mode='anchor',ha='center',va='center')
            plt.text(4e-12,0.03e-7,r'{\bf IGM}',fontsize=fs,color='w',rotation=-39,rotation_mode='anchor',ha='center',va='center')
            plt.gcf().text(0.233*(1-0.005),0.565*(1+0.003),r'{\bf DPDM heating}',color='k',fontsize=23)
            plt.gcf().text(0.233,0.565,r'{\bf DPDM heating}',color='w',fontsize=23)

        return

    def LeoT(ax,col='mediumseagreen',fs=18,text_on=True):
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/DarkPhoton/LeoT.txt")
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=0.3061)
        plt.plot(dat[:,0],dat[:,1],color='k',alpha=0.68,zorder=0.3062,lw=2)

        if text_on:
            plt.text(7e-13*(1-0.05),0.2e-9*(1+0.07),r'{\bf Leo T}',fontsize=fs,color='k',rotation=-39,rotation_mode='anchor',ha='center',va='center')
            plt.text(7e-13,0.2e-9,r'{\bf Leo T}',fontsize=fs,color='w',rotation=-39,rotation_mode='anchor',ha='center',va='center')
        return

    def GasClouds(ax,col='#00cc66',fs=18,text_on=True):
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/DarkPhoton/GasClouds.txt")
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=0.306)
        plt.plot(dat[:,0],dat[:,1],color='k',alpha=0.6,zorder=0.307,lw=2)

        if text_on:
            plt.text(0.86e-13*(1-0.07),1e-10*(1+0.07),r'{\bf Gas clouds}',fontsize=fs,color='k',rotation=-38,rotation_mode='anchor',ha='center',va='center')
            plt.text(0.86e-13,1e-10,r'{\bf Gas clouds}',fontsize=fs,color='w',rotation=-38,rotation_mode='anchor',ha='center',va='center')
        return

    def SuperMAG(ax,col='#b5403e',fs=18,text_on=True):
        y2 = ax.get_ylim()[1]
        dat = loadtxt("limit_data/DarkPhoton/SuperMAG.txt")
        plt.plot(dat[:,0],dat[:,1],color='k',alpha=1,zorder=1,lw=2)
        plt.fill_between(dat[:,0],dat[:,1],y2=y2,edgecolor=None,facecolor=col,zorder=1)

        if text_on:
            plt.text(1.5e-17*(1-0.05),1e-1*(1+0.05)/1.4,r'{\bf Super}',fontsize=fs,color='k',rotation=0,rotation_mode='anchor',ha='center',va='center')
            plt.text(1.5e-17,1e-1/1.4,r'{\bf Super}',fontsize=fs,color='w',rotation=0,rotation_mode='anchor',ha='center',va='center')
            plt.text(1.5e-17*(1-0.05),0.2e-1*(1+0.05)/1.4,r'{\bf MAG}',fontsize=fs,color='k',rotation=0,rotation_mode='anchor',ha='center',va='center')
            plt.text(1.5e-17,0.2e-1/1.4,r'{\bf MAG}',fontsize=fs,color='w',rotation=0,rotation_mode='anchor',ha='center',va='center')

        return




#==============================================================================#
def MySaveFig(fig,pltname,pngsave=True):
    fig.savefig(pltdir+pltname+'.pdf',bbox_inches='tight')
    if pngsave:
        fig.set_facecolor('w') # <- not sure what matplotlib fucked up in the new version but it seems impossible to set png files to be not transparent now
        fig.savefig(pltdir_png+pltname+'.png',bbox_inches='tight',transparent=False)

def cbar(mappable,extend='neither',minorticklength=8,majorticklength=10,\
            minortickwidth=2,majortickwidth=2.5,pad=0.2,side="right",orientation="vertical"):
    ax = mappable.axes
    fig = ax.figure
    divider = make_axes_locatable(ax)
    cax = divider.append_axes(side, size="5%", pad=pad)
    cbar = fig.colorbar(mappable, cax=cax,extend=extend,orientation=orientation)
    cbar.ax.tick_params(which='minor',length=minorticklength,width=minortickwidth)
    cbar.ax.tick_params(which='major',length=majorticklength,width=majortickwidth)
    cbar.solids.set_edgecolor("face")

    return cbar

def MySquarePlot(xlab='',ylab='',\
                 lw=2.5,lfs=45,tfs=25,size_x=13,size_y=12,Grid=False):
    plt.rcParams['axes.linewidth'] = lw
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif',size=tfs)
    plt.rcParams.update({"text.usetex": True,"font.family": "serif","font.serif": ["Palatino"],})
    fig = plt.figure(figsize=(size_x,size_y))
    ax = fig.add_subplot(111)

    ax.set_xlabel(xlab,fontsize=lfs)
    ax.set_ylabel(ylab,fontsize=lfs)

    ax.tick_params(which='major',direction='in',width=2,length=13,right=True,top=True,pad=7)
    ax.tick_params(which='minor',direction='in',width=1,length=10,right=True,top=True)
    if Grid:
        ax.grid()
    return fig,ax

def MyDoublePlot(xlab1='',ylab1='',xlab2='',ylab2='',\
                 wspace=0.25,lw=2.5,lfs=45,tfs=25,size_x=20,size_y=11,Grid=False):
    plt.rcParams['axes.linewidth'] = lw
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif',size=tfs)
    plt.rcParams.update({"text.usetex": True,"font.family": "serif","font.serif": ["Palatino"],})
    fig, axarr = plt.subplots(1, 2,figsize=(size_x,size_y))
    gs = gridspec.GridSpec(1, 2)
    gs.update(wspace=wspace)
    ax1 = plt.subplot(gs[0])
    ax2 = plt.subplot(gs[1])
    ax1.tick_params(which='major',direction='in',width=2,length=13,right=True,top=True,pad=7)
    ax1.tick_params(which='minor',direction='in',width=1,length=10,right=True,top=True)
    ax2.tick_params(which='major',direction='in',width=2,length=13,right=True,top=True,pad=7)
    ax2.tick_params(which='minor',direction='in',width=1,length=10,right=True,top=True)

    ax1.set_xlabel(xlab1,fontsize=lfs)
    ax1.set_ylabel(ylab1,fontsize=lfs)

    ax2.set_xlabel(xlab2,fontsize=lfs)
    ax2.set_ylabel(ylab2,fontsize=lfs)

    if Grid:
        ax1.grid()
        ax2.grid()
    return fig,ax1,ax2


def MyDoublePlot_Vertical(xlab1='',ylab1='',xlab2='',ylab2='',\
                     hspace=0.05,lw=2.5,lfs=45,tfs=30,size_x=15,size_y=14,Grid=False,height_ratios=[2.5,1]):
    plt.rcParams['axes.linewidth'] = lw
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif',size=tfs)
    plt.rcParams.update({"text.usetex": True,"font.family": "serif","font.serif": ["Palatino"],})


    fig, axarr = plt.subplots(2,1,figsize=(size_x,size_y))
    gs = gridspec.GridSpec(2, 1,height_ratios=height_ratios)
    gs.update(hspace=hspace)
    ax1 = plt.subplot(gs[0])
    ax2 = plt.subplot(gs[1])

    ax1.tick_params(which='major',direction='in',width=2,length=13,right=False,top=True,pad=10)
    ax1.tick_params(which='minor',direction='in',width=1,length=10,right=False,top=True)

    ax2.tick_params(which='major',direction='in',width=2,length=13,right=False,top=True,pad=10)
    ax2.tick_params(which='minor',direction='in',width=1,length=10,right=False,top=True)

    ax1.set_xlabel(xlab1,fontsize=lfs)
    ax1.set_ylabel(ylab1,fontsize=lfs)

    ax2.set_xlabel(xlab2,fontsize=lfs)
    ax2.set_ylabel(ylab2,fontsize=lfs)


    if Grid:
        ax1.grid()
        ax2.grid()
    return fig,ax1,ax2



def MyTriplePlot(xlab1='',ylab1='',xlab2='',ylab2='',xlab3='',ylab3='',\
                 wspace=0.25,lw=2.5,lfs=45,tfs=25,size_x=20,size_y=7,Grid=False):
    plt.rcParams['axes.linewidth'] = lw
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif',size=tfs)
    plt.rcParams.update({"text.usetex": True,"font.family": "serif","font.serif": ["Palatino"],})
    fig, axarr = plt.subplots(1, 3,figsize=(size_x,size_y))
    gs = gridspec.GridSpec(1, 3)
    gs.update(wspace=wspace)
    ax1 = plt.subplot(gs[0])
    ax2 = plt.subplot(gs[1])
    ax3 = plt.subplot(gs[2])

    ax1.tick_params(which='major',direction='in',width=2,length=13,right=True,top=True,pad=7)
    ax1.tick_params(which='minor',direction='in',width=1,length=10,right=True,top=True)

    ax2.tick_params(which='major',direction='in',width=2,length=13,right=True,top=True,pad=7)
    ax2.tick_params(which='minor',direction='in',width=1,length=10,right=True,top=True)

    ax3.tick_params(which='major',direction='in',width=2,length=13,right=True,top=True,pad=7)
    ax3.tick_params(which='minor',direction='in',width=1,length=10,right=True,top=True)

    ax1.set_xlabel(xlab1,fontsize=lfs)
    ax1.set_ylabel(ylab1,fontsize=lfs)

    ax2.set_xlabel(xlab2,fontsize=lfs)
    ax2.set_ylabel(ylab2,fontsize=lfs)

    ax3.set_xlabel(xlab3,fontsize=lfs)
    ax3.set_ylabel(ylab3,fontsize=lfs)

    if Grid:
        ax1.grid()
        ax2.grid()
        ax3.grid()
    return fig,ax1,ax2,ax3
#==============================================================================#

def line_background(lw,col):
    return [pe.Stroke(linewidth=lw, foreground=col), pe.Normal()]


#==============================================================================#
def reverse_colourmap(cmap, name = 'my_cmap_r'):
    reverse = []
    k = []

    for key in cmap._segmentdata:
        k.append(key)
        channel = cmap._segmentdata[key]
        data = []

        for t in channel:
            data.append((1-t[0],t[2],t[1]))
        reverse.append(sorted(data))

    LinearL = dict(zip(k,reverse))
    my_cmap_r = mpl.colors.LinearSegmentedColormap(name, LinearL)
    return my_cmap_r
#==============================================================================#




from matplotlib import patches
from matplotlib import text as mtext
import numpy as np
import math

class CurvedText(mtext.Text):
    """
    A text object that follows an arbitrary curve.
    """
    def __init__(self, x, y, text, axes, **kwargs):
        super(CurvedText, self).__init__(x[0],y[0],' ', **kwargs)

        axes.add_artist(self)

        ##saving the curve:
        self.__x = x
        self.__y = y
        self.__zorder = self.get_zorder()

        ##creating the text objects
        self.__Characters = []
        for c in text:
            if c == ' ':
                ##make this an invisible 'a':
                t = mtext.Text(0,0,'a')
                t.set_alpha(0.0)
            else:
                t = mtext.Text(0,0,c, **kwargs)

            #resetting unnecessary arguments
            t.set_ha('center')
            t.set_rotation(0)
            t.set_zorder(self.__zorder +1)

            self.__Characters.append((c,t))
            axes.add_artist(t)


    ##overloading some member functions, to assure correct functionality
    ##on update
    def set_zorder(self, zorder):
        super(CurvedText, self).set_zorder(zorder)
        self.__zorder = self.get_zorder()
        for c,t in self.__Characters:
            t.set_zorder(self.__zorder+1)

    def draw(self, renderer, *args, **kwargs):
        """
        Overload of the Text.draw() function. Do not do
        do any drawing, but update the positions and rotation
        angles of self.__Characters.
        """
        self.update_positions(renderer)

    def update_positions(self,renderer):
        """
        Update positions and rotations of the individual text elements.
        """

        #preparations

        ##determining the aspect ratio:
        ##from https://stackoverflow.com/a/42014041/2454357

        ##data limits
        xlim = self.axes.get_xlim()
        ylim = self.axes.get_ylim()
        ## Axis size on figure
        figW, figH = self.axes.get_figure().get_size_inches()
        ## Ratio of display units
        _, _, w, h = self.axes.get_position().bounds
        ##final aspect ratio
        aspect = ((figW * w)/(figH * h))*(ylim[1]-ylim[0])/(xlim[1]-xlim[0])

        #points of the curve in figure coordinates:
        x_fig,y_fig = (
            np.array(l) for l in zip(*self.axes.transData.transform([
            (i,j) for i,j in zip(self.__x,self.__y)
            ]))
        )

        #point distances in figure coordinates
        x_fig_dist = (x_fig[1:]-x_fig[:-1])
        y_fig_dist = (y_fig[1:]-y_fig[:-1])
        r_fig_dist = np.sqrt(x_fig_dist**2+y_fig_dist**2)

        #arc length in figure coordinates
        l_fig = np.insert(np.cumsum(r_fig_dist),0,0)

        #angles in figure coordinates
        rads = np.arctan2((y_fig[1:] - y_fig[:-1]),(x_fig[1:] - x_fig[:-1]))
        degs = np.rad2deg(rads)


        rel_pos = 10
        for c,t in self.__Characters:
            #finding the width of c:
            t.set_rotation(0)
            t.set_va('center')
            bbox1  = t.get_window_extent(renderer=renderer)
            w = bbox1.width
            h = bbox1.height

            #ignore all letters that don't fit:
            if rel_pos+w/2 > l_fig[-1]:
                t.set_alpha(0.0)
                rel_pos += w
                continue

            elif c != ' ':
                t.set_alpha(1.0)

            #finding the two data points between which the horizontal
            #center point of the character will be situated
            #left and right indices:
            il = np.where(rel_pos+w/2 >= l_fig)[0][-1]
            ir = np.where(rel_pos+w/2 <= l_fig)[0][0]

            #if we exactly hit a data point:
            if ir == il:
                ir += 1

            #how much of the letter width was needed to find il:
            used = l_fig[il]-rel_pos
            rel_pos = l_fig[il]

            #relative distance between il and ir where the center
            #of the character will be
            fraction = (w/2-used)/r_fig_dist[il]

            ##setting the character position in data coordinates:
            ##interpolate between the two points:
            x = self.__x[il]+fraction*(self.__x[ir]-self.__x[il])
            y = self.__y[il]+fraction*(self.__y[ir]-self.__y[il])

            #getting the offset when setting correct vertical alignment
            #in data coordinates
            t.set_va(self.get_va())
            bbox2  = t.get_window_extent(renderer=renderer)

            bbox1d = self.axes.transData.inverted().transform(bbox1)
            bbox2d = self.axes.transData.inverted().transform(bbox2)
            dr = np.array(bbox2d[0]-bbox1d[0])

            #the rotation/stretch matrix
            rad = rads[il]
            rot_mat = np.array([
                [math.cos(rad), math.sin(rad)*aspect],
                [-math.sin(rad)/aspect, math.cos(rad)]
            ])

            ##computing the offset vector of the rotated character
            drp = np.dot(dr,rot_mat)

            #setting final position and rotation:
            t.set_position(np.array([x,y])+drp)
            t.set_rotation(degs[il])

            t.set_va('center')
            t.set_ha('center')

            #updating rel_pos to right edge of character
            rel_pos += w-used
