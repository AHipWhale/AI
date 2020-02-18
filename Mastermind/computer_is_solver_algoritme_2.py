import random


steps = []
for plays in range(50):
    def all_possibilities():
        lst1 = [1, 2, 3, 4, 5, 6]

        all_pos = [[a, b, c, d] for a in lst1 for b in lst1
                   for c in lst1 for d in lst1] # alle mogelijke combinaties
        return all_pos

    all_pos1 = all_possibilities()
    all_pos2 = all_possibilities()

    def black_pins(guess, solution):
        counter = 0
        for pin in range(len(guess)):
            if guess[pin] == solution[pin]:
                counter += 1
        return counter


    def white_pins(guess, solution):
        temp_solution = solution[:]
        counter = 0
        for pin in guess:
            if pin in temp_solution:
                temp_solution.remove(pin) # voorkomt dat er een witte pin wordt toegevoegd doordat een kleur die vaker
                                            # voorkomt in guess een kleur is die minder vaak voorkomt in de solution
                counter += 1
        return counter


    def feedback(guess, solution):
        white = white_pins(guess, solution)
        black = black_pins(guess, solution)
        white -= black  # als een pin zwart is hij in dit algoritme ook wit
        return [black, white]


    def remover(all_pos1, solution, guess):
        for i in all_pos1[:]:
            if feedback(guess, i) != feedback(guess, solution):
                all_pos1.remove(i)
        print(len(all_pos1))
        return all_pos1


    def graph(all_pos1, all_pos2):
        maximum = {}
        antwoord = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (3, 0), (4, 0)]
        for i in all_pos2:
            terug = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for j in all_pos1:
                x = feedback(i, j)
                for code in range(len(terug)
                if x == antwoord[code]:
                    terug[code] += 1
                                  
            #temp_lijst = [str(i), nul_nul, nul_een, nul_twee, nul_drie, nul_vier, een_nul, een_een, een_twee, een_drie, twee_nul, twee_een, twee_twee, drie_nul, vier_nul]
            update = {tuple(i) : max(terug)}
            maximum.update(update)
        next_guess = list(min(maximum, key=maximum.get))
        return next_guess



    def play(all_pos1, all_pos2):
        count = 0
        solution = []
        for i in range(0, 4):
            solution.append(random.randrange(1, 7))
        print(solution)
        next_guess = [1, 1, 2, 2]
        while next_guess != solution:
            count += 1
            if len(all_pos1) == 1:
                next_guess = all_pos1[0]
                print('solution is: ' + str(next_guess))
            else:
                remover(all_pos1, solution, next_guess)
                next_guess = graph(all_pos1, all_pos2)
        print('In {} stappen.'.format(count))
        return count

    steps.append(play(all_pos1, all_pos2))

print(steps)
print('minimale aantal stappen = ' + str(min(steps)))
print('maximale aantal stappen = ' + str(max(steps)))
print('gemiddeld aantal stappen = ' + str(sum(steps)/len(steps)))
