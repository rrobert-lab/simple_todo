import streamlit as st
import FunctionWeb

def add_todo():
  todos=st.session_state["new_todo"]+'\n'
  
  Oldtodos=FunctionWeb.get_todos()
  
  Oldtodos.append(todos)
  
  FunctionWeb.write_todos(Oldtodos)
  
todos=FunctionWeb.get_todos()
st.title("My Todo App")
st.subheader("This is my Todo")
st.write("This is my App to increase productivity")

for index, todo in enumerate(todos):
  checkbox=st.checkbox(todo, key=index)
 
  if checkbox:
    todos.pop(index)
    FunctionWeb.write_todos(todos)
    print(index)
    del st.session_state[index]
    st.rerun()
    
  
    
st.text_input(label="enter todo",placeholder="Add new todo",on_change=add_todo,key='new_todo')
print("Hello" )
