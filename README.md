# Problem: "Algorytmu generowania labiryntów w ASCII

# + przechodzenie z backtrackingiem"

## Autor: Łukasz Baran

### Rozwiązanie:

- Zastosowanie iteracyjnego algorytmu DFS za pomocą przechodzenia po komórkach\
  (zapisywanie ich na lokalnym stosie).
- Następnie wybieraniu losowej dostępnej sąsiedniej komórki i usuwanie\
  ich sąsiednich ścian oraz backtracking, aby do tworzenia labiryntów.
- Zastosowanie rekurencyjnego algorytmu DFS do przechodzenia labiryntu.

### Uruchomienie programu:

- python3 projekt_lukasz_baran.py
  - standardowe uruchomienie
- python3 projekt_lukasz_baran.py | tee out.txt
  - aby zapisac wynik do pliku\
    (łatwiej odczytać backtracking oraz wykonane kroki)

Całość kodu została opatrzona komentarzem w języku angielskim.\
Program prowadzi krok po kroku co można w nim wykonać i w jaki sposób.\
Sprawdza, jeżeli wprowadzone dane są nieprawidłowe.

### Zastosowane klasy:

#### Klasa Cell:

Tworzy obiekty który symuluje pojedynczą komórke w gridzie\
 Inicjalizowany jest z parametrami x oraz y, aby zachować swoje położenie

atrybuty:

- self.x, self.y: pozycja x,y na której się znajduje
- self.visited: zachowuje informacje czy została wcześniej odwiedzona
- self.walls: slownik który trzyma informacje o sąsiadach komorki
- self.directions: pomocnicza tablica zmiennych tuple,\
  aby łatwiej było iterować w pętli

funkcje:

- get_possible_adjacent_cells: zwraca tablice komórek,\
  które zostały jeszcze nieodwiedzone

#### Klasa CreateMazeDFS:

Na początku pyta użytkownika o "N" rozmiar labiryntu.\
 Sprawdza poprawność wybranego rozmiaru.\
 Później tworzy labirynt o wymiarach N x N.\
 Następnie inicjalizowana jest funkcja tworzenia labiryntu,\
 która wykorzystuje iteracyjny DFS z stosem.

atrybuty:

- self.size: ustawia rozmiar labiryntu
- self.grid: przechowuje grid komórek o rozmiarze N x N

funkcje:

- set_size: pyta użytkownika o rozmiar labiryntu\
- remove_wall_between_cells: funkcja do usuwania ścian\
  pomiędzy dwoma komórkami\
- start_algorithm: główna funkcja do tworzenia algorytmu,\
  za pomocą DFS który wybiera losową drogę z backtrackingiem\
- draw: wypisuje gotowy labirynt za pomocą znaków " " oraz "# "\
  w rozmiarze N \* 2 + 1

#### Klasa Setup:

Pozwala wybrać start i koniec w labiryncie.\
 Sprawdza ona poprawność wybranych punktów\
 (czy posiadają chociaż jednego sąsiada z polem ->" "\
 wybrane punkty należą do labiryntu,\
 punkty startu i końca nie nakładają się na siebie)\
 Inicjalizowana jest z parametrami maze oraz size, aby wykorzystać te dane.

atrybuty:

- self.maze: pobiera labirynt aby na nim sprawdzać wybrane punkty
- self.size: zachowuje rozmiar labiryntu (N \* 2 + 1)
- self.directions: pomocnicza tablica zmiennych tuple,\
  aby łatwiej było iterować w pętli
- self.start, self.end: zachowują punkty startu i końca\
  w typie tuple podane przez użytkownika

funkcje:

- check_setup: sprawdza wprowadzane dane
- get_positions: sprawdza czy na pewno wybrane punkty\
  nie nakładają sie i zwraca dane w formie tuple

legenda co jest wyświetlane:

- " " możliwa droga
- "# " ściana

#### Klasa SolveMazeDFS:

Ma za zadaniem przejść podany labirynt, z podanym wejściem i wyjściem.\
 Przyjmuje flagi które są wykorzystywane,\
 aby kontrolować co ma zostać wyświetlone.\
 Wykorzystuje algorytm DFS za pomocą rekurencji.

atrybuty:

- self.maze: pobiera labirynt
- self.size: zachowuje rozmiar labiryntu (N \* 2 + 1)\
- self.directions: pomocnicza tablica zmiennych tuple,\
  aby łatwiej było iterować w pętli\
- self.start, self.end: zachowują punkty startu i końca w typie tuple\
- self.backtrack, self.follow: flagi co ma zostać wyświetlone\

funkcje:

- printSolution: funkcja która wyświetla aktualny stan przejścia
- solve_maze_recursion: funkcje rekurencyjna,\
  która służy do generowania rozwiązania (DFS z backtrackingiem)
- solve_maze: funkcja inicjalizująca rekurencje,\
  ustawia pola początkowe i końcowe w rozwiązaniu

legenda co jest wyświetlane:

- " " możliwa nieodwiedzona droga
- "# " ściana
- "+ " końcowa trasa
- "B " backtracking
- "S " miejsce startu labiryntu
- "F " miesjce końca labiryntu
