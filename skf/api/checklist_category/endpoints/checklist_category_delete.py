from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, validate_privilege
from skf.api.checklist_category.business import delete_checklist_category
from skf.api.checklist_category.serializers import message
from skf.api.kb.parsers import authorization
from skf.api.restplus import api

ns = api.namespace('checklist_category', description='Operations related to checklist items')

@ns.route('/delete/<int:id>')
@api.doc(params={'id': 'The checklist type id'})
@api.response(404, 'Validation error', message)
class ChecklistCategoryDelete(Resource):

    @api.expect(authorization)
    @api.response(400, 'No results found', message)
    def delete(self, id):
        """
        Delete a checklist type.
        * Privileges required: **delete**
        """
        validate_privilege(self, 'delete')
        result = delete_checklist_category(id)
        return result, 200, security_headers()
