from Shape.AllinOne import Test

if __name__ == "__main__":
   try:
      test = Test()
      test.test_user_input_all()
   except KeyboardInterrupt:
      print("\n\nThe program was stopped by the user")
   finally:
      print("Thank you for using the program!", end="")