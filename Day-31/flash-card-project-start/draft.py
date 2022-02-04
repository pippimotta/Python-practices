import pandas
to_learn_list = pandas.read_csv('data/french_words.csv').to_dict(orient="records")

df = pandas.DataFrame(to_learn_list)
print(to_learn_list)