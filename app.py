from flask import Flask, render_template, request, redirect, url_for, flash

# Initialize the Flask application
app = Flask(__name__)
# Set a secret key for session management and flashing messages
app.secret_key = 'modern_bahay_kubo_secret'


# --- Product Details Route (Provided by user) ---
@app.route('/product-details')
def product_details():
    """Renders the product details page which contains the inquiry form."""
    # This route is correctly linked to render the product_details.html template
    return render_template('product_details.html')


# --- Inquiry Submission Route (Provided by user) ---
@app.route('/submit-inquiry', methods=['POST'])
def submit_inquiry():
    """Handles the POST request from the inquiry form."""
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    inquiry = request.form.get('inquiry')

    # In a real application, you would:
    # 1. Validate data (e.g., check for required fields, validate email format)
    # 2. Save to database (e.g., PostgreSQL, SQLite)
    # 3. Send a confirmation email
    print(f"--- New Inquiry Received ---")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Phone: {phone if phone else 'N/A'}")
    print(f"Message: {inquiry}")
    print(f"--------------------------")

    # Flash a message to be displayed on the redirected page
    flash('Thank you! Your inquiry has been submitted successfully. We will be in touch shortly.', 'success')

    # Redirect back to the product details page
    return redirect(url_for('product_details'))


# --- Placeholder Routes for Navigation (Referenced in HTML) ---

@app.route('/')
def home():
    """The main homepage, redirects to product details for this example."""
    # Since all content is in one file for this example, we redirect to the main view
    return redirect(url_for('product_details'))


@app.route('/products')
def products():
    """Placeholder for the products page."""
    flash('This is the Products page - showcasing all our modern Bahay Kubo models.', 'info')
    return redirect(url_for('product_details'))


@app.route('/about')
def about():
    """Placeholder for the about page."""
    flash('This is the About Us page - learn about our vision and sustainability pledge.', 'info')
    return redirect(url_for('product_details'))


@app.route('/contact')
def contact():
    """Placeholder for the general contact page."""
    flash('This is the Contact Us page - reach out to our team for partnerships.', 'info')
    return redirect(url_for('product_details'))


if __name__ == '__main__':
    # Flask apps are usually run using `flask run` in production,
    # but this is useful for local development outside the environment.
    app.run(debug=True)



