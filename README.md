# TRIE for Book Report - Because Shakespeare is Hard Enough Already

## What is This Thing?

Ever tried to write a book report on *Romeo and Juliet* and found yourself Googling "how to spell Montague" for the 47th time? Yeah, me too. 

This is a **completely over-engineered solution** to a simple problem: I can't spell Old English words. Instead of, you know, using a dictionary like a normal person, I built a Trie (prefix tree) data structure that autocompletes Shakespeare terms. Because why be normal when you can be *extra*?

## The Problem (AKA My Personal Tragedy)

Picture this: It's 2 AM. Your book report is due in 6 hours. You're trying to type "Wherefore art thou Romeo" but you keep typing "Werefor art thow Romayo". Your teacher is going to think you're illiterate. Your grade is doomed. Your future is crumbling.

**Enter: This ridiculous project.**

Now I have a program that reads the ENTIRE text of Romeo and Juliet and basically becomes my personal Shakespeare spell-checker. Take THAT, Old English!

## How This Madness Works

### The "Technology" (If We're Being Fancy)

1. **Feed the Beast**: The program slurps up the entire text of *Romeo and Juliet* like a data-hungry monster. Every. Single. Word.

2. **Build the Tree of Knowledge**: It creates a Trie (pronounced "try" but I call it "tree" because I do what I want), which is basically a fancy tree where:
   - Each character is a branch
   - Words are paths through the forest
   - The most common paths get VIP treatment

3. **The Magic Happens**: Type a few letters, and the program goes:
   - "Oh, you started with 'wher'? I got you fam."
   - *zooms through the tree*
   - "You probably mean 'wherefore' because that word shows up like a million times"
   - *returns the word like a boss*

### Why This is Actually Genius

Forget about guessing if it's "thou", "thee", or "thy" – the program knows exactly which one Shakespeare used most often. It's like having the Bard himself whisper in your ear, except less creepy and more algorithmic.
## How to Use This Masterpiece

1. **Fire it up**:
   ```bash
   python CODE/main.py
   ```

2. **Start typing like you're having a stroke**:
   ```
   ENTER THE WORD TO FIND MATCH: wher
   ```

3. **Watch the magic unfold**:
   ```
   wherefore
   ```
   
   *Chef's kiss* 👨‍🍳

(Note: Program may judge your spelling. It's fine. We all need tough love sometimes.)et the autocomplete suggestion**:
## Future Plans (AKA The Dream)

Imagine this: You're typing your book report in the terminal, and every time you start butchering a Shakespeare word, you just smash Tab and **BOOM** – autocomplete saves your GPA.

**The Vision**:
- Background process that stalks your typing (in a non-creepy way)
- Press Tab (or any cool key combo)
- Instant autocomplete like you're using a modern IDE, except it's for 400-year-old English
## What's Actually in Here

- `CODE/TRIES.py` - The brain of the operation (a.k.a. the Trie class that does all the heavy lifting)
- `CODE/main.py` - The simple interface that makes everything work
- `romeo_juliet.txt` - Shakespeare's entire play, now serving as my personal dictionary

## The Real Talk

Look, this is a **just-for-fun project** born from procrastination and desperation. Is it overkill? Absolutely. Could I have just used Google? Sure. But where's the fun in that?

This is what happens when a programmer has a book report due and decides to make their problem everyone else's solution. You're welcome.

Feel free to fork this for other texts! Maybe make one for *Hamlet* or *Macbeth*. Or the tax code. Actually, please make one for the tax code.

---

### In Conclusion

*"To spell, or not to spell, that is the question—*  
*Whether 'tis nobler in the mind to suffer*  
*The slings and arrows of outrageous autocorrect,*  
*Or to take arms against a sea of typos*  
*And by a Trie data structure, end them."*

**– Shakespeare, probably, if he knew what a Trie was** 🎭✨

(Spoiler: He didn't. But I bet he would've loved it.)
- `romeo_juliet.txt` - The complete text of Romeo and Juliet

## Just for Fun

This project was created purely for fun and personal use. It's a practical application of data structures to solve a real (if somewhat niche) problem. Feel free to adapt it for other texts or use cases!

---

*"What's in a name? That which we call a rose by any other name would smell as sweet... but it would still be hard to spell."* 🎭