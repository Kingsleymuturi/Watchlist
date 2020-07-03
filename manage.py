from app import create_app
from waitress import serve

# Creating app instance
app = create_app('development')



serve(app)
