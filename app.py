from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>Simple Flask App with XSS Vulnerability</h1>
        <form action="/search" method="GET">
            <label for="query">Search:</label>
            <input type="text" id="query" name="query">
            <button type="submit">Submit</button>
        </form>
    '''

@app.route('/search')
def search():
    query = request.args.get('query', '')
    # Vulnerable code: directly embedding user input into HTML without sanitization
    html = f"""
        <h1>Search Results</h1>
        <p>You searched for: {query}</p>
        <a href="/">Go back</a>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)