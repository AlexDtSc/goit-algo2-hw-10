# hw-10-1.py

# Визначення класу Teacher
class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        # Множина всіх предметів, які в принципі знає викладач
        self.can_teach_subjects = set(can_teach_subjects)
        # Множина предметів, які ми йому реально призначимо викладати
        self.assigned_subjects = set()

def create_schedule(subjects, teachers):
    # Створюємо копію предметів, які нам ще треба покрити
    uncovered_subjects = set(subjects)
    # Тут будемо зберігати вибраних викладачів
    schedule = []

    # Працюємо, поки є непокриті предмети
    while uncovered_subjects:
        best_teacher = None
        best_cover = set()

        for teacher in teachers:
            # Знаходимо, які з непокритих предметів може взяти цей викладач
            # Оператор '&' знаходить перетин двох множин (спільні елементи)
            cover = teacher.can_teach_subjects & uncovered_subjects
            
            # Якщо викладач не може взяти жодного потрібного предмета - пропускаємо його
            if not cover:
                continue

            # Якщо це перший викладач, якого ми перевіряємо, робимо його "найкращим"
            if best_teacher is None:
                best_teacher = teacher
                best_cover = cover
            else:
                # Порівнюємо з поточним "найкращим"
                # Якщо новий може покрити БІЛЬШЕ предметів
                if len(cover) > len(best_cover):
                    best_teacher = teacher
                    best_cover = cover
                # Якщо можуть покрити ОДНАКОВУ кількість предметів
                elif len(cover) == len(best_cover):
                    # Віддаємо перевагу молодшому (за умовою)
                    if teacher.age < best_teacher.age:
                        best_teacher = teacher
                        best_cover = cover

        # Якщо ми перебрали всіх і не знайшли жодного, хто може покрити залишок,
        # значить розклад скласти неможливо
        if best_teacher is None:
            return None

        # Призначаємо знайдені предмети найкращому викладачу
        best_teacher.assigned_subjects = best_cover
        # Додаємо його до нашого розкладу
        schedule.append(best_teacher)
        # Викреслюємо ці предмети зі списку непокритих (оператор '-')
        uncovered_subjects -= best_cover

    # Коли цикл while завершиться (всі предмети покриті), повертаємо розклад
    return schedule

if __name__ == '__main__':
    # Множина предметів, які треба викладати
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}
    
    # Створення списку викладачів (згідно з умовою)
    teachers = [
        Teacher("Олександр", "Іваненко", 45, "o.ivanenko@example.com", {'Математика', 'Фізика'}),
        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com", {'Хімія'}),
        Teacher("Сергій", "Коваленко", 50, "s.kovalenko@example.com", {'Інформатика', 'Математика'}),
        Teacher("Наталія", "Шевченко", 29, "n.shevchenko@example.com", {'Біологія', 'Хімія'}),
        Teacher("Дмитро", "Бондаренко", 35, "d.bondarenko@example.com", {'Фізика', 'Інформатика'}),
        Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com", {'Біологія'})
    ]

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")


# Виведення:

'''
Розклад занять:
Наталія Шевченко, 29 років, email: n.shevchenko@example.com
   Викладає предмети: Хімія, Біологія

Дмитро Бондаренко, 35 років, email: d.bondarenko@example.com
   Викладає предмети: Фізика, Інформатика

Олександр Іваненко, 45 років, email: o.ivanenko@example.com
   Викладає предмети: Математика

'''