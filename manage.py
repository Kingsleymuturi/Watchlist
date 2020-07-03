from app import create_app
from app.models import Movie, Review
from waitress import serve


# Creating app instance
app = create_app('development')

@app.shell_context_processor
def make_shell_context():
    """Makes the shell context, allowing for specific variables, and classes
       to be known by the interactive Python session on startup."""
    return {'Movie': Movie, 'Review': Review}


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=800)
