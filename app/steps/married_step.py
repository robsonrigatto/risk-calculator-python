def do_step(context):
    request = context.request

    if request['marital_status'] == "married":
        context.life.increase(1)
        context.disability.decrease(1)        

    return context