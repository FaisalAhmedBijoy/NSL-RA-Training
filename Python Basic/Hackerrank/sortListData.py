"""
Sort the list according to following criterion,
1. Sort by age
2. if age is same then sort by name
3. if name is same then sort by country

"""
persons = [
 {
 "name": "John",
 "age": 36,
 "country": "Norway"
 },
 {
 "name": "Bob",
 "age": 36,
 "country": "Norway"
 }
]
persons.sort(key=lambda x: (x["age"], x["name"], x["country"]))
print(persons)

