from data_page import acronyms
from data_page import meanings
from data_page import detailed_explinations
print(len(acronyms))
print(len(meanings))
print(len(detailed_explinations))

for i in range(len(detailed_explinations)):
    print(acronyms[i] + "|+|+|+|+|+|+|+|", meanings[i] + "|+|+|+|+|+|+|+|", detailed_explinations[i])