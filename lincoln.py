import matplotlib.pyplot as plt
import random, time, sys
from datetime import timedelta

def main(pop, rate):
    global start_time
    global estimates
    global number

    size = pop
    iterations = 100
    rate = rate
        
    percentage = rate
    percentage_2 = rate
    
    start_time = time.time()

    estimates = []

    a = 0
    while a < iterations:
        try:
            population = {}
            number = size
            number += 1

            for i in range(0, number):
                population[i] = 0

            marked = []
            
            collect = int((number / 100) * percentage)

            for i in range(0, collect):
                f = random.randint(0, number)
                marked.append(f)
                population[f] = 1

            match = []
            
            collect_2 = int((number / 100) * percentage_2)

            for i in range(0, collect_2):
                f = random.randint(0, number)
                if population[f] == 1:
                    match.append(f)

            try:
                lincoln = ((collect * collect_2) / (len(match)))

                estimates.append(lincoln)

            except ZeroDivisionError:
                lincoln = “No matches”

            print("\n[+] marked: ", len(marked))
            print("[+] collected: ", collect_2)
            print("[+] match: ", len(match))
            print("[+] population: ", (number - 1))
            print("[*] lincoln index estimates: ", lincoln)

            a += 1
            
        except KeyError:
            pass

def processing(estimates, number, start_time):
    total = 0
    for i in estimates:
        total += i

    average = (total / len(estimates)

    precision = ((average * 100) / (number - 1))

    if precision < 100 and precision > 0:
        precision = precision
    else:
        precision = (100 - (precision - 100))

    print("\nPrecision: {}%".format(int(precision)))

    elapsed_time = time.time() - start_time
    times = str(timedelta(seconds=elapsed_time))
    print("\nTime Elapsed:", str(times))

    return precision

results_effort = []
results_pop = []

def studies():
    for i in range(1,101):
        main(10000, i)
        results_effort.append(processing(estimates, number, start_time))
    for i in range(1,1001):
        main(i, 10)
        results_effort.append(processing(estimates, number, start_time))
