# 📌 Multilingual FAQ System

## 🚀 Overview
The **Multilingual FAQ System** is a Django-based application that allows users to create and retrieve FAQs in multiple languages (English, Hindi, and Bengali). It features **automatic translation**, **WYSIWYG rich-text editing**, **Redis caching for performance**, and a **REST API** for easy integration.

## 🛠 Features
- ✅ **Multilingual support**: FAQs are automatically translated into Hindi and Bengali.
- ✅ **Rich text editing**: Uses CKEditor5 for formatted FAQ answers.
- ✅ **API with Django REST Framework**: Fetch FAQs in different languages.
- ✅ **Caching with Redis**: Reduces database queries and improves speed.
- ✅ **Docker Support**: Run the project with Redis using Docker.

---

## 🏗 Installation

### 1️⃣ Clone the Repository
```sh
$ git clone https://github.com/yourusername/faq_project.git
$ cd faq_project
```

### 2️⃣ Create a Virtual Environment & Activate It
```sh
# Windows
$ python -m venv venv
$ venv\Scripts\activate

# macOS/Linux
$ python3 -m venv venv
$ source venv/bin/activate
```

### 3️⃣ Install Dependencies
```sh
$ pip install -r requirements.txt
```

### 4️⃣ Run Redis Container (Required for Caching)
Ensure you have Docker installed, then run:
```sh
$ docker run -d --name redis -p 6379:6379 redis
```
If you don’t use Docker, install Redis manually and start the Redis server.

### 5️⃣ Apply Migrations & Run Server
```sh
$ python manage.py migrate
$ python manage.py runserver
```

### 6️⃣ Access the API
- Open `http://127.0.0.1:8000/api/faqs/` to view FAQs.
- Use the `lang` query parameter (`?lang=hi` or `?lang=bn`) to get translations.

---

## 🔥 API Usage

### 📌 Get All FAQs
```http
GET /api/faqs/
```
#### 🔹 Response:
```json
{
  "faqs": [
    {
      "id": 1,
      "question": "What is Django?",
      "answer": "Django is a web framework."
    }
  ]
}
```

### 📌 Get FAQs in Hindi
```http
GET /api/faqs/?lang=hi
```
#### 🔹 Response:
```json
{
  "faqs": [
    {
      "id": 1,
      "question": "Django क्या है?",
      "answer": "Django is a web framework."
    }
  ]
}
```

---

## 🧪 Running Tests
```sh
$ python manage.py test
```

---

## 📜 Contribution Guidelines
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit changes with a clear message (`git commit -m "feat: Add caching to FAQ"`).
4. Push to GitHub and create a Pull Request.

---

## 📝 Git Commit Message Format
- **feat:** Add new functionality.
- **fix:** Fix a bug.
- **docs:** Update documentation.
- **test:** Add or update tests.


Made with ❤️ by **Aditya**

