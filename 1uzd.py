"""
Uzrakstiet programmu definējot klasi,lai veselu skaitli pārveidotu par romiešu ciparu.

1) kādus ciparus jūs ziniet? Arābu
2) kādus romiešu ciparus ziniet? I V X C M L D
3) kas ir klase? Klase ir programmēšanas struktūra, kas var definēt datu uzvedību un metodes.
4) klase sastāv no konstruktora/destruktora metodēm (iekšējām funkcijām).
5) kādas datu struktūras ziniet?
    -list
    -arry
    -dict
""" 
class ArabuSkaitli:
    def __init__(self):
        self.roma_sk={
            1:'I',
            4:'IV',
            5:'V',
            9: 'IX',
            10: 'X', 
            40: 'XL', 
            50: 'L', 
            90: 'XC', 
            100: 'C', 
            400: 'CD', 
            500: 'D', 
            900: 'CM', 
            1000: 'M'
        }
    def to_roman(self, num):
        result = ''
        for value, numeral in sorted(self.roma_sk.items(), key=lambda x:[0], reverse=True):
            while num>=value:
                result += numeral
                num -= value
        return result

skaitlis=21
kk=ArabuSkaitli()
romieshu=kk.to_roman(skaitlis)

print(f"{skaitlis} ar romiešu cipariem ir {romieshu}")