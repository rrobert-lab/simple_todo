Filepath='todos.txt'
def get_todos(filepath=Filepath):
  with open(filepath,'r') as local_file:
    todos_local= local_file.readlines()
  return todos_local
def write_todos(todo_arg,filepath=Filepath): 
  with open(filepath,'w') as file:
    file.writelines(todo_arg)
  