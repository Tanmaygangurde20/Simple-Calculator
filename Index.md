Here is your **cleaned, corrected, professional Markdown guide**
(`guide.md`) based on all the content you provided.

---

# ✅ **guide.md**

*(Clean, formatted, indentation-fixed, ready to submit)*

---

````markdown
# **Experiment Guide – Google App Engine + Python + Object Detection**

---

## 📘 **Experiment 03 – Hello World (Google App Engine – Python 2.7)**

```python
#!/usr/bin/env python
# Copyright 2007 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
````

---

## 📘 **Experiment 04 – Matrix Multiplication (GAE Web Application)**

```python
import webapp2

class MultiplyHandler(webapp2.RequestHandler):
    def get(self):
        # Example matrices
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]

        # Matrix multiplication logic
        result = [
            [sum(a * b for a, b in zip(row, col)) for col in zip(*B)]
            for row in A
        ]

        # HTML Output
        html = """
        <html>
        <head><title>Matrix Multiplication</title></head>
        <body>
            <h2>Matrix A:</h2>
            <pre>{}</pre>

            <h2>Matrix B:</h2>
            <pre>{}</pre>

            <h2>Result (A × B):</h2>
            <pre>{}</pre>
        </body>
        </html>
        """.format(format_matrix(A), format_matrix(B), format_matrix(result))

        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(html)


def format_matrix(m):
    return '\n'.join(['\t'.join(map(str, row)) for row in m])


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(
            '<a href="/multiply">Click here to view Matrix Multiplication</a>'
        )

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/multiply', MultiplyHandler),
], debug=True)
```

---

## 📘 **Experiment 05 – N Even Numbers (GAE Web Application)**

```python
import webapp2

class EvenNumbersHandler(webapp2.RequestHandler):
    def get(self):
        form_html = """
        <html>
        <body>
            <h2>Generate Even Numbers</h2>
            <form method="post">
                Enter value of n: <input type="number" name="n" min="1">
                <input type="submit" value="Generate">
            </form>
        </body>
        </html>
        """
        self.response.write(form_html)

    def post(self):
        n_str = self.request.get('n')

        try:
            n = int(n_str)
            if n <= 0:
                n = 10
        except:
            n = 10

        even_numbers = [str(2 * i) for i in range(1, n + 1)]

        result_html = """
        <html>
        <body>
            <h2>First {} even numbers:</h2>
            <p>{}</p>
            <br><br>
            <a href="/">Go Back</a>
        </body>
        </html>
        """.format(n, ", ".join(even_numbers))

        self.response.write(result_html)

app = webapp2.WSGIApplication([
    ('/', EvenNumbersHandler)
], debug=True)
```

---

# ⚙ **Installing Google App Engine (GAE – Python 2.7)**

Download and install the following:

* GAE Python SDK
  👉 [https://www.npackd.org/p/com.google.AppEnginePythonSDK/1.9.62](https://www.npackd.org/p/com.google.AppEnginePythonSDK/1.9.62)
* Python 2.7
  👉 [https://www.python.org/downloads/release/python-2712/](https://www.python.org/downloads/release/python-2712/)

---

# 📘 **Experiment 06 – Object Detection using YOLOv8**

## ✔ Install Required Libraries

```bash
pip install tensorflow numpy pillow ultralytics opencv-python matplotlib
```

## ✔ YOLOv8 Object Detection + Display Image (Notebook Compatible)

```python
from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt

model = YOLO("yolov8n.pt")  # Load light model

# Load image
image_path = "image.jpg"  # Replace with your image
img = cv2.imread(image_path)

# Perform detection
results = model(image_path)

# Draw bounding boxes
for result in results:
    for box in result.boxes:
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        conf = float(box.conf[0])
        cls = int(box.cls[0])
        label = result.names[cls]

        cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        cv2.putText(img, f"{label} {conf:.2f}",
                    (int(x1), int(y1)-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (0, 255, 0), 2)

# Convert BGR → RGB for Notebook
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(10, 10))
plt.imshow(img_rgb)
plt.axis("off")
plt.show()
```

---

# 🐧 **Ubuntu Commands – C Compiler Setup**

```bash
gcc --version
sudo apt install build-essential

cd Desktop/
touch hello.c
gcc hello.c -o test
./test
```

---

# ✅ **Guide Completed**

Let me know if you want:

✔ PDF version
✔ Diagram-based explanation
✔ More experiments formatted in Markdown
✔ Separate files for each experiment

```
```
