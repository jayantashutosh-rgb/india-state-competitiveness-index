# State Clustering Notes (Notebook 10)
India State Competitiveness Index (ISCI)

---

## What this notebook is for

This notebook groups states into types. Notebook 09 compared groups that we chose, like
region or coast. This notebook does something different: it lets the data decide the
groups. It puts states with similar scores together, without using any list we made in
advance.

## Why this notebook was needed

So far we ranked states and compared them. But we did not know if states fall into natural
types. Do the strong states all look alike? Is there a middle type? This notebook answers
that. It shows whether the 33 states form a few clear kinds of states.

## What we learned

We found three clear types of states. One important finding is that the middle type has
good basic conditions but weak industry. This told us that the main thing pulling the
middle states down is industry, not their basic conditions.

## How the grouping works, in simple words

- We use only the two measured parts: Factor Conditions and Related & Supporting
  Industries. We do not use region, population or income.
- We use a method called K-means. It looks at the scores and puts states that are close
  together into the same group.
- We first put both parts on the same scale, so the part with the wider spread does not
  have more influence on the grouping than the other part.

## What each cell does and what it found

- Setup:
  Opens the two part-scores for the 33 ranked states and puts them on the same scale.
  Found: 33 states are ready to group.

- Choose the number of groups:
  Tries 2, 3, 4 and 5 groups. It checks two things for each: how tight the groups are
  (inertia) and how well separated they are (the silhouette score).
  Found: two groups had the best score, but only split states into strong and weak. Three
  groups scored almost as well, but they showed a clearer middle type. So we picked three.

- Make the groups and name them:
  Makes three groups, looks at the average scores of each, and names them from those
  scores.
  Found: the three types are "Strong on both parts", "Strong basic conditions, weaker
  industry", and "Weak on both parts".

- Group summary:
  Shows one row per group with the number of states and the average scores and rank.
  Found: the average rank is about 7 for the strong group, 17 for the middle group and 26
  for the weak group.

- Scatter plot:
  Draws every state by its two part-scores, with a colour for each group.
  Found: states with similar scores appear close together, forming three clear groups.

## What we understood overall

- The 33 states form three clear types, not a random spread.
- The top type is strong on both parts, and best on industry.
- The middle type has good basic conditions but weak industry. Its basic conditions are
  about as high as the top type. The only real difference is industry.
- The weak type is low on both parts.
- No group has weak basic conditions and strong industry. This pattern appears both in the
  groups and in the individual states.

## FAQ

### General

What is clustering?
Putting things that are alike into the same group. Here we group states that have similar
scores.

Why not decide the groups ourselves?
Because we wanted the groups to come from the data, not from our expectations. If we named
the groups first, we might miss something the data shows.

Does this notebook change the index?
No. It only reads the Version 1.0 results and groups the states.

Does it give advice or reasons?
No. It only says which states look alike and which look different. Reasons and advice come
in the later notebooks.

### The method

What is K-means?
A common grouping method. You tell it how many groups you want, and it puts each state
into the nearest group by score.

Why put both parts on the same scale?
One part (industry) is more spread out than the other. Without scaling, it would decide
the groups almost by itself. Scaling gives both parts a fair say.

What is the silhouette score?
A number from -1 to 1 that shows how well separated the groups are. Higher is better.

What is inertia?
A number that shows how tight the groups are. Lower means the states in a group are closer
together.

### Choosing the number of groups

Two groups had the best score. Why did you use three?
Two groups only split states into strong and weak. Three groups scored almost as well and
showed a clear middle type. Because the goal is to explain the results, three groups is
more useful.

Are three groups the only right answer?
No. Two, four and five groups are also possible. Three simply gives the clearest and
simplest split for this data. Different studies may choose a different number of groups
depending on their goal.

### The groups

Why does the middle group stand out?
Its basic conditions are as strong as the top group, but its industry is much weaker. So
industry is what sets it apart from the top.

What does "No group has weak basic conditions and strong industry" mean?
No group of states is weak on basic conditions while being strong on industry. This is an
observation from the data. It does not tell us why.

### Next

What happens after this notebook?
Notebook 11 measures the gaps: how far each state is from the top, and what it would need
to improve.
