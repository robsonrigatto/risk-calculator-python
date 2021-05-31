from src.constants import fields, values

def do_step(context):
    request = context.request
    response = context.response

    age = request[fields.AGE]

    if age > 60:
        response.disability = values.INELIGIBLE
        response.life = values.INELIGIBLE

    if age < 30:
        context.auto.decrease(2)
        context.disability.decrease(2)
        context.home.decrease(2)
        context.life.decrease(2)

    if age >= 30 and age <= 40:
        context.auto.decrease(1)
        context.disability.decrease(1)
        context.home.decrease(1)
        context.life.decrease(1)

    return context