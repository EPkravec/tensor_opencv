import pytesseract
from PIL import Image
from config import *

'''
=======================================================================================================================
Данный код служит для распознавания цыфр в заданных областях документа. Используя библиотеку opencv мы из гласного 
изображения image выделяем области. для вычисления полученых сумм доходов в классе Money и количества месяцев в классе
Month используем библиотеку pytesseract, преварительно переводя заданные области (изображение) в бинарное и RGB. После 
получения "текста" убираем некорректные символы и получаем списки с данными. 

Этот способ применим только к этому документу. Для реализации к массовому подходу, необходимо применить другой способ:
выявление линий всех таблиц, разделение их на ячейки(изображения), перевод полученых изображений в банарные и считывания
с них необходимой информации для выполнения дальнейших вычислений.   
=======================================================================================================================
'''
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


class Month():
    """
    Таблицу Доходы, облагаемые по ставке 13% разбыл на две части левую и правую соответсвенно, где:
    дополнение к переменное ml - означает месяца из первой левой таблицы изображения image,
    дополнение к переменное mr - означает месяца из первой правой таблицы изображения image.


    binar_ml - переводит изображение month_left в бинарное.
    noises_ml - убираем некорретные символы из тескта с изображения month_left.

    binar_mr - переводит изображение month_right в бинарное.
    noises_mr - убираем некорретные символы из тескта с изображения month_right.
noises_r
    quantity_month - полученый результат из noises_ml и noises_mr получаем общий спикок всех месяцев и считаем их
                    колличество.
    """

    def binar_ml(month_left):
        threshold_ml = 98

        _, img_binarized_ml = cv2.threshold(month_left, threshold_ml, 196, cv2.THRESH_BINARY)
        pil_img_ml = Image.fromarray(img_binarized_ml)
        list_of_salary_amounts_ml = pytesseract.image_to_string(pil_img_ml, config=config_binar_ml_mr)

        return list_of_salary_amounts_ml

    def noises_ml(list_of_salary_amounts_ml):
        for char in list_of_salary_amounts_ml:
            if char in '[|':
                list_of_salary_amounts_ml = list_of_salary_amounts_ml.replace(char, '')

        list_of_salary_amounts_ml = list_of_salary_amounts_ml.split('\n')

        for i in list_of_salary_amounts_ml[:]:
            if i == '':
                list_of_salary_amounts_ml.remove(i)
        return list_of_salary_amounts_ml

    def binar_mr(month_right):
        threshold_mr = 90

        _, img_binarized_mr = cv2.threshold(month_right, threshold_mr, 280, cv2.THRESH_BINARY)
        pil_img_mr = Image.fromarray(img_binarized_mr)
        list_of_salary_amounts_mr = pytesseract.image_to_string(pil_img_mr, config=config_binar_ml_mr)

        return list_of_salary_amounts_mr

    def noises_mr(list_of_salary_amounts_mr):
        for char in list_of_salary_amounts_mr:
            if char in '[|':
                list_of_salary_amounts_mr = list_of_salary_amounts_mr.replace(char, '')

        list_of_salary_amounts_mr = list_of_salary_amounts_mr.split('\n')

        for i in list_of_salary_amounts_mr[:]:
            if i == '':
                list_of_salary_amounts_mr.remove(i)

        return list_of_salary_amounts_mr

    def quantity_month(list_of_salary_amounts_ml, list_of_salary_amounts_mr):
        month_list = list_of_salary_amounts_ml + list_of_salary_amounts_mr
        quantity_mon = len(set(month_list))

        return quantity_mon


class Money():
    """

        Таблицу Доходы, облагаемые по ставке 13% разбыл на две части левую и правую соответсвенно, где:
        дополнение к переменное l - означает суммы из первой левой таблицы изображения image,
        дополнение к переменное r - означает суммы из первой правой таблицы изображения image.


        rgb_l - переводит изображение table_left в RGB.
        noises_l - убираем некорретные символы из тескта с изображения table_left.

        binarized_r - переводит изображение table_right в бинарное.
        noises_r - убираем некорретные символы из тескта с изображения table_right.

        """

    def rgb_l(table_left):
        img = cv2.cvtColor(table_left, cv2.COLOR_BGR2RGB)
        list_of_salary_amounts_l = pytesseract.image_to_string(img, lang='rus')
        return list_of_salary_amounts_l

    def noises_l(list_of_salary_amounts_l):
        for char in list_of_salary_amounts_l:
            if char in '[|':
                list_of_salary_amounts_l = list_of_salary_amounts_l.replace(char, '')

        list_of_salary_amounts_l = list_of_salary_amounts_l.split('\n')

        for i in list_of_salary_amounts_l[:]:
            if i == '':
                list_of_salary_amounts_l.remove(i)

        list_of_salary_amounts_l[0] = float(list_of_salary_amounts_l[0].replace(' ', ''))
        list_of_salary_amounts_l[1] = float(list_of_salary_amounts_l[1].replace(' ', ''))
        list_of_salary_amounts_l[2] = float(list_of_salary_amounts_l[2].replace(' ', ''))
        list_of_salary_amounts_l[3] = float(list_of_salary_amounts_l[3].replace(' ', ''))
        list_of_salary_amounts_l[4] = float(list_of_salary_amounts_l[4].replace(' ', ''))
        list_of_salary_amounts_l[5] = float(list_of_salary_amounts_l[5].replace(' ', ''))
        list_of_salary_amounts_l[6] = float(list_of_salary_amounts_l[6].replace(' ', ''))

        return list_of_salary_amounts_l

    def binarized_r(table_right):
        threshold_r = 110
        _, img_binarized = cv2.threshold(table_right, threshold_r, 255, cv2.THRESH_BINARY)
        pil_img = Image.fromarray(img_binarized)
        list_of_salary_amounts_r = pytesseract.image_to_string(pil_img, lang='rus', config=config_binarized_r)

        return list_of_salary_amounts_r

    def noises_r(list_of_salary_amounts_r):
        for char in list_of_salary_amounts_r:
            if char in '[|':
                list_of_salary_amounts_r = list_of_salary_amounts_r.replace(char, '')

        list_of_salary_amounts_r = list_of_salary_amounts_r.split('\n')

        for i in list_of_salary_amounts_r[:]:
            if i == '' or i == ' ':
                list_of_salary_amounts_r.remove(i)

        list_of_salary_amounts_r[0] = float(list_of_salary_amounts_r[0])
        list_of_salary_amounts_r[1] = float(list_of_salary_amounts_r[1])
        list_of_salary_amounts_r[2] = float(list_of_salary_amounts_r[2])
        list_of_salary_amounts_r[3] = float(list_of_salary_amounts_r[3])
        list_of_salary_amounts_r[4] = float(list_of_salary_amounts_r[4])
        list_of_salary_amounts_r[5] = float(list_of_salary_amounts_r[5])

        return list_of_salary_amounts_r
