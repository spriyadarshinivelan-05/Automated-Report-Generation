# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
# Data create
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Sales": [12000, 15000, 10000, 18000]
}
df = pd.DataFrame(data)
df
# Analysis 
total = df["Sales"].sum()
average = df["Sales"].mean()
print("Total Sales:", total)
print("Average Sales:", average)
# Graph create
plt.plot(df["Month"], df["Sales"], marker='o')
plt.title("Monthly Sales Report")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.savefig("sales.png")
plt.show()
# Automatic PDF Report Generated
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=14)
pdf.cell(200, 10, "AUTOMATED SALES REPORT", ln=True, align='C')
pdf.ln(10)
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, f"Total Sales: {total}", ln=True)
pdf.cell(200, 10, f"Average Sales: {average}", ln=True)
pdf.ln(10)
pdf.cell(200, 10, "Monthly Data:", ln=True)
for i in range(len(df)):
    pdf.cell(200, 10, f"{df.Month[i]} : {df.Sales[i]}", ln=True)
pdf.image("sales.png", x=10, y=120, w=180)
pdf.output("Automated_Report.pdf")
