from django.test import TestCase
from .models import Post
from django.contrib.auth import get_user_model #author section
from django.utils.timezone import now
User = get_user_model()

class PostListTest(TestCase): #tests for lists page

    def setUp(self): #setting up user and password for every test
        user = User.objects.create (username = "test_user101")
        user.set_password("abc123")
        user.save()
        self.client.login(username = "test_user101", password = "abc123")

    def test_noteposts(self):
        """When there are no posts on the page it will still load successfully"""
        response = self.client.get("/") #url of the page is just /
        self.assertEqual(response.status_code, 200) # djangos assertEqual method (status code of 200, success)
        self.assertEqual(response.context["posts"].count(),0) #loading a lists of posts even if there isn't any

    def test_postsvisible(self):
        """When there are posts on the page it will still load successfully"""
        author = User.objects.create (username = "hello_there101") #created the author
        published_post = Post.objects.create(title = "Post1", text = "Post 1 data", author = author, published_date = now()) #create the posts the author wrote
        unpublished_post = Post.objects.create(title = "Post2", text = "Post 2 data", author = author)
        response = self.client.get("/") #loading the page
        self.assertEqual(response.status_code, 200) # djangos assertEqual method (status code of 200, success) checking if loaded successfully
        self.assertEqual(response.context["posts"].count(),1) #checking that there is one post on page

    def test_loggedout(self):
        """When user isnt logged in the page will still load sucessfully"""
        self.client.logout()
        author = User.objects.create (username = "hello_there101") #created the author
        published_post = Post.objects.create(title = "Post1", text = "Post 1 data", author = author, published_date = now()) #create the posts the author wrote
        unpublished_post = Post.objects.create(title = "Post2", text = "Post 2 data", author = author)
        response = self.client.get("/") #loading the page
        self.assertEqual(response.status_code, 200) # djangos assertEqual method (status code of 200, success) checking if loaded successfully
        self.assertEqual(response.context["posts"].count(),1)

class PostDetailTest(TestCase):

        def setUp(self): #setting up user and password for every test
            user = User.objects.create (username = "test_user101")
            user.set_password("abc123")
            user.save()
            self.client.login(username = "test_user101", password = "abc123")

        def test_postpublished(self):
            """If post published user should be able to view it sucessfully"""
            author = User.objects.create (username = "hello_there101") #created the author
            published_post = Post.objects.create(title = "Post1", text = "Post 1 data", author = author, published_date = now())
            response = self.client.get(f"/post/{published_post.pk}/") #f string allows you to put functions in curly braces
            self.assertEqual(response.status_code, 200) #making sure its sucessful
            self.assertEqual(response.context["post"], published_post)

        def test_postunpublished(self):
            """If post unpublished user should not be able to view it sucessfully"""
            author = User.objects.create (username = "hello_there101")
            unpublished_post = Post.objects.create(title = "Post2", text = "Post 2 data", author = author)
            response = self.client.get(f"/post/{unpublished_post.pk}/")
            self.assertEqual(response.status_code, 404) #making sure its unsucessful (not found)

        def test_loggedout(self):
            """When user is logged out they should be able to successfully read published posts but not unpublished"""
            self.client.logout()
            author = User.objects.create (username = "hello_there101")
            published_post = Post.objects.create(title = "Post1", text = "Post 1 data", author = author, published_date = now())
            response = self.client.get(f"/post/{published_post.pk}/")
            self.assertEqual(response.status_code, 200)
            unpublished_post = Post.objects.create(title = "Post2", text = "Post 2 data", author = author)
            response = self.client.get(f"/post/{unpublished_post.pk}/")
            self.assertEqual(response.status_code, 404)

        def test_doesnotexist(self):
            """If the user requests a page that does not exist there should be an error"""
            response = self.client.get("/post/1000000/")
            self.assertEqual(response.status_code, 404)
            response = self.client.get("/post/!/")
            self.assertEqual(response.status_code, 404)

