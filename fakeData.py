import faker
fake = faker.Faker("ja_JP")
for i in range(50):
    print(fake.name())
    # print(fake.name_female())
    # print(fake.country())
    # print(fake.emoji())
    # print(fake.language_name())
    # print(fake.language_code())
