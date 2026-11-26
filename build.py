import html as H, json

def e(s): return H.escape(str(s), quote=False)

# ---------- infographic helpers ----------
def flow(items, cap=""):
    out = []
    for i, it in enumerate(items):
        if isinstance(it, str):
            a, b = it, ""
        else:
            a, b = it
        out.append(f'<div class="fb"><b>{a}</b>{f"<span>{b}</span>" if b else ""}</div>')
        if i < len(items) - 1: out.append('<div class="fa">→</div>')
    c = f'<p class="cap">{cap}</p>' if cap else ""
    return f'<div class="flow">{"".join(out)}</div>{c}'

def cards(items, cols=3):
    return f'<div class="cg c{cols}">' + "".join(
        f'<div class="cd"><div class="ct">{t}</div><div class="cb">{b}</div>{f"<div class=cn>{n}</div>" if n else ""}</div>'
        for t, b, *rest in items for n in [rest[0] if rest else ""]) + '</div>'

def eq(s, note=""):
    return f'<div class="eq">{s}</div>' + (f'<p class="cap">{note}</p>' if note else "")

def vs(lt, lb, rt, rb):
    return f'<div class="vs"><div><div class="ct">{lt}</div><div class="cb">{lb}</div></div><div class="vsx">vs</div><div><div class="ct">{rt}</div><div class="cb">{rb}</div></div></div>'

def bars(rows, mx):
    out = ""
    for lab, v, kind, note in rows:
        w = abs(v) / mx * 100
        out += f'<div class="br {kind}"><div class="bl">{lab}</div><div class="bt"><div style="width:{w:.1f}%"></div></div><div class="bv">{note}</div></div>'
    return f'<div class="bars">{out}</div>'

def tbl(head, rows):
    h = "".join(f"<th>{x}</th>" for x in head)
    b = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<div class="scroll"><table>{f"<tr>{h}</tr>" if head else ""}{b}</table></div>'

def arrows(lines):
    return '<div class="chain">' + "".join(f'<div>{l}</div>' for l in lines) + '</div>'

# ---------- content ----------
CH = []

