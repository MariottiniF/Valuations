from scipy.optimize import brentq
P=186340.46; E1=21000; ipca=0.035; pib=0.02
g=(1+ipca)*(1+pib)-1; ROE=0.15
def pv(r,E1=E1,payout1=0.60,ROE=ROE):
    E=E1; v=0; gs=[0.04,0.045,0.05,0.055]  # crescimento anos 2..5 convergindo ao LTG
    for t in range(1,6):
        if t>1: E*=1+gs[t-2]
        pay = payout1 + (1-g/ROE-payout1)*(t-1)/4
        v+=E*pay/(1+r)**t
    TV=E*(1+g)*(1-g/ROE)/(r-g)
    return v+TV/(1+r)**5
r=brentq(lambda r:pv(r)-P,0.06,0.5)
rf_lp=(1.0710)*(1+ipca)-1; rf_37=(1.0750)*(1+ipca)-1
print(f"g={g:.4%} r={r:.4%} rf2060nom={rf_lp:.4%} ERP={r-rf_lp:.4%} rf2037={rf_37:.4%}")
for E in (20476,21831):
  for roe in (0.13,0.15,0.17):
    rr=brentq(lambda x:pv(x,E1=E,ROE=roe)-P,0.06,0.5); print(E,roe,f"{rr:.2%} ERP {rr-rf_lp:.2%}")
print("--- ROE perpétuo = r (consistente com D3: ROIC=WACC)")
def pv2(r,E1=E1,payout1=0.60):
    E=E1; v=0; gs=[0.04,0.045,0.05,0.055]
    pT=1-g/r
    for t in range(1,6):
        if t>1: E*=1+gs[t-2]
        pay=payout1+(pT-payout1)*(t-1)/4
        v+=E*pay/(1+r)**t
    TV=E*(1+g)*pT/(r-g)
    return v+TV/(1+r)**5
for E in (20476,21000,21831):
  for p1 in (0.5,0.6,0.7):
    rr=brentq(lambda x:pv2(x,E1=E,payout1=p1)-P,0.06,0.5); print(E,p1,f"r={rr:.2%} ERP={rr-rf_lp:.2%}")
