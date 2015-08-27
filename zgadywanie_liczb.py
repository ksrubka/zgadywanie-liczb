import random

'''Program do zgadywania liczb:

- użytkownik podaje liczbę maksymalną (int_max),
- program losuje liczbę do zgadnięcia, która mieści się w zakresie od 0 do max,
- użytkownik zgaduje jaką liczbę program wylosował.
- Program liczy w ilu próbach to się użytkownikowi udało
  i wypisuje liczbę prób,
- jeśli liczba prób do zgadnięcia liczby jest mniejsza niż w poprzednich razach
  to program wypisuje, że padł rekord,
- po zakończeniu zgadywania program pyta czy użytkownik chce zgadywać jeszcze
  raz nowo wylosowaną liczbę, czy zakończyć. '''

text = ''
rekord = 100
print('Witaj')
while text.lower() != 'nie':

    maks = input('\nWymyśl i podaj liczbę maksymalną (większą od zera): ')
    
    # sprawdzam czy maks jest liczbą
    is_digit = maks.isdigit()
    if is_digit == False:
        print('To jednak musi być liczba')
        continue

    # sprawdzam czy maks nie jest zerem lub ''
    is_true = bool(maks)
    if is_true == False:
        continue
    
    int_max = int(maks)
    if int_max == 0:
        liczba = random.randint(0, int_max)
    else:
        liczba = random.randint(1, int_max)
        
    zgadnij = 0
    licznik_prob = 0
    int_zgadnij = 0
    
    while int_zgadnij != liczba:
        zgadnij = input('Zgadnij jaką liczbę wylosowałem? ')
        licznik_prob += 1
        
        # sprawdzam czy wpisano liczbę
        is_int = zgadnij.isdigit()
        if is_int == False:
            print('Niestety nie zgadłeś\nTo jednak musi być liczba')
            continue
        
        int_zgadnij = int(zgadnij)
        if int_zgadnij == liczba:
            print('Zgadłeś! Wylosowałem', liczba)
            if licznik_prob < rekord:
                print('Padł rekord!')
                rekord = licznik_prob
            print('Udało Ci się zgadnąć po %d próbach' % licznik_prob)
            text = input('Czy chcesz zagrać jeszcze raz? (tak/nie) ')
        elif int_zgadnij != liczba:
            print('Niestety, nie zgadłeś')
            if int_zgadnij < liczba:
                print('Wylosowana liczba jest większa')
            elif int_zgadnij > liczba:
                print('Wylosowana liczba jest mniejsza')
            
                

        
