from tkinter import * 
from tkinter import ttk
class TodoProject:

    # Config all the root window
    def __init__(self):
        self.totalTasks = 0
        self.root = Tk()
        self.settings_window()
        self.center_window(self.root)
        self.load_components(self.root)

    def center_window(self, window):
        window.update_idletasks()
        width = window.winfo_width()
        height = window.winfo_height()
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        window.geometry(f"{width}x{height}+{x}+{y}")
        print("============== Window centered ==============")

    def settings_window(self):
       
        self.root.title("ToDo GUI")
        self.root.geometry("500x560")
        self.root.config(background= "Light Blue")
        print("==============  Settings Done ==============")

    def load_components(self, window):
        label_1 = Label(window,
                        text="Task: ",
                        bg="Light Blue",
                        fg="White",
                        font= ("Arial", 16)
                        )


        text_field = Text(window,
                        height=1,
                        width=32,
                        )


        tasks = Text(window,
                        height=15,
                        width=42,
                        state="disabled"
                        )
        
        button = Button(window,
                        text="Add The Task",
                        cursor="heart",
                        fg="White",
                        bg="Black",
                        font=("Arial",12),
                        command= lambda: self.addTask(text_field,tasks)
                        )

        label_2 = Label(window,
                        text="Delete Task by ID:",
                        bg="Light Blue",
                        fg="White",
                        font= ("Arial", 16)
                        )

        task_id = Text(window,
                        height=1,
                        width=10,
                        
                        )
        
        button_2 = Button(window,
                        text="Delete Task Task",
                        cursor="target",
                        fg="White",
                        bg="Red",
                        font=("Arial",13),
                        command= lambda: self.delete_task(tasks,task_id)
                        )

        label_1.pack(padx=100)
        text_field.pack(padx=100)
        button.pack(padx=100,pady=20)
        tasks.pack(padx=100, pady=20)
        label_2.pack(padx=100)
        task_id.pack(padx=100,pady=20)
        button_2.pack(padx=100,pady=20)

        print("============ Components Loaded ==============")

    def start_app(self):
        print("********************************************")
        print("*************** App Running ****************")
        print("********************************************")
        self.root.mainloop()
        

    # Logic functions
    def setTotalTasks(self):
        self.totalTasks += 1
        return self.totalTasks

    def addTask(self,text_field,tasks):
        if len(text_field.get("1.0", "end-1c")) == 0:
            print("the widget is empty")
        else:
            x = self.setTotalTasks()
            task = text_field.get("1.0",END)
            text_field.delete("1.0",END)

            print("A task was added")

            tasks.configure(state='normal')
            #Write the task and add a line break
            tasks.insert(str(x)+'.0',str(x) +" -> " +task+"\n")
            tasks.configure(state='disabled')

    def delete_task(self, total_tasks, task_id):
        list_of_tasks = total_tasks.get("1.0", END)
        id = task_id.get("1.0", END)
        task_id.delete("1.0",END)

        x = []
        t=""
        # Adding a loop to make the array with every single task
        for c in list_of_tasks:            
            if c != "\n":
                t += c
            else: 
                x.append(t)
                t = ""
        
        total_tasks.configure(state='normal')
        # Adding a loop to search the row that we want to delete
        for i,item in enumerate(x):
            if item not in ("", "\n", " ","\n","\r"):
                if int(item[0]) is int(id):
                    print("TASK DELETED")
                    total_tasks.delete(str(i+1)+".0", str(i+1)+"."+str(len(item)))
        
        total_tasks.configure(state='disabled')
        
               

myapp = TodoProject()
myapp.start_app()