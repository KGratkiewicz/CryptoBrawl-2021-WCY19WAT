# CryptoBrawl 2021 - WCY19WAT
Bot stworzony na konkurs [CryptoBrawl](https://cryptobrawl.pl) ogranizowany przez IBM.

## O konkursie i zespole
### Przebieg konkursu
>Show us what you would do with 1.000.000 USD in just five days when investing in cryptocurrencies.

Konkurs polegał na osiągnięciu największego zysku poprzez inwestowanie 1.000.000 $ w kryptowaluty Bitcoin i Etherum. 
Konkurs został podzielony na 2 etapy, zasadniczy i finałowy. Każdy etap trwał 5 dni.

Do handlu kryptowalutani została otwarta specjalna platforma, na której każdy z zespołów posiadał początkowo kapitał w wyskokości 1.000.000$. Sekcja trade dopuszczała jedynie transakcje natychmiastowe. Stanowiło to utrudnienie, gdyż bez narzędzi stworzonych samodzielnie, storna wymagała stałego śledzenia kursu i dokonywania transakcji ręcznie. Konkurs zawierając w nazwie słowo _Hackathon_ stawiał wyznwanie stworzenia oprogramowania wspomagającego wykonywanie transakcji.

### Zespół WCY19WAT
Zespół studentów z Wojskowej Akademi Technicznej WCY19WAT współtworzyli:

[Jakub Grątkiewicz](https://github.com/KGratkiewicz) 

Józef Wesołowki 

Michał Mojkowski

## Oprogramowanie stworzone przez zespół 
Na potrzeby konkursu stworzyliśmy oraz rozwijaliśmy oprogramowanie wspomagające wymianę walut na platformie konkursowej. Do obsługi platformy użyliśmy języka Python oraz biblioteki Selenium.

### Narzędzia użyte w pierwszym etapie
Pierwszy etap konkursu spędziliśmy na analizie kursów oraz zależności między giełdą a platformą. W tym etapie wykonywaliśmy handel ręczny, do którego wsparcia stworzyliśmy narzędzie pozwalające nam ustawiać zlecenia kupna/sprzedaży. Po wyciągnięciu wniosków rozwinęliśmy program do postaci bota który dokonywał transakcji przy spełnieniu określonych przez nas kryteriów (weak AI).

### Narzędzia użyte w finałowym etapie
Zespół w czasie trwania pierwszego etapii określił dwie strategie możliwe do wprowadzenia strategie. Zostały one przetestowane w środowisku testowym, oraz został wyłoniony z nich zwycięzca osiągający lepsze wyniki.

#### Strategia nr 1 - odrzucona
Strategia ta opierała się na przewidywaniu wzrostów i spadków w ich początkowej fazie. 

Na wykresie zostało ideowo przedstawione kiedy bot mialby dokonywać kupna i sprzedaży:
![Rysunek1](https://user-images.githubusercontent.com/71324202/140382507-72fd2899-bc65-4fa5-8807-8ff4d5d5c779.png)

Strategia ta zakładała ewidencjonowanie ekstremów lokalnych kursów oraz ich odchylenia od aktualnego kursu. W przypadku kiedy kurs odchylał się od ostatniego minimum/maximum lokalnego o pewną wartość wyrażoną w procentach, bot wykonywał operację kupna/sprzedaży kryptowaluty. 

Wartość procentową odchylenia, która daje najwyższe przychody została wyznaczona przez osobny program testujący za pomocą metody prób i błędów. W czasie testowania wykorzystywane były zapisy kursu z bazy danych giełdy [Binance](https://www.binance.com/pl).
Symulacje przynosiły wynik w granicach 10-15% przychodu w ciągu tygodnia, więc strategia ta została odrzucona. 

#### Strategia nr 2 - użyta
##### Warian podstawowy
Strategia ta operała się na obserwowaniu ruchu giełdowego na innych giełdach w czasie rzeczywistym. Kurs występujący na stronie [CoinGecko](https://www.coingecko.com/pl) był najbliższy temu z platformy konkursowej więc to on został zaimplementowany do logiki bota. Bot działał jedynie na wymianie walut Ethereum i USD gdyż uznaliśmy, że w tej walucie występują większe dobowe ruchy procentowe, a co za tym idzie większy dobowy przychód. 

##### Pierwszy napotkany problem - rozwiązanie
Strategia miała jednak wady, gdyż zdarzały się sytuacje gdzie bot dokonywał nieopłacalnych transakcji. Zdarzało się to w sytuacji zawahań kursu na stronie [CoinGecko](https://www.coingecko.com/pl), które nie były wychwycone przez platformę konkursową. Poniżej załączam wykres kursu ETHUSD oraz punkt w którym bot nietrawnie dokonał zakupu tracąc 18,000$. 

![Rysunek2](https://user-images.githubusercontent.com/71324202/140411355-80ba1d2b-5c85-4ed4-a0c2-f4d1a7dfab4b.png)

W celu ochrony przed podobnymi błędami w przyszłości, bot dostał pewnien bufor kursu, dzięki któremu ignorował podobne zawahania kursu w przyszłości. 

##### Drugi napotkany problem - rozwiązanie
Kolejnym problemem, który napotkał bot było odczytanie jego aktywności jako aktywności typu DDoS przez stronę [CoinGecko](https://www.coingecko.com/pl).

![rysunek4](https://user-images.githubusercontent.com/71324202/140417491-ae9d4b93-01d4-45da-8fef-55330bf0b034.jpg)

Aby go rozwiązać musieliśmy zmienić ustawienia systemowe na urządzeniu, na którym bot był uruchamiany.

##### Problemy nierozwiązane
Bardzo dużym problemem była użyta technologia z bibiloteki Selenium. Działała ona poprawnie jednak zdecdowanie zbyt wolno. Nie zawsze udawało się maszynie dokonać zakupu przed zmianą kursu, co zmniejszało zyski uzyskane z transakcji. Program był optymalizowany całą rundę finałową więc błędy związane z tym faktem zostały zminimalizowane. Aby całkowicie usunąć problem należałoby całkowicie przekształcić program, rezygnując z technologi dostępnej w Selenium na rzecz czegoś innego.

## Osiągnięcia oraz podsumowanie
> Program ten, jest pierwszym moim programem w języku Python. W celu przygotowania się do stworzenia bota, w tyrybie przyspieszonym zapoznałem się z ponad 200 stronami książki [Python dla programistów](https://www.empik.com/python-dla-programistow-big-data-i-ai-studia-przypadkow-deitel-paul-j-deitel-harvey,p1249591285,ksiazka-p), oraz z dokumentacją kilku bibliotek języka Python. Z wykonanej pracy jestem bardzo zadowolony. Konkurs na pewno zainteresował mnie tematem handlu kryptowalutami, pobudził moją kreatywność oraz zmusił do poznania nowych narzędzi technologicznych. Dziękuję również kolegom z zespołu, którzy nie współworzyli ze mną kodu, jednak określili logiczne kryteria kupna i sprzedaż. Współpracując z nimi czułem, że tworzymy zespół i każdy z nas pełni w tym zespole swoją rolę najlepiej jak potrafi. [~JG](https://github.com/KGratkiewicz)

Ostatecznie nasz zespół zakończył rywalizację na III miejscu z saldem 2.792.419,60$ (income 179,24%).

[Wyniki konkursu](https://www.mimuw.edu.pl/wyniki-hackatonu-cryptobrawl)

![rysunek5](https://user-images.githubusercontent.com/71324202/140427280-65f0da08-d4c2-4604-a4d6-bd6dcd765567.png)

Zobacz również jaką strategię opracował zespół _Bank Busters_ który zajął I miejsce:
[Strategia Bank Busters CryptoBrawl 2021](https://github.com/HakierGrzonzo/ibm_cryptobrawl)







