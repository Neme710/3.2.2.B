from Post import Post

all_posts_archive = []
usernames = ["aiden", "aidan", "aden", "adan"]
new_post():
  new_post_input = input("New Post's txt here --")

  

remove_post():
  pass



username = input("Please input youyr user name here - ")
if username in usernames:
  print ("hello", username)
  user_choice = int(input("Would you like to make new post (1) or remove a previos one (2)"))
  match user_choice:
    case 1:
      print (1)
      new_post()
    case 2:
      print(2)
      remove_post()
    case _:
      print("Wrong input")
      
      


