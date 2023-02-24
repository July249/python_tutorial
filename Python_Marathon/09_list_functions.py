
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby']
# friends.extend(lucky_numbers) # ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby', 4, 8, 15, 16, 23, 42]
# friends.append('Creed') # ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby', 'Creed']
# friends.insert(1, 'Kelly') # ['Kevin', 'Kelly', 'Karen', 'Jim', 'Oscar', 'Toby']
# friends.remove('Jim') # ['Kevin', 'Karen', 'Oscar', 'Toby']
# friends.clear() # []
# friends.pop() # ['Kevin', 'Karen', 'Jim', 'Oscar']
# friends.sort() # ['Jim', 'Jim', 'Karen', 'Kevin', 'Oscar', 'Toby']

friend2 = friends.copy() # ['Jim', 'Jim', 'Karen', 'Kevin', 'Oscar', 'Toby']

print(friends)
print(friend2)
# print(friends.index('Kevin')) # 0
# print(friends.index('Mike')) # ValueError

friends = ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby', 'Jim']
print(friends.count('Jim')) # 2

lucky_numbers.sort() # [4, 8, 15, 16, 23, 42]
print(lucky_numbers) 

lucky_numbers.reverse() # [42, 23, 16, 15, 8, 4]
print(lucky_numbers)
