# LLMSQLProject
Purpose: To store players in a simple RPG video game with their stats, items, and progress.

Database Scheme:
![IMG_BC94CB94E9D7-1](https://github.com/user-attachments/assets/c0bc64a7-05f5-4562-bbf8-c23f3d89657c)

Each question has two outputs: zero-shot and single-domain-double-shot.
As you will see, the single-domain-double-shot got every question right while the zero-shot had a syntax error on one question.

Successful Question:
Q: Which player has the lowest level?
A1: The player with the lowest level is Hero1.
A2: Hero1 has the lowest level.

Unsuccessful Question:
I did not have a question that failed completely which surprised me!

Other Questions:
Q: What weapons does Hero1 have?
A1: Hero1 has two weapons: a Sword with 50 power for melee combat and a Bow with 35 power for ranged attacks.
A2: Hero1 has a sword and a bow.
Both Correct

Q: What mission is each player on?
A1: Hero1 is on a mission to Retrieve the Artifact, Warrior2 is tasked with Defeating the Dragon, and Mage3's mission is to Rescue the Princess.
A2: Hero1 is on a mission to Retrieve the Artifact, Warrior2 is tasked to Defeat the Dragon, and Mage3 is set out to Rescue the Princess.
Both Correct

Q: Who has the most money?
A1: Warrior2 has the most money.
A2: The individual identified as 'Warrior2' has the most money.
Both Correct

Q: Do any of the players have the same item?
A1: No, none of the players have the same item.
A2: No, none of the players have the same item.
Both Correct

Q: How much money will Warrior2 have after they complete the mission they are on?
A1: Syntax Error
A2: Warrior2 will have $750 after completing their mission. Correct!

Q: Who has the item that is closest to breaking and what is that item?
A1: Mage3 has a Magic Staff that is closest to breaking, with a durability of 75.
A2: Mage3 has a Magic Staff that's closest to breaking, with durability at 75.
Both Correct
