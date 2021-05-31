def do_step(context):
    request = context.request
    income = request['income']

    if income > 200000:
        context.auto.decrease(1)
        context.disability.decrease(1)
        context.home.decrease(1)
        context.life.increase(1)

    return context