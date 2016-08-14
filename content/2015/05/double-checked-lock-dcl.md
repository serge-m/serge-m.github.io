Title: Double checked lock (DCL)
Author: SergeM
Date: 2015-05-19 17:46:00
Slug: double-checked-lock-dcl
Tags: multithreading

<div dir="ltr" style="text-align: left;" trbidi="on">[http://www.javaworld.com/article/2074979/java-concurrency/double-checked-locking--clever--but-broken.html](http://www.javaworld.com/article/2074979/java-concurrency/double-checked-locking--clever--but-broken.html)

<div>
</div><div></div>DCL  relies on an unsynchronized use of the resource field. That appears to  be harmless, but it is not. To see why, imagine that thread A is inside  the synchronized block, executing the statement resource = new  Resource(); while thread B is just entering getResource(). Consider the  effect on memory of this initialization. Memory for the new Resource  object will be allocated; the constructor for Resource will be called,  initializing the member fields of the new object; and the field resource  of SomeClass will be assigned a reference to the newly created object.<div>
</div>However,  since thread B is not executing inside a synchronized block, it may see  these memory operations in a different order than the one thread A  executes. It could be the case that B sees these events in the following  order (and the compiler is also free to reorder the instructions like  this): allocate memory, assign reference to resource, call constructor.  Suppose thread B comes along after the memory has been allocated and the  resource field is set, but before the constructor is called. It sees  that resource is not null, skips the synchronized block, and returns a  reference to a partially constructed Resource! Needless to say, the  result is neither expected nor desired.</div>