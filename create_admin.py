from app import create_app, db
from app.models import User, Room

app = create_app()

with app.app_context():
    # Création de l'admin s'il n'existe pas
    if not User.query.filter_by(username='admin').first():
        admin = User(username='admin', role='admin')
        admin.set_password('admin123')
        db.session.add(admin)
        print("✅ Admin créé.")
    else:
        print("ℹ️ Admin existe déjà.")

    # Création de 4 salles si elles n'existent pas
    room_names = ['Salle A', 'Salle B', 'Salle C', 'Salle D']
    for name in room_names:
        if not Room.query.filter_by(name=name).first():
            db.session.add(Room(name=name))
            print(f"✅ Salle '{name}' ajoutée.")
        else:
            print(f"ℹ️ Salle '{name}' existe déjà.")

    db.session.commit()
