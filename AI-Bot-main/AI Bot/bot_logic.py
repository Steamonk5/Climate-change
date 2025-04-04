import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>123456789"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)


def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "ОРЕЛ"
    else:
        return "РЕШКА"
    


def get_random_fact():
    facts = ["В результате добычи угля, нефти и газа ежегодно в атмосферу выбрасываются миллиарды тонн углекислого газа.",
         "Вместе с тем если мы не замедлим темпы глобальных выбросов, то к 2100 году температура может подняться до 3° С сверх доиндустриальных уровней, что нанесет дополнительный непоправимый ущерб нашим экосистемам.",
         "Если не принять никаких мер, то целые районы Нью-Йорка, Шанхая, Абу-Даби, Осаки, Рио-де-Жанейро и многих других городов могут уйти под воду уже на нашем веку, что приведет к перемещению миллионов людей.",
         "Засухи могут вызывать разрушительные песчаные и пыльные бури, способные перемещать миллиарды тонн песка через континенты.",
         "В настоящее время 90 процентов стихийных бедствий классифицируются как связанные с погодой и климатом, и наносимый ими мировой экономике ущерб оценивается в 520 млрд долл. США в год, в результате чего 26 миллионов человек оказываются в нищете."]
    return random.choice(facts)