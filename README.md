# Popular Design Patterns

Design Patterns are general, reusable solutions to a commonly occurring problem within a given context in software design. A design pattern is not a finished design which can be transformed directly into source or machine code.

There are hundreds of design patterns available; this repo only covers some of the most common ones:

- Singleton :white_check_mark:
- Factory :white_check_mark:
- Template Method :white_check_mark:
- Adapter :white_check_mark:
- Facade :white_check_mark:
- Strategy :white_check_mark:
- State :white_check_mark:
- Proxy :white_check_mark:
- Chain of responsibility :white_check_mark:
- Bridge
- Composite
- Decorator
- Observer
- Builder
- Flyweight
- Repository

## Singleton

Ensures only one instance of a class is created.

## Factory

Have a dedicated place in which to create objects.
The first rule of design patterns is always program to an interface (or at least, a base class).

## Template Method

Subclasses decide how to implement steps in an algorithm.

## Adapter

Converts the interface of a class into another interface the client expects.
Adapter lets classes work together which couldn't otherwise due to incompatible interfaces.

## Facade

Simplifies the interface of a set of classes. It makes a software library easy to use.

## Strategy

Enables an algorithm's behaviour to be selected at runtime.

## State

Similar to the strategy pattern. However, in the state pattern there are usually only two implementations;
an online state and offline state. In addition, a state pattern provides a default implementation.

## Proxy

Wraps an object to control access to it.

## Chain Of Responsibility

Delegates commands to a chain of processing objects. A given group of objects is expected to solve a problem. 
If the first object can't solve it, it passes the data to the next object in the chain.
