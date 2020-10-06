students_list = ['ethan bishop', 'india ward']






def input_student_name(prompt: str) -> int:
  while True:
    response = input(prompt)
    if response == students_list[:-1]
      response = int(response)
      if response >= 0:
        return response
    print("Please Enter a Valid Name")
