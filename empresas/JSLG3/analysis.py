import json
exec(open('model.py').read().split("base=run()")[0])
from scipy.optimize import brentq
res={}
b=run(); res['base']=b
# Lucro líquido ano 1 e múltiplos implícitos
r1=b['rows'][0]
netfin_ltm=(1368.534-224.036)-(1034.528-173.620)+(1039.471-165.695)
netfin1=netfin_ltm*0.95
ni1=(r1['ebit']-netfin1)*(1-t)+r1['jcp']
ebitda_ltm=ebit_ltm_rep+da0+185.653-ext_ltm
claims=debt_fin+deriv_net+leases+acq+div_pay+sist_s+conting-cash-inv_nc
mult=dict(ev_ebitda_ltm=b['ev']/ebitda_ltm, ev_ebitda_1=b['ev']/r1['ebitda'], pl_1=b['eq']/ni1, pvp=b['eq']/1208.247,
          mkt_ev=E+claims, mkt_ev_ebitda_ltm=(E+claims)/ebitda_ltm, mkt_ev_ebitda_1=(E+claims)/r1['ebitda'], mkt_pl_1=E/ni1, mkt_pvp=E/1208.247,
          ni1=ni1, netfin_ltm=netfin_ltm, ebitda_ltm=ebitda_ltm, claims=claims)
res['mult']=mult
# Pares (ajuste para 30/09 via retorno de 1 mês reportado)
peers={'TGMA3':dict(ev=6.16,nd=0.07,pl=9.36,pvp=2.39,r=-0.0451,mg=15.58,roic=20.57),
       'SIMH3':dict(ev=3.45,nd=3.24,pl=None,pvp=0.48,r=-0.4974,mg=30.41,roic=13.11),
       'VAMO3':dict(ev=3.74,nd=3.00,pl=6.99,pvp=0.84,r=-0.4465,mg=62.53,roic=13.55),
       'HBSA3':dict(ev=7.44,nd=2.87,pl=None,pvp=1.92,r=-0.1141,mg=39.09,roic=7.58)}
for k,p in peers.items():
    f=1/(1+p['r']); p['ev_set']=p['nd']+(p['ev']-p['nd'])*f; p['pl_set']=p['pl']*f if p['pl'] else None; p['pvp_set']=p['pvp']*f
import statistics as st
med=dict(ev=st.median([p['ev_set'] for p in peers.values()]), pl=st.median([p['pl_set'] for p in peers.values() if p['pl_set']]), pvp=st.median([p['pvp_set'] for p in peers.values()]),
         ev_now=st.median([p['ev'] for p in peers.values()]))
res['peers']=peers; res['med']=med
# Cenários ERP
res['erp_scen']={f"{e:.2%}":run(erp_p=e)['ps'] for e in (erp_impl,0.0431,erp,0.0631)}
res['wacc_alvo50']=run(erp_p=erp,dvT=0.5)['ps']
# Sensibilidade WACC x margem
res['grid_wm']={f"{ws:+.0%}":{f"{m:.1%}":run(wacc_shift=ws,mT=m)['ps'] for m in (0.108,0.113,0.118,0.123,0.128)} for ws in (-0.02,-0.01,0,0.01,0.02)}
res['grid_g']={f"{ws:+.0%}":{f"{gg:.2%}":run(wacc_shift=ws,gL=gg)['ps'] for gg in (0.045,g,0.065)} for ws in (-0.01,0,0.01)}
res['grid_ronic']={f"{ro:.1%}":run(ronic_x=ro)['ps'] for ro in (0.11,0.12,0.135,0.15,0.17)}

# D3a: ROIC perpétuo > WACC (só ilustrativo)
def tv_roic(roic):
    bb=run(); wp=bb['wp']; n11=bb['rows'][-1]['nopat']*(1+g); tv=n11*(1-g/roic)/(wp-g); return (bb['pv']+tv*bb['rows'][-1]['fd']-claims)/shares
res['d3a']={f"{x:.1%}":tv_roic(x) for x in (0.136,0.16,0.20)}
# Guidance: receita bruta 21,4 bi em 2030 (~líquida 18,3 bi, razão líquida/bruta LTM)
nb=9951.753/(11.7e3)  # ROL/ROB LTM aprox
gs_g=[0.14]*4+[0.10,0.09,0.08,0.07,0.06,0.0557]
gd=run(gs=gs_g); res['guid']=dict(ps=gd['ps'],rev4=gd['rows'][3]['receita'],ebitda4=gd['rows'][3]['ebitda'])
gd2=run(gs=gs_g,mT=0.125); res['guid2']=dict(ps=gd2['ps'])
# Taxa implícita no preço: deslocamento uniforme de WACC que iguala ao preço
for px in (8.06,5.44):
    sh=brentq(lambda x: run(wacc_shift=x)['ps']-px,-0.08,0.05); res[f'impl_{px}']=dict(shift=sh,w1=b['rows'][0]['wacc']+sh,wp=b['wp']+sh)
json.dump(res,open('analysis.json','w'),default=float,indent=1)
print(json.dumps({k:v for k,v in res.items() if k!='base'},default=lambda x:round(x,3),indent=1))
