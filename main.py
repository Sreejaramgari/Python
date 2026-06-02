#Creating new file
#try:
#    with open('sample.txt','w') as file:
#        print("new file created")

#except Exception as e:
#   print("Error:{e}")

#Writing content into a file
#try:
#    with open('sample.txt','w') as file:
#       string = """Hi hello 
#        how are you"""
#       file.write(string)
#       lines = ['i am a python student\n','at codegnan\n']
#       file.writelines(lines)
#
#except Exception as e:
#   print("Error:{e}")

#reading content from file
#try:
#    with open('sample.txt','r') as file:
#       content = file.read()
#       content1 = file.read()
#       print(content)
#       print("content1:",content1)
#       file.seek(0)
#       lines = file.readlines()
#       print(lines)
#except Exception as e:
#  print(f"Error:{e}")

#appending a+
try:
    with open('sample.txt','a+') as file:
       content = file.read()
       content1 = file.read()
       print(content)
       print("content1:",content1)
       file.seek(0)
       lines = file.readlines()
       print(lines)
except Exception as e:
    print(f"Error:{e}")
