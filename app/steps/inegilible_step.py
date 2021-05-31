def do_step(context):
    request = context.request
    response = context.response

    if request['income'] == 0:
        response.disability = "ineligible"

    if request.get('vehicle') is None:
        response.auto = "ineligible"

    if request.get('house') is None:
        response.home = "ineligible"

    return context