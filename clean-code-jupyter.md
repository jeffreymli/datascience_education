# Clean Code in Jupyter notebooks, using Python 

[Link to lecture](https://www.youtube.com/watch?v=2QLgf2YLlus&t=1904s)

## Why we end-up with messy jupyter notebooks? 

" Any fool can write code that a computer can understand. Good programmers write cod that humans can understand " - Kent Beck

Jupyter notebooks are written for *others* to understand. 

We don't write clean code because we don't think anyone else is going to use it. 

## What is Clean Code?
- Clean cod reads like well written prose

## Steps
1. First, make it work
2. Make it right
3. Then, make it fast and small 

1. Run all the tests
2. Remove duplicate code
3. Express all the ideas
4. Minimize classes and methods 

Leave the campground cleaner than you found it -> After reading code, make it **cleaner** than you found it. 

## Naming Things 
- long_descriptive_names -> Comes from Objective C 
	- Avoid x, i, stuff, avoid very short names 

- Pronounceable and searchable

- Avoid encodings, abbreviations, prefixes, suffixes.. if possible

- Add meaningful context
	- daily_revenue_per_payer

- Don't be lazy - Spend time naming and renaming things 

## Functions

- Small - Maximum **five lines long**. Maybe ten. 

- Do one thing

- One level of abstraction 

- Have only a few arguments (one is the best)

## Comments 

- When writing comments, first try to refactor the code so it's descriptive using variable names. 

- You should feel sorry that you're writing a comment. 

- Use good names

- Avoid obvious comments

- Dead Commented-out Code


"Long functions are where classes are trying to hide" - Robert C. Martin 

## How to write clean code? Specifically for Python 

- PEP 8 -- Style Guide or Google Python Style Guide

## How to write Clean Python Code in Jupyter Notebooks?

**Standard Python Notebook Structure** 

![ipython_notebook_structure](/img/ipython_notebook_structure.png)


**How big should a notebook file be?** 

One notebook file:
1. Hypothesis 
2. Data 
3. Interpretation 

One notebook file = One hypothesis

Keep notebooks small, (4 to 10 cells each)

Break fat notebooks into many small ones. For example 

`1_datapreparation.ipynb`

`2_linear_model.py`

`3_ensemble.py`

**Create a Shared Library** - Create a shared utils folder of the most common functions used.

**Don't be pythonic. Be IPYTHONIC.**

- Don't hide your recipe in an imported module. For example, your modeling technique.

"Clean code reads like well-written prose."

**How big should one cell be?**

- Each cell should have one logical output

**Write tests in jupyter notebooks** - Use pytest-ipynb 1.1.0

## Code Smells in ipynb

- Cells can't be executed in order (with runAll and Restart & RunAll)

- Mixing analysis w/ checking ideas. -> Duplicate the notebook.

- Debugging cells 

- Copy + Paste Cells

- Duplicate code

- Multiple notebooks that re-implement the same function

Another tip - **Run notebook from another notebook!** - Can pull another notebook and specify parameters to run through. 

Then, you can turn your notebook into a product -> Brilliant IPi widgets library

## Summary

1. Notebook should have one Hypothesis-Data-Interpretation loop

2. Make multi-project utils library

3. Good jupyter notebooks read like well-written prose

4. Each cell should have one and only one output

5. Write tests in notebooks

6. Deploy a shared Jupyter server

7. Keep code inside notebooks. Avoid refactoring to mdules, if possible.







