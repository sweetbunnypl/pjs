# pjs
Projekt w języku skryptowym

Gra autorstwa Karola Bolanowskiego.
Żeby ją włączyć wystarczy w konsoli wpisać "python3 game.py"
Życzę miłej gry :)

----------------------------------------------------------------------------------------------------------
# SPRAWOZDANIE 1

Jak na razie udało mi się zrobić:
- zapoznać się z możliwościami biblioteki pygame, dzięki której będę tworzył grę
- szkielet całej gry, podzieliłem grę na kilka pod folderów (tekstury, gracze, itp.)
- ogólną pętle w której gra będzie działać
- zaimplementować podstawowy odczyt działań na klawiaturze
- zaimplementować proste poruszanie się graczy

Do następnego sprawozdania planuję:
- wprowadzić kolizje między obiektami
- dodać możliwość skakania przez obiekty i odbijania piłki
- lepsze elementy graficzne
- podłoże muzyczne

Finalnie chciałbym żeby gra zawierała również te elementy:
- menu, wybieranie czy gramy w dwie osoby czy z botem czy chcemy otworzyć ustawienia
- możliwość wybierania skórek postaci, którymi będziemy grali
- możliwe, że również (jeśli starczy mi czasu) pojawią się jakieś dodatkowe zdolności dla poszczególnych postaci, ale wątpię, że mi się uda

----------------------------------------------------------------------------------------------------------
# SPRAWOZDANIE 2

Od ostatniego sprawozdania udało mi się:
- wprowadzić dopracowane kolizje między obiektami
- dodać "hitboxy" mapy, graczy, siatki i piłki
- dodać możliwość skakania przez graczy oraz odbijania piłki

Nie udało mi się jeszcze:
- zaimplementować lepszych elementów graficznych (jak na razie są to jedynie prostokąty i kwadraty, lecz jest to kwestia podmiany tekstur, a na takich obiektach lepiej się pracuje)
- podłoże muzyczne (doszedłem do wniosku, że zajmę się nim na końcu, a jak na razie powinienem bardziej skupić się na elementach funkcjonalnych i problemach, na które natrafiłem) 

Do następnego sprawozdania planuję:
- podzielić wszystkie elementy na osobne pliki, zawierające klasy (klasa gracz, piłka itp.)
- wprowadzić zdobywanie punktów
- poprawić kilka elementów graficznych

Finalnie chciałbym żeby gra zawierała również te elementy:
- podłoże muzyczne
- menu
- lepsze elementy graficzne wraz z możliwością wybierania skórek postaci, którymi będziemy grali

----------------------------------------------------------------------------------------------------------
# SPRAWOZDANIE 3

Od ostatniego sprawozdania udało mi się:
- podzielić główny plik gry na osobne pliki, zawierające klasy (klasa gracz, ustawienia itp.)
- wprowadzić zdobywanie punktów
- poprawić kilka błędów graficznych (powodowanych przez złą kolizję między obiektami lub lagiem głównej pętli gry)

Dodatkowo udało mi się:
- wprowadzić podłoże muzyczne (muzyka w tle gry)
- proste menu, które będę udoskonalał
- odczytywanie ustawień z pliku tekstowego

Do następnego sprawozdania planuję:
- wprowadzić tzw. sound effects (np. jak piłka się odbije od gracza, albo ściany, żeby usłyszeć dźwięk
- dopracować wizualnie i funkcjonalnie menu
- podmienić wszystkie proste obiekty (prostokąty) na postacie zrobione graficznie (możliwe, że nie dam rady wprowadzić skórek, aczkolwiek postaram się) 
- usunę widoczność hitboxów

----------------------------------------------------------------------------------------------------------
# SPRAWOZDANIE 4

Od ostatniego sprawozdania udało mi się:
- wprowadzić tzw. sound effects (np. jak piłka się odbije od gracza, albo ściany, żeby usłyszeć dźwięk);
- dopracować wizualnie i funkcjonalnie menu;
- podmienić wszystkie proste obiekty (prostokąty) na elementy bardziej zaawansowane graficznie;
- usunąć widoczność hitboxów;

Dodatkowo wprowadziłem:
- sound effects w menu tzn. gdy zmieniamy obecną opcję lub wracamy do poprzedniej słyszymy różniące się od siebie dźwięki;
- zmianę planszy w zależności od godziny ustawionej na komputerze użytkownika;

Finalnie nie udało mi się spełnić następujących myśli, które przewijały się podczas projektu:
- różne skórki postaci i efekty (głownie ze względu na to, że uznałem że nie jest to aż tak potrzebne i postacie wyglądają w miarę estetycznie);
- bot, który sprostałby użytkownikowi (głównie z powodu braku czasu na zaznajomienie się z mechaniką działania AI);
