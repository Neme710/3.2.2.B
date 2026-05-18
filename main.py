from Post import Post
all_posts_archive = []
usernames = ["aiden", "aidan", "aden", "adan"]
def new_post():
  new_post_input = input("New Post's txt here --")
  all_post_archive.append(Post(username, new_post_input)
  #Dont know the proper sytenx for the post method
def remove_post():
  for index, value in enumerate(all_posts_archive):
    print(f"Index: {index}, Value: {value}")
  remove_post_input = int(input("Please selcect the post you would like to remove --"))
  del all_posts_archive [remove_post_input]
username = input("Please input youyr user name here - ")
for username in usernames:
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
    print (all_post_archive)
