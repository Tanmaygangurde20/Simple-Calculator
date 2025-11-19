

Experiment 03  -Hello World



#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
'''


#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#








######################################################################################################3



#Matrix Multiplication

'''
import webapp2


class MultiplyHandler(webapp2.RequestHandler):
    def get(self):
        # Inbuilt matrices
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]

        # Matrix multiplication
        result = [
            [sum(a * b for a, b in zip(row, col)) for col in zip(*B)]
            for row in A
        ]

        # Format the output as HTML
        html = """
        <html>
        <head><title>Matrix Multiplication</title></head>
        <body>
            <h2>Matrix A:</h2>
            <pre>{}</pre>

            <h2>Matrix B:</h2>
            <pre>{}</pre>

            <h2>Result (A x B):</h2>
            <pre>{}</pre>
        </body>
        </html>
        """.format(format_matrix(A), format_matrix(B), format_matrix(result))

        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(html)


def format_matrix(matrix):
    # Helper function to format matrix as a string
    return '\n'.join(['\t'.join(map(str, row)) for row in matrix])


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(
            '<a href="/multiply">Click here to view Matrix Multiplication</a>'
        )


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/multiply', MultiplyHandler),
], debug=True)
'''












#############################################################################################

#N even numbers
import webapp2

class EvenNumbersHandler(webapp2.RequestHandler):
    def get(self):
        # HTML form to ask the user for n
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
        # Read n from form input
        n_str = self.request.get('n')

        try:
            n = int(n_str)
            if n <= 0:
                n = 10
        except (ValueError, TypeError):
            n = 10

        # Generate n even numbers
        even_numbers = [str(2 * i) for i in range(1, n + 1)]

        # Display result
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



######################################################################################################

Installing the GAE:

https://www.npackd.org/p/com.google.AppEnginePythonSDK/1.9.62
https://www.python.org/downloads/release/python-2712/

#########################################################################################################
Experiment -5:

!pip install tensorflow numpy pillow ultralytics opencv-python
from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt

# Load YOLOv8 model
model = YOLO("yolov8n.pt")  # small & fast model

# Load your image
image_path = "image.jpg"  # <-- replace with your image
img = cv2.imread(image_path)

# Run YOLO detection
results = model(image_path)

# Draw bounding boxes
for result in results:
    for box in result.boxes:
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        conf = float(box.conf[0])
        cls = int(box.cls[0])
        label = result.names[cls]

        # Draw box
        cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)

        # Draw label
        cv2.putText(img, f"{label} {conf:.2f}",
                    (int(x1), int(y1)-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (0, 255, 0), 2)

# Convert BGR → RGB (for notebook display)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Display image in notebook
plt.figure(figsize=(10, 10))
plt.imshow(img_rgb)
plt.axis("off")
plt.show()

###################################################################################

Ubuntu Command
C compiler :
gcc --version
sudo apt install build-essential
cd Desktop/
touch hello.c
gcc hello.c -o test
./test
