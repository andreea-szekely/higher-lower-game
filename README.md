# Higher-lower guessing game 🏆📱

## The Game

In this game, the user will be presented with two entities at a time, each represented by a dictionary. The dictionary includes the following information for each entity:

- **Name**: The entity's name, e.g., "Instagram."
- **Follower Count**: The number of followers on Instagram, e.g., 346.
- **Description**: A brief description of the entity, e.g., "Social media platform."
- **Country**: The country of origin, e.g., "United States."

The user's goal is to guess which of the two entities has more Instagram followers. The game will display the information for both entities, and the player will type 'A' if they think the first entity disaplayed has more followers or 'B' if they believe the second entity has the higher follower count.

## How to Play

1. The game shuffles the entities to provide a different challenge each time the user plays.
2. The user starts with a score of 0.
3. For each comparison, the user sees the following information:
   - Entity A: Name, Description, and Country
   - Entity B: Name, Description, and Country
4. The user will type 'A' or 'B' to make a choice.
5. If the guess is correct, the user's score increases, and the game continues with a new comparison.
6. If the guess is incorrect, the game ends, and the user's final score is displayed.

## Purpose

This conding challenge served a dual purpose:

1. **Learning Python**: This game offered a great opportunity to learn and practice Python programming while working with loops, dictionaries, conditional statements, and user input.

2. **Game Design**: It was actually interesting to figure out which comparison to display next based on how the data is modeled.
