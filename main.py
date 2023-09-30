from backend.app import App
from initializer.initializer import initializeDatabase


if __name__ == "__main__":
    initializeDatabase()
    app = App()
    app.run()
