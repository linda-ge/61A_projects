# 61A_projects
Projects I wrote for the Structure and Interpretation of Computer Programs class at UC Berkeley.

---

In chronological order:

1. **Hog**
  * I developed a simulator and multiple strategies for the dice game Hog, where two players alternate turns trying to be the first to end a turn with at least 100 total points. On each turn, the current player chooses some number of dice to roll, up to 10. That player's score for the turn is the sum of the dice outcomes.
  * This implementation has some special rules: 
    * *Pig Out.* If any of the dice outcomes is a 1, the current player's score for the turn is 1.
    * *Free Bacon.* A player who chooses to roll zero dice scores 2 more than the absolute difference between the digits in the opponent's total score.
    * *Swine Swap.* After points for the turn are added to the current player's score, if both scores are larger than 1 and either one of the scores is a positive integer multiple of the other, then the two scores are swapped.

2. **Maps**
  * I created a visualization of Berkeley restaurant ratings using machine learning and the Yelp academic dataset. The unsupervised learning phase was completed with k-means clustering, and the supervised learning phase was completed with least-squares linear regressions.
  
3. **Ants**
  * I created a tower defense game called Ants Vs. SomeBees, the concept of which was based off of PopCap Games' [Plants Vs. Zombies](https://www.ea.com/studios/popcap/plants-vs-zombies).
  * The project combines functional and object-oriented programming paradigms.
  
4. **Scheme**
  * I developed an interpreter for a subset of the Scheme language.