class PostEditTest(TestCase):

        def setUp(self): #setting up user and password for every test
            user = User.objects.create (username = "test_user101")
            user.set_password("abc123")
            user.save()
            self.client.login(username = "test_user101", password = "abc123")

        def test_get_postpublished(self):
            """If post published user should be able to view it sucessfully"""
            author = User.objects.create (username = "hello_there101") #created the author
            published_post = Post.objects.create(title = "Post1", text = "Post 1 data", author = author, published_date = now())
            response = self.client.get(f"/post/{published_post.pk}/edit/")
            self.assertEqual(response.status_code, 200) #making sure its sucessful
            self.assertEqual(response.context["form"].instance, published_post)

        def test_get_postunpublished(self):
            """If post unpublished user should not be able to view it sucessfully"""
            author = User.objects.create (username = "hello_there101")
            unpublished_post = Post.objects.create(title = "Post2", text = "Post 2 data", author = author)
            response = self.client.get(f"/post/{unpublished_post.pk}/edit/")
            self.assertEqual(response.status_code, 200)

        def test_loggedout(self):
            "If user is logged out they wont be able to edit posts"
            self.client.logout()
            author = User.objects.create (username = "hello_there101")
            published_post = Post.objects.create(title = "Post1", text = "Post 1 data", author = author, published_date = now())
            response = self.client.get(f"/post/{published_post.pk}/edit/")
            self.assertEqual(response.status_code, 404) #making sure its sucessful
            unpublished_post = Post.objects.create(title = "Post2", text = "Post 2 data", author = author)
            response = self.client.get(f"/post/{unpublished_post.pk}/edit/")
            self.assertEqual(response.status_code, 404)

        def test_post_published(self):
            """If post published user should be able to edit it sucessfully"""
            author = User.objects.create (username = "hello_there101") #created the author
            published_post = Post.objects.create(title = "Post1", text = "Post 1 data", author = author, published_date = now())
            response = self.client.post(f"/post/{published_post.pk}/edit/", {"title":"new title","text":"new text"})
            self.assertRedirects(response,f"/post/{published_post.pk}/") #making sure its sucessful
            published_post.refresh_from_db() #makes sure to get the most recent data from the data base
            self.assertEqual(published_post.title, "new title")
            self.assertEqual(published_post.text, "new text")

        def test_post_unpublished(self):
            """If post is unpublished user should not be able to edit it sucessfully"""
            author = User.objects.create(username = "user1")
            unpublished_post = Post.objects.create(title = "Post02", text = "Great", author = author)
            response = self.client.post(f"/post/{unpublished_post.pk}/edit/", {"title": "new title", "text": "new text"})
            self.assertRedirects(response, f"/post/{unpublished_post.pk}/")
            unpublished_post.refresh_from_db()
            self.assertEqual(unpublished_post.title, "new title")
            self.assertEqual(unpublished_post.text, "new text")

        def test_post_loggedout(self):
            """If user is logged out they wont be able to edit posts"""
            self.client.logout()
            author = User.objects.create (username = "hello_there101")
            published_post = Post.objects.create(title = "Post1", text = "Post 1 data", author = author, published_date = now())
            response = self.client.post(f"/post/{published_post.pk}/edit/")
            self.assertEqual(response.status_code, 404) #making sure its sucessful
            unpublished_post = Post.objects.create(title = "Post2", text = "Post 2 data", author = author)
            response = self.client.post(f"/post/{unpublished_post.pk}/edit/")
            self.assertEqual(response.status_code, 404)

        def test_post_doesnotexist(self):
            """If post doest not exist user should not be able to edit posts"""
            response = self.client.post(f"/post/1000000/edit/")
            self.assertEqual(response.status_code, 404)
            response = self.client.post(f"/post/!!!!!/edit/")
            self.assertEqual(response.status_code, 404)

class PostNewTest(TestCase):

        def setUp(self): #setting up username and password for every tests
            user = User.objects.create (username = "test_user101")
            user.set_password("abc123")
            user.save()
            self.client.login(username = "test_user101", password = "abc123")

        def test_get(self):
            """Getting the page to create a new post"""
            response = self.client.get('/post/new/')
            self.assertEqual(response.status_code, 200)

        def test_post_invalid_data(self):
            """Getting the page to create a new post"""
            response = self.client.post('/post/new/')
            self.assertEqual(response.status_code, 200) #making sure its sucessful
            self.assertEqual(response.context["form"].errors, {"title": ["This field is required."], "text": ["This field is required."]})

        def test_post_valid_data(self):
            response = self.client.post('/post/new/', {"title": "new title", "text": "new text"})
            new_post = Post.objects.get(title = "new title", text = "new text")
            self.assertRedirects(response,f'/post/{new_post.pk}/')

        def test_post_not_logged_in(self):
            """If user is not logged in they shouldnt be able to create new posts"""
            self.client.logout() #since we are creating a new post we dont need an author or published posts
            response = self.client.post("/post/new/")
            self.assertEqual(response.status_code, 404)
            response = self.client.post('/post/new/', {"title": "new title", "text": "new text"})
            self.assertEqual(response.status_code, 404)

        def test_post_sametitle(self):
            """If user creates another post with same title they should be able to create new posts"""
            response = self.client.post('/post/new/')
            author = User.objects.create (username = "hello_there101")
            published_post = Post.objects.create(title = "Post1", text = "Post 1 data", author = author, published_date = now())
            response = self.client.post('/post/new/', {"title": "Post1", "text": "Great"})
            self.assertEqual(response.context["form"].errors, {"__all__": ["Post already has existing title"]})
            self.assertEqual(response.status_code, 200)
            unpublished_post = Post.objects.create(title = "Post02", text = "Great", author = author)
            rresponse = self.client.post('/post/new/', {"title": "Post2", "text": "Great"})
            self.assertEqual(response.context["form"].errors, {"__all__": ["Post already has existing title"]})
            self.assertEqual(response.status_code, 200)
