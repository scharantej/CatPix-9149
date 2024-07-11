
from flask import Flask, render_template

app = Flask(__name__)

cat_images = [
    {'id': 1, 'name': 'Whiskers', 'breed': 'Siamese', 'image': 'cat1.jpg'},
    # Add more cat data here
]

@app.route("/")
def index():
    """Homepage that displays a gallery of cat pictures."""
    return render_template("index.html", cat_images=cat_images)

@app.route("/cat/<int:cat_id>")
def cat_profile(cat_id):
    """Displays a page showcasing a single cat's picture, name, and breed."""
    cat = next((cat for cat in cat_images if cat['id'] == cat_id), None)
    if cat:
        return render_template("cat.html", cat=cat)
    else:
        return "Cat not found."

if __name__ == "__main__":
    app.run(debug=True)
