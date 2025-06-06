from flask import Flask, request, jsonify
from ai_generator import generate_blog_post
from seo_fetcher import get_seo_metrics
from utils import save_post
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

app = Flask(__name__)

# This is the keyword we'll focus on generating a blog post for every single day automatically
DAILY_KEYWORD = "wireless earbuds"

# Here a scheduler is created that runs tasks behind the scenes
scheduler = BackgroundScheduler()
scheduler.start()

@app.route('/generate', methods=['GET'])
def generate():
    # First, we grab the 'keyword' from the URL's query parameters.
    keyword = request.args.get('keyword')

    # If someone forgot to provide a keyword, we will provide a reminder.
    if not keyword:
        return jsonify({
            "error": "Oops! You need to give me a keyword like this: ?keyword=your_keyword"
        }), 400

    # Now, let's fetch some SEO info for that keyword. This could be real data or just some mocked-up numbers.
    seo_data = get_seo_metrics(keyword)

    # With the keyword and SEO info in hand, we ask the AI generator to create a blog post draft for us.
    blog_post = generate_blog_post(keyword, seo_data)

    # We will save that blog post locally with a filename that includes the current date and the keyword, so it's easy to find later.
    timestamp = datetime.now().strftime("%Y-%m-%d")
    filename = f"{timestamp}_{keyword.replace(' ', '_')}.md"
    save_post(blog_post, filename)

    # Finally a JSON response is sent back containing the keyword, the SEO info, and the generated blog post itself.
    return jsonify({
        "keyword": keyword,
        "seo_data": seo_data,
        "blog_post": blog_post
    })

def daily_job():
    """
    This function runs once every day without anyone needing to push a button.
    It generates a fresh blog post for our special daily keyword, then saves it.
    """
    seo_data = get_seo_metrics(DAILY_KEYWORD)
    blog_post = generate_blog_post(DAILY_KEYWORD, seo_data)

    timestamp = datetime.now().strftime("%Y-%m-%d")
    filename = f"{timestamp}_{DAILY_KEYWORD.replace(' ', '_')}.md"
    save_post(blog_post, filename)

    print(f"[INFO] Daily post for '{DAILY_KEYWORD}' generated and saved as {filename}")

# Schedule the daily_job function to run every 24 hours automatically.
scheduler.add_job(daily_job, 'interval', days=1)

if __name__ == "__main__":
    print("🚀 Starting the AI Blog Post Generator app...")
    app.run(debug=True)
