from backend.src.infrastructure.database.session import engine

def test_connection():
    try:
        with engine.connect():
            print("Database connected successfully!")
    except Exception as e:
        print("Database connection failed:", e)

if __name__ == "__main__":
    test_connection()