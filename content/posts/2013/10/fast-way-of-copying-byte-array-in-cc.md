---
Title: Fast way of copying byte array in C/C++ (With measurements)
Author: SergeM
Date: 2013-10-15 15:22:00
Slug: fast-way-of-copying-byte-array-in-cc
aliases: [/fast-way-of-copying-byte-array-in-cc.html]
Tags: [ c++,algorithm performance,video processing,obsolete]
---




UPD 2017: these are early experimnts on c++ compiler optimizations. I don't think it is useful any more.

I have the following code for copying several buffers from one object to another:

```c++
    // Copy several buffers (images)
    for( int i = 0; i < MIN( conf_.size(), src.conf_.size() ); ++ i )
    {
       // Copy pixels
       for( int j = 0; j < MIN( sizeOfBuffer_, src.sizeOfBuffer_ ); ++ j )
       {
          conf_[i][j] = src.conf_[i][j];
       }
    }
``` 


Array `conf_` is defined as follows: 

```c++
    std::vector<BYTE*> conf_;
```

BYTE is unsigned char. That code is written with no doubt about software performance. It just works. When I do so I hope compiler make it better for me.
This fragment takes about **45 ms** for copying of 2 images with ( 1980x1080 pixels ) x 3 planes = 6.2 MPixels.
I use Microsoft Visual Studio 2008 compiler on Intel Core i7 950 @ 3.07 GHz. The code is built for x64 platform. Disabled compiler option for buffer security check (GS-) and debug information has no effect on the productivity.

Slightly better solution:

```c++
    // Copy several buffers (images)
    for( int i = 0; i < MIN( conf_.size(), src.conf_.size() ); ++ i )
    {
       int sizeOfArray = MIN( sizeOfBuffer_, src.sizeOfBuffer_ );
    
       // Copy pixels
       for( int j = 0; j < sizeOfArray; ++ j )
       {
          conf_[i][j] = src.conf_[i][j];
       }
    }
```

It takes about **35 ms **per full copy. 

Much better solution:


```c++
    // Copy several buffers (images)
    for( int i = 0; i < MIN( conf_.size(), src.conf_.size() ); ++ i )
    {
       BYTE * arrDst = conf_[i];
       BYTE * arrSrc = src.conf_[i];
       int sizeOfArray = MIN( sizeOfBuffer_, src.sizeOfBuffer_ );
    
       // Copy pixels
       for( int j = 0; j < sizeOfArray; ++ j )
       {
          arrDst[j] = arrSrc[j];
       }
    }
``` 

Everything is the same except for using additional temporary variable. This version runs for **8 ms**. 
UPD: Intel Compiler 2011 demonstrates **2 ms** latency for this code.

And even better solution for Visual Studio:

```c++
    // Copy several buffers (images)
    for( int i = 0; i < MIN( conf_.size(), src.conf_.size() ); ++ i )
    {
       BYTE * arrDst = conf_[i];
       BYTE * arrSrc = src.conf_[i];
       int sizeOfArray = MIN( sizeOfBuffer_, src.sizeOfBuffer_ );
    
       // Copy pixels
       std::copy( arrSrc, arrSrc + sizeOfArray, arrDst );
    }
```

It uses **copy **function from standard C++ library. Time of this version is **2 ms**.   
UPD: Intel Compiler 2011 demonstrates **2 ms** latency for this code too, but it seems that for multiple runs the last version is slightly slower than previous one for ICC. My previous time measuremets have integer precision. So for 50 frames ICC+last-version got **141 ms** and ICC+previous-version got **112 ms.** That is strange.

On Intel Compiler memcpy and `std::copy` give nearly the same results.