# ===== Chapter 6 =====
CH.append({"n": "6", "t": "Understanding Great Businesses", "q": "ธุรกิจนี้ดีไหม · ทำเงินยังไง · กำไรจะอยู่นานไหม",
"topics": [
 {"t": "Total Return", "s": "ผู้ถือหุ้นได้ผลตอบแทนจาก 2 ทาง",
  "info": flow([("Dividends", "ปันผลระหว่างถือ"), ("+ Capital gain", "ราคาขาย − ราคาซื้อ"), ("÷ Purchase price", "หารราคาซื้อเสมอ"), ("= Total return", "%")]) +
          vs("Shareholders", "Residual claim → ได้ส่วนที่เหลือหลังจ่ายเจ้าหนี้ → ผลตอบแทนขึ้นกับผลงาน + ราคาหุ้น", "Bondholders", "Contractual claim → ได้ดอกเบี้ย + เงินต้นตามสัญญา → ได้รับชำระก่อน"),
  "f": [["Capital gain", "Sale price − Purchase price"], ["Total return", "(Dividend + Capital gain) ÷ Purchase price"], ["Ownership %", "Shares held ÷ Shares outstanding"]],
  "ex": ["ซื้อหุ้น 100 · ได้ปันผล 5 · ขาย 110", [["Capital gain", "110 − 100", "10"], ["Total return", "(5 + 10) ÷ 100", "15.00%"]]],
  "qs": [{"q": "ซื้อ 50 · ปันผล 2 · ขาย 45 → Total return?", "s": [["Capital gain", "45 − 50 = −5"], ["Total return", "(2 + (−5)) ÷ 50 = −6.00%"]], "a": "−6.00% · ขาดทุนให้ใส่ค่าติดลบ"}]},
 {"t": "Business Model Canvas (BMC)", "s": "อ่านจากขวา → ซ้าย เริ่มที่ลูกค้า",
  "info": '<div class="bmc">' + "".join(f'<div class="bk {c}"><b>{t}</b><span>{d}</span></div>' for t, d, c in [
     ("Key Partners", "Supplier มีอำนาจ → COGS ↑", "kp"), ("Key Activities", "ที่มาของ Opex ก้อนใหญ่", "ka"), ("Value Proposition", "Better → Margin ↑", "vp"),
     ("Customer Relationships", "Repeat ↑ Churn ↓ → รายได้นิ่ง", "cr"), ("Customer Segments", "จำนวนลูกค้า = เพดานรายได้", "cs"),
     ("Key Resources", "Physical หนัก → CapEx ↑", "kr"), ("Channels", "Dealer ให้เครดิต → AR ↑", "ch"),
     ("Cost Structure", "Fixed สูง → กำไรแกว่ง", "cost"), ("Revenue Streams", "Recurring → Risk ↓", "rev")]) + '</div>' +
     '<p class="cap">ฝั่งขวา (ลูกค้า → รายได้) = ขนาดและความเสี่ยงของรายได้ · ฝั่งซ้าย (ทรัพยากร → ต้นทุน) = Margin และเงินลงทุน</p>' +
     '<div class="ct">แต่ละช่องตีความอะไรได้บ้าง (อ่านตามลำดับ 1 → 9)</div>' + tbl(["#","Block","ถามอะไร","ตีความว่าดี","ตีความว่าเสี่ยง","กระทบ"], [["1", "Customer Segments", "ลูกค้าคือใคร ต้องการอะไร", "ลูกค้าเยอะ / Need จำเป็น (Functional)", "ลูกค้าน้อยราย / B2B ขอเครดิตนาน", "Revenue ceiling · AR days"], ["2", "Value Proposition", "ทำไมลูกค้าเลือกเรา", "Better → ตั้งราคาสูงได้ · มีหลักฐาน (Repeat, Willingness to pay)", "Cheaper แต่ต้นทุนไม่ต่ำจริง", "Gross margin"], ["3", "Channels", "ลูกค้าหาเจอ ซื้อ รับของยังไง", "ขายตรง → เก็บ Margin เอง", "ผ่าน Dealer → เสีย Margin + ให้เครดิต", "Margin · AR days"], ["4", "Customer Relationships", "หาและรักษาลูกค้ายังไง", "Self-serve → Cost to serve ต่ำ · Repeat ↑ Churn ↓", "Dedicated → ค่าดูแลสูง · Churn สูง", "Opex · รายได้นิ่งแค่ไหน"], ["5", "Revenue Streams", "เงินเข้ามาแบบไหน", "Subscription / Recurring → คาดการณ์ได้", "One-time → ต้องหาลูกค้าใหม่ตลอด", "Revenue risk · Multiple"], ["6", "Key Resources", "ต้องมีสินทรัพย์อะไร", "Intangible ลอกยาก (Brand, Patent) → ฐานของ Moat", "Physical หนัก (โรงงาน, สาขา)", "CapEx → FCFF"], ["7", "Key Activities", "งานหลักที่ต้องทำ", "Collections ดี → เก็บเงินเร็ว", "กิจกรรมเยอะ ใช้คนมาก", "Opex → EBITDA"], ["8", "Key Partners", "ใครช่วยจากภายนอก", "Supplier หลายราย → ต่อรองได้", "พึ่ง Supplier รายเดียว / Supplier มีอำนาจ", "COGS · Supply risk"], ["9", "Cost Structure", "ต้นทุนหลัก คงที่หรือผันแปร", "Variable สูง → ปรับตามยอดขายได้", "Fixed สูง → กำไรแกว่งตามยอดขายมาก", "Margin · Breakeven"]]) +
     eq("ทุกช่องตอบคำถามเดียว: ช่องนี้ทำให้ Cash flow มากขึ้น / Margin สูงขึ้น / Risk ลดลง หรือเปล่า"),
  "f": [["Revenue Streams, Segments", "→ Revenue, Growth"], ["Value Prop., Partners", "→ Gross margin"], ["Activities, Cost Structure", "→ Opex → EBITDA"], ["Key Resources", "→ CapEx"], ["Channels, Segments", "→ AR days → ΔNWC"]],
  "ex": ["ร้านกาแฟขายให้ออฟฟิศ (B2B) ให้เครดิต 30 วัน", [["Customer Segments", "ลูกค้าบริษัท ขอเครดิต", "AR ↑"], ["ผลต่องบ", "เงินเข้าช้า → NWC ↑", "FCFF ↓"]]],
  "qs": [{"q": "บริษัทเปลี่ยนจากขายตรงเป็นขายผ่านตัวแทนที่ขอเครดิต 60 วัน กระทบอะไร", "s": [["Block ที่เกี่ยว", "Channels → Dealer / Retail"], ["ผล", "เสีย Margin ให้ตัวแทน + AR days ↑ → ΔNWC ↑ → FCFF ↓"]], "a": "Margin ↓ และเงินสดเข้าช้าลง"}]},
 {"t": "Revenue Streams", "s": "เงินเข้ามาแบบไหน คาดการณ์ได้แค่ไหน",
  "info": cards([("One-time sale", "จ่ายครั้งเดียว · หาลูกค้าใหม่ตลอด", "คาดการณ์ยาก"), ("Usage / Transaction", "จ่ายทุกครั้งที่ใช้ · แกว่งตามการใช้", "ปานกลาง"),
                 ("Subscription", "จ่ายประจำ · Recurring", "คาดการณ์ได้สุด"), ("Razor-and-blade", "ขายเครื่อง แล้วกินจากของซื้อซ้ำ", "ดูกำไรของซื้อซ้ำ")], 4) +
          eq("Recurring ↑ → คาดการณ์ได้ → Risk ↓ → Valuation multiple ↑"),
  "f": [], "ex": ["Netflix vs ร้านขายแอร์", [["Netflix", "Subscription", "Recurring"], ["ร้านแอร์", "One-time sale", "ต้องหาลูกค้าใหม่"]]],
  "qs": [{"mcq": 1, "q": "Printer ราคาถูก แต่หมึกแพงและต้องซื้อซ้ำ เป็นแบบไหน", "o": ["One-time sale", "Subscription", "Razor-and-blade", "Usage"], "a": 2, "e": "ขายเครื่องถูก แล้วกินกำไรจากของที่ซื้อซ้ำ (หมึก)"}]},
 {"t": "Breakeven", "s": "ต้องขายกี่หน่วยถึงไม่ขาดทุน",
  "info": flow([("Price", "ราคาขาย"), ("− Variable cost", "ต้นทุนต่อหน่วย"), ("= Contribution", "กำไรต่อหน่วย"), ("Fixed cost ÷ Contribution", "= Breakeven units")]) +
          eq("Fixed cost สูง → กำไรแกว่งตามยอดขายมาก · ขายเกิน Breakeven → Fixed cost ต่อหน่วย ↓ → Margin ↑"),
  "f": [["Total cost", "Fixed cost + Variable cost per unit × Output"], ["Contribution per unit", "Price − Variable cost per unit"], ["Breakeven units", "Fixed cost ÷ (Price − Variable cost per unit)"], ["Profit", "Contribution × Units − Fixed cost"]],
  "ex": ["ขายแก้วละ 50 · ต้นทุนแปรผัน 30 · ค่าเช่า + เงินเดือน 10,000", [["Contribution", "50 − 30", "20"], ["Breakeven", "10,000 ÷ 20", "500 แก้ว"], ["ขาย 700 แก้ว กำไร", "20 × 700 − 10,000", "4,000"]]],
  "qs": [{"q": "ราคา 80 · VC 50 · FC 6,000 → Breakeven และกำไรถ้าขาย 300 หน่วย", "s": [["Contribution", "80 − 50 = 30"], ["Breakeven", "6,000 ÷ 30 = 200 หน่วย"], ["Profit @300", "30 × 300 − 6,000 = 3,000"]], "a": "200 หน่วย · กำไร 3,000"}]},
 {"t": "Economic Moat", "s": "ทำไมกำไรถึงอยู่ได้นาน",
  "info": cards([("Cost advantage", "ต้นทุนต่ำกว่า · Scale, Process"), ("Switching costs", "ลูกค้าเปลี่ยนเจ้าแล้วเสียเวลา/เงิน"), ("Network effects", "คนใช้มาก → มีค่ามากขึ้น"),
                 ("Intangible assets", "Brand, Patent, License"), ("Efficient scale", "ตลาดเล็ก รองรับได้ไม่กี่ราย")], 5) +
          '<div class="ct" style="margin-top:14px">ดู Moat จากตัวเลข</div>' + flow(["Margin สูงกว่าคู่แข่ง + นิ่ง", "ขึ้นราคาได้ยอดไม่หาย", "Churn ต่ำ", "AR สั้น · AP ยาว", "กำไรดีทุกปี"]) +
          eq("Moat แข็ง → กำไรสูงอยู่นาน → Cash flow มั่นคง → Value ↑ · อ้างว่ามี Moat ต้องเห็นในตัวเลข"),
  "f": [], "ex": ["Grab", [["Moat", "Network effects", "คนขับมาก → ผู้โดยสารมาก"], ["หลักฐาน", "รอรถสั้นกว่าคู่แข่ง", "ลูกค้าอยู่ต่อ"]]],
  "qs": [{"mcq": 1, "q": "บริษัทซอฟต์แวร์บัญชี ลูกค้าเลิกใช้ยากเพราะต้องย้ายข้อมูลทั้งหมด", "o": ["Cost advantage", "Switching costs", "Network effects", "Efficient scale"], "a": 1, "e": "ลูกค้าเปลี่ยนเจ้าแล้วต้องย้ายข้อมูล + เทรนใหม่ = Switching costs"}]},
 {"t": "Porter's Five Forces", "s": "อุตสาหกรรมเอื้อให้ทำกำไรไหม",
  "info": '<div class="ff"><div class="fc">Rivalry<span>คู่แข่งเยอะ + โตช้า → Price war</span></div>' + "".join(
      f'<div class="fo {p}">{t}<span>{d}</span></div>' for t, d, p in [("New entrants", "Barriers ต่ำ → คนใหม่เข้ามาแย่ง", "n"), ("Suppliers", "Supplier น้อย → กิน Margin", "w"), ("Buyers", "ลูกค้ารายใหญ่ → กดราคา", "e"), ("Substitutes", "มีทางเลือกอื่น → กดเพดานราคา", "s")]) + '</div>' +
          eq("Force ยิ่งแรง → กำไรของทั้งอุตสาหกรรมยิ่งถูกกด · ให้ระดับ Low / Moderate / High + เหตุผล"),
  "f": [], "ex": ["ร้านชานมไข่มุกในย่านที่มี 20 ร้าน", [["Rivalry", "ร้านคล้ายกันเยอะ", "High"], ["New entrants", "เปิดร้านง่าย ลงทุนน้อย", "High"], ["สรุป", "Forces แรง", "Unattractive"]]],
  "qs": [{"mcq": 1, "q": "สายการบินต้องซื้อเครื่องบินจากผู้ผลิตแค่ 2 ราย เป็น Force ไหนที่แรง", "o": ["Buyers", "Suppliers", "Substitutes", "New entrants"], "a": 1, "e": "Supplier น้อยราย → อำนาจต่อรองสูง → กิน Margin"}]},
 {"t": "Market Size", "s": "ตลาดใหญ่แค่ไหน · รายได้มีเพดานไหม",
  "info": flow([("TAM", "Demand ทั้งหมด"), ("× % → SAM", "ส่วนที่ให้บริการได้"), ("× Share → SOM", "ส่วนที่ชนะได้จริง")]) +
          eq("Revenue ceiling = Visits per day × Average ticket × Open days", "ต่อให้มี Moat ถ้าตลาดเล็ก รายได้ก็มีเพดาน"),
  "f": [["SAM", "TAM × % ที่ให้บริการได้"], ["SOM", "SAM × Market share"], ["Annual revenue", "Visits/day × Ticket × Days"]],
  "ex": ["ตลาดกาแฟ 1,000 ล้าน · ให้บริการได้ 40% · ชนะได้ 10%", [["SAM", "1,000 × 40%", "400"], ["SOM", "400 × 10%", "40 ล้าน"]]],
  "qs": [{"q": "ร้านมีลูกค้า 200 คน/วัน · ซื้อเฉลี่ย 100 บาท · เปิด 360 วัน → รายได้สูงสุดต่อปี", "s": [["คูณ 3 ตัว", "200 × 100 × 360"]], "a": "7,200,000 บาท"}]},
 {"t": "วิธีตอบข้อเขียน", "s": "Point → Evidence → Impact",
  "info": flow([("Point", "ตัดสินก่อน เช่น Strong moat"), ("Evidence", "ยกข้อมูลจากโจทย์"), ("Impact", "กระทบ Cash flow / Margin / Risk ยังไง")]) +
          tbl(["Six questions", "ดูจาก"], [["1 ลูกค้าคือใคร", "Customer Segments"], ["2 ทำไมเลือกเรา", "Value Proposition"], ["3 รายได้ / ต้นทุน", "Revenue Streams · Cost Structure"], ["4 Units work ไหม", "Contribution · Breakeven"], ["5 มี Moat จริงไหม", "5 Moat types + ตัวเลข"], ["6 ตลาด + อุตสาหกรรม", "TAM/SAM/SOM · Five Forces"]]) +
          eq("ธุรกิจดี ≠ หุ้นน่าซื้อ → ต้องดูการเงิน (บท 7) + ราคา (บท 8)"),
  "f": [], "ex": ["ตัวอย่างคำตอบ", [["Point", "The company has a strong moat (switching costs).", ""], ["Evidence", "Churn is 3% vs peers' 15%.", ""], ["Impact", "Revenue is predictable → lower risk → higher value.", ""]]],
  "qs": [{"q": "Margin ของบริษัท 35% คู่แข่ง 12% มา 5 ปี ตอบแบบ Point → Evidence → Impact", "s": [["Point", "Likely has a durable moat"], ["Evidence", "Margin 35% vs 12%, stable for 5 years"], ["Impact", "Profits likely to last → stable cash flows → value ↑"]], "a": "อ้าง Moat ต้องมีตัวเลขยืนยันเสมอ"}]},
]})

