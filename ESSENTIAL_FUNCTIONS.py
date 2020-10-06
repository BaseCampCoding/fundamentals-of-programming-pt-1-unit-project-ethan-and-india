students_list = [
    ["ethan bishop", "india ward", "charles mardis", "joseph dandan", "lathe ward", "seth hogue", "jeremiah tatum", "travis alexander", "sean coh", "loveen kaur", "kenia sandoval", "lance easley", "gregory bowles", "dylan mccreary", "aj hardaway", "al dees", "asiah moton", "bryce taylor", "jeremiah bass", "evan sanders", "matthew wilson", "andy duarte"]

def input_student_name(prompt: str) -> int:
  while True:
    response = input(prompt)
    if response == students_list[:-1]
      response = int(response)
      if response >= 0:
        return response
    print("Please Enter a Valid Name")
