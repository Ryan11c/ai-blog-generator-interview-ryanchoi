# AI Blog Generator 

This is a Flask application that generates SEO blog posts for any keyword. It uses mock SEO metrics and simulates OpenAI content generation. A built-in scheduler creates a blog post daily and saves it locally.

---

## Features

- `GET /generate?keyword=<your_keyword>` endpoint to generate a blog post in real-time.
- Simulates OpenAI text generation
- APScheduler runs daily blog generation and saves Markdown files.

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Ryan11c/ai-blog-generator-interview-ryanchoi.git
cd ai-blog-generator-interview-ryanchoi
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

## Running the App

### 1. Start the Flask App
```
python app.py
```

### 2. Access the Blog Generator
```
go to http://localhost:5000/generate?keyword=wireless%20earbuds
```
You’ll receive a JSON response containing:
* The keyword
* SEO metrics (mocked)
* A generated Markdown blog post

## Daily Blog Generation

The app uses APScheduler to auto-generate a blog post once every 24 hours using a fixed keyword.
