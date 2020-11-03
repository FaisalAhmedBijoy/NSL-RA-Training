numbers=[1,2,3,4,5,6,7,8,9,10]
# find out even number in this list: for loop
even_number=[]
for i in numbers:
    if i%2==0:
        even_number.append(i)
print(even_number)

#list comprehensive
num=1
even=[num for i in numbers]
print(even)

#dictionary
fruit_ranking = [1, 2, 3]
fruit_name = ['Mango', 'Pineapple', 'Watermelon']
fruit_rank_dict = {}

for i in range(len(fruit_ranking)):
    fruit_rank_dict[fruit_ranking[i]] = fruit_name[i]

print(fruit_rank_dict)

# dict comprehensive
fruit={fruit_ranking[i]:fruit_name[i] for i in range(len(fruit_ranking))}
print(fruit)