from src.constants import values
from src.dtos.score import Score

def to_score(context):
    score = context.response

    score.auto = calculate_plan(score.auto, context.auto.value)
    score.home = calculate_plan(score.home, context.home.value)
    score.disability = calculate_plan(score.disability, context.disability.value)
    score.life = calculate_plan(score.life, context.life.value)

    return score

def calculate_plan(existing_plan, calculated_value):
    if existing_plan == values.INELIGIBLE:
        return existing_plan
    
    if calculated_value <= 0:
        return values.ECONOMIC

    if calculated_value >= 3:
        return values.RESPONSIBLE

    return values.REGULAR