---
Title: Learning Rust
Author: SergeM
Date: 2021-06-21 17:30:00
Slug: learning-rust
Tags: [ rust, links ]
---


# Resources (books, tutorials, etc.)

[A half-hour to learn Rust](https://fasterthanli.me/articles/a-half-hour-to-learn-rust) - blog post, a great intro into the language. 
It may be enough to start reading the code, but not enough for writing.

[Easy Rust](https://dhghomon.github.io/easy_rust/Chapter_1.html) — a book about rust 

> Many companies and people now learn Rust, and they could learn faster with a book that has easy English. This textbook is for these companies and people to learn Rust with simple English.


[The Rust Programming Language](https://doc.rust-lang.org/book/) — "Rust book". It's a standard choice for those 
who want to start with Rust. A bit difficult to read sometimes.


[The Rust Standard Library](https://doc.rust-lang.org/std/) — documentation of the standard library. 


[Rust by Example](https://doc.rust-lang.org/rust-by-example/index.html) — "Rust by Example (RBE) is a collection of runnable examples that illustrate various Rust concepts and standard libraries"




# Rust code snippets

## String basics

    
    // Statically allocated string slice
    let hello = "Hello";

    // Equivalent to the previous one, a bit more verbose
    let hello_again: &'static str = "Hello";

    // create a mutable empty String
    let mut s = String::new();

    // A mutable empty String with a pre-allocated buffer
    let mut s_with_capacity = String::with_capacity(10);

    // Add a string slice to a String
    s.push_str("foo");

    // Convert from a string slice to a String
    let foo = "foo".to_string();
    // another way
    let bar = String::from("bar");

    // Coerce a String into &str with &
    let baz: &str = &bar;


### Length of strings

    fn main() {
        let s = String::from("hello🤦‍♂️");
        println!("length of '{}' is {}", s, s.len());
        let s = String::from("hello🤦");
        println!("length of '{}' is {}", s, s.len());
        let s = String::from("hello");
        println!("length of '{}' is {}", s, s.len());
    }

prints 

    length of 'hello🤦‍♂️' is 18
    length of 'hello🤦' is 9
    length of 'hello' is 5


Iterate over all the prefixes of a String:

    for (i, _) in s.chars().enumerate() {
        let prefix = &s[..i+1];
    }
    
[playground](https://play.rust-lang.org/?version=stable&mode=debug&edition=2015&code=fn%20main()%20%7B%0A%20%20%20%20let%20s%20%3D%20String%3A%3Afrom(%22blablaaaa%22)%3B%0A%20%20%20%20for%20(i%2C%20_)%20in%20s.chars().enumerate()%20%7B%0A%20%20%20%20%20%20%20%20let%20prefix%20%3D%20%26s%5B..i%2B1%5D%3B%0A%20%20%20%20%20%20%20%20println!(%22%7B%7D%22%2C%20prefix)%3B%0A%20%20%20%20%7D%0A%7D)


## Iteration

    fn main() {
        let a = [1, 2, 3];

        // forward
        for x in a.iter() {
            print!("{} ", x);
        }
        
        // backward
        for x in a.iter().rev() {
            print!("{} ", x);
        }
    }

[playground](https://play.rust-lang.org/?version=stable&mode=debug&edition=2015&code=fn%20main()%20%7B%0A%20%20%20%20let%20a%20%3D%20%5B1%2C%202%2C%203%5D%3B%0A%0A%20%20%20%20%2F%2F%20forward%0A%20%20%20%20for%20x%20in%20a.iter()%20%7B%0A%20%20%20%20%20%20%20%20print!(%22%7B%7D%20%22%2C%20x)%3B%0A%20%20%20%20%7D%0A%20%20%20%20%0A%20%20%20%20%2F%2F%20backward%0A%20%20%20%20for%20x%20in%20a.iter().rev()%20%7B%0A%20%20%20%20%20%20%20%20print!(%22%7B%7D%20%22%2C%20x)%3B%0A%20%20%20%20%7D%0A%7D)


## Hashmap

Counting strings using a Hashmap:

    let mut counter: HashMap<String, usize> = HashMap::new();
    // s is a str to add
    match counter.get_mut(s) {
        Some(x) => {
            *x += 1;
        }
        None => {
            counter.insert(s.to_string(), 1);
        }
    }

More info:
* [Go version of program is 40% quicker than Rust version](https://www.reddit.com/r/rust/comments/aaood3/go_version_of_program_is_40_quicker_than_rust/) - reddit post. See discussion.
* Fast word counting implementation: [daboross/main.rs](https://gist.github.com/daboross/f65be8feb62e92c0e45e3649a06f6826)
        
## Testing 
    fn f(x: i32) -> i32 {
        x * 2
    }
    
    fn f_unwrap(x: Option<i32>) -> i32 {
        x.unwrap()
    }
    
    // The module is only built when testing
    #[cfg(test)]
    mod test {
        // loading functions from the parent space
        use super::f;
        use super::f_unwrap;
        
        // actual test
        #[test]
        fn test_f() {
            assert_eq!(f(12), 24);
        }
        
        // another test
        #[test]
        fn test_f_unwrap_ok() {
            f_unwrap(Some(12));
        }
        
        // verify that function panics
        #[test]
        #[should_panic]
        fn test_f_unwrap_must_fail() {
            f_unwrap(None);
        }
    }


[playground](https://play.rust-lang.org/?version=stable&mode=debug&edition=2015&code=fn%20f(x%3A%20i32)%20-%3E%20i32%20%7B%0A%20%20%20%20x%20*%202%0A%7D%0A%0Afn%20f_unwrap(x%3A%20Option%3Ci32%3E)%20-%3E%20i32%20%7B%0A%20%20%20%20x.unwrap()%0A%7D%0A%0A%23%5Bcfg(test)%5D%0Amod%20test%20%7B%0A%20%20%20%20use%20super%3A%3Af%3B%0A%20%20%20%20use%20super%3A%3Af_unwrap%3B%0A%20%20%20%20%0A%20%20%20%20%23%5Btest%5D%0A%20%20%20%20fn%20test__f()%20%7B%0A%20%20%20%20%20%20%20%20assert_eq!(f(12)%2C%2024)%3B%0A%20%20%20%20%7D%0A%20%20%20%20%0A%20%20%20%20%23%5Btest%5D%0A%20%20%20%20fn%20test__f_unwrap__ok()%20%7B%0A%20%20%20%20%20%20%20%20f_unwrap(Some(12))%3B%0A%20%20%20%20%7D%0A%20%20%20%20%0A%20%20%20%20%23%5Btest%5D%0A%20%20%20%20%23%5Bshould_panic%5D%0A%20%20%20%20fn%20test__f_unwrap__must_fail()%20%7B%0A%20%20%20%20%20%20%20%20f_unwrap(None)%3B%0A%20%20%20%20%7D%0A%7D)


