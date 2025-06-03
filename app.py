from flask import Flask, request, jsonify
from seo_fetcher import fetch_seo_data
from ai_generator import generate_blog_post
from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv
import atexit
import datetime
import os

#when i use api key
load_dotenv()

app = Flask(__name__)

@app.route('/generate', methods=['GET'])
def generate():
    keyword = request.args.get('keyword', 'wireless earbuds')
    seo_data = fetch_seo_data(keyword)
    blog_content = generate_blog_post(keyword, seo_data)

    return jsonify({
        "keyword": keyword,
        "seo": seo_data,
        "blog": blog_content
    })

def blog_generator():
    keyword = "wireless earbuds"
    seo_data = fetch_seo_data(keyword)
    blog_content = generate_blog_post(keyword, seo_data)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d")
    filename = f"blog_{keyword.replace(' ', '_')}_{timestamp}.md"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(blog_content)

    print(f"[{timestamp}] Blog post generated and saved as {filename}")

#runs the job once per day
scheduler = BackgroundScheduler()
scheduler.add_job(blog_generator, 'interval', days=1)
scheduler.start()
atexit.register(lambda: scheduler.shutdown())

if __name__ == "__main__":
    #runs the schedule for testing
    blog_generator()
    app.run(debug=True)
