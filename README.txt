This repository is a fork of [reportlab 3.6.11](https://pypi.org/project/reportlab/) with added AES-256 PDF encryption

```
pip install reportlab2
```

**Example:**
```python
from reportlab.pdfgen import canvas

c = canvas.Canvas("encrypted.pdf")
c.drawString(100, 750, "Hello")
c.showPage()
c.setEncrypt("password")
c.save()
```
