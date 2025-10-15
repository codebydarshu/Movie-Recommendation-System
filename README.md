# 🎬 Movie Recommendation System (Tkinter + TF-IDF)

A simple **Movie Recommendation System** built using **Python**, **Tkinter GUI**, and **TF-IDF (Text Similarity)** from **scikit-learn**.  
This application recommends movies either by **genre** or by **similar movie title** using text-based similarity.

---

## 🚀 Features

✅ Recommend movies by **genre**  
✅ Recommend similar movies by **title**  
✅ Uses **TF-IDF Vectorization** and **Cosine Similarity**  
✅ Built with a simple **Tkinter GUI**  
✅ Includes a **background image** for better visualization  

---

## 🧠 Working Methodology

1. The app creates a **movie dataset** using `pandas`.  
2. Combines **movie description** and **genre** as text features.  
3. Applies **TF-IDF Vectorization** to convert text into numerical vectors.  
4. Computes **cosine similarity** between movie features.  
5. Takes user input (title or genre) and shows top matching movies.

---

## 🧩 Flow of Execution

1. Load dataset and compute TF-IDF matrix  
2. User enters movie **title** or **genre**  
3. If genre found → recommend by genre  
4. Else → recommend by title similarity  
5. Show recommended movies in a popup window  

---

## 🖥️ GUI Preview

| Function | Screenshot |
|-----------|-------------|
| App Main Window | ![Main Window](assets/main_window.png) |
| Recommendation Popup | ![Popup](assets/popup_example.png) |

*(Place your screenshots inside an `assets/` folder and update the paths above.)*

---

## 🧰 Requirements

Make sure you have the following installed:

```bash
pip install pandas scikit-learn tkinter
