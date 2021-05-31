from src.constants import fields

def do_step(context):
    request = context.request
    income = request[fields.INCOME]

    if income > 200000:
        context.auto.decrease(1)
        context.disability.decrease(1)
        context.home.decrease(1)
        context.life.decrease(1)

    return context