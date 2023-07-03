# Popular Design Patterns

Design Patterns are known solutions to common problems.

There are hundreds of design patterns available, so this repo only covers some of the most common ones:

- Singleton :white_check_mark:
- Factory :white_check_mark:
- Template Method :white_check_mark:
- Adapter :white_check_mark:
- Facade
- Strategy
- State
- Proxy
- Chain of responsibility
- Bridge
- Composite
- Decorator
- Observer
- Builder
- Flyweight
- Repository

## Singleton

If we want a class to only have one object, we use the singleton pattern.

Consider the example of Database connectivity. When each object creates a unique Database 
Connection to the Database, it increases the cost and expenses of the project.

Thus, it is better to share a single connection rather than making extra irrelevant 
connections.

## Factory

Have a dedicated place in which to create objects.

The first rule of design patterns is always program to an interface (or at least, a base class).

## Template Method

Subclasses decide how to implement steps in an algorithm.

## Adapter

Converts the interface of a class into another interface the client expects.

Adapter lets classes work together which couldn't otherwise due to incompatible interfaces.