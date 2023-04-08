from . import create_app

# filtered the main app in __init__.py
app = create_app()

if __name__ == '__main__':
    app.run()