# Python Deliberate Practice

## Performance Outcomes
The over-arching goal is to build a reputation of reliability & quality by improving my [software development skills](http://treycausey.com/software_dev_skills.html) for data science. 

To achieve a higher bar in quality, this includes: 

**1. Write elegant, production-level python code**: Write read-able code that's clean, modular and re-usable. Elegant code should follow PEP8 standards and be using the best python practices. Cleanliness will also reduce the number of errors and make others' lives easier. 

**2. Reduce the number of errors by incorporating defensive programming**: Defensive programming include asserts, logging, and unit tests. This is important because producing error-free analysis is what will build trust with partners while opening up more opportunities for future projects. 

**3. Accelerate code speed**: Improving code speed will be broken down into a few components:
- Solving problems quickly 
- Distributed Computing
- Understanding different runtimes 

## Project Outcomes 

**November**: Productionize dash_ml interpretability package

**December**: Build an end-to-end ML pipeline in Spark 

## Skill De-Construction 
#### 1. Clean, Pythonic Code [11/3 to 11/10]
Key here will be to remove bad habits from my programming, make my code legible and easy to understand. 

Resources:
- [Clean Python - Chapter 1](https://www.amazon.com/dp/1788996666?aaxitk=O0D8QewWcjJgRm12H9gWAw&pd_rd_i=1788996666&pf_rd_p=44fc3e0f-4b9e-4ed8-b33b-363a7257163d&hsa_cr_id=4159268800601&sb-ci-n=asinImage&sb-ci-v=https%3A%2F%2Fm.media-amazon.com%2Fimages%2FI%2F71aUCNW6ONL.jpg&sb-ci-a=1788996666)
- [Clean Code in Jupyter Notebooks](https://www.youtube.com/watch?time_continue=390&v=2QLgf2YLlus)
- [Data Scientists, Your Variable Names Suck. Here's how to fix them](https://towardsdatascience.com/data-scientists-your-variable-names-are-awful-heres-how-to-fix-them-89053d2855be)
- [Pylint & Other Linting Tools](https://www.codementor.io/satwikkansal/python-practices-for-efficient-code-performance-memory-and-usability-aze6oiq65)
- [Coding Habits for Data Scientists](https://www.thoughtworks.com/insights/blog/coding-habits-data-scientists)

Method of Learning/Training:
1. Read Clean Python + Clean Code in Jupyter Notebooks [20 minutes]
2. Code Review + Rewrite code in at least one notebook according to PEP8 style [20 minutes] 
3. Active Recall on prior concepts [20 minutes] 
4. Commit code to Github [1 minute] 

Specific Outcome: Write a blog post detailing best practices for writing clean python code. 

<p>

**2. Writing Better Functions/Classes [11/10 to 11/17]** - Improve the quality, effectiveness of the functions, classes I write. 

Resources: 
- [Clean Python - Chapter 3](https://www.amazon.com/dp/1788996666?aaxitk=O0D8QewWcjJgRm12H9gWAw&pd_rd_i=1788996666&pf_rd_p=44fc3e0f-4b9e-4ed8-b33b-363a7257163d&hsa_cr_id=4159268800601&sb-ci-n=asinImage&sb-ci-v=https%3A%2F%2Fm.media-amazon.com%2Fimages%2FI%2F71aUCNW6ONL.jpg&sb-ci-a=1788996666)
- [Top 10 Tips & Tricks for Writing Better Code](https://www.youtube.com/watch?v=C-gEQdGVXbk)
- [Sci-Kit Learn Source code](https://github.com/scikit-learn/scikit-learn/tree/master/sklearn)

Method of Learning
1. Read Clean Python - Ch. 3 [20 minutes] 
2. Interpretability Class [40 minutes] 
- Write code for interpretability class 
- Get Stuck 
- Identify concept to get unstuck 
- Understand the concept
3. Reflection + Plan Next Session [5 minutes] 

Try this for a few days. If this doesn't work, then spend the entire time working on step 2. 

<p>

**3. Debugging/Testing in Python[11/17 to 11/24]** - Key here will be to reduce the number of errors in my code. 

Resources:
- [Clean Python - Chapter 6](https://www.amazon.com/dp/1788996666?aaxitk=O0D8QewWcjJgRm12H9gWAw&pd_rd_i=1788996666&pf_rd_p=44fc3e0f-4b9e-4ed8-b33b-363a7257163d&hsa_cr_id=4159268800601&sb-ci-n=asinImage&sb-ci-v=https%3A%2F%2Fm.media-amazon.com%2Fimages%2FI%2F71aUCNW6ONL.jpg&sb-ci-a=1788996666)
- [Improve Your Python Understanding - Jeff Knupp](https://jeffknupp.com/blog/2013/12/09/improve-your-python-understanding-unit-testing) 
- [How to Conduct Code Reviews](https://www.kevinlondon.com/2015/05/05/code-review-best-practices.html)

Method of Learning
1. Read Clean Python - Debugging/Testing or Read Scikit Learn Test Cases 
2. Interpretability Class [40 minutes] 
- Write code for interpretability class 
- Get Stuck 
- Identify concept to get unstuck 
- Understand the concept
3. Reflection + Plan Next Session [5 minutes] 

Specific Outcome - Write Unit Tests for Interpretability class 

**4. Project - Productionize Interpretability Class or write Diff-in-Diff Library [11/24 to 11/31]** - Interpretability Class is already written. Re-writing dash_ml will likely be too much to take on. However, improving upon the interpretability class will allow me to apply everything learned in the prior three weeks. It'll also force me to get feedback from co-workers. 

Method of Learning
1. Write code for interpretability class 
2. Get Stuck 
3. Identify concept to get unstuck 
4. Understand the concept

**5. Python Runtimes [12/1 to 12/8]**  - Understand Big Oh notation and the speed of different implementations. Key here is to better understand how code runs underneath the hood so I can speed up my code. 

Resources:
- [MIT's Intro to Computer Science & Programming](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/lecture-slides-code/MIT6_0001F16_Lec10.pdf)
- Leetcode

Method of Learning
1. Read/Watch MIT Open Courseware Lecture [60 minutes]
2. Add notes into Anki 
3. Active Recall on key concepts [10 minutes]
4. Leetcode Problem + Optimize for Run-time[30 to 40 minutes]
5. Commit my code to Github 

**6. Distributed Computing [12/8 to 12/31]** - Note: This is subject to change. The purpose here is to understand how to significantly accelerate the speed of my code. This can include:
- PySpark
- Pandas UDF's

Resources:
- [DataCamp's PySpark Course](https://www.datacamp.com/courses/introduction-to-pyspark)

*Specific Outcome* - Build an end to end ML pipeline using PySpark or Spark

**Implementing ML Algorithms from Scratch** - Write my own implementation of popular machine learning algorithms. This'll force me to deeply understand the models I'm using while also forcing me to write good code. 

**Git/Version Control** - Expand my current knowledge of different git commands. 

**Linux/Unix Commands** - Expand my current knowledge of different linux commands. 

**Sublime Shortcuts** - Learn all the important shortcuts in sublime text editor. 

## Scheduling 

![schedule_1](/img/schedule_1.png)

Key decisions:
- Will I do this in the morning or at night? **Morning**
- If I do it in the morning, when/how will I commute to work? **boosted board or scooter**. this would significantly reduce my commute to about 15 minutes. 

## Test Week [11/3 to 11/10] - Pythonic Code 
- Reevaluate on 11/10 on effectiveness of this plan. 

