Title: why does your data science project fail again
Author: SergeM
Date: 2017-10-29 23:50
Slug: why-does-your-data-science-project-fail-again
Tags: data science, pm

## why does your data science project fail again

* Your data scientists aren't real scientists
  
  For example, science differs from non-science by writing down the results. 
Maybe your data scientists just talks about awesomeness of his new model and doesn't provide you with written reports and measurements? Then probably you will go in circles of to the dead end. 

  No progress proven == no need for changes at all.


* You don't perform reproducible experiments

  reproducible experiments allow you to compare your old solution with a new one. 
  If you can run the new algorithm on current data only it is not a proof that it works. 
  It can be really a coincidence.
  
* You don't measure your performance
  
  If you build a new algorithm and it is better only because it's 
  a) optimal by design 
  b) robust 
  c) easy to build 
  d) reduces technical depth 
  e) based on a new cool technology 
  f) reduces the coupling 
  g) but you version here. 

  It is not a proof! Probably you lie!
  
  Interesting talk about optimization in C++ and scientific approach from CppCon 2020: 
  [Performance Matters](https://cppcon2020.sched.com/event/e7g0/performance-matters?linkback=grid-full&iframe=no) 
  by Emery Berger.
  > I'll show -- using a new experimental methodology -- that the difference between clang's -O2 and -O3 optimization levels is essentially indistinguishable from noise.


* You have only engineers in your team
  Many tasks cannot be done by pure engineers. 
  These guys can build robust architectures, they write reliable and maintainable code, 
  they understand concepts of testing and continuous integration. 
  But they don't know how to approach research. They may tell you they know and continue trying solving 
  research topics with building a new super flexible architecture 
  instead of experimenting and discovering solutions. 
  They prefer depth first search instead of breadth first search. Write 
  what you really need is a combination of both.

*  You are afraid of changes in your system

  * technical changes
    
    You probably don't have tests, you deploy rarely and you don't maintain your code clean. 
    That makes you being afraid of introducing new features. That leads to the degradation of the system.

  * business rules changes

    Business changes. That's totally fine. How to prepare for these changes. 
    I think it is good to have high level acceptance tests that are written together with your product guy. 
    Ideally he/she is able to write such test alone. 
    You should run those test together with unit tests if possible or regularly, say once a day. 
    At least for each major release.

    When new use case comes you write a new test and implement a feature in the system. Then you test that it didn't break old acceptance tests. If old test breaks you investigate together with product and find our what is the desired/correct behavior. 

    This requires a lot of efforts but I believe it pays off in a long run. 


* You don't really need data science

  Business doesn't need sophisticated algorithms in 99% of the cases. 
  Usually a linear models and ability to play with parameters is more than enough. 
  It's very nice to have a fast and reliable enough simulations,
  plus ability to fix the errors as you go.

  Smart models are often too rigid, slow and complicated. Business changes fast. 
  Excel is still the biggest competitor for the most of the startups. 
  It is widely used because it is a universal tool, that can be easily adapted to the changing needs, 
  everyone knows how to work with it.
   
  Companies usually hire experts that know the market pretty good. 
  They do mistakes but it is very difficult to replace them with software products. 
  So probably software should first try to help them, not to replace them.
