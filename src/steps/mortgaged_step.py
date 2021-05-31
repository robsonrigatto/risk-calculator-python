from src.constants import fields, values

def do_step(context):
    request = context.request
    house = request.get(fields.HOUSE)

    if (house is not None) and (house[fields.OWNERSHIP_STATUS] == values.MORTGAGED):
        context.home.increase(1)
        context.disability.increase(1)        

    return context