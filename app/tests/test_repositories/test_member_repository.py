# import unittest
#
# from app.db.session import SessionLocal
# from app.repositories import MemberRepository
#
#
# class TestMemberRepository(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.db = SessionLocal()
#         cls.repository = MemberRepository(cls.db)
#
#     def setUp(self):
#         pass
#
#     def tearDown(self):
#         self.db.rollback()
#
#     def test_create_member(self):
#         member_data = MemberCreate(name="John Doe", email="john.doe@example.com", password="password123")
#
#         member = self.repository.create(member_data)
#
#         self.assertEqual(member.name, "John Doe")
#         self.assertEqual(member.email, "john.doe@example.com")
#         self.assertIsNotNone(member.id)
#
#     def test_get_member_by_id(self):
#         member_data = MemberCreate(name="Jane Doe", email="jane.doe@example.com", password="password123")
#         created_member = self.repository.create(member_data)
#
#         member = self.repository.get_by_id(created_member.id)
#
#         self.assertEqual(member.name, "Jane Doe")
#         self.assertEqual(member.email, "jane.doe@example.com")
#         self.assertEqual(member.id, created_member.id)
#
#     def test_delete_member(self):
#         member_data = MemberCreate(name="Delete Me", email="delete.me@example.com", password="password123")
#         created_member = self.repository.create(member_data)
#
#         deleted_member = self.repository.delete(created_member.id)
#
#         self.assertEqual(deleted_member.name, "Delete Me")
#         self.assertEqual(deleted_member.email, "delete.me@example.com")
#
#         member = self.repository.get_by_id(created_member.id)
#         self.assertIsNone(member)
#
# if __name__ == "__main__":
#     unittest.main()
