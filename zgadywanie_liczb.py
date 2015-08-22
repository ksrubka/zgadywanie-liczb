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
rekord = [100]
while text.lower() != 'nie':
    
    int_max = int(input('Wymyśl i podaj liczbę maksymalną (Proszę, tylko nie zero): '))
    if int_max == 0:
        print('...bo zero to następujące kłopoty:')
    liczba = random.randint(1, int_max)
    zgadnij = 0
    licznik_prób = 0
    while zgadnij != liczba:
        zgadnij = int(input('Zgadnij jaką liczbę wylosowałem? '))
        if zgadnij == liczba:
            print('Zgadłeś! Wylosowałem', liczba)
            licznik_prób += 1
            if licznik_prób < rekord[-1]:
                print('Padł rekord!')
                rekord.append(licznik_prób)
            print('Udało Ci się zgadnąć po %d próbach' % licznik_prób)
            text = input('Czy chcesz zagrać jeszcze raz? (tak/nie) ')
        elif zgadnij != liczba:
            print('Niestety, nie zgadłeś')
            licznik_prób += 1

        
