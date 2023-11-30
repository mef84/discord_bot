import random
from datetime import date
from requests import get
from time import sleep



def get_response(message: str) -> str:
    p_message = message.lower()

    answers = [f"Cześć, co słychać! :)", f"No hej!", f"Siemanko!", f"No pozdrawiam!"]
    if p_message in ['hey bot hello', 'hey bot cześć']:
        return random.choice(answers)

    if p_message in ['hey bot co u ciebie']:
        return "w porządku! Pamiętaj, że jestem tylko BOTem więc zawsze mam się SUPER!"

    if p_message == 'hey bot jaka jest pogoda':
        response = get('https://danepubliczne.imgw.pl/api/data/synop')
        for city in response.json():
            if city['stacja'] == 'Katowice':
                date_measurement = city['data_pomiaru']
                station_name = city['stacja']
                temperature = city['temperatura']
                pressure = city['cisnienie']
        return f'Obecnie jest {temperature} stopni, a ciśnienie atmosferyczne to {pressure} hp'

    if p_message =='hey bot jaki jest dzień':
        now = date.today()
        today = now.strftime("%d.%m.%Y")
        day_of_week = date.weekday(now)

        days_of_week = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"]
        weekday_name = days_of_week[day_of_week]
        current_day = days_of_week[day_of_week]
        return f'Dzisiaj jest {current_day}, a data to {today}.'

    if p_message == 'hey bot kostka':
        roll = str(random.randint(1, 6))
        return f'Rzucasz kostką! Wyrzuciłeś: {roll}'


    if 'hey bot ile jest' in p_message:
        try:
            result = eval(p_message[16:].replace(',', '.'))
            return f"Wynik operacji: {result}"
        except Exception:
            return f'Błąd: Nie wpisałeś żadnych wartości!!'

    if 'hey bot policz do' in p_message:
        try:
            number = int(p_message[17:])
            if number > 0:
                counter = 1
                digits = [str(counter) for counter in range(1, number+1)]
                return '\n'.join(digits)
        except ValueError:
            return 'Błąd: Nie wpisałeś poprawnej liczby!!'


    if p_message == 'help':
        return "`Oto komendy jakie można użyć: \n1) hey bot jaka jest pogoda - Wyświetla aktualną pogodę\n2) hey bot cześć - Przywitaj się\n3) hey bot policz do (np. hey bot policz do 10)\n4) hey bot ile jest (np. hey bot ile jest 2+2)\n5) hey bot kostka - rzucasz kostką!\n6) hey bot jaki jest dzień - sprawdza jaki jest dzisiaj dzień\n7) hey bot co u ciebie - interakcja z botem`"

