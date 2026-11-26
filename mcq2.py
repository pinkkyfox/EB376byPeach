def M(q,o,a,e): return {"mcq":1,"q":q,"o":o,"a":a,"e":e}
G7 = {  # chapter 7 → multiple choice (given data shown once per topic)
 0: ("Current assets 150 · Current liabilities 110", [
   M("NWC = ?", ["260", "40", "1.36", "−40"], 1, "NWC = CA − CL = 150 − 110 = 40"),
   M("ซื้อเครื่องจักรด้วยเงินสด อยู่ในกิจกรรมไหน", ["CFO", "CFI", "CFF", "ไม่อยู่ใน Cash flow"], 1, "CapEx = ลงทุนสินทรัพย์ระยะยาว → Investing"),
   M("จ่ายปันผลให้ผู้ถือหุ้น อยู่ในกิจกรรมไหน", ["CFO", "CFI", "CFF", "Income statement"], 2, "เงินที่จ่ายให้ผู้ให้ทุน → Financing")]),
 1: ("Revenue 200 → 240 · Gross profit 80 → 90", [
   M("Revenue growth = ?", ["16.67%", "20.00%", "40.00%", "12.50%"], 1, "(240 − 200) ÷ 200 = 20% · หารด้วยปีก่อน (16.67% คือหารด้วยปีนี้ ผิด)"),
   M("Gross margin ปี 2 = ?", ["37.50%", "40.00%", "12.50%", "45.00%"], 0, "90 ÷ 240 = 37.50%"),
   M("Gross margin เปลี่ยนไปเท่าไหร่", ["+2.50 pp", "−2.50 pp", "−12.50 pp", "ไม่เปลี่ยน"], 1, "40% → 37.5% = −2.50 pp · GP โตช้ากว่า Revenue"),
   M("EBIT คืออะไร", ["Revenue − COGS", "EBITDA − D&A", "PBT − Tax", "Gross profit − Interest"], 1, "EBIT = EBITDA − D&A = Operating profit")]),
 2: ("Current assets 90 · Inventory 35 · Cash 20 · Current liabilities 60", [
   M("Current ratio = ?", ["0.67x", "1.50x", "0.92x", "2.00x"], 1, "90 ÷ 60 = 1.50x"),
   M("Quick ratio = ?", ["0.92x", "1.50x", "0.58x", "0.33x"], 0, "(90 − 35) ÷ 60 = 0.92x · 0.58 = เอา Inventory มาหาร ผิด"),
   M("ใช้เงินสดซื้อ Inventory จะเกิดอะไร", ["ทั้ง 2 ratio ลด", "Current เท่าเดิม · Quick ลด", "Current ลด · Quick เท่าเดิม", "ทั้ง 2 ratio เท่าเดิม"], 1, "CA รวมเท่าเดิม แต่ Quick ตัด Inventory ออก")]),
 3: ("Total assets 250 · Total liabilities 150 · Equity 100 · EBIT 40 · Interest 5", [
   M("D/E = ?", ["0.60x", "1.50x", "2.50x", "0.67x"], 1, "150 ÷ 100 = 1.50x"),
   M("Equity multiplier = ?", ["1.50x", "2.50x", "0.40x", "1.67x"], 1, "250 ÷ 100 = 2.50x = 1 + D/E"),
   M("Interest coverage = ?", ["8.00x", "0.13x", "30.00x", "6.00x"], 0, "EBIT ÷ Interest = 40 ÷ 5 = 8.00x"),
   M("ใช้เงินสด 30 คืนหนี้ → D/E ใหม่", ["1.50x", "1.20x", "1.80x", "0.90x"], 1, "(150 − 30) ÷ 100 = 1.20x · Equity ไม่เปลี่ยน")]),
 4: ("COGS 189 · Inventory 50 · Sales 300 · AR 30", [
   M("Inventory turnover = ?", ["6.00x", "3.78x", "0.26x", "10.00x"], 1, "COGS ÷ Inventory = 189 ÷ 50 = 3.78x · 6.00 = ใช้ Sales ผิด"),
   M("Inventory days = ?", ["96.56", "60.83", "36.50", "189.00"], 0, "365 ÷ 3.78 = 96.56 วัน"),
   M("Collection days = ?", ["10.00", "36.50", "30.00", "96.56"], 1, "AR turnover = 300 ÷ 30 = 10 → 365 ÷ 10 = 36.50 วัน"),
   M("Inventory days เพิ่มจาก 85 เป็น 97 วัน หมายความว่า", ["ขายของเร็วขึ้น", "ขายของช้าลง · เงินจมใน Inventory มากขึ้น", "เก็บเงินลูกค้าเร็วขึ้น", "จ่าย Supplier ช้าลง"], 1, "Days ยาวขึ้น = ของอยู่ในสต็อกนานขึ้น")]),
 5: ("Net income 30 · Sales 300 · Total assets 250 · Equity 100", [
   M("ROA = ?", ["10%", "12%", "30%", "120%"], 1, "30 ÷ 250 = 12%"),
   M("ROE = ?", ["12%", "10%", "30%", "25%"], 2, "30 ÷ 100 = 30% = ROA 12% × EM 2.5"),
   M("บริษัท X: ROA 10% EM 2x · บริษัท Y: ROA 4% EM 5x · ROE เท่ากัน 20% ตัวไหนน่าลงทุนกว่า", ["X · ธุรกิจเก่งจริง", "Y · ใช้หนี้เยอะได้ผลตอบแทนเท่ากัน", "เท่ากัน", "ดู ROE อย่างเดียวพอ"], 0, "ROE ของ Y มาจากหนี้ (EM 5x) → เสี่ยงกว่า")]),
 6: ("Equity market value 320 · ST debt 20 · LT debt 80 · Trade payables 50 · Cash 40 · EBITDA 50", [
   M("Interest-bearing debt = ?", ["150", "100", "80", "200"], 1, "20 + 80 = 100 · ไม่รวม Trade payables"),
   M("EV = ?", ["380", "420", "460", "280"], 0, "320 + (100 − 40) = 380"),
   M("EV/EBITDA = ?", ["6.40x", "7.60x", "8.40x", "9.20x"], 1, "380 ÷ 50 = 7.60x"),
   M("ข้อไหนจับคู่ถูก", ["Market cap ÷ EBITDA", "EV ÷ Net income", "EV ÷ EBITDA", "Price ÷ EBITDA"], 2, "EV ↔ EBITDA (ของทุกคน) · Price ↔ EPS (ของผู้ถือหุ้น)")]),
}
G9 = {  # extra choice questions for chapter 9
 0: [M("ธนาคารรับเงินฝากแล้วปล่อยกู้ให้บริษัท ธนาคารอยู่กลุ่มไหน", ["Savers", "Intermediaries", "Users of capital", "Regulators"], 1, "ตัวกลางเชื่อมคนมีเงินกับคนใช้เงิน"),
     M("หุ้นและหุ้นกู้ซื้อขายในตลาดไหน", ["Money market", "Capital market", "Derivatives market", "Forex market"], 1, "Capital market = หุ้น + หุ้นกู้ · Money market = ระยะสั้น")],
 1: [M("ใครดูแลว่าบริษัทมีเงินสดพอจ่ายและจัดการความเสี่ยงค่าเงิน", ["FP&A", "Treasury", "Accounting", "IR"], 1, "Treasury = เงินสด + ธนาคาร + ความเสี่ยงค่าเงิน/ดอกเบี้ย"),
     M("เลือกว่าจะหาเงินด้วยเงินกู้ หุ้นกู้ หรือออกหุ้นใหม่ เป็นงานของใคร", ["Corporate Finance", "Payroll", "Accounts Receivable", "Corporate Development"], 0, "Corporate Finance เลือกวิธีระดมทุน")],
 2: [M("PE กับ VC ต่างกันยังไง", ["PE ลงทุน Startup · VC ลงทุนบริษัทใหญ่", "PE ลงทุนบริษัทที่ตั้งตัวแล้ว · VC ลงทุนธุรกิจเริ่มต้น", "เหมือนกัน", "PE เป็นองค์กร · VC เป็นกลยุทธ์"], 1, "PE = Established · VC = Early-stage / growth"),
     M("Family office คืออะไร", ["กลยุทธ์ลงทุนแบบหนึ่ง", "องค์กรที่บริหารความมั่งคั่งของครอบครัว", "ธนาคารพาณิชย์", "หน่วยงานกำกับ"], 1, "Family office = Organisation (ใช้ PE/VC เป็นกลยุทธ์ได้)")],
 3: [M("ใครประเมินว่าผู้กู้ผ่อนไหวไหม", ["Relationship Manager", "Credit Analyst", "Loan Operations", "Debt Counsellor"], 1, "Credit Analyst ประเมิน Repayment capacity"),
     M("Debt counsellor อยู่ฝั่งไหน", ["ฝั่งเจ้าหนี้", "ฝั่งลูกหนี้", "ฝั่งหน่วยงานกำกับ", "ฝั่งโบรกเกอร์"], 1, "Debt counsellor ช่วยลูกหนี้ · Restructuring officer อยู่ฝั่งเจ้าหนี้")],
 4: [M("ใครตั้งราคาเบี้ยประกันและประมาณการเคลม", ["Underwriter", "Actuary", "Claims specialist", "Broker"], 1, "Actuary = Claims, Pricing, Reserves"),
     M("Investment banker ช่วยบริษัท IPO ใครตัดสินใจขั้นสุดท้าย", ["Investment banker", "บริษัท", "SEC", "นักลงทุน"], 1, "Banker แนะนำ + จัดดีล · บริษัทตัดสินใจ")],
 5: [M("ใครดูแลธนาคารและระบบชำระเงิน", ["SEC", "BOT", "OIC", "SET"], 1, "BOT = Financial stability"),
     M("ระบบตรวจพบการซื้อขายผิดปกติ ขั้นต่อไปคืออะไร", ["ลงโทษทันที", "สืบสวนก่อน (Enforcement)", "ปิดตลาด", "ไม่ต้องทำอะไร"], 1, "Unusual trading ≠ Misconduct ต้องสืบสวนก่อน")],
 6: [M("Mortgage เป็นหนี้แบบไหน", ["Unsecured + Revolving", "Secured + Installment", "Unsecured + Installment", "Secured + Revolving"], 1, "มีบ้านเป็นหลักประกัน + ผ่อนเป็นงวด"),
     M("PE / VC คือ ___ ส่วน Family office คือ ___", ["Organisation · Strategy", "Strategy · Organisation", "Regulator · Investor", "Bank · Fund"], 1, "PE/VC = Strategy · Family office = Organisation")],
}
