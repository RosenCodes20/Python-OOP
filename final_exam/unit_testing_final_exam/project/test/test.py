from project.social_media import SocialMedia
from unittest import TestCase, main


class TestSocialMedia(TestCase):

    def setUp(self) -> None:
        self.social_media = SocialMedia(
            "Nova",
            "YouTube",
            30,
            "Action"
        )

    def test_correct_init(self):
        self.assertEqual("Nova", self.social_media._username)
        self.assertEqual("YouTube", self.social_media.platform)
        self.assertEqual(30, self.social_media.followers)
        self.assertEqual("Action", self.social_media._content_type)
        self.assertEqual([], self.social_media._posts)

    def test_platform_setter_working_right(self):
        allowed_platforms = ['Instagram', 'YouTube', 'Twitter']
        with self.assertRaises(ValueError) as ve:
            self.social_media.platform = "Tv"

        self.assertEqual(f"Platform should be one of {allowed_platforms}", str(ve.exception))

    def test_followers_setter_working_properly_right(self):
        with self.assertRaises(ValueError) as ve:
            self.social_media.followers = -1

        self.assertEqual("Followers cannot be negative.", str(ve.exception))

    def test_if_create_post_method_works_right(self):
        result = self.social_media.create_post("Hello")
        self.assertEqual([{'content': "Hello", 'likes': 0, 'comments': []}], self.social_media._posts)
        self.assertEqual("New Action post created by Nova on YouTube.", str(result))

    def test_if_like_post_method_works_right_not_expecting_an_error(self):
        self.social_media.create_post("Hello")
        result = self.social_media.like_post(0)
        self.assertEqual([{'content': "Hello", 'likes': 1, 'comments': []}], self.social_media._posts)
        self.assertEqual("Post liked by Nova.", str(result))

    def test_like_post_method_if_likes_are_higher_than_ten(self):
        self.social_media._posts = [{'content': "Hello", 'likes': 11, 'comments': []}]
        result = self.social_media.like_post(0)

        self.assertEqual("Post has reached the maximum number of likes.", str(result))

    def test_if_like_post_method_works_with_invalid_index(self):
        self.social_media.create_post("Hello")
        result = self.social_media.like_post(1)

        self.assertEqual("Invalid post index.", str(result))

    def test_if_comment_on_post_method_works_right(self):
        self.social_media.create_post("Hello")
        self.social_media.like_post(0)
        result = self.social_media.comment_on_post(0, "Hello how are you today")

        self.assertEqual([{'content': "Hello", 'likes': 1, 'comments': [{"user": "Nova", "comment": "Hello how are you today"}]}], self.social_media._posts)
        self.assertEqual("Comment added by Nova on the post.", str(result))

    def test_comment_on_post_method_if_comment_is_too_short(self):
        self.social_media.create_post("Hello")
        self.social_media.like_post(0)
        result = self.social_media.comment_on_post(0, "Bro")
        self.assertEqual("Comment should be more than 10 characters.", str(result))


if __name__ == "__main__":
    main()
