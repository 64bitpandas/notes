## Introduction

> [!warning] Warning
>
> This page was originally written in Fall 2021. It is likely outdated. Please ask your TA for the latest information!


I get asked a lot about whether I have any advice for doing well on 61A exams, so I thought it would be nice to type some of it out. The following is my opinion/experience only, so feel free to ignore some or all of it if something else is more effective for you!

For a more complete guide, please visit [https://cs61a.org/articles/studying/](https://cs61a.org/articles/studying/)!

## General Info

- Midterm 1 is *very early* in the semester. The purpose of this is to allow you the option of using the midterm as feedback in case you are considering switching to CS10, CS88, etc.
- Exams emphasize material covered more recently, but due to the highly cumulative nature of the course you should expect anything you’ve seen so far to appear.
- Exams generally have three parts:
    - **What Would Python Do (WWPD)-** similar to WWPD in labs, where you’re given some code and asked about the output/behavior of the code.
    - **Environment Diagram-** typically 1 per exam. These are very similar to the ED’s we do in lecture and discussion, but may be more difficult.
    - **Code-writing-** typically ~2-3 per midterm, slightly more for the final. Nearly all exam-type coding problems are fill in the blank, either with multiple choice or short answer.
- Midterm 1 is worth 40 points, midterm 2 is worth 50, and the final is worth 75. This means that it’s totally ok if you don’t do as well as you’d like early in the semester!
- The average score for exams is usually somewhere around 55-65% of full score. 61A exams are not curved.

## Topics

### Midterm 1

- Control statements (if, while)
    - Digit chopping (`%` and `//` to process large integers using `while`)
- Booleans and conditional statements (and, or, not; short circuiting)
- Environment diagrams
- Higher order functions (passing in or receiving another function as a parameter)
- Lambda functions

### Midterm 2

- Recursion and tree recursion
    - Partition problems (count coins)
- Iterators and Generators (yield, yield from)
- Lists and mutability
    - Append vs extend, pop vs remove
    - List slicing
- Trees
- Object Oriented Programming
- Linked Lists
- Less emphasized: efficiency, string representation (str, repr)

### Final

- Everything from MT1 and MT2
- Interpreters
    - REPL
    - Scheme project design
    - Eval/apply
- Scheme
- Regex
- BNF

## Suggested Timeline

Here's how I study for 61A exams, and CS exams in general. This might not work for you though, so don't be afraid to experiment and come up with your own list of priorities!

**3-5 days before exam:** 

1. Make sure you've watched all of the lectures and caught up on homeworks, labs, etc. I think a lot of students underestimate how important it is to attempt all of the problems: they're given for a reason, and many exam problems will feel very familiar if you understand the homework problems (for example, the pattern of splitting large numbers with `%` and `//` will almost certainly show up on the exam).
2. Even if it's not required, make a **written** cheat sheet to summarize the most important topics on the exam. I find that typing out notes isn't quite enough for it to sink in, and leaves room for a lot of detrimental shortcuts (copy pasting, linking to existing resources, etc.) It's actually a good sign if you end up not using your cheat sheet at all during the exam, since that means you've internalized everything on it already!

**After the above steps are completed:**

1. Attempt a past semester's exam untimed and with external help (friends, your cheat sheet, Google...). This will give you a taste of the exam's content without making you feel overwhelmed or discouraged at being unable to complete problems on your own just yet.
2. Carefully review the solutions to the exam after you're done, and make a note of all the problems and topics you need to work on. If needed, add more items to your cheat sheet or re-watch past lectures to gain a better understanding of the topic.
3. If you still have time, you can repeat steps 1-2 a couple more times until you feel confident in your ability to solve problems on the exam!
4. Try at least one exam in a more formal setting (timed, no distractions, using only the resources allowed on the actual exam).

## Mental Health

I would argue that especially for CS exams that involve complex problem-solving, feeling your best during the exam is more important than studying after a few hours of practice. Here are some things I always try my best to do:

- **Talk to someone and bounce ideas around before the exam.** This could be a friend, lab partner, TA during office hours, or even a [rubber duck](https://medium.com/@katiebrouwers/why-rubber-ducking-is-one-of-your-greatest-resources-as-a-developer-99ac0ee5b70a#:~:text=By%20definition%2C%20rubber%20ducking%20is,a%20method%20of%20debugging%20code.&text=Very%20often%2C%20by%20rubber%20ducking,to%20do%20any%20Googling%20whatsoever.)! Being able to communicate your strengths, weaknesses, and concerns helps greatly in identifying a battle plan for upcoming studying sessions.
- **Get 8-9 hours of sleep before the exam.** Even if you're still in the middle of studying, just drop everything and go sleep! I've found that it improves performance far more than that extra hour or two of studying would ever do.
- **Take a break immediately before the exam.** If you study right up until exam time, you will risk burning out. Take a walk, grab some boba, play some games, read a book, do some push ups- doesn't matter, as long as you're not thinking about 61A or coding in any way.
- **Expect the worst, hope for the best!** Do whatever you need to in order to stay as relaxed as possible during the exam. Set a low bar for yourself (e.g. you'll try to complete 1 problem at least), and feel good about doing more than that! If you ever blank out, you'll have your cheat sheet to get you un-stuck :)
- **If you're feeling unwell, don't take the exam!!** We will likely excuse you from this midterm, and your score will be replaced by some function of your MT2 and final scores. You are also welcome to request to take the exam remotely if you are experiencing symptoms but otherwise feel ok.

And last of all, remember that the exam is far more inconsequential than you might think, so as long as you show up, do your best, and have fun (honestly, 61A tests are kinda fun without all the stress), everything will be ok!

- For intended-CS stressed about that 3.3 GPA: students consistently get higher grades in 61B than 61A, so you can likely declare even if you don't do as well as you'd like in 61A.
- For those who just want to pass: exams aren't worth a whole lot, and there are plenty of opportunities for extra credit / recovery, so as long as you turn in *something* and be diligent in completing homeworks/labs/projects you will pass!

## During the Exam

- **Remember your data types!!!!** The one trick that almost singlehandedly got me through 61A exams: before filling out a problem of any kind, read through the code and label any variables, fill-in-the-blank lines, parameters, and return values with what type of object you think they should be (e.g. number, function, string, list...). This will make it much easier to figure out what is happening, especially for reverse ED's and skeleton code problems, since you have now severely restricted the possible answers to each blank.
    - This also applies for homeworks/labs/projects. Data type mismatches are by far the most common issues that I see when helping out during office hours.
- **Try to attempt every problem first, before going back to fix your answers.** A blank box is instantly worth 0 points- and oftentimes your split-second intuition can really come in handy for coming up with solutions that are *almost* correct in very little time.
- **Don't panic!** The midterm's not really that important (as explained above). If something does go wrong during or before the exam that prevents you from doing your best work, you can also contact us (61A staff) to discuss further arrangements.

## FAQ

(Will be populated as more questions arise)

**Q:** How many practice exams should I do?

**A:** As many or few as feels most comfortable for you, but remember that quality > quantity for practice. It's better to do fewer and really understand them, rather than rushing through like 10. I typically do 2-3 for CS courses.

**Q:** This midterm was easier/harder than expected, will the next exam be harder/easier as a result?

**A:** Due to phenomenon of [regression to the mean](https://fs.blog/regression-to-the-mean/), it’s actually more likely than not that this will occur, but not by any intentional acts of malice. Basically, if you took an unusually difficult exam, the next one will probably be more average in difficulty, and thus feel easier than the last one.

**Q:** Will ____ be emphasized on the midterm?

**A:** Not sure; I don’t write the exam. If it was emphasized on previous exams, OR it was specifically mentioned by TA's or the instructor that it would be on the exam, then the likelihood that it will be on this exam is high.

**GLHF!** 🥰