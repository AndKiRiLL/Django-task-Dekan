from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import InputCaption, InputPrice, InputpathImg, InputSelect

processors = [
             {'price': '30 499', 'caption': 'Процессор AMD Ryzen 7 7700 BOX [AM5, 8 x 3.8 ГГц, L2 - 8 МБ, L3 - 32 МБ, 2 х DDR5-5200 МГц, AMD Radeon Graphics, TDP 65 Вт, кулер]', 'img': 'https://s3-alpha-sig.figma.com/img/0fee/dc42/f158c6c8e4e92c253de2b7b9066cd687?Expires=1703462400&Signature=GpWHeWuLc1qHH~~hmbyivpl557NNRwwnGpnIzIFL3gWYzozc9iSj9tZIy3qFZztXpae9EGde-LhCveo2sUGgdoIrmkgPwRQ5EisTMnSVsjPTs5zy5BVPsqvNdEPU2iIKonLlgexKgXVjo9TMaX9Echbf5oPF3jw8OApj0kEk2tvN9DU8FMeFdaJZZKM8l6Dlv3tge-Cd1ofGz2RqUa7gN9cBMEgAoIIftJa24i5ftm6phe6e4mrLkmxQow94WFSQLhK3KqGdvh84WcRs6iiBO8HpeFNmI5YKGTf4ZIZhwEwyKNb6eOgTkjNlmZlq9pktSvICSgDTF-fLFHLYCbftbg__&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4'},
             {'price': '20 699', 'caption': 'Процессор Intel Core i5-10600KF BOX [LGA 1200, 6 x 4.1 ГГц, L2 - 1.5 МБ, L3 - 12 МБ, 2 х DDR4-2666 МГц, TDP 125 Вт]', 'img': 'https://c.dns-shop.ru/thumb/st1/fit/200/200/2078f9e6892618b74eacb9385ef5156e/2916415ba132690248f3ce825118ddd804079b70adc8d88165f0e76c6624d420.jpg.webp'},
             {'price': '23 499', 'caption': 'Процессор Intel Core i7-11700F BOX [LGA 1200, 8 x 2.5 ГГц, L2 - 4 МБ, L3 - 16 МБ, 2 х DDR4-3200 МГц, TDP 65 Вт, кулер]', 'img': 'https://c.dns-shop.ru/thumb/st4/fit/200/200/470f64ff4325faca777977a861b6c2b2/9de6039b3501e2fe82f6cbfe8f85d21609fdf2a3bbf9b73e3f2cd5fe6677fa88.jpg.webp'},
             ]

video_cards = [
              {'price': '35 999', 'caption': 'Видеокарта INNO3D GeForce RTX 4060 TWIN X2 [N40602-08D6-173051N] [PCI-E 4.0 8 ГБ GDDR6, 128 бит, DisplayPort x3, HDMI, GPU 1830 МГц]', 'img': 'https://c.dns-shop.ru/thumb/st4/fit/200/200/7fe74372358a2f921149041c9fea097c/2680b7d9c50120b0504cce8ae7673c0b1d14eedeff752e897bf771a316c089b1.jpg.webp'},
              {'price': '79 999', 'caption': 'Видеокарта ASUS GeForce RTX 4070 Dual White OC Edition [DUAL-RTX4070-O12G-WHITE] [PCI-E 4.0 12 ГБ GDDR6X, 192 бит, DisplayPort x3, HDMI, GPU 1920 МГц]', 'img': 'https://c.dns-shop.ru/thumb/st4/fit/200/200/23f1a4bfe0f134af11c51d848ef1c35c/a5a61ab837e3504cd7302deba13cc25bcae9a5f8da9f4767cfa090410b237733.jpg.webp'},
              {'price': '234 999', 'caption': 'Видеокарта GIGABYTE GeForce RTX 4090 AORUS MASTER [GV-N4090AORUS M-24GD] [PCI-E 4.0 24 ГБ GDDR6X, 384 бит, DisplayPort x3, HDMI, GPU 2230 МГц]', 'img': 'https://c.dns-shop.ru/thumb/st4/fit/200/200/7e3159d124a889a379e321e67d4ae8a3/77cb98b39f342b6ff40d35645703bda3da69b76480d58cb5f941a8b4feeefbd4.jpg.webp'},
              ]

RAM = [
      {'price': '1 950', 'caption': 'Оперативная память ADATA XPG GAMMIX D10 [AX4U32008G16A-SW10] 8 ГБ [DDR4, 8 ГБx1 шт, 3200 МГц, 16-20-20]', 'img': 'https://c.dns-shop.ru/thumb/st4/fit/200/200/a2515e20cc6a46d59260faa3acc1bb03/1e7eb599c8a3d744eff4be61a487f32673780df1b97264757034a5be0060c695.jpg.webp'},
      {'price': '2 699', 'caption': 'Оперативная память Kingston FURY Beast Black RGB [KF432C16BBA/8] 8 ГБ [DDR4, 8 ГБx1 шт, 3200 МГц, 16-18-18]', 'img': 'https://c.dns-shop.ru/thumb/st4/fit/200/200/32dbe7ce1ae77e5cf03f0b3a80cf3f6b/3b4ac8101cc3637eff9e04575055f9b6c66fcf8ab9a5ac1313b6dff554fe4755.jpg.webp'},
      {'price': '7 399', 'caption': 'Оперативная память ADATA XPG Lancer RGB [AX5U5600C3616G-CLARWH] 16 ГБ [DDR5, 16 ГБx1 шт, 5600 МГц, 36-36-36]', 'img': 'https://c.dns-shop.ru/thumb/st1/fit/200/200/a5c6e2a7ff5962ac54e603b6641ccbe7/af8269207187ed046d5d52565c9b73ab5e3dd643fd66a042b91a7da3405b1aec.jpg.webp'},
      ]


def page_1(request):
    data = {'processors': processors}
    return render(request, 'Page_1.html', context = data)

def page_2(request):
    data = {'video_cards': video_cards}
    return render(request, 'Page_2.html', context = data)

def page_3(request):
    data = {'RAM': RAM}
    return render(request, 'Page_3.html', context = data)

def pageform(request):
    if request.method == "POST":

        caption = request.POST.get("caption", "Undefined")
        price = request.POST.get("price", "Undefined")
        path_img = request.POST.get("path_img", "Undefined")

        input_select = InputSelect(request.POST)
        if input_select.is_valid():
            chapter = input_select.cleaned_data['ch']

        if chapter == '1':
            processors.append({"price": price, "caption": caption, "img": path_img})
        elif chapter == '2':
            video_cards.append({"price": price, "caption": caption, "img": path_img})
        elif chapter == '3':
            RAM.append({"price": price, "caption": caption, "img": path_img})

        return HttpResponseRedirect("/")

    else:
        input_caption = InputCaption()
        input_price = InputPrice()
        input_path_img = InputpathImg()
        input_select = InputSelect()

        return render(request, 'Page_form.html', {'input_caption': input_caption, 'input_price': input_price, 'input_path_img': input_path_img, 'input_select': input_select})
