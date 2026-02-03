class Instagram:
    def __init__(self,title,description,creator_name,location):
        self.title = title
        self.description = description
        self.likes = 0
        self.creator_name = creator_name
        self.location = location
        self.comments = []
    def display_title(self):
        print("The title of the reel is ",self.title)
    def display_description(self):
        print("The description of the reel is ",self.description)
    def display_likes(self):
        print("The likes of the reel is ",self.likes)
    def liked(self):
        self.likes += 1
    def disliked(self):
        if self.likes > 0:
            self.likes-=1
    def display_creator_name(self):
        print("The creator name of the reel is ",self.creator_name)
    def display_location(self):
        print("The location of the reel is ",self.location)
    def display_comments(self):
        if len(self.comments)==0:
            print("No comments yet")
        else:
            print("The comments are:")
            for comment in self.comments:
                print(comment)
    def add_comments(self,comment):
        self.comments.append(comment)
    def delete_comments(self):
        temp_comment=self.comments.pop()
        print("Deleted comment:",temp_comment)

reel1=Instagram("My First Reel","This is my first reel","John Doe","New York")
reel1.display_comments()

reel1.add_comments("Great reel!")
reel1.add_comments("Nice work!")
reel1.display_comments()

reel1.delete_comments()
reel1.display_comments()

