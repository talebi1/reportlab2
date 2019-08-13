This repository is a fork of [reportlab](https://bitbucket.org/rptlab/reportlab/src/default/) with added AES-256 PDF encryption

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

