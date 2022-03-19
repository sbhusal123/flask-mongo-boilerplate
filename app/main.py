from app import app
from settings import DEBUG

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=DEBUG)
