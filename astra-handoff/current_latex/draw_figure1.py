"""Protocol illustration, not experimental data. Editable SVG and vector PDF."""
from pathlib import Path
import io, os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch, FancyArrowPatch, Arc, Circle
from matplotlib.textpath import TextPath
from matplotlib.font_manager import FontProperties
ROOT=Path(__file__).resolve().parent/'figures'
plt.rcParams.update({'font.family':'DejaVu Serif','svg.fonttype':'none','pdf.fonttype':42,'mathtext.fontset':'dejavuserif',
 'lines.solid_capstyle':'round','lines.dash_capstyle':'round','lines.solid_joinstyle':'round'})
W,H=178/25.4*72,150
fig=plt.figure(figsize=(W/72,140/72));ax=fig.add_axes([0,0,1,1],xlim=(0,W),ylim=(H,0));ax.axis('off')
INK='#28343D';MUT='#62717A';BLUE='#517C9A';ORANGE='#B77B57';TEAL='#558E88'
def text(x,y,s,size=9,c=INK,weight='normal',ha='left',**kw):
 return ax.text(x,y,s,fontsize=max(9,size),color=c,weight=weight,ha=ha,va='center',**kw)
def line(xs,ys,c='#C2CCD3',lw=.6,**kw):ax.plot(xs,ys,color=c,lw=lw,**kw)
def box(x,y,w,h,fill='white',edge='#C8D2DA',r=1,lw=.6):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',facecolor=fill,edgecolor=edge,linewidth=lw))
def arrow(x,y,xx,yy,c=MUT,lw=.7,rad=0):
 ax.add_patch(FancyArrowPatch((x,y),(xx,yy),arrowstyle='-|>',mutation_scale=6.5,linewidth=lw,color=c,shrinkA=1,shrinkB=1,connectionstyle=f'arc3,rad={rad}'))
def stage(x,label,title,w,c):
 text(x,9.5,label,weight='bold');text(x+18,9.5,title,weight='bold');line([x,x+w],[20,20],c,.65)
stage(3,'(a)','Frozen candidates',112,BLUE)
stage(128,'(b)','Selection-stage reranking',234,ORANGE)
stage(391,'(c)','Held-out audit',110,TEAL)
text(3,32,'Frozen CLIP + target',c=MUT)
text(128,32,'Target tolerance + worst-foil margin',c=MUT)
text(391,32,'3 held-out templates',c=MUT)

# The same eight synthetic region identities in the partition and mask gallery.
palette=['#BCD0DF','#DCE5ED','#A8C5C8','#DDC4AE','#C4D4C5','#E7DCCB','#CBC8DC','#D4DFD7']
ids=[[0,0,1,1,1,2],[0,0,1,1,2,2],[3,3,3,4,4,2],[3,3,4,4,4,5],[6,6,6,4,5,5],[6,6,7,7,7,5]]
for row in range(6):
 for col in range(6):
  ax.add_patch(Rectangle((5+col*8.5,48+row*8.5),8.5,8.5,facecolor=palette[ids[row][col]],edgecolor='white',linewidth=.4))
