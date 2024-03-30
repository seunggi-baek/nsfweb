import database

from flask import request, jsonify
from flask_restx import Resource, Api, Namespace

Ir = Namespace(
        name='Ir',
        description='적외선센서 호출 API'
    )

@Ir.route('/')
class IrList(Resource):
    def get(self):
        '''적외선 센서 목록 조회'''
        result = database.execute_query("SELECT * FROM Equipment where EquipmentTypeID = 3")
        return jsonify(result)

@Ir.route('/<int:ir_id>')
@Ir.param('ir_id', '적외선센서 API')
class IrService(Resource):
    def get(self, ir_id):
        '''특정 사용자 조회'''
        result = database.execute_query("SELECT * FROM Equipment where EquipmentTypeID = 3")
        return jsonify(result)

    def put(self, ir_id):
        '''특정 사용자 정보 업데이트'''
        result = database.execute_query("SELECT * FROM Equipment where EquipmentTypeID = 3")
        return jsonify(result)

#     def delete(self, user_id):
#         '''특정 사용자 삭제'''
#         return {'message': '사용자 삭제'}

