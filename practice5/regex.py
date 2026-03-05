#1
import re  # Regex модулін қосамыз

pattern = r"ab*"  
# a  → міндетті түрде 'a'
# b* → 0 немесе одан көп 'b'

text = "abbb a ab b"

matches = re.findall(pattern, text)  
# findall() → сәйкес келетін барлық бөліктерді табады

print(matches)

#2
import re

pattern = r"ab{2,3}"
# b{2,3} → 'b' 2 немесе 3 рет қайталанады

text = "ab abb abbb abbbb"

matches = re.findall(pattern, text)

print(matches)

#3
import re

pattern = r"[a-z]+_[a-z]+"
# [a-z]+ → бір немесе бірнеше кіші әріп
# _ → underscore
# қайтадан [a-z]+ → кіші әріптер

text = "hello_world test_var A_B"

matches = re.findall(pattern, text)

print(matches)

#4
import re

pattern = r"[A-Z][a-z]+"
# [A-Z] → бір үлкен әріп
# [a-z]+ → одан кейін бір немесе бірнеше кіші әріп

text = "Hello World TEST Python"

matches = re.findall(pattern, text)

print(matches)

#5
import re

pattern = r"a.*b"
# a → басталуы 'a'
# .* → кез келген символ 0 немесе көп рет
# b → 'b' әрпімен аяқталады

text = "axxxb a123b ab ac"

matches = re.findall(pattern, text)

print(matches)

#6
import re

text = "Hello, world. Python is cool"

result = re.sub(r"[ ,\.]", ":", text)
# [ ,\.] → пробел, үтір немесе нүкте
# re.sub() → табылғандарды ":" белгісіне ауыстырады

print(result)

#7
import re

def snake_to_camel(text):
    return re.sub(r"_([a-z])", lambda x: x.group(1).upper(), text)
    # _([a-z]) → underscore + әріп
    # x.group(1) → табылған әріп
    # upper() → оны үлкен әріпке айналдырады

print(snake_to_camel("hello_world_test"))

#8
import re

pattern = r"[A-Z][^A-Z]*"
# [A-Z] → сөз үлкен әріптен басталады
# [^A-Z]* → келесі үлкен әріпке дейінгі барлық символдар

text = "HelloWorldPython"

matches = re.findall(pattern, text)

print(matches)

#9
import re

text = "HelloWorldPython"

result = re.sub(r"([A-Z])", r" \1", text)
# ([A-Z]) → үлкен әріп
# \1 → сол табылған әріпті қайта қолдану
# алдында пробел қосамыз

print(result.strip())  # strip() → басындағы артық пробелді өшіреді

#10
import re

def camel_to_snake(text):
    result = re.sub(r"([A-Z])", r"_\1", text)
    # Әр үлкен әріптің алдына "_" қояды
    
    return result.lower().lstrip("_")
    # lower() → бәрін кіші әріпке айналдырады
    # lstrip("_") → басындағы артық "_" өшіреді

print(camel_to_snake("HelloWorldPython"))