# ===== Chapter 7 =====
CH.append({"n": "7", "t": "Financial Statement Analysis", "q": "การเงินแข็งแรงไหม · ทำกำไรไหม · จ่ายหนี้ไหวไหม",
"topics": [
 {"t": "งบการเงิน 3 ตัว", "s": "แต่ละงบตอบคำถามอะไร",
  "info": cards([("Balance Sheet", "ภาพ ณ จุดเวลา · มีอะไร (Assets) เงินมาจากไหน (Liabilities + Equity)", "Assets = Liabilities + Equity"),
                 ("Income Statement", "ผลงานในช่วงเวลา · กำไรมาจากไหน", "Revenue → Net income"),
                 ("Cash Flow Statement", "เงินสดเข้า-ออกจริง · 3 กิจกรรม", "CFO + CFI + CFF")], 3) +
          vs("Current (≤ 1 ปี)", "Cash · AR · Inventory / AP · ST debt", "Long-term (> 1 ปี)", "PP&E · Intangibles / LT debt · Equity") +
          eq("Profit ≠ Cash → Depreciation หักในกำไรแต่ไม่มีเงินออก · AR ↑ = ขายได้แต่ยังไม่ได้เงิน"),
  "f": [["Balance sheet", "Assets = Liabilities + Equity"], ["NWC", "Current assets − Current liabilities"], ["Net change in cash", "CFO + CFI + CFF"]],
  "ex": ["CA 120 · CL 80", [["NWC", "120 − 80", "40"], ["อ่านผล", "บวก", "จ่ายหนี้สั้นไหว"]]],
  "qs": [{"mcq": 1, "q": "ซื้อเครื่องจักรด้วยเงินสด อยู่ในกิจกรรมไหนของ Cash flow", "o": ["CFO", "CFI", "CFF", "ไม่อยู่ใน Cash flow"], "a": 1, "e": "CapEx = ลงทุนในสินทรัพย์ระยะยาว → Investing (CFI)"}]},
 {"t": "Income Statement", "s": "หักค่าใช้จ่ายทีละชั้น",
  "info": bars([("Revenue", 100, "p", "100"), ("− COGS", 60, "c", "(60)"), ("= Gross profit", 40, "p", "40"), ("− SG&A", 20, "c", "(20)"), ("= EBITDA", 20, "p", "20"), ("− D&A", 5, "c", "(5)"), ("= EBIT", 15, "p", "15"), ("− Interest", 3, "c", "(3)"), ("= PBT", 12, "p", "12"), ("− Tax 20%", 2.4, "c", "(2.4)"), ("= Net income", 9.6, "p", "9.6")], 100) +
          eq("ถึง EBIT = กำไรของทุกคน (เจ้าหนี้ + เจ้าของ) · หลังหักดอกเบี้ย + ภาษี = ของผู้ถือหุ้น"),
  "f": [["Gross profit", "Revenue − COGS"], ["EBITDA", "Gross profit − SG&A"], ["EBIT", "EBITDA − D&A"], ["PBT", "EBIT − Interest"], ["Net income", "PBT − Tax"], ["Margin", "กำไรชั้นนั้น ÷ Revenue"], ["Growth", "(ปีนี้ − ปีก่อน) ÷ ปีก่อน"]],
  "ex": ["Revenue 100 · COGS 60 · SG&A 20 · D&A 5 · Interest 3 · Tax 20%", [["Gross profit", "100 − 60", "40"], ["EBITDA", "40 − 20", "20"], ["EBIT", "20 − 5", "15"], ["PBT", "15 − 3", "12"], ["Net income", "12 × (1 − 20%)", "9.6"], ["Gross margin", "40 ÷ 100", "40%"]]],
  "qs": [{"q": "Revenue 200 → 240 · Gross profit 80 → 90 · Margin ดีขึ้นไหม", "s": [["Revenue growth", "(240 − 200) ÷ 200 = 20%"], ["GP growth", "(90 − 80) ÷ 80 = 12.5%"], ["GPM", "80 ÷ 200 = 40% → 90 ÷ 240 = 37.5% (−2.5 pp)"]], "a": "ไม่ดีขึ้น · GP โตช้ากว่า Revenue → COGS โตเร็วกว่า"}]},
 {"t": "Liquidity Ratios", "s": "จ่ายหนี้ระยะสั้นไหวไหม",
  "info": flow([("Current ratio", "CA ÷ CL"), ("Quick ratio", "ตัด Inventory ออก"), ("Cash ratio", "เงินสดอย่างเดียว")], "ซ้าย → ขวา = เข้มขึ้นเรื่อย ๆ (ตัดสินทรัพย์ที่คล่องน้อยออก)") +
          eq("≥ 1 = จ่ายหนี้สั้นไหว · Current สูงแต่ Quick ต่ำ = พึ่ง Inventory มาก"),
  "f": [["Current ratio", "Current assets ÷ Current liabilities"], ["Quick ratio", "(Current assets − Inventory) ÷ Current liabilities"], ["Cash ratio", "Cash ÷ Current liabilities"]],
  "ex": ["CA 120 · Inventory 50 · Cash 40 · CL 80", [["Current", "120 ÷ 80", "1.50x"], ["Quick", "(120 − 50) ÷ 80", "0.88x"], ["Cash", "40 ÷ 80", "0.50x"]]],
  "qs": [{"q": "CA 90 · Inventory 35 · CL 60", "s": [["Current", "90 ÷ 60 = 1.50x"], ["Quick", "(90 − 35) ÷ 60 = 0.92x"]], "a": "Quick < 1 → ถ้าไม่ขาย Inventory จ่ายหนี้สั้นไม่พอ"}]},
 {"t": "Leverage Ratios", "s": "ใช้หนี้มากแค่ไหน · จ่ายดอกเบี้ยไหวไหม",
  "info": vs("ใช้หนี้มากแค่ไหน", "Debt ratio · D/E · Equity multiplier", "จ่ายดอกเบี้ยไหวไหม", "Interest coverage · Cash coverage") +
          eq("หนี้ ↑ → Return ผู้ถือหุ้น ↑ แต่ Risk ↑ · Coverage สูง = ปลอดภัย"),
  "f": [["Total debt ratio", "Total liabilities ÷ Total assets"], ["Debt-to-equity", "Total liabilities ÷ Equity"], ["Equity multiplier", "Assets ÷ Equity = 1 + D/E"], ["Interest coverage", "EBIT ÷ Interest"], ["Cash coverage", "EBITDA ÷ Interest"]],
  "ex": ["Assets 200 · Liabilities 120 · Equity 80 · EBIT 30 · Interest 5", [["Debt ratio", "120 ÷ 200", "60%"], ["D/E", "120 ÷ 80", "1.50x"], ["EM", "200 ÷ 80", "2.50x"], ["Interest cov.", "30 ÷ 5", "6.00x"]]],
  "qs": [{"q": "Liabilities 150 · Equity 100 · ใช้เงินสด 30 คืนหนี้ → D/E ก่อนและหลัง", "s": [["ก่อน", "150 ÷ 100 = 1.50x"], ["หลัง", "หนี้ลด 30 · Equity เท่าเดิม → 120 ÷ 100 = 1.20x"]], "a": "Leverage ลด แต่เงินสดลด → สภาพคล่องลด"}]},
 {"t": "Turnover Ratios", "s": "ใช้สินทรัพย์ทำเงินเก่งแค่ไหน",
  "info": flow([("Turnover", "กี่รอบต่อปี"), ("Days = 365 ÷ Turnover", "กี่วันต่อรอบ")]) +
          cards([("Inventory", "COGS ÷ Inventory · DIO สั้น = ของไม่จม"), ("Receivables", "Sales ÷ AR · DSO สั้น = เก็บเงินเร็ว"), ("Payables", "COGS ÷ AP · DPO ยาว = ถือเงินนาน")], 3) +
          eq("Days ยาวขึ้น → เงินสดจมใน Inventory / AR มากขึ้น"),
  "f": [["Inventory turnover", "COGS ÷ Inventory"], ["Receivables turnover", "Sales ÷ Receivables"], ["Payables turnover", "COGS ÷ Payables"], ["Days", "365 ÷ Turnover"], ["Asset turnover", "Sales ÷ Total assets"]],
  "ex": ["COGS 180 · Inventory 45 · Sales 300 · AR 25", [["Inventory turnover", "180 ÷ 45", "4.00x"], ["Inventory days", "365 ÷ 4", "91.25"], ["AR turnover", "300 ÷ 25", "12.00x"], ["Collection days", "365 ÷ 12", "30.42"]]],
  "qs": [{"q": "COGS 189 · Inventory 50 · Sales 300 · AR 30", "s": [["Inventory", "189 ÷ 50 = 3.78x → 365 ÷ 3.78 = 96.56 days"], ["AR", "300 ÷ 30 = 10.00x → 365 ÷ 10 = 36.50 days"]], "a": "ใช้ตัวเลขเต็มในเครื่อง ห้ามปัด 3.78 ก่อนหาร"}]},
 {"t": "Profitability Ratios", "s": "ทำกำไรจากยอดขาย สินทรัพย์ และทุนได้ดีแค่ไหน",
  "info": eq("ROE = ROA × Equity multiplier", "ROA = ธุรกิจเก่งแค่ไหน · EM = ใช้หนี้ขยายแค่ไหน") +
          tbl(["", "ROA", "EM", "ROE", ""], [["บริษัท X", "10%", "2x", "20%", "ธุรกิจเก่ง ✓"], ["บริษัท Y", "4%", "5x", "20%", "กู้หนัก เสี่ยง ✗"]]) +
          eq("ROE สูง ≠ ดีเสมอ → ต้องดู EM ด้วย"),
  "f": [["Gross margin", "Gross profit ÷ Sales"], ["EBITDA margin", "EBITDA ÷ Sales"], ["Net margin", "Net income ÷ Sales"], ["ROA", "Net income ÷ Total assets"], ["ROE", "Net income ÷ Equity = ROA × EM"]],
  "ex": ["NI 20 · Sales 200 · Assets 250 · Equity 100", [["Net margin", "20 ÷ 200", "10%"], ["ROA", "20 ÷ 250", "8%"], ["ROE", "20 ÷ 100", "20%"], ["เช็ก", "8% × (250 ÷ 100)", "20% ✓"]]],
  "qs": [{"q": "ROA 6% · Equity multiplier 3 → ROE?", "s": [["ROE = ROA × EM", "6% × 3 = 18%"]], "a": "18% · สูงเพราะหนี้ ไม่ใช่เพราะธุรกิจเก่ง"}]},
 {"t": "Market Value Ratios", "s": "ตลาดให้ราคาเท่าไหร่",
  "info": vs("ของผู้ถือหุ้น", "Market cap · Price · P/E · P/B → ใช้กับ Net income", "ของทั้งบริษัท", "EV · EV/EBITDA → ใช้กับ EBITDA") +
          eq("EV = Market cap + Debt − Cash", "Debt ใน EV = หนี้ที่มีดอกเบี้ยเท่านั้น (ไม่รวม AP)"),
  "f": [["EPS", "Net income ÷ Shares"], ["P/E", "Price ÷ EPS"], ["BVPS", "Equity ÷ Shares"], ["P/B", "Price ÷ BVPS"], ["Market cap", "Price × Shares"], ["Net debt", "Interest-bearing debt − Cash"], ["EV", "Market cap + Net debt"], ["EV/EBITDA", "EV ÷ EBITDA"]],
  "ex": ["NI 50 · Shares 10 · Price 60 · Equity 200 · Debt 100 · Cash 20 · EBITDA 80", [["EPS", "50 ÷ 10", "5.00"], ["P/E", "60 ÷ 5", "12.00x"], ["P/B", "60 ÷ (200 ÷ 10)", "3.00x"], ["Market cap", "60 × 10", "600"], ["EV", "600 + 100 − 20", "680"], ["EV/EBITDA", "680 ÷ 80", "8.50x"]]],
  "qs": [{"q": "Equity market value 320 · ST debt 20 · LT debt 80 · Cash 40 · EBITDA 50", "s": [["Debt", "20 + 80 = 100"], ["Net debt", "100 − 40 = 60"], ["EV", "320 + 60 = 380"], ["EV/EBITDA", "380 ÷ 50 = 7.60x"]], "a": "7.60x (Practice A5)"}]},
]})

