from app import create_app

app = create_app()

if __name__ == "__main__":
    # Important sur Windows pour éviter les bugs avec multiprocessing
    import os
    os.environ["FLASK_ENV"] = "development"  # optionnel : indique à Flask qu'on est en dev
    app.run(debug=True)
