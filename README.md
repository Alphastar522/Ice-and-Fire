#**Pokéstat Calculator**#
This is a Python console application designed to calculate the final stats of a Pokémon based on its base stats, level, randomly generated hidden stats, and a user-provided battle record.

About
Have you ever wondered what your Pokémon's final stats would be without having to use an online calculator? This program simulates the process of training a Pokémon by allowing you to input the Pokémon you have defeated. It then calculates the final stats using the in-game formula, taking into account crucial factors like IVs, EVs, and nature.

Features
Wide Pokémon Selection: Includes all starter Pokémon from Generations 1 through 8, along with their full evolutionary lines.

Complete Eeveelution Logic: Specifically designed to handle all of Eevee's evolutions—including Vaporeon, Jolteon, Flareon, Espeon, Umbreon, Leafeon, Glaceon, and Sylveon.

Simulated Training: Input the Pokémon you've battled to accumulate Effort Values (EVs), with a cap of 510 total EVs.

Random Hidden Stats: The program generates a random Nature and Individual Values (IVs) for a realistic calculation.

Clear Output: Displays the Pokémon's name, level, nature, and the final calculated stats for all six categories (HP, Attack, Defense, Special Attack, Special Defense, Speed).

How to Use
To use this program, simply run the Python script. The application will guide you through the process with a series of prompts.

Select a Pokémon: Choose from the list of available starter Pokémon. For Eevee, the program will ask you about its evolution status later.

Enter Level: Input your Pokémon's current level (1-100).

Record Battles: Enter the names of the Pokémon you have defeated. The program will automatically tally the corresponding EVs. Type done when you are finished.

Eevee Evolution: If you chose Eevee, you will be prompted to select its evolutionary form from a numbered list.

View Stats: The program will then output a summary of your Pokémon's calculated final stats!

How it Works
The program uses the official Pokémon stat calculation formula, which is a standard for games from Generation 3 onward:

HP: floor(0.01 * (2 * Base + IV + floor(EV/4)) * Level) + Level + 10

Other Stats: floor(floor(0.01 * (2 * Base + IV + floor(EV/4)) * Level) + 5) * Nature

This program handles all the math for you, making it easy to see how different factors influence your Pokémon's performance.

License
This project is open-source and available under the MIT License.