# ===== Chapter 8 =====
CH.append({"n": "8", "t": "Valuation Analysis", "q": "หุ้นควรมีมูลค่าเท่าไหร่ · ราคาตลาดถูกหรือแพง",
"topics": [
 {"t": "EV vs Equity Value", "s": "มูลค่าของใคร",
  "info": flow([("EV", "มูลค่าทั้งธุรกิจ"), ("− Debt + Cash", "= − Net debt"), ("= Equity value", "ของผู้ถือหุ้น"), ("÷ Shares", "= Value per share")]) +
          vs("Price < Value", "Undervalued · ถูก", "Price > Value", "Overvalued · แพง") +
          eq("ได้ EV เมื่อไหร่ → หัก Net debt ก่อนหารหุ้นเสมอ"),
  "f": [["Net debt", "Debt − Cash"], ["EV", "Equity value + Net debt"], ["Equity value", "EV − Net debt"], ["Value per share", "Equity value ÷ Shares"]],
  "ex": ["EV 5,000 · Debt 1,200 · Cash 200 · หุ้น 100 · ราคา 35", [["Net debt", "1,200 − 200", "1,000"], ["Equity", "5,000 − 1,000", "4,000"], ["Per share", "4,000 ÷ 100", "40.00"], ["เทียบ", "40 > 35", "Undervalued"]]],
  "qs": [{"q": "EV 8,000 · Debt 2,500 · Cash 500 · หุ้น 200 · ราคา 32", "s": [["Net debt", "2,500 − 500 = 2,000"], ["Equity", "8,000 − 2,000 = 6,000"], ["Per share", "6,000 ÷ 200 = 30.00"]], "a": "30.00 < 32 → Overvalued"}]},
 {"t": "Comparable Companies", "s": "ดูราคาร้านข้าง ๆ",
  "info": flow([("1 Median", "Multiple ของคู่แข่ง"), ("2 × ตัวเลขเรา", "EBITDA / EPS"), ("3 แปลงเป็นราคา", "EV − Net debt ÷ หุ้น"), ("4 เทียบราคา", "Premium")]) +
          vs("EV/EBITDA", "× EBITDA → ได้ EV → ต้องหัก Net debt", "P/E", "× EPS → ได้ราคาต่อหุ้นเลย") +
          eq("Multiple มาจากคู่แข่ง · ตัวเลขที่คูณ หัก หาร มาจากบริษัทเรา"),
  "f": [["Median", "เรียงน้อย → มาก · คู่ = เฉลี่ย 2 ตัวกลาง"], ["EV", "Median EV/EBITDA × EBITDA"], ["Equity", "EV − Net debt"], ["Value per share (P/E)", "Median P/E × EPS"], ["Premium", "Value ÷ Price − 1"]],
  "ex": ["EBITDA 50 · EPS 2 · Debt 80 · Cash 30 · หุ้น 20 · ราคา 14 · Peers EV/EBITDA 6, 7, 9 · P/E 8, 10, 7", [["Median", "EV/EBITDA 7.0x · P/E 8.0x", ""], ["EV", "7 × 50", "350"], ["Equity", "350 − (80 − 30)", "300"], ["Per share", "300 ÷ 20", "15.00"], ["P/E", "8 × 2", "16.00"], ["Premium", "15 ÷ 14 − 1", "+7.14%"]]],
  "qs": [{"q": "EBITDA 40 · EPS 3 · Debt 60 · Cash 20 · หุ้น 10 · ราคา 25 · Peers EV/EBITDA 8, 5, 7 · P/E 9, 6, 11", "s": [["Median", "EV/EBITDA 7.0x · P/E 9.0x"], ["EV/EBITDA", "7 × 40 = 280 − 40 = 240 ÷ 10 = 24.00"], ["P/E", "9 × 3 = 27.00"], ["Premium (EV/EBITDA)", "24 ÷ 25 − 1 = −4.00%"]], "a": "EV/EBITDA → Overvalued · P/E → Undervalued → ตอบเป็น Range"}]},
 {"t": "FCFF", "s": "เงินสดที่ธุรกิจเหลือจริงแต่ละปี",
  "info": bars([("EBIT", 50, "p", "50"), ("− Tax (EBIT × t)", 10, "c", "(10)"), ("+ D&A", 10, "p", "10"), ("− ΔNWC", 5, "c", "(5)"), ("− CapEx", 15, "c", "(15)"), ("= FCFF", 30, "p", "30")], 50) +
          eq("ΔNWC = NWC ปีนี้ − ปีก่อน → เพิ่ม = หัก · ลด = บวก", "Tax คิดจาก EBIT ไม่ใช่ PBT"),
  "f": [["FCFF", "EBIT × (1 − t) + D&A − ΔNWC − CapEx"], ["ΔNWC", "NWC ปีนี้ − NWC ปีก่อน"], ["Operating NWC", "AR + Inventory − AP"]],
  "ex": ["EBIT 50 · D&A 10 · CapEx 15 · NWC 20 → 25 · Tax 20%", [["EBIT × (1 − t)", "50 × 0.8", "40"], ["ΔNWC", "25 − 20", "+5 → หัก"], ["FCFF", "40 + 10 − 5 − 15", "30.00"]]],
  "qs": [{"q": "EBIT 28 · D&A 18 · CapEx 38 · NWC 16 → 22 · Tax 20%", "s": [["EBIT × 0.8", "22.40"], ["ΔNWC", "22 − 16 = +6 → หัก"], ["FCFF", "22.40 + 18 − 6 − 38 = (3.60)"]], "a": "−3.60 (Practice B 2027E) · ติดลบได้ ถ้าลงทุนหนัก"}]},
 {"t": "WACC + Discount", "s": "เงินในอนาคตมีค่าน้อยกว่าเงินวันนี้",
  "info": flow([("WACC", "อัตราลดค่าเงิน"), ("DF = 1 ÷ (1 + WACC)^t", "ปีไกล = DF เล็ก"), ("PV = FCFF × DF", "รวมทุกปี")]) +
          tbl(["WACC", "DF ปี 3", "เงิน 100 ในปี 3 = วันนี้"], [["5%", "0.8638", "86.38"], ["10%", "0.7513", "75.13"], ["15%", "0.6575", "65.75"]]) +
          eq("เสี่ยงมาก → WACC ↑ → DF ↓ → PV ↓ → มูลค่า ↓"),
  "f": [["WACC", "E/V × Re + D/V × Rd × (1 − t)"], ["V", "E + D (E = Market cap)"], ["DF", "1 ÷ (1 + WACC)^t"], ["PV", "FCFF × DF"]],
  "ex": ["E 800 · D 200 · Re 11.5% · Rd 5% · Tax 20% · FCFF 44, 60.5, 66.55", [["WACC", "80% × 11.5% + 20% × 5% × 0.8", "10.0%"], ["DF", "1 ÷ 1.1, 1.1², 1.1³", "0.9091 · 0.8264 · 0.7513"], ["PV", "40 + 50 + 50", "140.00"]]],
  "qs": [{"q": "E 700 · D 300 · Re 11% · Rd 6% · Tax 20% · FCFF 50, 60, 70", "s": [["WACC", "70% × 11% + 30% × 6% × 0.8 = 9.14%"], ["DF", "0.9163 · 0.8395 · 0.7692"], ["PV", "45.81 + 50.37 + 53.85 = 150.03"]], "a": "PV รวม 150.03"}]},
 {"t": "Terminal Value → Equity", "s": "มูลค่าหลังปีสุดท้าย + รวมทุกก้อน",
  "info": flow([("TV", "EBITDA ปีสุดท้าย × Exit multiple"), ("× DF ปีสุดท้าย", "= PV of TV"), ("+ PV of FCFF", "= EV"), ("− Net debt", "= Equity"), ("÷ Shares", "= ราคาต่อหุ้น")]) +
          eq("TV เกิดปลายปีสุดท้าย → ใช้ DF ปี N ไม่ใช่ N+1", "Debt, Cash ใช้ ณ วันประเมิน · TV มักเป็น 70–80% ของ EV"),
  "f": [["TV (Exit)", "EBITDA_N × Exit multiple"], ["TV (Gordon)", "FCFF_N × (1 + g) ÷ (WACC − g)"], ["PV of TV", "TV × DF_N"], ["EV", "Σ PV FCFF + PV of TV"], ["Equity", "EV − Debt − NCI + Cash"]],
  "ex": ["ต่อจากข้อก่อน · EBITDA ปี 3 = 100 · Exit 6.0x · Debt 300 · Cash 50 · หุ้น 20", [["TV", "100 × 6.0", "600"], ["PV of TV", "600 × 0.7692", "461.53"], ["EV", "150.03 + 461.53", "611.56"], ["Equity", "611.56 − 300 + 50", "361.56"], ["Per share", "361.56 ÷ 20", "18.08"]]],
  "qs": [{"q": "Σ PV FCFF 53.85 · EBITDA 2031E 70 · Exit 4.5x · DF ปี 5 0.6209 · Debt 75 · Cash 25", "s": [["TV", "4.5 × 70 = 315.00"], ["PV of TV", "315 × 0.6209 = 195.58"], ["EV", "53.85 + 195.58 = 249.43"], ["Equity", "249.43 − 50 = 199.43"]], "a": "199.43 (Practice C)"}]},
 {"t": "เทียบราคา + สรุป", "s": "รวมผลทุกวิธี แล้วตัดสินใจ",
  "info": flow([("มูลค่าแต่ละวิธี", "DCF · EV/EBITDA · P/E"), ("ทำ Range", "Low – High"), ("เทียบราคาตลาด", "Premium"), ("สรุป", "+ เหตุผล + ข้อจำกัด")]) +
          vs("ทุกวิธี > ราคา", "Potentially Undervalued", "ทุกวิธี < ราคา", "Potentially Overvalued") +
          eq("ผลเป็นแค่ Input ไม่ใช่ Fair value ที่การันตี · Comps ขึ้นกับ Peers · DCF ขึ้นกับ Assumptions"),
  "f": [["Premium (vs ตลาด)", "Value ÷ Price − 1"], ["Asking premium", "(Asking − Estimate) ÷ Estimate"]],
  "ex": ["ผู้ขายเสนอ 220 · ประเมินได้ 180", [["ส่วนต่าง", "220 − 180", "40.00"], ["Asking premium", "40 ÷ 180", "22.22%"], ["สรุป", "Asking > Estimate", "แพงเกิน"]]],
  "qs": [{"q": "ผู้ขายเสนอ 220 · DCF ได้ 199.43", "s": [["ส่วนต่าง", "220 − 199.43 = 20.57"], ["Asking premium", "20.57 ÷ 199.43 = 10.31%"]], "a": "ราคาเสนอสูงกว่ามูลค่า DCF 10.31% (Practice D2)"}]},
]})

