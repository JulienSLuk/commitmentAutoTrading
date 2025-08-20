# Car Listings Website

A simple website that lists cars with **price, pictures, and details**, powered by data from **Google Sheets**.  
The site is hosted for free on **GitHub Pages**, and car details can be updated easily by editing a Google Sheet (no coding required).

---

## 🚗 Features
- Car listings with images, price, and details
- Data pulled directly from Google Sheets (auto-updated)
- Supports multiple images per car (stored in `/images`)
- Mobile-friendly layout
- Contact form section

---

## 📂 Project Structure
├── index.html # Main website
├── style.css # Styling
├── script.js # Fetches data from Google Sheets Web App
├── images/ # Local images for each car
│ ├── honda/
│ │ ├── 1.jfif
│ │ ├── 2.jfif
│ └── ford/
│ ├── 1.jfif
│ └── 2.jfif
└── README.md # Project documentation



---

## 📝 How to Update Car Listings
1. Open the linked **Google Sheet** (provided to the client).  
2. Each row = 1 car listing. Suggested columns:  
   - `Name` (Car Model)  
   - `Price`  
   - `Mileage`  
   - `Color`  
   - `Year`  
   - `ImageFolder` (e.g., `honda` → pulls from `/images/honda/`)  
   - `Extra Details` (optional notes, description, etc.)  

   Example:

   | Name        | Price   | Mileage   | Color  | Year | ImageFolder | Extra Details        |
   |-------------|---------|-----------|--------|------|-------------|----------------------|
   | Honda Civic | $25,000 | 20,000 km | Blue   | 2021 | honda       | One-owner, accident free |
   | Ford Mustang| $40,000 | 15,000 km | Red    | 2022 | ford        | Sports package       |

3. The website will **automatically refresh** when you reload, pulling the latest sheet data.

---

## 🔒 Security Notes
- The site only **reads** from Google Sheets.  
- Users cannot edit the sheet via the website.  
- Anyone with the published Web App link can **see the sheet data**, so avoid storing private information (like phone numbers or emails) directly in the sheet.  
- If you need private details, keep them in a **separate private sheet** (not published).

---

## 🌐 Deployment (GitHub Pages)
1. Push this project to a GitHub repository.  
2. Go to **Settings → Pages → Build and Deployment → Source = `main` branch, root folder**.  
3. Your site will be available at:  

https://your-username.github.io/your-repo-name

4. Optional: Add a **custom domain** in GitHub Pages settings.

---

## 📞 Contact Form
The `Contact` section currently uses a basic HTML form.  
- If you want it to **send emails**, you can connect it with:
- [Formspree](https://formspree.io/) (free for small use)  
- [Google Forms](https://forms.google.com/)  
- or your own backend.

---

## ✅ Requirements
- A published Google Sheets Web App (read-only JSON output)  
- Images saved in `/images/{car_folder}`  
- GitHub account for deployment  

---

## 🚀 Quick Start
1. Clone this repo:  

git clone https://github.com/your-username/car-listings.git


Update script.js with your Google Sheets Web App URL.

Add your car images inside /images/{car_name}/.

Commit and push to GitHub.

Deploy with GitHub Pages.

⚠️ Important

Don’t publish sensitive details in the Google Sheet (e.g., seller phone numbers).

Only share the sheet for car listings data.

If you want private contact details, handle them separately.


---

👉 Do you want me to also include a **sample Google Apps Script** (the one that turns the sheet into a JSON API) inside the README, so it’s all in one place for your client?

