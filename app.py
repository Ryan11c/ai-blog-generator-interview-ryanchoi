from flask import Flask, request, jsonify
from seo_fetcher import fetch_seo_data
from ai_generator import generate_blog_post
from apscheduler.schedulers.background import BackgroundScheduler
import atexit
import datetime

app = Flask(__name__)

#generate url
@app.route('/generate', methods=['GET'])
def generate():
    keyword = request.args.get('keyword', 'wireless earbuds')
    seo_data = fetch_seo_data(keyword)
    content = generate_blog_post(keyword, seo_data)
    return jsonify({
        "keyword": keyword,
        "seo": seo_data,
        "blog_html": content
    })

#scheduled job to run daily
def scheduled_blog_generation():
    keyword = "wireless earbuds"
    seo_data = fetch_seo_data(keyword)
    content = generate_blog_post(keyword, seo_data)

    #saving to file
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    filename = f"blog_{keyword.replace(' ', '_')}_{now}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[{now}] Generated blog for: {keyword} saved as {filename}")

#starting the scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(scheduled_blog_generation, 'interval', days=1)
scheduler.start()
atexit.register(lambda: scheduler.shutdown())

if __name__ == "__main__":
    #runs the schedule for testing
    scheduled_blog_generation()
    app.run(debug=True)
