from flask import request
from flask_restx import Resource, Api, Namespace


todos = {}
count = 1


Todo = Namespace(
        name='Todo',
        description='Todo 리스트를 작성하기 위해 사용하는 API'
    )

@Todo.route('')
class TodoPost(Resource):
    def post(self):
        '''Todo 리스트에 할 일을 등록합니다.'''
        global count
        global todos
        
        idx = count
        count += 1
        todos[idx] = request.json.get('data')
        
        return {
            'todo_id': idx,
            'data': todos[idx]
        }


@Todo.route('/<int:todo_id>')
class TodoSimple(Resource):
    def get(self, todo_id):
        '''Todo 리스트에 todo_id와 일치하는 ID를 가진 할 일을 가져옵니다'''
        return {
            'todo_id': todo_id,
            'data': todos[todo_id]
        }

    def put(self, todo_id):
        '''Todo 리스트에 todo_id와 일치하는 ID를 가진 할 일을 수정합니다'''
        todos[todo_id] = request.json.get('data')
        return {
            'todo_id': todo_id,
            'data': todos[todo_id]
        }
    
    def delete(self, todo_id):
        '''Todo 리스트에 todo_id와 일치하는 ID를 가진 할 일을 삭제합니다'''
        del todos[todo_id]
        return {
            "delete" : "success"
        }
