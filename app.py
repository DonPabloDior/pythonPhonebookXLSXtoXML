from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/runcode')
def run_code():
    try:
        # Run the Python code using subprocess
        result = subprocess.check_output(['python', 'test.py'], universal_newlines=True)
        return result
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output}"

if __name__ == '__main__':
    app.run(debug=True)