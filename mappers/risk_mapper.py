from dtos.score import Score

def to_score(context):
    score = context.response

    score.auto = calculate_plan(score.auto, context.auto.value)
    score.home = calculate_plan(score.home, context.home.value)
    score.disability = calculate_plan(score.disability, context.disability.value)
    score.life = calculate_plan(score.life, context.life.value)

    return score

def calculate_plan(existing_plan, calculated_value):
    if existing_plan == "ineligible":
        return existing_plan
    
    if calculated_value <= 0:
        return "economic"

    if calculated_value >= 3:
        return "responsible"

    return "regular"