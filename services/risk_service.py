from dtos.context import Context
from steps import age_step, dependents_step, income_step, inegilible_step, married_step, mortgaged_step, vehicle_step
from mappers import risk_mapper

all_steps = [age_step, dependents_step, income_step, inegilible_step, married_step, mortgaged_step, vehicle_step]

def calculate(request):
    questions = request['risk_questions']
    base_score = sum(questions)

    context = Context(request, base_score)

    for step in all_steps:
        context = step.do_step(context)

    score = risk_mapper.to_score(context)
    return score