import cv2

'''
=======================================================================================================================
Данный код настройки и входные данные для выбора областей и распорзновая цыфр.
=======================================================================================================================
'''


# исходное изображение
image = cv2.imread('wo_personal.jpg')

# Выделяем необходимые области для распознования интересующей информации
month_left = image[598:795, 110:135]
month_right = image[598:795, 789:814]
table_left = image[598:778, 329:425]
table_right = image[598:760, 960:1075]

# Критерии распознования цыфр
config_binar_ml_mr = '--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789'
config_binarized_r = 'outputbase digits'
