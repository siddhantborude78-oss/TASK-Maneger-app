tasks=[]
print("_____WELCOME TO TASK MANAGER APP___")
def task():
	total_tasks=int(input("\nEnter how many tasks you can add::"))
	for t in range(1,total_tasks+1):
		tasks_name=input(f"enter task{t}=")
		tasks.append(tasks_name)
	
task()	
print(f"\ntodays tasks are\n {tasks}")
while True:
    	
    	operation=int(input("\nEnter 1-add/2-update/3-delete/4-exit_or_stope::"))
    	if operation==1:
    		add=input("Enter a task you want to add:")
    		tasks.append(add)
    		print(f"Your task {add} has been added successfully")
    		print(f"new tasks are \n{tasks}")
    		
    	elif operation==2:
    		old_task=input("\n Enter a task you want to update:")
    		if old_task in tasks:
    			new_task=input("Enter a new task:")
    			ind=tasks.index(old_task)
    			tasks[ind]=new_task
    			print(f"Your new task {new_task} has been addded")
    			print(f"updated task list are\n{tasks}")
    			
    	elif operation==3:
    		delete_task=input("\n enter task you want to delete::")
    		if delete_task in tasks:
    			tasks.remove(delete_task)
    			print(f"your task {delete_task} are deleted in task book")
    			print(f"Your updated tasks are \n{tasks}")
    		
    	elif operation==4:
    		print("THANK YOU...PLEASE VISIT AGAIN")
    		break
    		
    	else:
    		print("\n\nSomething is wrong..please enter 1/2/3")