# ===== Chapter 9 =====
CH.append({"n": "9", "t": "Careers in Finance", "q": "เงินไหลยังไงในระบบ · ใครทำหน้าที่อะไร",
"topics": [
 {"t": "Financial System Map", "s": "เงินไหลจากคนมีเงิน → ไปหาคนใช้เงิน",
  "info": flow([("Savers / Investors", "บุคคล · Pension · Insurer"), ("Intermediaries", "Banks · Brokers · Fund managers"), ("Users of Capital", "Companies · Government · Individuals")], "Regulators คุมทั้งระบบ · ทุกจุดมี Risk, Compliance, Audit") +
          cards([("Money market", "ระยะสั้น"), ("Capital market", "หุ้น · หุ้นกู้"), ("Derivatives", "สัญญาอ้างอิง")], 3),
  "f": [["Savers / Investors", "ให้เงิน → แลก Return, Safety, Liquidity"], ["Intermediaries", "ตัวกลาง → Trust, Liquidity, Expertise"], ["Users of Capital", "กู้ หรือออก Shares / Bonds"], ["Regulators", "ตั้งกฎ + กำกับดูแล"]],
  "ex": ["คนฝากเงินธนาคาร แล้วบริษัทกู้ไปขยายโรงงาน", [["Saver", "คนฝากเงิน", ""], ["Intermediary", "ธนาคาร", ""], ["User", "บริษัท", ""]]],
  "qs": [{"mcq": 1, "q": "กองทุนบำนาญ (Pension fund) อยู่ในกลุ่มไหน", "o": ["Users of capital", "Savers / Investors", "Regulators", "Intermediaries"], "a": 1, "e": "Pension fund มีเงินก้อนใหญ่ไว้ลงทุน → Capital owner / Investor"}]},
 {"t": "การเงินในบริษัท", "s": "Users of capital · ตำแหน่งในบริษัท",
  "info": '<div class="ct">งานวนทุกเดือน</div>' + flow([("Plan", "FP&A"), ("Buy / Sell / Pay / Collect", "AR · AP · Payroll · Treasury"), ("Record", "Accounting"), ("Report", "Investor Relations")]) +
          '<div class="ct" style="margin-top:14px">โปรเจกต์ใหญ่</div>' + flow([("Identify", "Corporate Development"), ("Evaluate", "Investment Analysis"), ("Fund", "Corporate Finance / Treasury")]),
  "f": [["CFO", "หัวหน้าการเงิน · ให้คำแนะนำ CEO + Board"], ["FP&A", "Budget, Forecast, อธิบายผลต่างจากแผน"], ["Treasury", "เงินสดพอใช้ · ธนาคาร · ความเสี่ยงค่าเงิน/ดอกเบี้ย"], ["AR / AP", "เก็บเงินลูกค้า / จ่าย Supplier"], ["Investor Relations", "อธิบายผลงานให้นักลงทุน"], ["Corporate Finance", "เลือก Loan vs Bond vs Shares"]],
  "ex": ["บริษัทอยากซื้อกิจการคู่แข่ง", [["หาดีล", "Corporate Development", ""], ["ประเมินว่าคุ้มไหม", "Investment Analysis", ""], ["หาเงินมาซื้อ", "Corporate Finance", ""]]],
  "qs": [{"mcq": 1, "q": "ผลประกอบการไตรมาสนี้ต่ำกว่างบที่ตั้งไว้ ใครต้องอธิบายสาเหตุ", "o": ["Treasury", "FP&A", "Accounts Payable", "Investor Relations"], "a": 1, "e": "FP&A ทำ Budget / Forecast และอธิบายว่าทำไมผลจริงต่างจากแผน"}]},
 {"t": "Investors", "s": "ใครให้เงิน · ทีมลงทุนทำงานยังไง",
  "info": flow([("Research Analyst", "วิเคราะห์ + เสนอไอเดีย"), ("Portfolio Manager", "ตัดสินใจลงทุนเท่าไร"), ("Trader", "ส่งคำสั่ง"), ("Operations", "Confirm · Settle")], "Risk & Compliance คุมตลอดกระบวนการ") +
          vs("PE / VC", "กลยุทธ์ลงทุน · PE = บริษัทตั้งตัวแล้ว · VC = Startup", "Family Office", "องค์กร · บริหารเงินครอบครัว (ใช้ PE/VC ได้)"),
  "f": [["Retail", "Self-directed · With advice · Managed funds"], ["Pension fund", "เก็บเงินจ่ายบำนาญ"], ["Insurer", "เก็บเบี้ยจ่ายเคลม → Match assets กับ liabilities"], ["Endowment", "ใช้ทุกปีแต่ต้องอยู่ยาว"]],
  "ex": ["Analyst เสนอซื้อหุ้น A", [["เสนอ", "Research Analyst", ""], ["ตัดสินใจ", "Portfolio Manager", ""], ["ส่งคำสั่ง", "Trader", ""], ["ปิดงาน", "Operations", ""]]],
  "qs": [{"mcq": 1, "q": "ใครเป็นคนตัดสินใจขั้นสุดท้ายว่าจะลงทุนในหุ้นตัวไหน เท่าไร", "o": ["Research Analyst", "Trader", "Portfolio Manager", "Operations"], "a": 2, "e": "PM ตัดสินใจโดยดูภาพรวมทั้งพอร์ต"}]},
 {"t": "Banks & Lending", "s": "เงินกู้เดินผ่านธนาคารยังไง",
  "info": flow([("Understand", "Relationship Manager"), ("Assess", "Credit Analyst"), ("Decide", "Credit Approver"), ("Complete", "Loan Operations")]) +
          tbl(["หนี้", "หลักประกัน", "การผ่อน"], [["Credit card", "Unsecured", "Revolving"], ["Mortgage", "Secured (บ้าน)", "Installment"], ["Auto loan", "Secured (รถ)", "Installment"], ["Personal loan", "Unsecured", "Installment"]]) +
          vs("Debt Counsellor", "ฝั่งลูกหนี้ · ช่วยวางแผนผ่อน", "Restructuring Officer", "ฝั่งเจ้าหนี้ · ปรับเงื่อนไขตาม Policy ธนาคาร"),
  "f": [["Relationship Manager", "รับเรื่อง เข้าใจลูกค้า"], ["Credit Analyst", "ประเมินว่าผ่อนไหวไหม"], ["Credit Approver", "Approve / Decline / เปลี่ยนเงื่อนไข"], ["Loan Operations", "ตรวจเอกสาร ปล่อยเงิน ติดตาม"]],
  "ex": ["SME ขอกู้ 5 ล้าน", [["คุยกับลูกค้า", "RM", ""], ["ดูงบว่าจ่ายไหว", "Credit Analyst", ""], ["อนุมัติ", "Credit Approver", ""], ["ปล่อยเงิน", "Loan Operations", ""]]],
  "qs": [{"mcq": 1, "q": "บัตรเครดิตเป็นหนี้แบบไหน", "o": ["Secured + Installment", "Unsecured + Revolving", "Secured + Revolving", "Unsecured + Installment"], "a": 1, "e": "ไม่มีหลักประกัน + ยืม-คืน-ยืมใหม่ได้ในวงเงิน"}]},
 {"t": "IB · Insurance · Brokers", "s": "ตัวกลางอื่น ๆ",
  "info": cards([("Investment Banking", "Capital raising (IPO, Bonds) · M&A advisory"), ("Insurance", "Actuary ตั้งราคา → Underwriter รับประกัน → Claims จ่าย → Investment หาเงิน"), ("Brokerage", "Order → Clearing → Settlement → Custody"), ("Fintech", "Product · Engineering · Risk · Operations")], 4) +
          eq("ซื้อหุ้นใน Secondary market → เงินไปนักลงทุนคนอื่น ไม่ใช่บริษัท"),
  "f": [["Investment banker", "ช่วยระดมทุน + M&A · บริษัทเป็นคนตัดสินใจ"], ["Actuary", "ประมาณ Claims, Pricing, Reserves"], ["Underwriter", "พิจารณาใบสมัคร + เงื่อนไข"], ["Financial planner", "วางแผนการเงินรวม"], ["Investment adviser", "แนะนำการลงทุนตามเป้า + ความเสี่ยง"]],
  "ex": ["บริษัทอยาก IPO", [["ไปหา", "Investment Bank", "Capital raising"], ["เงินไปที่", "บริษัท", "Primary market"]]],
  "qs": [{"mcq": 1, "q": "นาย A ซื้อหุ้น PTT ผ่านแอปโบรกเกอร์ เงินไปถึงใคร", "o": ["บริษัท PTT", "นักลงทุนที่ขายหุ้นให้", "ก.ล.ต.", "ตลาดหลักทรัพย์"], "a": 1, "e": "Secondary market → เงินไปผู้ขาย ไม่ใช่บริษัท"}]},
 {"t": "Regulators", "s": "ใครคุมระบบ",
  "info": cards([("BOT", "ธนาคาร · ระบบชำระเงิน → Financial stability"), ("SEC (ก.ล.ต.)", "ตลาดทุน → Investor protection"), ("OIC (คปภ.)", "ประกัน → Policyholder protection"), ("SET", "ดำเนินตลาดหุ้น · อยู่ใต้ SEC")], 4) +
          flow(["Develop rules", "License", "Monitor", "Investigate", "Review"]) +
          '<div class="ct" style="margin-top:14px">ในบริษัท</div>' + cards([("Risk Management", "ประเมินความเสี่ยง"), ("Compliance", "ช่วยให้ทำตามกฎ"), ("Internal Audit", "ตรวจอิสระ")], 3),
  "f": [["Policy Analyst", "ศึกษาความเสี่ยง ร่างนโยบาย"], ["Financial Supervisor", "ตรวจว่าบริษัทคุมความเสี่ยงได้"], ["Market Surveillance", "ตรวจการซื้อขายผิดปกติ"], ["Enforcement Investigator", "สืบสวนเมื่อพบปัญหา"]],
  "ex": ["หุ้นตัวหนึ่งราคาพุ่งผิดปกติก่อนประกาศข่าว", [["ตรวจเจอ", "Market Surveillance", ""], ["สืบสวน", "Enforcement Investigator", ""], ["หน่วยงาน", "SEC / SET", ""]]],
  "qs": [{"mcq": 1, "q": "บริษัทประกันอยู่ภายใต้การกำกับของหน่วยงานไหน", "o": ["BOT", "SEC", "OIC", "SET"], "a": 2, "e": "OIC (คปภ.) ดูแลบริษัทประกัน"}]},
 {"t": "Exam Traps", "s": "จุดที่ออกสอบบ่อย",
  "info": tbl(["อย่าสับสน", "ที่ถูก"], [["ซื้อหุ้นในตลาด", "เงินไปนักลงทุนคนอื่น ไม่ใช่บริษัท"], ["Budget approved", "≠ Cash available"], ["Unusual trading", "≠ Misconduct (ต้องสืบก่อน)"], ["PE / VC", "= Strategy · Family office = Organisation"], ["Debt counsellor", "ฝั่งลูกหนี้ · Restructuring officer = ฝั่งเจ้าหนี้"], ["Credit card", "Revolving + Unsecured · Mortgage = Installment + Secured"], ["Investment banker", "แนะนำ + จัดดีล · บริษัทตัดสินใจ"]]),
  "f": [], "ex": None,
  "qs": [{"mcq": 1, "q": "รัฐบาลอนุมัติงบโครงการแล้ว หมายความว่ามีเงินสดจ่ายทันทีใช่ไหม", "o": ["ใช่ อนุมัติแล้วจ่ายได้เลย", "ไม่ใช่ ต้องมี Cash manager ดูว่ามีเงินสดพอ", "ขึ้นกับ BOT", "ขึ้นกับ SET"], "a": 1, "e": "Budget approved ≠ Cash available → Government cash manager ดูแลให้มีเงินจ่าย"}]},
]})

