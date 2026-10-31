import json, numpy as np
M=1.0  # R$ milhões
# ---------- Macro / WACC ----------
ipca_lp=0.035; pib_lp=0.02
g=(1+ipca_lp)*(1+pib_lp)-1
rr37=0.0750; rr60=0.0710
rf_x=(1+rr37)*(1+ipca_lp)-1; rf_p=(1+rr60)*(1+ipca_lp)-1
erp_mat=0.0420; crp=0.0324; ds=0.0213
erp=erp_mat+(crp-ds)          # âncora 2 (maduro + diferencial de risco-país ações vs. soberano)
erp_impl=0.0156
bu=0.87; t=0.34; spread=0.023
price=8.06; shares=285.368917
E=price*shares
debt_fin=793.507+4333.247+299.893+1490.775+8.477+5.785
deriv_net=(120.658+116.777)-196.663
leases=277.457+693.580
acq=99.002+402.522
D=debt_fin+deriv_net+leases+acq
cash=259.690+1553.229+1.892
div_pay=421.064; sist_s=212.601; conting=324.495-213.918-72.346; inv_nc=21.073
def wacc(dv,rf,erp=erp,bu=bu,spread=spread):
    de=dv/(1-dv); bl=bu*(1+(1-t)*de); ke=rf+bl*erp; kd=rf+spread
    return ke*(1-dv)+kd*(1-t)*dv, bl, ke, kd
dv0=D/(D+E); dvT=0.50
# ---------- Operação ----------
rev0=9640.608-7186.586+7497.731
ebit_ltm_rep=1141.757-867.115+643.526
ext_ltm=118.621-106.055+17.168
ppa_ltm=48.4
ebit0=ebit_ltm_rep+185.653-ext_ltm+ppa_ltm
da0=817.370-593.997+650.700
IC0=1208.247+debt_fin+deriv_net+leases+acq+div_pay+sist_s-cash
def run(gs=None,m0=None,mT=0.118,ronic_x=0.135,erp_x=None,erp_p=None,dvT=dvT,gL=g,bu=bu,wacc_shift=0.0,spread=spread,verbose=False):
    erp_x=erp_impl if erp_x is None else erp_x
    erp_p=erp if erp_p is None else erp_p
    gs=gs or [0.10,0.10,0.09,0.08,0.07,0.066,0.063,0.060,0.058,0.0557]
    m0=m0 if m0 is not None else ebit0/rev0
    N=len(gs); wp=wacc(dvT,rf_p,erp_p,bu,spread)[0]+wacc_shift
    rows=[]; rev=rev0; disc=1; pv=0; jcp_eq=1208.247
    for i in range(N):
        rev*=1+gs[i]
        mg=m0+(mT-m0)*min(i+1,3)/3
        ebit=rev*mg; nopat=ebit*(1-t)
        gnext=gs[i+1] if i+1<N else gL
        ronic=ronic_x+(wp-ronic_x)*max(0,i-4)/5   # converge para WACC perpétuo nos anos 6-10
        reinv=gnext/ronic*nopat
        jcp=0.085*jcp_eq*t; jcp_eq*=1+gs[i]
        fcff=nopat-reinv+jcp
        dv=dv0+(dvT-dv0)*min(i,4)/4
        w=wacc(dv,rf_x,erp_x,bu,spread)[0]+wacc_shift
        disc/= (1+w); pv+=fcff*disc
        rows.append(dict(ano=i+1,receita=rev,g=gs[i],margem=mg,ebit=ebit,ebitda=ebit+rev*da0/rev0,nopat=nopat,ronic=ronic,reinv=reinv,jcp=jcp,fcff=fcff,wacc=w,fd=disc,pv=fcff*disc))
    nopat11=rows[-1]['nopat']*(1+gL)
    tv=nopat11*(1-gL/wp)/(wp-gL)   # ROIC = WACC => TV = NOPAT/WACC
    pvtv=tv*disc
    ev=pv+pvtv
    eq=ev-debt_fin-deriv_net-leases-acq-div_pay-sist_s-conting+cash+inv_nc
    return dict(rows=rows,wp=wp,tv=tv,pvtv=pvtv,pv=pv,ev=ev,eq=eq,ps=eq/shares)
base=run()
w0=wacc(dv0,rf_x,erp_impl); wT=wacc(dvT,rf_p,erp); w0b=wacc(dv0,rf_x,erp)
out=dict(w0b=w0b,g=g,rf_x=rf_x,rf_p=rf_p,erp=erp,E=E,D=D,dv0=dv0,w0=w0,wT=wT,w_xT=wacc(dvT,rf_x),cash=cash,debt_fin=debt_fin,deriv_net=deriv_net,leases=leases,acq=acq,
  rev0=rev0,ebit0=ebit0,ebit_rep=ebit_ltm_rep,da0=da0,IC0=IC0,roic0=ebit0*(1-t)/IC0,m0=ebit0/rev0)
print(json.dumps({k:(round(v,4) if isinstance(v,float) else [round(x,4) for x in v]) for k,v in out.items()},indent=0))
print({k:round(v,2) for k,v in base.items() if k!='rows'})
json.dump(dict(out=out,base={k:v for k,v in base.items()}),open('/home/claude/work/out/base.json','w'),default=float,indent=1)

for lab,kw in [("A base D5 (impl expl / 5,31 perp)",{}),("B 5,31 em tudo",dict(erp_x=erp)),("C implícito em tudo",dict(erp_p=erp_impl))]:
    r=run(**kw); print(lab, {k:round(v,1) for k,v in r.items() if k!='rows'}, "wacc anos",[round(x['wacc'],4) for x in r['rows']])
