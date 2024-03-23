from flask import Flask, render_template, request, jsonify

from search import search_keywords

from crawling import create_crawler

app = Flask(__name__)


@app.route('/')
def index():
    message = "Hello from Flask!"
    return render_template('index.html', message=message)

# Coté test utilisateur

@app.route('/crawler', methods=['POST'])
def handle_crawler_submission():
    url = request.form.get('url')
    print(url)
    data = create_crawler(url,25)
    
    return jsonify({"data": data, 'ok': True})

@app.route('/keywordingClient', methods=['POST'])
def handle_form_submissionClient():
    keyword = request.form.get('crawler-key')
    results = search_keywords(keyword,'./clientkeywords.csv','./clientwebpages.csv')
    if len(results) == 0:
        print("No results found")
        return jsonify({"error": "No results found"})
    print(results)
    return jsonify(results)

# Nos datas

@app.route('/keywording', methods=['POST'])
def handle_form_submission():
    keyword = request.form.get('key')
    results = search_keywords(keyword,'./data/keywords.csv','./data/webpages.csv')
    if len(results) == 0:

        return jsonify({"error": "No results found"})
    return jsonify(results)



if __name__ == '__main__':
    app.run()