# ---------- render ----------
from quiz import Q, MCQ
from mcq2 import G7, G9
import json as _j
def topic_html(ch, i, tp):
    tid = f"c{ch['n']}-{i+1}"
    f = tp["f"]
    if ch["n"] == "9":
        fhead = "ตำแหน่ง · หน้าที่"
    else:
        fhead = "สูตร"
    fbox = f'<div class="box"><div class="bh">{fhead}</div><table class="ft">' + "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in f) + '</table></div>' if f else ""
    exb = ""
    if tp.get("ex"):
        t, rows = tp["ex"]
        exb = f'<div class="box"><div class="bh">ตัวอย่าง</div><p class="given">{t}</p><ol class="st">' + "".join(
            f'<li><span class="sl">{a}</span><span class="sw">{b}</span><span class="sa">{c}</span></li>' for a, b, c in rows) + '</ol></div>'
    qs = ""
    key = (ch["n"], i)
    if key in Q and ch["n"] != "7":
        z = Q[key]; qid = f"{tid}-z"
        rows = "".join(f'<li data-ans="{a}" data-dp="{dp}"><span class="ip">{p}</span><span class="iw"><input inputmode="decimal" aria-label="{e(p)}"><em>{u}</em></span><span class="mk"></span><span class="hw">{h}</span></li>' for p, a, u, h, dp in z["items"])
        qs += f'<div class="nq" id="{qid}"><div class="gv"><b>โจทย์</b>{z["g"]}</div><ol class="ni">{rows}</ol><div class="row"><button class="pri" data-chk>ตรวจคำตอบ</button><button data-show>ดูเฉลย</button><button data-reset>ลองใหม่</button><span class="sc"></span></div><p class="ans">{z["end"]}</p></div>'
    tpqs = [MCQ[key]] if key in MCQ else [q for q in tp["qs"] if q.get("mcq")] if key in Q else tp["qs"]
    if key in Q: tpqs = [q for q in tpqs if q.get("mcq")]
    if ch["n"] == "7":
        g, tpqs = G7[i]; qs = f'<div class="gv"><b>โจทย์</b>{g}</div>'
    if ch["n"] == "9": tpqs = [q for q in tp["qs"] if q.get("mcq")] + G9[i]
    for j, q in enumerate(tpqs):
        qid = f"{tid}-q{j}"
        if q.get("mcq"):
            qs += f'<div class="qz" data-a="{q["a"]}"><p class="qq">{q["q"]}</p><div class="op">' + "".join(f'<button>{chr(65+k)}. {o}</button>' for k, o in enumerate(q["o"])) + f'</div><p class="ex2">{q["e"]}</p></div>'
        else:
            qs += f'<div class="qs"><p class="qq">{q["q"]}</p><div class="row"><button class="pri" data-next="{qid}">ขั้นต่อไป</button><button data-all="{qid}">เฉลยทั้งหมด</button></div><ol class="sol" id="{qid}">' + "".join(
                f'<li><span class="sl">{a}</span><span class="sw">{b}</span></li>' for a, b in q["s"]) + f'</ol><p class="ans" id="{qid}a">{q["a"]}</p></div>'
    two = f'<div class="two">{fbox}{exb}</div>' if (fbox or exb) else ""
    return f'''<section class="tp" id="{tid}"><div class="th"><span class="tn">{ch['n']}.{i+1}</span><div><h3>{tp['t']}</h3><p>{tp['s']}</p></div></div>
<div class="info">{tp['info']}</div>{two}<div class="box try"><div class="bh">ลองทำ · {"เลือกคำตอบ" if ch["n"] in ("7","9") else "พิมพ์คำตอบแล้วกดตรวจ"}</div>{qs}</div></section>'''

