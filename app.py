from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_FORM = """
<h2>Standard Laptop Order - IT Procurement</h2>
<form method="POST" action="/order">
  Employee ID: <input name="emp_id" required><br><br>
  Laptop Model:
  <select name="model">
    <option>Dell Latitude 5430 - Rs.75000</option>
    <option>Lenovo ThinkPad E14 - Rs.68000</option>
    <option>HP EliteBook 840 - Rs.72000</option>
  </select><br><br>
  Quantity: <input type="number" name="qty" value="1"><br><br>
  Justification: <textarea name="just"></textarea><br><br>
  <button type="submit">Submit Request (Triggers Flow)</button>
</form>
"""

@app.route('/')
def home():
    return render_template_string(HTML_FORM)

@app.route('/order', methods=['POST'])
def order():
    emp_id = request.form['emp_id']
    model = request.form['model']
    # Trigger Flow Designer simulation
    from flow_designer_main import FlowDesigner
    flow = FlowDesigner()
    result = flow.trigger_catalog_request({
        "number": "RITM0010002",
        "user": emp_id,
        "manager": "hod@company.com",
        "item": model,
        "price": 75000
    })
    return f"<h3>Flow Completed!</h3><p>PO: {result['po_number']}</p><p>Vendor: {result['vendor']['name']}</p>"

if __name__ == '__main__':
    app.run(debug=True)