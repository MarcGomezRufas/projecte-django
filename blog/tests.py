from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Autors, Post, Tag

class AutorModelTest(TestCase):
    def setUp(self):
        self.autor = Autors.objects.create(
            nom="Pau",
            cognom="Garcia",
            email="pau@example.com"
        )

    def test_autor_creation(self):
        self.assertEqual(self.autor.nom, "Pau")
        self.assertEqual(self.autor.cognom, "Garcia")
        self.assertEqual(self.autor.email, "pau@example.com")



class PostModelTest(TestCase):
    def setUp(self):
        self.autor = Autors.objects.create(nom="Anna", cognom="Roca", email="anna@example.com")
        self.post = Post.objects.create(
            titol="Test Post",
            contingut="Contingut test",
            descripcio="Descripció curta",
            imatge="test.jpg",
            autor=self.autor
        )

    def test_post_creation(self):
        self.assertEqual(self.post.titol, "Test Post")
        self.assertEqual(self.post.autor, self.autor)

    def test_post_str(self):
        self.assertEqual(str(self.post), "Test Post")


class TagModelTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(caption="Python")

    def test_tag_creation(self):
        self.assertEqual(self.tag.caption, "Python")

    def test_tag_str(self):
        self.assertEqual(str(self.tag), "Python")

    def test_tag_unique(self):
        with self.assertRaises(Exception):
            Tag.objects.create(caption="Python")


class PostTagRelationshipTest(TestCase):
    def setUp(self):
        self.autor = Autors.objects.create(nom="Marc", cognom="Lopez", email="marc@example.com")
        self.post = Post.objects.create(
            titol="Relació Post",
            contingut="Text",
            descripcio="Resum",
            imatge="img.jpg",
            autor=self.autor
        )
        self.tag1 = Tag.objects.create(caption="Django")
        self.tag2 = Tag.objects.create(caption="Python")

    def test_post_tags(self):
        self.post.tag.add(self.tag1, self.tag2)
        self.assertEqual(self.post.tag.count(), 2)
        self.assertIn(self.tag1, self.post.tag.all())

    


class BlogViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.autor = Autors.objects.create(nom="Laura", cognom="Vidal", email="laura@example.com")
        self.post = Post.objects.create(
            titol="Vista Post",
            contingut="Text de prova",
            descripcio="Desc",
            imatge="foto.jpg",
            autor=self.autor
        )
        self.tag = Tag.objects.create(caption="Flask")
        self.post.tag.add(self.tag)

    def test_home_view(self):
        response = self.client.get(reverse('inici'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/index.html')

    def test_posts_view(self):
        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/posts.html')

    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detall', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Vista Post")

    def test_tag_detail_view(self):
        response = self.client.get(reverse('tags_posts', args=[self.tag.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Vista Post")

    def test_autor_detail_view(self):
        response = self.client.get(reverse('autors_detall', args=[self.autor.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Laura")