def chapter_html(ch):
    toc = "".join(f'<a href="#c{ch["n"]}-{i+1}"><span>{ch["n"]}.{i+1}</span>{tp["t"]}</a>' for i, tp in enumerate(ch["topics"]))
    allf = [r for tp in ch["topics"] for r in tp["f"]]
    summ = ""
    if allf:
        summ = f'<section class="tp" id="c{ch["n"]}-sum"><div class="th"><span class="tn">∑</span><div><h3>สรุป{"ตำแหน่ง" if ch["n"]=="9" else "สูตร"}ทั้งบท</h3><p>ไว้ทวนก่อนสอบ</p></div></div><div class="box"><table class="ft">' + "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in allf) + '</table></div></section>'
    body = "".join(topic_html(ch, i, tp) for i, tp in enumerate(ch["topics"]))
    return f'''<div class="view" id="v-ch{ch['n']}"><div class="chead"><span class="big">{ch['n']}</span><div><h1>{ch['t']}</h1><p>{ch['q']}</p></div></div>
<nav class="toc">{toc}<a href="#c{ch['n']}-sum"><span>∑</span>สรุป</a></nav>{body}{summ}</div>'''

home_cards = "".join(f'<a class="hc" href="#ch{c["n"]}"><span class="big">{c["n"]}</span><b>{c["t"]}</b><p>{c["q"]}</p><ol>' + "".join(f"<li>{tp['t']}</li>" for tp in c["topics"]) + '</ol></a>' for c in CH)

tpl = open("tpl.html").read()
from practice import render as prac
out = tpl.replace("__HOME__", home_cards).replace("__CHAPTERS__", "".join(chapter_html(c) for c in CH) + prac())
open("index.html", "w").write(out)
print(len(out))
