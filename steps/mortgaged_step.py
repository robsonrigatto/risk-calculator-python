def do_step(context):
    request = context.request
    house = request.get('house')

    if (house is not None) and (house['ownership_status'] == "mortgaged"):
        context.home.increase(1)
        context.disability.increase(1)        

    return context