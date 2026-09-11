"""Validate the authorized layout revision without relaxing data invariants."""
from pathlib import Path
import re, hashlib, io, sys
import xml.etree.ElementTree as ET
from PIL import Image, ImageChops
import fitz
root=Path(__file__).resolve().parent
base=(root/'baseline/main.tex').read_text()
current=(root/'main.tex').read_text()
assert r'\paragraph{Acknowledgment.}' not in current
assert r'\paragraph{Interpretation and scope.}' in current
for name in ['icassp2027_paperkit.sty']:
    assert (root/'baseline'/name).read_bytes()==(root/name).read_bytes(),name
authors=(root/'authors.tex').read_text()
author_line=next(l for l in authors.splitlines() if l.startswith(r'\name{'))
expected=['Kaixin Liu','Zhipeng Ye','Feng Jiang','Qiufeng Wang','Hao Li','Xihang Zhou']
assert [author_line.index(n) for n in expected]==sorted(author_line.index(n) for n in expected)
assert author_line.endswith(r'Xihang Zhou$^{4}$}')
assert 'xihang.zhou@mail.utoronto.ca' in authors
assert 'lihao@arizona.edu' in authors
refs=(root/'references.bib').read_text()
assert (root/'baseline/references.bib').read_text().strip() in refs
assert refs.count('@article{ye2026idea,')==1
assert '10.1016/j.patcog.2025.112224' in refs
assert r'\cite{ye2026idea}' in current
assert r'\section{Additional Results and Conclusion}' not in current
assert 'All-three semantic-family agreement' in current
assert 'Predeclared' not in current
assert '20 seed--direction deltas' in current
assert 'does not\nestablish equivalence or a no-loss guarantee' in current
def equations(s):
    return re.findall(r'\\begin\{(equation\*?|align\*?)\}([\s\S]*?)\\end\{\1\}',s)
assert equations(base)==equations(current),'Main equations changed'
def table_numbers(s,label):
    block=s[s.index(r'\label{'+label+'}'):].split(r'\end{table',1)[0]
    data=block.split(r'\midrule',1)[1].split(r'\bottomrule',1)[0]
    return re.findall(r'[+-]?(?:\d*\.\d+|\d+)',data)
for label in ['tab:main','tab:baselines','tab:foilcount','tab:diagnostics','tab:frontier','tab:repair_accounting']:
    assert table_numbers(base,label)==table_numbers(current,label),label
archived=(root.parent/'identification_controls_archived_table.tex').read_text()
assert table_numbers(base,'tab:ident')==table_numbers(archived,'tab:ident')
csv=root/'data/round2_identification.csv'
assert hashlib.sha256(csv.read_bytes()).hexdigest()=='ad81b2cf0531fda2bc408998af25bc72928bd0f96525a043174e6ad57eb63743'
name=sys.argv[1] if len(sys.argv)>1 else ('paper_final' if (root/'paper_final.pdf').exists() else 'main')
doc=fitz.open(root/(name+'.pdf'))
assert len(doc)==5
assert 'REFERENCES' in doc[4].get_text()
assert 'Conclusion.' in doc[3].get_text()
assert not re.search(r'Overfull|undefined|LaTeX Warning',(root/(name+'.log')).read_text())
for name in ['figure1_method_final','figure2_identification_final','figure3_qualitative_final']:
    svg=ET.parse(root/'figures'/f'{name}.svg')
    assert svg.findall('.//{http://www.w3.org/2000/svg}text')
    for element in svg.findall('.//{http://www.w3.org/2000/svg}text'):
        # Ordinary labels must be >=9 pt. Math superscripts/subscripts retain
        # conventional reduced sizes and are nested tspans, not plain labels.
        size=re.search(r'font-size:\s*([\d.]+)px',element.get('style',''))
        if size: assert float(size.group(1))>=9,(name,element.text)
    p=fitz.open(root/'figures'/f'{name}.pdf')[0]
    for b in p.get_text('dict')['blocks']:
        for l in b.get('lines',[]):
            for s in l['spans']:
                assert p.rect.contains(fitz.Rect(s['bbox'])),(name,s['text'])
    if name!='figure3_qualitative_final':assert not p.get_images()
q=fitz.open(root/'figures/figure3_qualitative_final.pdf')
assert set(q[0].get_text().split())=={'(a)','(b)','(c)','CCI','WF'}
original=Image.open(root/'figures/qualitative_cases_compact_labels.png').convert('RGB')
expected=[original.crop((125,83,1760,600)),original.crop((125,666,1760,1160))]
# Matplotlib stores image rows bottom-to-top and uses the PDF transform to orient them.
actual=[Image.open(io.BytesIO(q.extract_image(i[0])['image'])).convert('RGB').transpose(Image.Transpose.FLIP_TOP_BOTTOM) for i in q[0].get_images()]
assert len(actual)==2
for e in expected:
    assert any(a.size==e.size and ImageChops.difference(a,e).getbbox() is None for a in actual),'Photographic pixels changed'
print('PASS: 5 pages; six authors with Xihang Zhou last; IDEA cited with DOI; unified Results; original equations, prior bibliography entries and table estimates/CIs preserved; vector figure text verified; Figure 3 photographs unchanged; no overfull boxes or unresolved references.')
