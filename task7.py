import random
import matplotlib.pyplot as plt

def roll_dice():
    return random.randint(1, 6)

def monte_carlo_simulation(num_trials):
    results = {}
    for _ in range(num_trials):
        roll_sum = roll_dice() + roll_dice()
        results[roll_sum] = results.get(roll_sum, 0) + 1
    
    probabilities = {k: v / num_trials for k, v in results.items()}
    return probabilities

def plot_probabilities(probabilities):
    plt.bar(probabilities.keys(), probabilities.values(), color='skyblue')
    plt.xlabel('Sum of Dice')
    plt.ylabel('Probability')
    plt.title('Probabilities of Dice Sum')
    plt.xticks(range(2, 13))
    plt.show()

def main():
    num_trials = 10000
    probabilities = monte_carlo_simulation(num_trials)
    plot_probabilities(probabilities)

if __name__ == "__main__":
    main()
