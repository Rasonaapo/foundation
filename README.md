# Jiraj Lina Por Foundation Website

A modular, CMS-ready website for the Jiraj Lina Por Foundation, built with Django and Bootstrap.  
Empowering communities through education, health initiatives, and preservation of cultural heritage.

---

## 🌟 Features

- **Dynamic Home Page** – Easily update hero text, founder images, and marquee from the admin dashboard
- **About Section** – Mission, vision, and values managed via Django Admin
- **Gallery** – Upload and manage images; set optional expiry dates
- **Board of Directors** – List board members with photos and bios
- **Contact Form** – Secure contact submissions with email support (and optional database storage)
- **Admin Dashboard** – Manage all site content and images; ready for future CMS extensions

---

## 🏗 App Structure

| App Name         | Purpose                                   |
|------------------|-------------------------------------------|
| `core`           | Home page, base templates, site-wide models, founder marquee |
| `about`          | Mission, Vision, Values                   |
| `media_gallery`  | Gallery images & marquee                  |
| `board`          | Board of Directors                        |
| `contact`        | Contact form                              |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- [Pipenv](https://pipenv.pypa.io/en/latest/) or `virtualenv` (recommended)
- Git

### Installation

1. **Clone the repo:**
    ```bash
    git clone https://github.com/YOUR_USERNAME/jirajlinaporfoundation.git
    cd jirajlinaporfoundation
    ```

2. **Set up your environment:**
    ```bash
    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    ```

3. **Configure settings:**
    - Copy `foundation/settings.example.py` to `foundation/settings.py`
    - Set your `SECRET_KEY`, `ALLOWED_HOSTS`, and database credentials

4. **Apply migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the server:**
    ```bash
    python manage.py runserver
    ```

7. **Access the site:**
    - Site: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
    - Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🗂 Project Organization

jirajlinaporfoundation/
├── core/
├── about/
├── media_gallery/
├── board/
├── contact/
├── foundation/
│ └── settings.py
├── manage.py
├── requirements.txt
└── README.md


---

## 📸 Assets

- Bootstrap template: [Bcharity by Colorlib](https://colorlib.com/wp/template/bcharity/)
- Images, logo, and content provided by the Jiraj Lina Por Foundation

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss your idea.

---

## 📜 License

This project is licensed under the MIT License – see [LICENSE](LICENSE) for details.

---

## 🙏 Credits

- Project initiated by Fredrick Tachie Mensah (originalpastorfred@gmail.com)
- Designed and built for the [Jiraj Lina Por Foundation](http://jirajlinaporfoundation.org)
- Website template by [Colorlib](https://colorlib.com/)
- Content, images, and board member profiles provided by the Foundation’s team
