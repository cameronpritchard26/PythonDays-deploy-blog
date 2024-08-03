# This file is the entry point for the Flask application. It imports the app object from the blog_package package and runs the application on port 5003. The debug mode is enabled to help with development.
from blog_package import app
from blog_package import routes

if __name__ == "__main__":
    app.run(debug=False, port=5001)