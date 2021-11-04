# CryptoBrawl 2021
Bot stworzony na konkurs [CryptoBrawl](https://cryptobrawl.pl) ogranizowany przez IBM.
## O konkursie i zespole

>Show us what you would do with 1.000.000 USD in just five days when investing in cryptocurrencies.

Konkurs polegał na osiągnięciu największego zysku poprzez inwestowanie 1.000.000 $ w kryptowaluty Bitcoin i Etherum. 
Konkurs został podzielony na 2 etapy, zasadniczy i finałowy.

Zespół studentów z Wojskowej Akademi Technicznej WCY19WAT współtworzyli:

-Jakub Grątkiewicz - programista

-Józef Wesołowki - analityk giełdy

-Michał Mojkowski - analityk giełdy

## Narzędzia użyte w pierwszym etapie
Pierwszy etap konkursu spędziliśmy na analizie kursów oraz zależności między giełdą a platformą. Do tego musieliśmy handlować ręcznie. Do ręcznego handlu stworzyliśmy narzędzie pozwalające nam ustawiać zlecenia kupna/sprzedaży. Po wyciągnięciu wniosków rozwinęliśmy program o bota który dokonywał transakcji przy spełnieniu określonych przez nas kryteriów.

## Narzędzia użyte w finałowym etapie
Zespół określił w pierwszym etapie dwie strategie w ciągu pierwszego tygodnia. Jedną z nich odrzuciliśmy, a drugą zaimplementowaliśmy.

### Strategia nr 1 - odrzucona
Strategia ta opierała się na przewidywaniu wzrostów i spadków w początkowej jego fazie. 

Na wykresie zostało ideowo przedstawione kiedy bot mialby dokonywać kupna i sprzedaży:
![Rysunek1](https://user-images.githubusercontent.com/71324202/140382507-72fd2899-bc65-4fa5-8807-8ff4d5d5c779.png)

Strategia ta zakładała ewidencjonowanie ekstremów lokalnych kursów oraz ich odchylenia od aktualnego kursu. W przypadku kiedy kurs odchylał się od ostatniego minimum/maximum lokalnego o pewną wartość wyrażoną w procentach, bot wykonywał operację kupna/sprzedaży kryptowaluty. 

Wartość procentową odchylenia, która daje najwyższe przychody została wyznaczona przez osobny program testujący za pomocą metody prób i błędów. W czasie testowania wykorzystywane były zapisy kursu z bazy danych giełdy [Binance](https://www.binance.com/pl).
Symulacje przynosiły wynik w granicach 10-15% przychodu w ciągu tygodnia, więc strategia ta została odrzucona. 

### Strategia nr 2 - użyta
#### Warian podstawowy
Strategia ta operała się na obserwowaniu ruchu giełdowego na innych giełdach. Kurs występujący na stronie [CoinGecko](https://www.coingecko.com/pl) był najbliższy temu z platformy konkursowej więc to on został zaimplementowany do logiki bota. Bot działał jedynie na wymianie walut Ethereum i USD gdyż uznaliśmy, że w tej walucie występują większe dobowe ruchy procentowe, a co za tym idzie większy dobowy przychód.

#### Pierwszy napotkany problem - rozwiązanie
Strategia miała jednak wady, gdyż zdarzały się sytuacje gdzie bot dokonywał nieopłacalnych transakcji. Zdarzało się to w sytuacji zawahań kursu na stronie [CoinGecko](https://www.coingecko.com/pl), które nie były wychwycone przez platformę konkursową. Poniżej załączam wykres kursu ETHUSD oraz punkt w którym bot nietrawnie dokonał zakupu tracąc 18,000$. 

![Rysunek2](https://user-images.githubusercontent.com/71324202/140411355-80ba1d2b-5c85-4ed4-a0c2-f4d1a7dfab4b.png)

W celu ochrony przed podobnymi błędami w przyszłości, bot dostał pewnien bufor kursu, dzięki któremu ignorował podobne zawahania kursu w przyszłości. 

#### Drugi napotkany problem - rozwiązanie
Kolejnym problemem, który napotkał bot było odczytanie jego aktywności jako aktywności typu DDoS przez stronę [CoinGecko](https://www.coingecko.com/pl).

![rysunek4](https://user-images.githubusercontent.com/71324202/140417491-ae9d4b93-01d4-45da-8fef-55330bf0b034.jpg)

Aby go rozwiązać musieliśmy zmienić ustawienia systemowe na urządzeniu, na którym bot był uruchamiany.

#### Problemy nierozwiązane
Bardzo dużym problemem była użyta tachnologia z bibiloteki Selenium. Działała ona poprawnie jednak zdecdowanie za wolno. Nie zawsze udawało się maszynie dokonać zakupu przed zmianą kursu, co zmniejszało zyski uzyskane z transakcji. Program był optymalizowany całą rundę finałową, oraz błędy związane z tym faktem zostały zminimalizowane. Aby całkowicie rozwiązać problem należałoby całkowicie przekształcić program, rezygnując z technologi Selenium. 

### Osiągnięcia oraz podsumowanie
> Program ten, jest pierwszym moim programem w języku Python. W celu przygotowania się do stworzenia bota, w tyrybie przyspieszonym zapoznałem się z ponad 200 stronami książki [Python dla programistów](https://www.empik.com/python-dla-programistow-big-data-i-ai-studia-przypadkow-deitel-paul-j-deitel-harvey,p1249591285,ksiazka-p). ~JG

Kluczową rolę w rozwoju programu miały biblioteki języka Python:
[Selenium](https://selenium-python.readthedocs.io/) - działanie bota (kupno/sprzedaż, ściąganie danych ze stron)
[Pandas](https://pandasguide.readthedocs.io/en/latest/) - analiza oraz testy





