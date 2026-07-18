# Why Python Mattered

Every research project needs tools. This project used Python. Not because Python is
fashionable, but because the work would have been slow, difficult and easy to get wrong
without it. This note explains why Python was an important part of the project.

## The problem with doing it by hand

The main data source is a 472-page PDF. It has table after table, in different shapes and
units. Doing this by hand would mean copying thousands of numbers into a spreadsheet, one by
one.

Three things go wrong when you do that:

- Mistakes. Copying by hand always adds small errors, and they are hard to find later.
- No repeat. If the data changes next year, you have to do all the copying again.
- Hard to check. Nobody can see how a number was made, so nobody can trust it fully.

Excel is a very useful tool. It is excellent for small tables and quick analysis. The problem
begins when the work has to be repeated many times, or when the data comes from hundreds of
pages. That is where Python becomes more practical.

## Reading the PDFs

Excel cannot read a big PDF table on its own. Python can. The project uses a tool called
pdfplumber to open the PDF and pull the numbers out. Some tables are printed sideways or
across two pages. Python code was written to read even those.

Some tables also needed manual checking. Python made the work faster, but it did not remove
the need for careful review.

A wrong number is often worse than a missing number. Whenever Python could not read a table
correctly, the code stopped instead of guessing. This made the project more trustworthy.

## Cleaning and joining the data with Pandas

Pandas is a Python tool for working with tables. It did much of the work:

- Handle missing values, so gaps stay as gaps and are never filled with guesses.
- Fix data types, so numbers are treated as numbers.
- Fix the state names so every table uses the same list.
- Join many tables into one.
- Calculate the indicators, shares, densities and the final index score.
- Run checks on the values along the way.

All of this is written as code. So it runs the same way every time, with no hand-typing.

## What about SQL?

SQL is a language for asking questions from a database. It is very useful when the data is
huge. Here the data is small, only 36 states and union territories, so Pandas was enough and
a database was not needed. For a much larger version of this project, SQL would be a good
choice. It was not used here, and this note does not pretend it was.

## Grouping the states

To group the states into types, the project uses scikit-learn, another Python tool. It ran
the grouping method (K-means) and the checks that helped choose the number of groups. Doing
the calculations by hand would be slow and difficult, especially when trying different
numbers of groups.

## Charts

The charts were made with Matplotlib and Seaborn, two Python drawing tools. Every chart is
made by code, so it can be redrawn at any time and always looks the same.

## Why Jupyter Notebook

Jupyter lets you keep the code, the explanation and the result together, in one place, step
by step. So a reader can follow the work like a story: here is the step, here is the code,
here is what came out. This is why the whole project is written as notebooks.

## Automation

Because everything is code, the whole project can be run again from start to finish. Press
run, and the same result comes out. No copying, no hand-typing, no chance of a new mistake.

Automation also made future updates easy. When new government reports are published, the same
workflow can be run again instead of starting from the beginning.

Because the workflow is written as code, the project can also be improved step by step
without rebuilding everything from the beginning.

## Validation

Python also checked the work. The code compared many values against the printed source, and
stopped if a table did not read correctly. Later, the ranking was tested by changing some
choices to see if the result held.

The computer performs the same checks every time. Unlike manual work, it does not get tired
or forget a step.

## Reproducibility

Reproducibility means someone else can take the same data and the same code and get the same
answer. This is the heart of good research.

Think of it like following a recipe. If two people use the same ingredients and the same
recipe, they should get almost the same result. Good research works in the same way. Because
this project is all code and official data, it is reproducible.

## Markdown reports

The reports are written in Markdown, a simple text format. Plain text is easy to read, easy
to search, and easy to track over time. It also shows nicely on GitHub.

## Git and GitHub

Git keeps a history of every change, so you can see how the project grew. GitHub stores it
online, so others can read it, and the dates show when each part was done.

GitHub also lets other people inspect the work. They can read the code, check the methods and
suggest improvements. This is what open research looks like.

## What Python taught us

- Good research is repeatable.
- Small mistakes can become big mistakes.
- Clean data matters more than fancy analysis.
- Automation saves time.
- Validation builds trust.
- Code is easier to repeat than manual work.
- A wrong number is worse than a missing one.
- Documentation matters as much as the code.
- Open work makes research stronger.

## What Python gave this project

- It made a locked PDF of official data usable.
- It removed hand-copying and the errors that come with it.
- It made every step repeatable and checkable.
- It kept the code, the explanation and the results together.
- It let the work be shared openly.

Python turned a pile of government PDFs into a clear, open and reproducible study. That is
something a spreadsheet alone could not do.

Python did not replace economic theory. It helped us apply that theory carefully,
consistently and transparently. The theory came first. Python simply made it possible to
organise the data, check every step, and repeat the work in a transparent way.

Python answered the question of "how". Economic theory answered the question of "what". Both
were needed to complete this project.
