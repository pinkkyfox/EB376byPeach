from quiz import T

f = lambda x: f"{x:,.2f}"
def g(x):  # compact number for given tables
    return f"{x:,.1f}".rstrip("0").rstrip(".") if isinstance(x, float) else f"{x:,}"

def nq(qid, title, ask, items, end="", mcqs=()):
    rows = "".join(f'<li data-ans="{a}" data-dp="{dp}"><span class="ip">{p}</span><span class="iw"><input inputmode="decimal" aria-label="{p}"><em>{u}</em></span><span class="mk"></span><span class="hw">{h}</span></li>' for p, a, u, h, dp in items)
    body = f'<div class="nq" id="{qid}"><ol class="ni">{rows}</ol><div class="row"><button class="pri" data-chk>ตรวจคำตอบ</button><button data-show>ดูเฉลย</button><button data-reset>ลองใหม่</button><span class="sc"></span></div><p class="ans">{end}</p></div>' if items else ""
    mq = "".join(f'<div class="qz pm" data-a="{a}"><p class="qq">{q}</p><div class="op">' + "".join(f'<button>{chr(65+k)}. {o}</button>' for k, o in enumerate(opts)) + f'</div><p class="ex2">{e}</p></div>' for q, opts, a, e in mcqs)
    return f'<div class="pq"><div class="pqh"><span class="tn">{title}</span><p>{ask}</p></div>{body}{mq}</div>'

def mcq(q, right, wrongs, pos, e):
    opts = list(wrongs); opts.insert(pos, right)
    return (q, opts, pos, e)

