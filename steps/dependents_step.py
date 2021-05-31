def do_step(context):
    request = context.request
    dependents = request['dependents']

    if dependents > 0:
        context.disability.increase(1)
        context.life.increase(1)

    return context