from flask import request
from flask_restx import Resource, Api, Namespace

Users = Namespace(
        name='Users',
        description='User 리스트를 작성하기 위해 사용하는 API'
    )

@Users.route('/')
class UserList(Resource):
    def get(self):
        '''사용자 목록 조회'''
        return {'message': '모든 사용자 조회111'}

    def post(self):
        '''새 사용자 추가'''
        return {'message': '새 사용자 추가'}, 201

@Users.route('/<int:user_id>')
@Users.param('user_id', '사용자 ID')
class User(Resource):
    def get(self, user_id):
        '''특정 사용자 조회'''
        return {'user_id': user_id, 'message': '사용자 정보 조회'}

    def put(self, user_id):
        '''특정 사용자 정보 업데이트'''
        return {'message': '사용자 정보 업데이트'}

    def delete(self, user_id):
        '''특정 사용자 삭제'''
        return {'message': '사용자 삭제'}

