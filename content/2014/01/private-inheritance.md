---
Title: Private inheritance
Author: SergeM
Date: 2014-01-06 12:49:00
Slug: private-inheritance
aliases: [/private-inheritance.html]
Tags: [ c++]
---



Example from Meyers "Effective C++"

```
    class Timer {
    public:
    explicit Timer(int tickFrequency);
    virtual void onTick() const; // Called automatically for each tic, 
    // onTick() must be redefined to do things
    ...
    };
    
    
    class Widget: private Timer { // private inheritance
    private:
    virtual void onTick() const; // redefined to make job done
    ... 
    };
```

Now clients of Widget get interface untouched and required job is done

Example of protecting method from redefinition in derived classes:  

```
    class Widget {
    private:
        class WidgetTimer: public Timer {
        public:
            virtual void onTick() const;
            ...
        };
        WidgetTimer timer;
        ...
    };
```
Classes derived from Widget unable to redefine onClick. Analogue of **final** in Java and **sealed** in C#
