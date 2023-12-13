from django.shortcuts import render

def index(request):
    header = 'Информация о студенте'
    student = {'study_place': 'Алабуга политех', 'group_num': "3324А",
               'specialization': 'Программирование Python',
               'after_graduation': 'Владелец бизнеса'}

    data = {'student': student}

    return render(request, 'index.html', context=data)

def about(request):
    student = {'name': 'Анисимов Артемий Михайлович', 'height': '185', 'weight': '52', 'age': 16}
    data = {'student': student}
    return render(request, 'about.html', context=data)


def contact(request, phone, social_network, address, link):
    return render(request, 'contact.html', {'phone': phone, 'social_network': social_network, 'address': address, 'link': link})

def contacts(request):
    contacts_data = [
        {'name': 'Имя1', 'email': 'email1@example.com', 'phone': '+7234567893'},
        {'name': 'Имя2', 'email': 'email2@example.com', 'phone': '+7876543216'},
    ]
    return render(request, 'contacts.html', {'contacts_data': contacts_data})
def form(request):
    return render(request, 'form.html')
