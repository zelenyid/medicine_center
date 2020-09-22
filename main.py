from app.database.patient import Patient


if __name__ == '__main__':
    print(Patient.collection_name)
    print(Patient.insert_obj({'name': 'qwerty', 'phone_number': 6419836}))
    print(Patient.get_all_objects())
