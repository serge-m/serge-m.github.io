Title: why does your data science project fail again
Author: SergeM
Date: 2017-10-29 23:50
Slug: why-does-your-data-science-project-fail-again.md
Tags: data science, project management,work in progress

[Work in progress]

# why does your data science project fail again


You work in a mid size company. Business goes well. Engineering department is split into many small teams. One of them works on data intense project. Like rooting of parcels from a warehouse or demand prediction for millions of sales per month. Everything is ok, but upgrading from very basic algorithm that is here from the beginning fails miserably. Maybe it fails multiple times in a row. Changing leads and even heads of the department doesn't help. 

Well old system works. It is obsolete, too slow, has bad precision but the team


# your data scientists aren't real scientists
For example, science differs from non-science by writing down the results. 
Maybe your data scientists just talks about awesomeness of his new model and doesn't provide you with written reports and measurements? Then probably you will go in circles of to the dead end. 

No progress proven == no need for changes at all.


# you don't perform reproducible experiments

reproducible experiments allow you to compare your old solution with a new one. If you can run the new algorithm on current data only it is not a proof that it works. It can be really a coincidence.

# you don't measure your performance
 
You just build a new algorithm and you think it is better because it is a) optimal by design b) robust c) easy to build d) reduces technical depth e) based on a new cool technology f) reduces the coupling g) but you version here. 

It is not a proof! Probably you lie!

# you have only engineers in your team
Many tasks cannot be done by pure engineers. These guys can build robust architectures, they write reliable and maintainable code, they understand concepts of testing and continuous integration. But they don't know how to approach research. They may tell you they know and continue trying solving research topics with building a new super flexible architecture instead of experimenting and discovering solutions. They prefer depth first search instead of breadth first search. Write what you really need is a combination of both.

# You are afraid of changes in your system

## technical changes
You probably don't have tests, you deploy rarely and you don't maintain your code clean. That makes you being afraid of introducing new features. That leads to the degradation of the system.

## business rules changes
Business changes. That's totally fine. How to prepare for these changes. I think it is good to have high level acceptance tests that are written together with your product guy. Ideally he/she is able to write such test alone. You should run those test together with unit tests if possible or regularly, say once a day. At least for each major release.

When new use case comes you write a new test and implement a feature in the system. Then you test that it didn't break old acceptance tests. If old test breaks you investigate together with product and find our what is the desired/correct behavior. 

This requires a lot of efforts but I believe it pays off in a long run. 


# you don't really need data science
Business people 99% of the cases don't need complicated, powerful algorithms. They need some linear models and ability to play with parameters. They need fast and reliable enough simulations and ability to fix the errors or steer the parameters.
