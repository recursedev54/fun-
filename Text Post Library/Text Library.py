import tkinter as tk
from tkinter import simpledialog
from datetime import datetime
import json

def save_posts(posts, filename):
    # Function to save the posts to a JSON file
    with open(filename, "w") as f:
        json.dump(posts, f)

def load_posts(filename):
    # Function to load the posts from a JSON file
    try:
        with open(filename, "r") as f:
            posts_data = json.load(f)
            print("Posts data loaded:", posts_data)
            return posts_data
    except FileNotFoundError:
        return []

# Load the posts data
posts_catalog = load_posts("posts_catalog.json")
print("Loaded posts data:", posts_catalog)

save_posts(posts_catalog, "posts_catalog.json")

def add_post():
    # Function to add a new text post
    title = simpledialog.askstring("Input", "Enter the title for your post:")
    if title:
        content = simpledialog.askstring("Input", "Enter the content of your post:")
        if content:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            posts_catalog.append({"title": title, "content": content, "timestamp": timestamp})
            view_posts()
            save_posts(posts_catalog, "posts_catalog.json")

def delete_post(index):
    # Function to delete a text post
    if 0 <= index < len(posts_catalog):
        deleted_post = posts_catalog.pop(index)
        save_posts(posts_catalog, "posts_catalog.json")
        print("Deleted post:", deleted_post)
        view_posts()
    else:
        print("Index out of range for posts_catalog")

def edit_post(index):
    # Function to edit a text post
    if 0 <= index < len(posts_catalog):
        post_to_edit = posts_catalog[index]
        new_title = simpledialog.askstring("Edit Post", "Enter the new title for your post:", initialvalue=post_to_edit["title"])
        if new_title:
            new_content = simpledialog.askstring("Edit Post", "Enter the new content for your post:", initialvalue=post_to_edit["content"])
            if new_content:
                post_to_edit["title"] = new_title
                post_to_edit["content"] = new_content
                post_to_edit["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                save_posts(posts_catalog, "posts_catalog.json")
                view_posts()
    else:
        print("Index out of range for posts_catalog")

def view_posts():
    # Function to view all stored text posts
    for widget in frame.winfo_children():
        widget.destroy()

    for i, post in enumerate(posts_catalog):
        row = i // 2
        column = i % 2

        post_frame = tk.Frame(frame, relief=tk.GROOVE, borderwidth=2)
        post_frame.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")

        title_label = tk.Label(post_frame, text=post["title"], font=("Helvetica", 16, "bold"))
        title_label.pack(padx=5, pady=5)

        content_label = tk.Label(post_frame, text=post["content"])
        content_label.pack(padx=5, pady=5)

        timestamp_label = tk.Label(post_frame, text=post["timestamp"], font=("Helvetica", 8))
        timestamp_label.pack(padx=5, pady=5)

        edit_button = tk.Button(post_frame, text="Edit", command=lambda idx=i: edit_post(idx))
        edit_button.pack(padx=5, pady=5)

        delete_button = tk.Button(post_frame, text="Delete", command=lambda idx=i: delete_post(idx))
        delete_button.pack(padx=5, pady=5)

def on_closing():
    # Function to handle application closing
    save_posts(posts_catalog, "posts_catalog.json")
    print("Posts catalog before closing:", posts_catalog)
    root.destroy()

root = tk.Tk()
root.title("Text Post Manager")

add_button = tk.Button(root, text="Add Post", command=add_post)
add_button.pack()

frame = tk.Frame(root)
frame.pack()

view_posts()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
