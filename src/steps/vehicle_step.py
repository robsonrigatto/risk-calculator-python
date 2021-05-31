from src.constants import fields
import datetime

def do_step(context):
    request = context.request
    vehicle = request.get(fields.VEHICLE)

    if vehicle is None:
        return context

    current_time = datetime.datetime.now()
    current_year = current_time.year

    difference = current_year - vehicle[fields.YEAR]

    if difference <= 5:
        context.auto.increase(1)

    return context