# 📄 Resume-ATS-Checker  
# 🚀 AI-Powered ATS Resume Evaluator

## 🧩 Overview  
This project is an **AI-powered Application Tracking System (ATS) Resume Evaluator** built to help job seekers optimize their resumes against specific job descriptions (JD).  
Using **Google Gemini Pro**, it provides:

- ✅ Match percentage between resume & JD  
- 🔍 Missing keyword detection  
- 📝 Actionable feedback with improvement suggestions  
- ⚙️ ATS-friendly analysis in a clean JSON-like output  

The tool is built with **Streamlit**, offering a fast, intuitive, and interactive UI.

---

## ✨ Key Features  

### 🔗 Resume–JD Matching  
Calculates an accurate match percentage between the uploaded PDF resume and the provided job description.

### 🧩 Keyword Identification  
Highlights missing keywords critical to ATS systems and required by the JD.

### 📝 Profile Summary  
Generates a detailed summary with action verbs, strengths, and improvement tips.

### 🎨 Intuitive UI  
A clean, responsive interface built using Streamlit.

---

## 🛠️ Tech Stack  

| Category         | Technology     | Version / Tool     | Purpose                                                                 |
|------------------|----------------|---------------------|-------------------------------------------------------------------------|
| Frontend/UI      | Streamlit      | streamlit           | Provides a simple, interactive web-based interface.                    |
| AI/Core Logic    | Google Gemini  | gemini-2.5-pro      | Powers resume evaluation, matching, and feedback generation.           |
| Document Parsing | PyPDF2         | PyPDF2              | Extracts raw text content from uploaded PDF resumes.                   |
| Language         | Python         | 3.8+                | Primary backend programming language.                                   |
| Configuration    | python-dotenv  | .env file           | Securely loads the `GOOGLE_API_KEY` from environment variables.         |

---

## ⚙️ Setup and Installation  

Follow the steps below to run the project locally:

### **1. Prerequisites**  
Ensure Python **3.8+** is installed.

### **2. Get Your API Key**  
Generate a Google API Key from **Google AI Studio**.

### **3. Clone the Repository**  
```bash
git clone <YOUR_REPO_URL>
cd <YOUR_REPO_NAME>
```
### **4. Create a Virtual Environment (Recommended)**  
Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
.\venv\Scripts\activate       # Windows
```

### **5. Install Dependencies**  
Install all required Python packages from requirements.txt:
```bash
pip install -r requirements.txt
```

### **6. Configure Environment Variables**  
Create a .env file in the project root and add your API key:
```bash
GOOGLE_API_KEY="YOUR_API_KEY_HERE"
```