def build(sid, P):
    A, B = P["A"], P["B"]
    # ---------- Section A ----------
    r1, r2 = A["rev"]; c1, c2 = A["cogs"]; o1, o2 = A["opex"]; d1, d2 = A["da"]; i1, i2 = A["int"]
    gp1, gp2 = r1 - c1, r2 - c2; eb1, eb2 = gp1 - o1, gp2 - o2; e1, e2 = eb1 - d1, eb2 - d2; p1, p2 = e1 - i1, e2 - i2; t1, t2 = p1 * .2, p2 * .2; n1, n2 = p1 - t1, p2 - t2
    ca1 = A["cash"][0] + A["ar"][0] + A["inv"][0]; ca2 = A["cash"][1] + A["ar"][1] + A["inv"][1]
    ta1, ta2 = ca1 + A["ppe"][0], ca2 + A["ppe"][1]
    cl1, cl2 = A["ap"][0] + A["std"][0], A["ap"][1] + A["std"][1]
    tl1, tl2 = cl1 + A["ltd"][0], cl2 + A["ltd"][1]
    q1, q2 = ta1 - tl1, ta2 - tl2
    gpm1, gpm2 = gp1 / r1 * 100, gp2 / r2 * 100
    rg, gg = (r2 / r1 - 1) * 100, (gp2 / gp1 - 1) * 100
    cr1, cr2 = ca1 / cl1, ca2 / cl2
    qr1, qr2 = (ca1 - A["inv"][0]) / cl1, (ca2 - A["inv"][1]) / cl2
    it1, it2 = c1 / A["inv"][0], c2 / A["inv"][1]; id1, id2 = 365 / it1, 365 / it2
    at1, at2 = r1 / A["ar"][0], r2 / A["ar"][1]; ad1, ad2 = 365 / at1, 365 / at2
    de0 = tl2 / q2; de1 = (tl2 - A["repay"]) / q2
    debt = A["std"][1] + A["ltd"][1]; nd = debt - A["cash"][1]; ev = A["mv"] + nd; evx = ev / eb2

    adata = T(["Income statement", "Year 1", "Year 2"], [["Revenue", g(r1), g(r2)], ["Cost of goods sold", g(c1), g(c2)], ["Gross profit", g(gp1), g(gp2)], ["Operating expenses before D&A", g(o1), g(o2)], ["EBITDA", g(eb1), g(eb2)], ["D&A", g(d1), g(d2)], ["EBIT", g(e1), g(e2)], ["Interest expense", g(i1), g(i2)], ["Profit before tax", g(p1), g(p2)], ["Income tax", g(t1), g(t2)], ["Net profit", g(n1), g(n2)]]) + \
        T(["Balance sheet", "End Y1", "End Y2"], [["Cash", *map(g, A["cash"])], ["Trade receivables", *map(g, A["ar"])], ["Inventory", *map(g, A["inv"])], ["Total current assets", g(ca1), g(ca2)], ["Net PP&E", *map(g, A["ppe"])], ["Total assets", g(ta1), g(ta2)], ["Trade payables", *map(g, A["ap"])], ["Short-term interest-bearing debt", *map(g, A["std"])], ["Total current liabilities", g(cl1), g(cl2)], ["Long-term interest-bearing debt", *map(g, A["ltd"])], ["Total liabilities", g(tl1), g(tl2)], ["Shareholders' equity", g(q1), g(q2)]]) + \
        f'<p class="gl">All sales are on credit · ใช้ยอดสิ้นปี · 365 วัน · Equity market value สิ้น Year 2 = {g(A["mv"])}</p>'

    up = gpm2 > gpm1
    m_a1 = mcq("A1(c) Sales and gross profit both increased. Did gross profit margin also improve?",
        (f"Yes. Gross profit grew {f(gg)}%, faster than revenue ({f(rg)}%), so margin rose to {f(gpm2)}%." if up else f"No. Revenue grew {f(rg)}% but gross profit grew only {f(gg)}%, so margin fell to {f(gpm2)}%."),
        ["Yes. Both sales and gross profit increased, so margin must have improved.",
         (f"No. Gross profit grew faster than revenue, so margin fell." if up else f"Yes. COGS grew slower than revenue, so margin rose."),
         "It cannot be judged without net profit."], 1 if up else 2,
        "ดัก: ยอดขาย + GP เพิ่ม ≠ Margin เพิ่ม · ต้องเทียบ % การเติบโตของ GP กับ Revenue")
    crU, qrU = cr2 > cr1, qr2 > qr1
    if crU and qrU: right = f"Improved. Both current ratio ({f(cr1)}x → {f(cr2)}x) and quick ratio ({f(qr1)}x → {f(qr2)}x) rose."
    elif not crU and not qrU: right = f"Weakened. Both current ratio ({f(cr1)}x → {f(cr2)}x) and quick ratio ({f(qr1)}x → {f(qr2)}x) fell."
    elif crU: right = f"Mixed. Current ratio rose ({f(cr1)}x → {f(cr2)}x) but quick ratio fell ({f(qr1)}x → {f(qr2)}x), so the improvement relies on inventory."
    else: right = f"Mixed. Current ratio fell ({f(cr1)}x → {f(cr2)}x) but quick ratio rose ({f(qr1)}x → {f(qr2)}x)."
    pool = ["Improved. Both ratios rose.", "Weakened. Both ratios fell.", "Mixed. Current ratio rose but quick ratio fell, so it relies on inventory.", "Improved, because cash increased, so all liquidity ratios rise."]
    key = 0 if crU and qrU else 1 if (not crU and not qrU) else 2 if crU else None
    wr = [p for k, p in enumerate(pool) if k != key][:3]
    m_a2 = mcq("A2(c) Has liquidity improved from Year 1 to Year 2?", right, wr, 1, "ดัก: ต้องดูทั้ง 2 ratio · Quick ratio ตัด Inventory ออก")
    def speed(name, d1_, d2_, what, tied):
        fast = d2_ < d1_
        right = f"{'Faster' if fast else 'Slower'}: {what} days {'fell' if fast else 'rose'} from {f(d1_)} to {f(d2_)}, so {'less' if fast else 'more'} cash is tied up in {tied}."
        wrongs = [f"{'Slower' if fast else 'Faster'}: {what} days {'fell' if fast else 'rose'}, so {'more' if fast else 'less'} cash is tied up in {tied}.",
                  f"{'Faster' if fast else 'Slower'}, so {'more' if fast else 'less'} cash is tied up in {tied}.",
                  f"{'Faster' if not fast else 'Slower'}: turnover {'rose' if fast else 'fell'}, so days {'rose' if fast else 'fell'}."]
        return mcq(name, right, wrongs, 2 if fast else 0, "ดัก: Days ลด = เร็วขึ้น = เงินจมน้อยลง · Turnover กับ Days สวนทางกัน")
    m_a3a = speed("A3(b) Is the company selling inventory faster or slower in Year 2?", id1, id2, "Inventory", "inventory")
    m_a3b = speed("A3(d) Is the company collecting payments faster or slower in Year 2?", ad1, ad2, "Collection", "receivables")
    m_a4 = mcq(f"A4 The company uses {g(A['repay'])} of cash to repay bank debt. What happens?",
        f"Leverage falls (D/E {f(de0)}x → {f(de1)}x) but liquidity weakens because cash falls by {g(A['repay'])}.",
        ["Leverage rises because cash falls.", "Leverage falls and liquidity improves because debt is lower.", "D/E is unchanged because equity does not change."], 3,
        "ดัก: หนี้ลด → D/E ลด · แต่เงินสดก็ลด → Current/Quick ลด")

    secA = [
        nq(f"{sid}A1", "A1", "Growth และ Gross margin", [("Revenue growth", rg, "%", f"({g(r2)} − {g(r1)}) ÷ {g(r1)} = {f(rg)}%", 2), ("Gross profit growth", gg, "%", f"({g(gp2)} − {g(gp1)}) ÷ {g(gp1)} = {f(gg)}%", 2), ("GPM Year 1", gpm1, "%", f"{g(gp1)} ÷ {g(r1)} = {f(gpm1)}%", 2), ("GPM Year 2", gpm2, "%", f"{g(gp2)} ÷ {g(r2)} = {f(gpm2)}%", 2), ("Change", gpm2 - gpm1, "pp", f"{f(gpm2)} − {f(gpm1)} = {f(gpm2 - gpm1)} pp", 2)], "", [m_a1]),
        nq(f"{sid}A2", "A2", "Current ratio และ Quick ratio", [("Current ratio Y1", cr1, "x", f"{g(ca1)} ÷ {g(cl1)} = {f(cr1)}x", 2), ("Current ratio Y2", cr2, "x", f"{g(ca2)} ÷ {g(cl2)} = {f(cr2)}x", 2), ("Quick ratio Y1", qr1, "x", f"({g(ca1)} − {g(A['inv'][0])}) ÷ {g(cl1)} = {f(qr1)}x", 2), ("Quick ratio Y2", qr2, "x", f"({g(ca2)} − {g(A['inv'][1])}) ÷ {g(cl2)} = {f(qr2)}x", 2)], "", [m_a2]),
        nq(f"{sid}A3", "A3", "Turnover และ Days (365 วัน)", [("Inventory turnover Y1", it1, "x", f"{g(c1)} ÷ {g(A['inv'][0])} = {f(it1)}x", 2), ("Inventory days Y1", id1, "วัน", f"365 ÷ {f(it1)} = {f(id1)}", 2), ("Inventory turnover Y2", it2, "x", f"{g(c2)} ÷ {g(A['inv'][1])} = {f(it2)}x", 2), ("Inventory days Y2", id2, "วัน", f"365 ÷ {it2:.6f} = {f(id2)}", 2),
            ("AR turnover Y1", at1, "x", f"{g(r1)} ÷ {g(A['ar'][0])} = {f(at1)}x", 2), ("Collection days Y1", ad1, "วัน", f"365 ÷ {f(at1)} = {f(ad1)}", 2), ("AR turnover Y2", at2, "x", f"{g(r2)} ÷ {g(A['ar'][1])} = {f(at2)}x", 2), ("Collection days Y2", ad2, "วัน", f"365 ÷ {at2:.6f} = {f(ad2)}", 2)], "ห้ามปัด Turnover ก่อนหาร 365", [m_a3a, m_a3b]),
        nq(f"{sid}A4", "A4", f"ใช้เงินสด {g(A['repay'])} คืนหนี้ธนาคาร (Scenario แยก · D/E ใช้ Total liabilities)", [("D/E ก่อน (Year 2)", de0, "x", f"{g(tl2)} ÷ {g(q2)} = {f(de0)}x", 2), ("D/E หลังคืนหนี้", de1, "x", f"({g(tl2)} − {g(A['repay'])}) ÷ {g(q2)} = {f(de1)}x", 2)], "", [m_a4]),
        nq(f"{sid}A5", "A5", "Net debt, EV, EV/EBITDA (Year 2)", [("Interest-bearing debt", debt, "", f"{g(A['std'][1])} + {g(A['ltd'][1])} = {f(debt)}", 2), ("Net debt", nd, "", f"{f(debt)} − {g(A['cash'][1])} = {f(nd)}", 2), ("Enterprise value", ev, "", f"{g(A['mv'])} + {f(nd)} = {f(ev)}", 2), ("EV/EBITDA", evx, "x", f"{f(ev)} ÷ {g(eb2)} = {f(evx)}x", 2)], "",
           [mcq("ข้อไหน <u>ไม่</u> นับเป็น Interest-bearing debt ใน EV", "Trade payables", ["Short-term bank loan", "Long-term bonds", "Lease liabilities"], 0, "Trade payables เป็นหนี้การค้า ไม่มีดอกเบี้ย → ไม่นับใน EV")]),
    ]

    # ---------- Section B–D ----------
    yrs = ["2026A", "2027E", "2028E", "2029E", "2030E", "2031E"]
    EB, DA = B["ebitda"], B["da"]; EBIT = [a - b for a, b in zip(EB, DA)]
    NWC = [a + b - c for a, b, c in zip(B["ar"], B["inv"], B["ap"])]; dN = [NWC[k] - NWC[k - 1] for k in range(1, 6)]
    FC = [EBIT[k] * .8 + DA[k] - dN[k - 1] - B["capex"][k - 1] for k in range(1, 6)]
    w = B["wacc"]; DF = [round(1 / (1 + w / 100) ** t, 4) for t in range(1, 6)]
    PV = [a * b for a, b in zip(FC, DF)]; SPV = sum(PV); TV = B["exit"] * EB[5]; PTV = TV * DF[4]; EV = SPV + PTV
    ND = B["debt"] - B["cash"]; EQ = EV - ND
    pe = sorted(B["peers"]); MED = (pe[1] + pe[2]) / 2; EVm = MED * EB[1]; EQm = EVm - ND
    ask = B["ask"]; pd_, pm_ = (ask / EQ - 1) * 100, (ask / EQm - 1) * 100
    bdata = T(["THB mn"] + yrs, [["Revenue"] + [g(x) for x in B["rev"]], ["EBITDA"] + [g(x) for x in EB], ["D&A"] + [g(x) for x in DA], ["EBIT"] + [g(x) for x in EBIT],
        ["Trade receivables"] + [g(x) for x in B["ar"]], ["Inventory"] + [g(x) for x in B["inv"]], ["Trade payables"] + [g(x) for x in B["ap"]], ["Cash capex", ""] + [g(x) for x in B["capex"]]]) + \
        f'<p class="gl">Tax rate 20% · WACC {g(w)}% · Valuation date 31 Dec 2026 · Interest-bearing debt {g(B["debt"])} · Surplus cash {g(B["cash"])} · ผู้ขายเสนอ {g(ask)} สำหรับหุ้น 100% · Terminal EV สิ้นปี 2031 = {g(B["exit"])}x × EBITDA 2031E</p>' + \
        T(["Period", "1", "2", "3", "4", "5"], [["Discount factor"] + [f"{d:.4f}" for d in DF]]) + \
        T(["Peer", "A", "B", "C", "D"], [["2027E EV/EBITDA"] + [f"{x:.1f}x" for x in B["peers"]]])
    above = ask > EQ and ask > EQm; below = ask < EQ and ask < EQm
    if above: rd, ri = f"No. The asking price {g(ask)} is above both equity estimates (DCF {f(EQ)}, EV/EBITDA {f(EQm)}), so the buyer would overpay.", 0
    elif below: rd, ri = f"Yes, it looks attractive. The asking price {g(ask)} is below both equity estimates (DCF {f(EQ)}, EV/EBITDA {f(EQm)}).", 0
    else: rd, ri = f"Not clear-cut. The asking price {g(ask)} is between the two estimates (DCF {f(EQ)}, EV/EBITDA {f(EQm)}), so judge it as a range.", 0
    m_d3 = mcq(f"D3 Should the buyer accept the asking price of {g(ask)}?", rd,
        [f"Yes, because enterprise value ({f(EV)}) is above the asking price.", "Yes, because DCF gives a guaranteed fair value.", "Compare the asking price with EBITDA instead."], 2,
        "ดัก: ราคาที่เสนอเป็นราคาหุ้น 100% → ต้องเทียบกับ Equity value ไม่ใช่ EV · ผลเป็น Range ไม่ใช่ราคาการันตี")
    secB = [
        nq(f"{sid}B1", "B1", "Operating NWC = Trade receivables + Inventory − Trade payables", [("NWC 2026A", NWC[0], "", f"{g(B['ar'][0])} + {g(B['inv'][0])} − {g(B['ap'][0])} = {f(NWC[0])}", 2), ("NWC 2027E", NWC[1], "", f"{g(B['ar'][1])} + {g(B['inv'][1])} − {g(B['ap'][1])} = {f(NWC[1])}", 2), ("NWC 2031E", NWC[5], "", f"{g(B['ar'][5])} + {g(B['inv'][5])} − {g(B['ap'][5])} = {f(NWC[5])}", 2),
            ("Cash effect 2027E", -dN[0], "", f"{f(NWC[1])} − {f(NWC[0])} = {dN[0]:+.2f} → {'(' + f(dN[0]) + ')' if dN[0] > 0 else f(-dN[0])}", 2), ("Cash effect 2028E", -dN[1], "", f"{f(NWC[2])} − {f(NWC[1])} = {dN[1]:+.2f}", 2)], "NWC เพิ่ม = เงินจม → ค่าลบ (วงเล็บ)",
           [mcq("NWC เพิ่มขึ้น ส่งผลต่อ FCFF ยังไง", "FCFF ลดลง เพราะเงินไปจมใน Working capital", ["FCFF เพิ่มขึ้น เพราะสินทรัพย์เพิ่ม", "ไม่กระทบ เพราะ NWC อยู่ใน Balance sheet", "FCFF ลดลง เพราะ CapEx เพิ่ม"], 0, "ดัก: NWC ↑ = Cash outflow ไม่ใช่สินทรัพย์ที่ทำให้เงินเพิ่ม")]),
        nq(f"{sid}B2", "B2", "FCFF = EBIT × (1 − 20%) + D&amp;A − ΔNWC − CapEx", [(f"FCFF {yrs[k]}", FC[k - 1], "", f"{g(EBIT[k])} × 0.8 + {g(DA[k])} − {g(dN[k-1])} − {g(B['capex'][k-1])} = {f(FC[k-1])}", 2) for k in range(1, 6)], "",
           [mcq("ภาษีใน FCFF คิดจากอะไร", "EBIT × Tax rate", ["Profit before tax × Tax rate", "Income tax expense ในงบ", "Net income × Tax rate"], 0, "ดัก: FCFF เป็นกระแสเงินก่อนจ่ายเจ้าหนี้ → ใช้ภาษีบน EBIT ไม่ใช่ PBT")]),
        nq(f"{sid}C1", "C1", "Discount FCFF แต่ละปี", [(f"PV {yrs[k+1]}", PV[k], "", f"{f(FC[k])} × {DF[k]:.4f} = {f(PV[k])}", 2) for k in range(5)] + [("Σ PV of FCFF", SPV, "", f"รวม = {f(SPV)}", 2)], ""),
        nq(f"{sid}C2", "C2", "Terminal value และ PV", [("Terminal EV", TV, "", f"{g(B['exit'])} × {g(EB[5])} = {f(TV)}", 2), ("PV of TV", PTV, "", f"{f(TV)} × {DF[4]:.4f} = {f(PTV)}", 2)], "",
           [mcq("Terminal value สิ้นปี 2031 ต้อง discount ด้วย DF ปีไหน", "Period 5 (ปีสุดท้าย)", ["Period 6 เพราะเป็นมูลค่าหลังปีสุดท้าย", "Period 1", "ไม่ต้อง discount"], 0, "ดัก: TV คิด ณ สิ้นปีที่ 5 → ใช้ DF ปีที่ 5")]),
        nq(f"{sid}C3", "C3", "Enterprise-to-equity bridge", [("Enterprise value", EV, "", f"{f(SPV)} + {f(PTV)} = {f(EV)}", 2), ("Net debt", ND, "", f"{g(B['debt'])} − {g(B['cash'])} = {f(ND)}", 2), ("Equity value (100%)", EQ, "", f"{f(EV)} − {f(ND)} = {f(EQ)}", 2)], f"TV คิดเป็น {PTV/EV*100:.1f}% ของ EV"),
        nq(f"{sid}D1", "D1", "EV/EBITDA valuation (2027E)", [("Median EV/EBITDA", MED, "x", "เรียง " + ", ".join(f"{x:.1f}" for x in pe) + f" → ({pe[1]:.1f} + {pe[2]:.1f}) ÷ 2 = {f(MED)}x", 2), ("Enterprise value", EVm, "", f"{f(MED)} × {g(EB[1])} = {f(EVm)}", 2), ("Equity value", EQm, "", f"{f(EVm)} − {f(ND)} = {f(EQm)}", 2)], "",
           [mcq("Multiple ของคู่แข่งเป็นปี 2027E ต้องคูณกับ EBITDA ปีไหน", "2027E", ["2026A", "2031E", "ค่าเฉลี่ย 5 ปี"], 0, "ดัก: Multiple กับ EBITDA ต้องเป็นปีเดียวกัน")]),
        nq(f"{sid}D2", "D2", f"เทียบราคาเสนอ {g(ask)}", [("ส่วนต่าง vs DCF", ask - EQ, "", f"{g(ask)} − {f(EQ)} = {f(ask - EQ)}", 2), ("Asking premium vs DCF", pd_, "%", f"{f(ask - EQ)} ÷ {f(EQ)} = {f(pd_)}%", 2), ("ส่วนต่าง vs EV/EBITDA", ask - EQm, "", f"{g(ask)} − {f(EQm)} = {f(ask - EQm)}", 2), ("Asking premium vs EV/EBITDA", pm_, "%", f"{f(ask - EQm)} ÷ {f(EQm)} = {f(pm_)}%", 2)], "ติดลบ = ราคาเสนอต่ำกว่ามูลค่าที่ประเมิน", [m_d3]),
    ]
    return [("A", "Ratios", f"{A['name']} (THB mn)", adata, secA[:5]), ("B–D", "FCFF · DCF · Multiples", f"{B['name']} (THB mn)", bdata, secB)]

