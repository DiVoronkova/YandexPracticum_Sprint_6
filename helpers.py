from faker import Faker


faker = Faker('ru_RU')

stations = ['Черкизовская', 'Бульвар Рокоссовского', 'Преображенская площадь', 'Сокольники', 'Красносельская', 'Комсомольская', 'Красные Ворота', 'Чистые пруды']

# Генерирует рандомные данные для регистрации
def generate_random_credentials():
    name = faker.first_name()
    surname = faker.last_name()
    street = faker.street_name()      # «ул. Ленина»
    house = faker.random_int(1, 999)
    address = f"{street}, {house}"
    phone = '+7' + faker.numerify('###########')
    date_obj = faker.future_datetime(end_date="+30d")  # Будущая дата
    date = date_obj.strftime("%d.%m.%Y")
    comment = faker.text(max_nb_chars=10)
    return name, surname, address, phone, date, comment
