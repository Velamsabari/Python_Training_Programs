def calculate_grade():
  x  = int(input("Enter the marks between 0 to 100 : \n"))
  match x:
    case x if 90<= x <= 100 :
        print("Grade-A")
    case x if 80<= x <= 89 :
        print("Grade-B")
    case x if 70<= x <= 79 :
        print("Grade-C")
    case x if 60<= x <= 69 :
        print("Grade-D")
    case x if x <= 59 :
        print("Grade-F")
    case _:
        print("Not a valid input")

calculate_grade()
