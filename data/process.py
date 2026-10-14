import json,sys,math
d=sys.argv[1]
C=json.load(open(d+'/countries.json'))[1]
meta={c['id']:c for c in C if c['region']['value']!='Aggregates'}
def load(f):
    out={}
    for r in json.load(open(d+'/'+f))[1]:
        iso=r['countryiso3code']
        if iso in meta and r['value'] is not None:
            out.setdefault(iso,{})[int(r['date'])]=r['value']
    return out
g=load('gini.json'); p=load('gdp.json')
rows=[]
for iso,ys in g.items():
    pts=[[y,round(v,1),round(p[iso][y])] for y,v in sorted(ys.items()) if iso in p and y in p[iso]]
    if pts:
        m=meta[iso]
        rows.append({'iso':iso,'name':m['name'],'region':m['region']['value'].strip(),'income':m['incomeLevel']['value'],'pts':pts})
rows.sort(key=lambda r:r['name'])
json.dump(rows,open(sys.argv[2],'w'),separators=(',',':'))
print(len(rows),sum(len(r['pts']) for r in rows))
print(sorted(set(r['region'] for r in rows)))
lat=[r for r in rows if r['pts'][-1][0]>=2015]
print('latest>=2015',len(lat))
xs=[math.log10(r['pts'][-1][2]) for r in lat]; ys=[r['pts'][-1][1] for r in lat]
n=len(xs);mx=sum(xs)/n;my=sum(ys)/n
cov=sum((a-mx)*(b-my) for a,b in zip(xs,ys));vx=sum((a-mx)**2 for a in xs);vy=sum((b-my)**2 for b in ys)
print('r',cov/math.sqrt(vx*vy))
