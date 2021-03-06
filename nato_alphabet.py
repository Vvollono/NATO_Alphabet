import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# Create a dictonary from the dataframe using dictonary comprehension
alph = {x["letter"] : x["code"] for x in data.to_dict(orient="records")}
name = input("What is the name? ").upper()
#Create a list from the dictonary using list comprehension
list_name = [alph[letter]for letter in name]
print(list_name)
