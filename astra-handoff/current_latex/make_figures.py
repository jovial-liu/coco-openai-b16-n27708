"""Deterministic publication figures; exact archived estimates, no fitting."""
from pathlib import Path
import csv
import hashlib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.lines import Line2D

ROOT = Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans', 'font.size':9,
    'svg.fonttype':'none', 'pdf.fonttype':42, 'mathtext.fontset':'dejavusans',
    'axes.linewidth':.5, 'savefig.facecolor':'white'})
INK='#303E4A'; MUTED='#64717B'; BLUE='#577B95'; ORANGE='#AA7556'

def export(fig, name):
    for ext in ('svg','pdf','png'):
        fig.savefig(ROOT/'figures'/f'{name}.{ext}', dpi=220)
    plt.close(fig)

def method():
    import runpy
    runpy.run_path(str(ROOT/'draw_figure1.py'))

def identification():
    path=ROOT/'data'/'round2_identification.csv'
    assert hashlib.sha256(path.read_bytes()).hexdigest() == 'ad81b2cf0531fda2bc408998af25bc72928bd0f96525a043174e6ad57eb63743'
    rows=list(csv.DictReader(path.open()))
    fig=plt.figure(figsize=(86/25.4,55/25.4))
    colors=[BLUE,ORANGE,'#59616B']; markers=['o','s','^']
    protocols=['Full foils','Cross-foil','Absent-only']
    handles=[Line2D([],[],marker=m,color=c,lw=0,markersize=4,markerfacecolor='white' if m=='^' else c)
             for m,c in zip(markers,colors)]
    fig.legend(handles,['Full','Cross-foil','Absent-only'],loc='upper center',
        bbox_to_anchor=(.5,1),ncol=3,frameon=False,fontsize=9,
        columnspacing=.8,handletextpad=.25,handlelength=.7,borderaxespad=.3)
    settings=['COCO B/16','COCO B/32','VOC B/16','VOC B/32']
    for i,setting in enumerate(settings):
        ax=fig.add_axes([.06+(i%2)*.49,.55-(i//2)*.37,.39,.24])
        ax.set_title(setting,loc='left',fontsize=9,pad=6,weight='bold',color=INK)
        for j,(protocol,c,m) in enumerate(zip(protocols,colors,markers)):
            r=next(r for r in rows if r['setting']==setting and r['protocol']==protocol)
            p,lo,hi=(float(r[k]) for k in ('delta','ci_low','ci_high'))
            assert lo < p < hi
            ax.errorbar(p,2-j,xerr=[[p-lo],[hi-p]],fmt=m,color=c,
                mfc='white' if m=='^' else c,ms=4,mew=.8,elinewidth=.85,capsize=2,capthick=.65)
        ax.set(xlim=(-.0007,.021),ylim=(-.5,2.5),yticks=[],xticks=[0,.01,.02])
        ax.set_xticklabels(['0','.010','.020'],fontsize=9,color=MUTED)
        ax.tick_params(axis='x',length=2,width=.5,pad=3,labelbottom=i>=2)
        ax.axvline(0,color='#8D98A4',lw=.65,zorder=0)
        for v in [.01,.02]: ax.axvline(v,color='#E5E8EC',lw=.5,zorder=0)
        for side in ['top','left','right']: ax.spines[side].set_visible(False)
        ax.spines['bottom'].set_color('#B8C2CC')
    fig.text(.5,.035,'Normalized aggregate gain ΔP',
        ha='center',fontsize=9,color=INK)
    export(fig,'figure2_identification_final')

if __name__=='__main__':
    method(); identification()
    import runpy
    runpy.run_path(str(ROOT/'draw_figure3.py'))
