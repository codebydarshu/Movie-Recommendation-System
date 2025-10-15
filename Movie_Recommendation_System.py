import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import tkinter as tk
from tkinter import messagebox

def load_dataset():
    #Creating a dataset
    data = {
        'title': [
            'The Shawshank Redemption', 'The Godfather','Sri Manjunatha', 'The Dark Knight',
            'Pulp Fiction', 'The Lord of the Rings', 'Forrest Gump', 'Inception',
            'Fight Club', 'The Matrix', 'Goodfellas'
        ],
        'description': [
            'Two imprisoned men bond over a number of years.',
            'The aging patriarch of an organized crime dynasty transfers control.',
            'Batman raises the stakes in his war on crime.',
            ' God Movie',
            'The lives of two mob hitmen, a boxer, and others intertwine.',
            'A meek Hobbit sets out on a journey to destroy a powerful ring.',
            'The presidencies of a man with a low IQ.',
            'A thief who steals corporate secrets through dream-sharing.',
            'An insomniac office worker forms an underground fight club.',
            'A computer hacker learns the true nature of his reality.',
            'The rise and fall of a mob associate.'
        ],
        'genre': [
            'Drama', 'Crime','Devotional', 'Action, Crime, Thriller', 'Crime, Thriller',
            'Adventure, Fantasy', 'Drama, Comedy', 'Sci-Fi, Thriller',
            'Drama, Thriller', 'Sci-Fi, Action', 'Crime, Drama'
        ]
    }
    return pd.DataFrame(data)

def recommend_movies_by_genre(genre, movies_df):
    """Recommend movies based on the genre."""
    genre_matches = movies_df[movies_df['genre'].str.contains(genre, case=False, regex=False)]
    if genre_matches.empty:
        return []
    return genre_matches[['title', 'genre']].values.tolist()

def recommend_movies_by_title(title, movies_df, tfidf_matrix):
    """Recommend movies based on the title."""
    try:
        idx = movies_df[movies_df['title'].str.contains(title, case=False, regex=False)].index[0]
    except IndexError:
        return []

    cosine_similarities = linear_kernel(tfidf_matrix[idx:idx+1], tfidf_matrix).flatten()
    related_indices = cosine_similarities.argsort()[-11:-1][::-1]  # Get top 10
    return movies_df.iloc[related_indices][['title', 'genre']].values.tolist()

def submit():
    """Handle submit button action."""
    user_input = entry.get()
    if not user_input:
        messagebox.showwarning("Input Error", "Please enter a movie title or genre.")
        return

    recommendations = recommend_movies_by_genre(user_input, movies_df)
    if not recommendations:
        recommendations = recommend_movies_by_title(user_input, movies_df, tfidf_matrix)

    if recommendations:
        rec_text = "\n".join([f"{title} ({genre})" for title, genre in recommendations])
        messagebox.showinfo("Recommendations", rec_text)
    else:
        messagebox.showinfo("No Results", "No similar movies or genres found.")

def exit():
    """Handle exit button action."""
    root.destroy()

# Load dataset and preprocess
movies_df = load_dataset()
movies_df['features'] = movies_df['description'] + ' ' + movies_df['genre']
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(movies_df['features'])

# Create GUI
root = tk.Tk()
root.title("Movie Recommendation System")
root.geometry("700x500")
#Background change
BG= tk.PhotoImage(file='bgimg/Bg.png')
BGL= tk.Label(image=BG).place(x=0, y=0)

# Input label and entry
label = tk.Label(root, text="Enter a movie title or genre:")
label.place(x=274,y=170)
entry = tk.Entry(root, width=29)
entry.place(x=260,y=200)

# Buttons
submit_btn = tk.Button(root, text="Search", command=submit)
submit_btn.place(x=325,y=230)
exit_btn = tk.Button(root, text="Exit", command=exit)
exit_btn.place(x=333,y=262)

root.mainloop()
