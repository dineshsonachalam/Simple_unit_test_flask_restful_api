from app import app
import unittest
from unittest import TestCase
from utility.auth_crud import crud_operation
from utility.basic_crud import basic_crud_operations
import json
import sys

auth = crud_operation()
basic_crud = basic_crud_operations("users", "user_management")

class TestIntegrations(TestCase):



    # setUp -> Called before calling test method.
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    # tearDown -> Called after test method called
    def tearDown(self):
        # Drop the users collection
        #basic_crud.delete_all()
        pass


    def test_user_registered(self):
        user_1 = "Tom"
        pswd = "admin"
        # content -> contains a list [{},status_code].
        # Here status_code -> 200 success and status_code -> 400 failure.
        content = auth.register_users(user_1,pswd)
        print("Content:",content)
        assert content[1] == 200


        user_2 = "John"
        content = auth.register_users(user_2,pswd)
        assert content[1] == 200

    def test_login(self):
        user_1 = "Tom"
        pswd = "admin"
        # content -> contains a list [{},status_code].
        # Here status_code -> 200 success and status_code -> 400 failure.
        content = auth.login_users(user_1,pswd)
        print("Content:",content)
        assert content[1] == 200









if __name__ == '__main__':
    unittest.main()