SETS = [
 {"A": dict(name="ร้านหนังสือ Book &amp; Bean", rev=(400, 460), cogs=(240, 290), opex=(90, 95), da=(20, 20), int=(8, 8), cash=(30, 25), ar=(40, 60), inv=(50, 70), ppe=(180, 185), ap=(45, 55), std=(25, 25), ltd=(100, 100), mv=450, repay=20),
  "B": dict(name="ร้านเบเกอรี่ Khao Hom", rev=[300, 330, 360, 390, 420, 450], ebitda=[45, 51, 57, 63, 69, 75], da=[15, 16, 17, 18, 19, 20], ar=[20, 23, 26, 28, 30, 32], inv=[25, 28, 31, 33, 35, 37], ap=[21, 23, 25, 27, 29, 31], capex=[30, 26, 24, 22, 24], wacc=10, exit=5.0, debt=90, cash=30, peers=[4.6, 5.4, 5.0, 6.2], ask=300)},
 {"A": dict(name="ร้านชา Tea Time", rev=(500, 550), cogs=(325, 341), opex=(110, 120), da=(25, 25), int=(10, 10), cash=(40, 30), ar=(45, 60), inv=(60, 55), ppe=(250, 285), ap=(50, 70), std=(30, 30), ltd=(120, 120), mv=600, repay=25),
  "B": dict(name="ร้านสลัด Green Bowl", rev=[400, 440, 480, 520, 560, 600], ebitda=[60, 66, 72, 78, 84, 90], da=[20, 22, 24, 26, 28, 30], ar=[30, 33, 36, 38, 40, 42], inv=[20, 22, 24, 25, 26, 27], ap=[25, 27, 29, 30, 31, 32], capex=[40, 36, 30, 28, 30], wacc=9, exit=6.0, debt=120, cash=40, peers=[5.5, 6.5, 6.0, 7.1], ask=380)},
 {"A": dict(name="โรงพิมพ์ Bright Print", rev=(300, 330), cogs=(180, 204), opex=(70, 72), da=(15, 16), int=(6, 6), cash=(25, 35), ar=(30, 30), inv=(40, 44), ppe=(160, 165), ap=(35, 38), std=(15, 15), ltd=(70, 60), mv=380, repay=15),
  "B": dict(name="ฟิตเนส Sun Gym", rev=[250, 275, 300, 330, 355, 380], ebitda=[50, 55, 61, 67, 72, 78], da=[18, 19, 21, 23, 24, 26], ar=[10, 11, 12, 13, 14, 15], inv=[5, 6, 6, 7, 7, 8], ap=[12, 13, 14, 15, 16, 17], capex=[45, 35, 28, 25, 26], wacc=11, exit=5.5, debt=100, cash=20, peers=[4.8, 5.6, 5.2, 5.9], ask=230)},
 {"A": dict(name="มินิมาร์ท Coco Mart", rev=(800, 880), cogs=(560, 620), opex=(150, 160), da=(30, 32), int=(20, 22), cash=(50, 45), ar=(60, 85), inv=(120, 150), ppe=(400, 420), ap=(110, 125), std=(60, 70), ltd=(200, 210), mv=700, repay=40),
  "B": dict(name="โรงเบียร์ Hop House", rev=[600, 660, 720, 780, 840, 900], ebitda=[80, 88, 96, 104, 112, 120], da=[30, 32, 34, 36, 38, 40], ar=[40, 44, 48, 52, 56, 60], inv=[50, 55, 60, 64, 68, 72], ap=[45, 49, 53, 57, 61, 65], capex=[70, 60, 55, 50, 52], wacc=12, exit=4.0, debt=150, cash=30, peers=[3.8, 4.4, 4.2, 5.0], ask=260)},
]

