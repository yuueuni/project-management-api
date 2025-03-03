# from unittest import TestCase
#
# from fastapi.testclient import TestClient
#
# from app.db.session import SessionLocal
# from app.main import app
#
#
# class TestMemberClient(TestCase):
#     def setUp(self):
#         self.client = TestClient(app)
#         self.db = SessionLocal()
#
#     def tearDown(self):
#         self.db.rollback()
#
#     def test_create_member(self):
#         data = {"name": "테스트유저", "email": "test.member@example.com", "password": "password123"}
#
#         # API 호출 (회원 생성)
#         response = self.client.post("/members/", json=data)
#
#         # 테스트 결과 검증
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json()["name"], data["name"])
#         self.assertEqual(response.json()["email"], data["email"])
#
#     def test_member_exists(self):
#         # 회원 추가
#         member_data = {"name": "테스트유저2", "email": "test.member2@example.com", "password": "password456"}
#         response = self.client.post("/members/", json=member_data)
#
#         # 회원 조회 테스트
#         response = self.client.get(f"/members/{response.json()["id"]}")  # 첫 번째 회원 조회
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json()["name"], "테스트유저2")
#
#     def test_delete_member(self):
#         # 회원 생성
#         member_data = {"name": "삭제테스트", "email": "delete.member@example.com", "password": "password789"}
#         response = self.client.post("/members/", json=member_data)
#         member_id = response.json()["id"]
#
#         # 회원 삭제
#         response = self.client.delete(f"/members/{member_id}")
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json()["message"], "Member deleted")
#
#         # 삭제 후 회원이 존재하지 않음을 확인
#         response = self.client.get(f"/members/{member_id}")
#         self.assertEqual(response.status_code, 404)  # 회원이 삭제되었으므로 404 응답