box(4.2,47.2,52.6,52.6,fill='none',edge='#A4B4BE',r=.8,lw=.5)
text(30,108,'Partition',c=MUT,ha='center')
FLOW_Y=77
arrow(60,FLOW_Y,69,FLOW_Y)
digit_font=FontProperties(family='DejaVu Serif',size=9)
for k in range(8):
 x=73+(k%2)*22;y=44.5+(k//2)*14
 box(x,y,18,13,fill='#F7F9FA',edge='#B8C5CE',r=.8,lw=.45)
 for row in range(6):
  for col in range(6):
   if ids[row][col]==k:
    ax.add_patch(Rectangle((x+1.4+col*1.15,y+3.05+row*1.15),1.15,1.15,facecolor=palette[k],edgecolor='none'))
 # Center the visible numeral outline, not its font's ascent/descent box.
 glyph=TextPath((0,0),str(k+1),prop=digit_font).get_extents()
 gx=x+13.3-(glyph.x0+glyph.x1)/2
 gy=y+6.5+(glyph.y0+glyph.y1)/2*(H/140)
 ax.text(gx,gy,str(k+1),fontproperties=digit_font,color=MUT,ha='left',va='baseline')
text(93,108,r'$K=8$',ha='center')
text(4,123,'Internal K/V masking')
text(4,134,'Prefix retained',c=MUT)
arrow(117,FLOW_Y,128,FLOW_Y)

# Reinstated target-drop / worst-foil-drop geometry, purely illustrative.
x0,x1,yt,yb=151,258,48,107;threshold=235
ax.add_patch(Rectangle((threshold,yt),254-threshold,yb-yt,facecolor='#F3E8DF',edgecolor='none'))
line([254,254],[yt,yb],'#B9CBD7',.45,ls=(0,(1.5,2.5)))
line([threshold,threshold],[yt,yb],ORANGE,.65,ls=(0,(2,2)))
arrow(x0,yb,x1+4,yb,c='#91A1AD',lw=.6)
arrow(x0,yb,x0,yt-4,c='#91A1AD',lw=.6)
text(202,119,r'Target drop $d^{\mathrm{sel}}(t)$',ha='center')
text(137,77,'Worst-foil drop',ha='center',rotation=90)
for x,y in [(161,96),(174,71),(183,89),(195,59),(211,84),(231,95)]:
 ax.plot(x,y,'o',ms=3.5,mfc='#C0CFD8',mec='white',mew=.45)
cci=(254,57);wf=(241,92)
ax.plot(*cci,'o',ms=5,mfc=BLUE,mec='white',mew=.6,zorder=5)
ax.plot(*wf,'D',ms=4.8,mfc=ORANGE,mec='white',mew=.6,zorder=5)
for x,y,c in [(*cci,BLUE),(*wf,ORANGE)]:
 line([x,x],[y+4,yb],c,.4,ls=(0,(1,3)),alpha=.55)
 line([x,x],[yb,yb+1.8],c,.55)
arrow(252,64,243,85,c=ORANGE,lw=.85,rad=-.22)
text(244.5,39.5,r'$\epsilon$',c=ORANGE,ha='center')
line([threshold,254],[46,46],ORANGE,.6)
line([threshold,threshold],[44.5,47.5],ORANGE,.6)
line([254,254],[44.5,47.5],ORANGE,.6)
ax.plot(277,51,'o',ms=4.5,color=BLUE)
text(285,51,'Original CCI',c=BLUE)
text(277,64,'Max. target drop')
ax.plot(277,81,'D',ms=4.5,color=ORANGE)
text(285,81,'WF rerank',c=ORANGE)
text(277,95,'Within ε of CCI')
text(277,106,'Feasible set · Eq. 5',c=MUT)
text(132,133.5,r'$\max\,[d_R^{\mathrm{sel}}(t)-\max_f d_R^{\mathrm{sel}}(f)]$',size=9.5)
text(272,133.5,'feasible set · Eq. 6',c=MUT)

# A small vector padlock reinforces the fixed-region boundary.
BOUNDARY_X=371
line([BOUNDARY_X,BOUNDARY_X],[40,142],'#9EB6B1',.65,ls=(0,(2.5,3)))
ax.add_patch(Arc((BOUNDARY_X,30.5),5,7,theta1=180,theta2=360,color=TEAL,lw=.65))
box(BOUNDARY_X-4,30.5,8,6,fill='#F1F7F5',edge=TEAL,r=.7,lw=.6)
ax.add_patch(Circle((BOUNDARY_X,33),.6,facecolor=TEAL,edgecolor='none'))
line([BOUNDARY_X,BOUNDARY_X],[33,34.5],TEAL,.5)
text(BOUNDARY_X,46,'Region',c=TEAL,ha='center',bbox=dict(facecolor='white',edgecolor='none',pad=1))
text(BOUNDARY_X,58,'fixed',c=TEAL,ha='center',bbox=dict(facecolor='white',edgecolor='none',pad=1))
arrow(356,FLOW_Y,397,FLOW_Y,c=TEAL,lw=.85)

# Three miniature ruled templates, all vector.
box(398,44,101,16,fill='#F1F7F5',edge='#AEC8C2',r=1.4,lw=.55)
for j in range(3):
 xx=401+j*5.3
 box(xx,48,4,8,fill='white',edge='#8AAEA5',r=.3,lw=.35)
 for yy in [50,52,54]:line([xx+.8,xx+3.1],[yy,yy],'#AAC3BB',.3)
text(459,52,'Fixed region × 3',c=TEAL,ha='center')

# Compact endpoint glyphs: bullseye, response curve, patch-grid localization.
line([398,398],[75,125],TEAL,.65)
for y,title,sub in [(77,'Specificity','target − worst foil'),(101,'Target response','held-out drop'),(125,'Locality','box overlap')]:
 ax.plot(398,y,'o',ms=2.1,color=TEAL)
 text(414,y-3,title)
 text(414,y+7,sub,c=MUT)
# Symbolic glyphs only: no measured values or new observations are encoded.
ax.add_patch(Circle((405.5,74),3.8,facecolor='#F3F7F5',edgecolor=TEAL,lw=.55))
ax.add_patch(Circle((405.5,74),1.75,facecolor='none',edgecolor=TEAL,lw=.5))
ax.add_patch(Circle((405.5,74),.6,facecolor=ORANGE,edgecolor='none'))
line([401.5,401.5,410],[95,103,103],'#8CADA5',.5)
ax.add_patch(FancyArrowPatch((402.8,96),(409,100.7),
 arrowstyle='-',connectionstyle='arc3,rad=.22',linewidth=.85,color=TEAL))
ax.add_patch(Circle((402.8,96),.7,facecolor=BLUE,edgecolor='none'))
ax.add_patch(Circle((409,100.7),.7,facecolor=ORANGE,edgecolor='none'))
box(401.5,119.5,9,9,fill='#F6F9F8',edge=TEAL,r=.5,lw=.5)
for offset in [3,6]:
 line([401.5+offset,401.5+offset],[119.5,128.5],'#CEDDD8',.35)
 line([401.5,410.5],[119.5+offset,119.5+offset],'#CEDDD8',.35)
box(404.5,122.5,6,3,fill='#D4E5DE',edge=ORANGE,r=0,lw=.6)
arrow(398,61,398,73,c=TEAL,lw=.65)
text(132,145,'Illustrative; not to scale.',c=MUT)

for ext in ['svg','pdf','png']:
 buffer=io.BytesIO();fig.savefig(buffer,format=ext,dpi=260,facecolor='white')
 target=ROOT/f'figure1_method_final.{ext}';tmp=target.with_suffix(target.suffix+'.tmp')
 with tmp.open('wb') as f:f.write(buffer.getvalue());f.flush();os.fsync(f.fileno())
 tmp.replace(target)
plt.close(fig)
