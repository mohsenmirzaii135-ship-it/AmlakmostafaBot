from database import add_house, search_price

print("🏡 سیستم املاک مصطفی")

while True:
    print("\n===================")
    print("1- ثبت ملک")
    print("2- جستجوی ملک")
    print("3- خروج")
    print("===================")

    choice = input("انتخاب: ")

    if choice == "1":
        house_type = input("نوع ملک (فروشی/رهن/اجاره): ")
        price = int(input("قیمت: "))
        area = int(input("متراژ: "))
        rooms = int(input("تعداد خواب: "))
        location = input("منطقه: ")
        description = input("توضیحات: ")
        photo = input("نام عکس: ")
        link = input("لینک آگهی: ")

        add_house(
            house_type,
            price,
            area,
            rooms,
            location,
            description,
            photo,
            link
        )

        print("✅ ملک ثبت شد.")

    elif choice == "2":
        min_price = int(input("حداقل قیمت: "))
        max_price = int(input("حداکثر قیمت: "))

        houses = search_price(min_price, max_price)

        if not houses:
            print("❌ ملکی پیدا نشد.")
        else:
            for h in houses:
                print("\n----------------------")
                print("شناسه:", h[0])
                print("نوع:", h[1])
                print("قیمت:", h[2])
                print("متراژ:", h[3])
                print("خواب:", h[4])
                print("منطقه:", h[5])
                print("توضیحات:", h[6])
                print("عکس:", h[7])
                print("لینک:", h[8])

    elif choice == "3":
        print("خروج...")
        break

    else:
        print("گزینه نامعتبر است.")