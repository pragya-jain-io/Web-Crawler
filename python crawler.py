from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

app = Flask(__name__)

# Helper function to extract links from a page
def extract_links(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        return [urljoin(url, a['href']) for a in soup.find_all('a', href=True)]
    except requests.RequestException:
        return []

# Recursive function to crawl pages
def crawl(url, depth, crawled):
    if depth == 0 or url in crawled:
        return
    links = extract_links(url)
    crawled[url] = links
    for link in links:
        crawl(link, depth - 1, crawled)

@app.route('/api/crawl', methods=['POST'])
def crawl_endpoint():
    data = request.json
    root_url = data.get('root_url')
    depth = data.get('depth', 1)
    
    if not root_url:
        return jsonify({'error': 'root_url is required'}), 400
    
    crawled = {}
    crawl(root_url, depth, crawled)
    
    return jsonify({
        'root_url': root_url,
        'crawled_links': crawled
    })

if __name__ == '__main__':
    app.run(debug=True)
