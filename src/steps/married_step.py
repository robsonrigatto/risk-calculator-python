from src.constants import fields, values

def do_step(context):
    request = context.request

    if request[fields.MARITAL_STATUS] == values.MARRIED:
        context.life.increase(1)
        context.disability.decrease(1)        

    return context