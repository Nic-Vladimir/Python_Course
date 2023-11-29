new_member = input('Add a new member: ') + '\n'

file = open(f'Files/members.txt', 'r')
members = file.readlines()
file.close()

members.append(new_member)

file = open(f'Files/members.txt', 'w')
file.writelines(members)
file.close()


