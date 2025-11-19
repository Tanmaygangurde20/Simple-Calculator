from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML form
html_template = """
<h2>Google App Engine Demo</h2>
<p>Select Operation:</p>
<form method="post" action="/">
    <label>Choose Task:</label>
    <select name="task">
        <option value="even">Generate Even Numbers</option>
        <option value="matrix">Multiply Two Matrices</option>
    </select><br><br>
    
    <label>Enter n (for even numbers):</label>
    <input type="text" name="n"><br><br>
    
    <label>Matrix 1 (comma-separated rows):</label><br>
    <textarea name="matrix1" rows="3" cols="30"></textarea><br><br>
    
    <label>Matrix 2 (comma-separated rows):</label><br>
    <textarea name="matrix2" rows="3" cols="30"></textarea><br><br>
    
    <input type="submit" value="Submit">
</form>

<hr>
<h3>Output:</h3>
<p>{{ result }}</p>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""
    if request.method == 'POST':
        task = request.form.get('task')

        # Task 1: Generate even numbers
        if task == "even":
            n = int(request.form.get('n', 0))
            result = [i for i in range(2, 2*n+1, 2)]
        
        # Task 2: Matrix multiplication
        elif task == "matrix":
            try:
                A = [[int(x) for x in row.split()] for row in request.form['matrix1'].strip().split(',')]
                B = [[int(x) for x in row.split()] for row in request.form['matrix2'].strip().split(',')]
                
                if len(A[0]) != len(B):
                    result = "Error: Incompatible matrix sizes for multiplication."
                else:
                    C = [[sum(a*b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]
                    result = C
            except Exception as e:
                result = f"Error: {e}"
                
    return render_template_string(html_template, result=result)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
