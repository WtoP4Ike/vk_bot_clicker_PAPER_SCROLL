tokenVK="0" #токен вк
tokenPS="0" #токен PS
idmPS="0" #номер магазина PS
owner_1="0" #ЦИФРОВОЕ ID вк владельца
group_id="0" #ID сообщества
get_bal1="""0"""
get_bal2="""0"""
"""
В переменные get_bal нужно написать часть ответа от API PS.
Получить ответ можно запустив файл get_p.
Пример полученного кода:
[{'merchant_id': 9284, 'owner_id': ТУТ ID ВЛАДЕЛЬЦА, 'group_id': 218479839, 'name': 'AdVeLSert | КЛИКЕР PS 2023', 'avatar': 'https://sun9-85.userapi.com/impg/8zpchcmE8vHkPbMOlQjWqbGiZS04IL5YwputjA/UfXTXuuBbx8.jpg?size=1400x1050&quality=95&sign=f53b2d1592d62e79f9185cba6b64a41b&type=album', 'balance': 1165272029000, 'create_date': 1674674022}]

В переменную get_bal1 записать ТУ ЧАСТЬ КОДА, полученную в файле get_p.py:
мой пример:
<'merchant_id': 9284, 'owner_id': ТУТ ID ВЛАДЕЛЬЦА, 'group_id': 218479839, 'name': 'AdVeLSert | КЛИКЕР PS 2023', 'avatar': 'https://sun9-85.userapi.com/impg/8zpchcmE8vHkPbMOlQjWqbGiZS04IL5YwputjA/UfXTXuuBbx8.jpg?size=1400x1050&quality=95&sign=f53b2d1592d62e79f9185cba6b64a41b&type=album', 'balance': > (без кавычек)
В переменную get_bal2 так-же как и в get_bal1, мой пример:
<, 'create_date': 1674674022> (без кавычек)
"""
user_agreement="https://vk.com/@clickerpscroll-ps" #ссылка на пользовательское соглашение