
# 🔍 SHL Assessment Recommender

An AI-powered system that simplifies the selection of SHL **Individual Test Solutions** by taking natural language queries or job descriptions and returning the most relevant assessments.

---

## 🌐 Live Demo & API (Replace with your real links)

| Component         | URL                                                    |
|------------------|---------------------------------------------------------|
| 🧪 Streamlit Demo | https://your-streamlit-url.streamlit.app               |
| 🔗 API Endpoint   | https://your-render-api.onrender.com/recommend?query= |
| 💻 GitHub Repo    | https://github.com/yourusername/shl-assessment-recommender |

---

## 🎯 Features

- Accepts natural language job descriptions or queries.
- Returns **1–10 relevant SHL Individual Test Solutions**.
- Each result includes:
  - 🔗 Assessment name (linked to SHL catalog)
  - ✅ Remote Testing Support (Yes/No)
  - 🔄 Adaptive/IRT Support (Yes/No)
  - 🧪 Test Type (A, B, C, etc.)

---

## 🛠 Tech Stack

- **Python** – Core language
- **Streamlit** – Frontend
- **FastAPI** – Backend API
- **sentence-transformers** – For semantic embeddings
- **BeautifulSoup & requests** – For scraping SHL's catalog
- **NumPy** – For cosine similarity
- **Uvicorn** – ASGI server for FastAPI

---

## 🚀 Quick Start Guide

### 🧱 1. Clone the Repo

```bash
git clone https://github.com/yourusername/shl-assessment-recommender.git
cd shl-assessment-recommender

📦 2. Install Dependencies

pip install -r requirements.txt



⸻

🧪 Run the App Locally

🔹 A. Scrape SHL Assessment Data

python app/scraper.py

🔹 B. Generate Embeddings

python app/embedding_model.py

🔹 C. Start the Streamlit Frontend

streamlit run streamlit_app.py

Open browser: http://localhost:8501

🔹 D. Start the FastAPI Backend

uvicorn api.main:app --reload

Test in browser:
	•	API Endpoint: http://localhost:8000/recommend?query=Looking for Python developer
	•	Swagger Docs: http://localhost:8000/docs

⸻

🧠 Evaluation Metrics

Supports these ranking-based evaluation metrics:
	•	Mean Recall@K
	•	MAP@K (Mean Average Precision)

✅ Results are returned in descending similarity order, making it compatible with SHL’s eval framework.

⸻

🧾 Example Queries to Try
	•	I am hiring for Java developers who can collaborate with business teams.
	•	Looking for Python, SQL, and JavaScript developers within 60 minutes.
	•	Here is a JD text, can you recommend assessments under 30 minutes?
	•	I want to assess cognitive and personality traits for an analyst role.

⸻

📁 Project Structure

shl-assessment-recommender/
├── app/
│   ├── scraper.py
│   ├── recommender.py
│   ├── embedding_model.py
│   └── utils.py
├── api/
│   └── main.py
├── data/
│   ├── assessments.json
│   └── embeddings.npy
├── streamlit_app.py
├── requirements.txt
├── README.md
└── approach.pdf



⸻

🙋 Author

Built with 💡 by Shubhang Pareek
For the SHL GenAI Challenge 2025