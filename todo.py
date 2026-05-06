my_task=[]
n=int(input('Enter a number of tasks you want to enter: '))
for i in range(n):
    tasks=input('Enter a task: ')
    my_task.append(tasks)
print("your to do tasks are:")
for i,tasks in enumerate(my_task,1):
    print(f'{i}. {tasks}')