from src.constants import fields, values

def do_step(context):
    request = context.request
    response = context.response

    if request[fields.INCOME] == 0:
        response.disability = values.INELIGIBLE

    if request.get(fields.VEHICLE) is None:
        response.auto = values.INELIGIBLE

    if request.get(fields.HOUSE) is None:
        response.home = values.INELIGIBLE

    return context