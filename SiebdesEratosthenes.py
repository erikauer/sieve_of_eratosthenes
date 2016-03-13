# -*- coding: utf-8 -*-
# Sieb des Eratosthenes. Dies ist ein Verfahren um alle Primzahl bis zu einer Schranke S zu finden.
#
# Idee des Verfahrens:
# Da 0 und 1 keine Primzahlen sind, ist 2 der Startpunkt des Verfahren. 2 ist eine Primzahl.
# Danach streicht man alle Zahlen die Vielfache der Zahl 2 sind (4,6,8,10,...), da diese ja durch 2
# teilbar sind und somit keine Primzahl sein können.
# Dies fuehrt man bis zur Schranke S durch. Danach sucht man sich die erste nicht gestrichene Zahl.
# Die nächste nicht gestrichen Zahl ist die Zahl 3. Diese ist erneut Primzahl, da ja keine niedrigere
# Zahl die 3 bis hier gelöscht hat. Analog streicht man alle Vielfachen der 3. Dies fuehrt man mit
# jeder Zahl die nicht zuvor von einer kleineren Zahl gestrichen wurden. Am Schluss bleiben
# nur noch Zahlen ueber, die Primzahlen sind.
#
# Optimierung des Verfahrens:
# 1) Bei jeder Zahl i bei der man die Vielfachen streicht (also bei jeder Primzahl), braucht man erst
# bei i^2 beginnen, Zahlen zu löschen.
# z.B.: für i=2 erst bei 4, für i=3 erst bei 9, für i=5 erst bei 25, usw.
# Grund: Betrachte man die Zahl 5. So so ist 2*5, 3*5 und 4*5 bereits Vielfache von 2, 3 bzw. 4.
# Diese Vielfachen wurden aber schon bei den vorigen Zahlen gestrichen, da ja im ersten Schritt
# alle Vielfachen der Zahl 2 zu streichen waren. Und im zweiten Schritt alle Vielfachen der 3.
#
# 2) Aus dem selben Grund brauchen wir das Streichen der Vielfachen einer Zahl i nur bis zu der
# Grenze Wurzel aus S unternehmen.
# Grund: Sei i > Wurzel aus S. Dann gilt wegen Überlegung 1), dass wir erst bei i^2 anfangen müssten
# Vielfache der Zahl i zu streichen. i^2 liegt aber wegen i > Wurzel aus S über der Grenze S
# wodurch keine weitere Zahl mehr zu streichen ist.

import math

# boundary ist die Schranke des Bereichs in dem wir das Sieb des Eratosthenes anwenden wollen.
# Im weiteren werden wir S für boundary in den Kommentaren verwenden.
boundary = 100000000;

# Instanziere ein Array von Index 0 bis S mit S+1 Boolean Werten. Der Index des Arrays beschreibt
# in unserem Beispiel alle ganzen Zahlen von 0 bis S. Durch die Boolean Werte wird durch setzen
# auf False ein Index und somit eine Zahl gestrichen.
numbers = [True]*(boundary+1);

# Für jeden index von 2 bis Wurzel aus S (Siehe Optimierung des Verfahrens 2) ) möchten wir das
# Sieb des Eratosthenes anwenden.
for index in range(2, int(math.sqrt(boundary))):

    # Im Fall, dass der Index bzw. die Nummer noch nicht auf False gesetzt wurde, werden wir die
    # Vielfachen Streichen.
    if numbers[index]:
        # Der Index selbst muss eine Primzahl sein, da sie noch nicht von vorigen Zahlen gestrichen
        # wurde.
        print index
        # Streiche alle Vielfachen beginnend mit dem Quadrat der Zahl.
        for j in range(index*index, boundary, index):
            numbers[j] = False;

# Print the rest of all numbers.
for index in range(int(math.sqrt(boundary)), boundary):
    if numbers[index]:
        print index
