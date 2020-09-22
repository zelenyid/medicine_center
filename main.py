from app.database.patient import Patient


if __name__ == '__main__':
    print(Patient.collection_name)
    # print(Patient.insert_obj({'name': 'name', 'phone_number': 38013213}))
    print(Patient.get_all_objects())