def render():
    out = '<div class="view" id="v-practice"><div class="chead"><span class="big">P</span><div><h1>Practice Exam</h1><p>ข้อสอบจำลอง 4 ชุด รูปแบบเดียวกับของอาจารย์ · ตัวเลขคำนวณพิมพ์ตอบ · ข้อเขียนเป็นช้อยส์ที่ดัก keyword · ตอบ 2 ทศนิยม ห้ามปัดกลางทาง</p></div></div>'
    out += '<div class="sets" id="sets">' + "".join(f'<button data-set="{i}" class="{"on" if i == 0 else ""}">ชุด {i+1}</button>' for i in range(len(SETS))) + '</div>'
    for i, P in enumerate(SETS):
        sid = f"s{i+1}"
        secs = build(sid, P)
        body = '<nav class="toc">' + "".join(f'<a href="#{sid}-{k}"><span>{t}</span>{n}</a>' for k, (t, n, *_) in enumerate(secs)) + '</nav>'
        for k, (t, n, s, data, qs) in enumerate(secs):
            body += f'<section class="tp" id="{sid}-{k}"><div class="th"><div><h3>Section {t} · {n}</h3><p>{s}</p></div></div><details class="data" open><summary>ข้อมูลโจทย์</summary>{data}</details>{"".join(qs)}</section>'
        out += f'<div class="set{" on" if i == 0 else ""}" data-s="{i}">{body}</div>'
    return out + '</div>'
