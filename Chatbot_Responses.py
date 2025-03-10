responses = {
    "greet": "Hey there! I'm here to help ya with Java questions. What can I do for you today?",
    "bye": "Alright, take care! Happy coding, and don't be a stranger!",
    "thank": "No problem! Don't hesitate to ask if you got more Java questions.",
    "help": "I'm all about Java control flow, data types, classes, and pretty much all of it. What do you wanna dive into?",
    "default": "Uh-oh, didn't quite catch that! Could you rephrase it? I'm here to help with Java though!",
    "what_can_you_do": "I can help you learn Java programming! I can explain syntax, control structures like if-else and loops, object-oriented concepts, data types, and few things Java-related. Just ask away!",
    
    #"if and for" responses
    "if_basic": "The if statement is like 'Hey, if this is true, do this.' You just write: if (condition) { code_to_execute }",
    "if_else": "If-else is used when you wanna do one thing if it's true, and another if it's false. Syntax: if (condition) { code_if_true } else { code_if_false }",
    "if_else_if": "An if-else-if ladder is like checking one condition, then another, and so on. Here's how: if (cond1) { code1 } else if (cond2) { code2 } else { code3 }",
    "if_nested": "Nested ifs are like ifs inside other ifs. so, you're checking for a condition after another condition. Cool, right?",
    "if_condition": "A condition inside an if statement just checks if something's true or false - usually using comparison stuff like ==, !=, >, <, >=, <=, or logic like &&, ||, and !.",
    "if_example": "Here's a quick example: \n\nint score = 85;\nif (score >= 60) {\n    System.out.println('You passed!');\n} else {\n    System.out.println('You failed.');\n}",
    "if_ternary": "The ternary operator is like a shortcut for if-else. It goes like: condition ? expr1 : expr2. If the condition's true, it'll do expr1, else expr2.",
    "for_basic": "A for loop is for when you wanna repeat code a certain number of times. Syntax: for (init; condition; update) { code_to_execute }",
    "for_components": "A for loop's got 3 parts: init (once at the start), condition (checked each time), and update (after each loop).",
    "for_example": "Here's an example of a for loop: \n\nfor (int i = 0; i < 5; i++) {\n    System.out.println('Count: ' + i);\n}\n\nThis'll print numbers from 0 to 4.",
    "for_each": "The for-each loop makes looping through arrays or collections easy. Syntax: for (dataType item : collection) { code_to_execute }",
    "for_break": "The break statement inside a for loop just stops the loop right away, so it won't keep going.",
    "for_continue": "The continue statement inside a for loop skips the rest of the current iteration and moves on to the next one.",
    "for_infinite": "A for loop can run forever if you're not careful like for(;;) { code }. Just make sure you have a way to break it!",
    "for_vs_while": "If you know how many times you want to repeat something, use a for loop. If you're not sure and wanna keep going until a condition changes, a while loop is better.",
    
    # Data types and variables
    "primitive_types": "Java's got 8 primitive types: byte, short, int, long (for numbers), float, double (for decimals), char (for single characters), and boolean (true/false).",
    "reference_types": "Reference types are like classes, arrays, and interfaces. They're pointers to objects, and they can be null.",
    "variable_declaration": "Declaring a variable is simple: just type the type and give it a name. For example: int age = 25;",
    "variable_naming": "When naming variables in Java, you can use letters, digits, $, and _. But don't start with a digit! Also, use camelCase (e.g., studentName).",
    "constants": "To make something a constant, use the final keyword—this means it can't change. For example: final double PI = 3.14159;",
    
    # Expressions and operators
    "expressions": "An expression is anything that can be evaluated into a single value. Like: x + y * 2 will first multiply y by 2, then add x to it.",
    "arithmetic_operators": "Java's arithmetic operators: + (add), - (subtract), * (multiply), / (divide), % (modulo), ++ (increment), -- (decrement).",
    "assignment_operators": "Assignment operators let you do things like: = (basic), +=, -=, *=, /=, %=. So, x += 5 is like writing x = x + 5.",
    "comparison_operators": "Comparison operators check if things are equal, greater, less, etc. ==, !=, >, <, >=, <=—they all give you true or false.",
    "precedence": "Operator precedence is important: * and / happen before + and -, so make sure you know what's happening first! (BODMAS or PEMDAS)",
    
    # Control flow (beyond if and for)
    "while_loop": "A while loop keeps going as long as the condition's true. It's like: while (condition) { do_stuff }",
    "switch_statement": "Switches are cool when you need to check a variable against a bunch of possible values. Syntax: switch(variable) { case val1: code1; break; ... }",
    
    # Classes and objects
    "class_basics": "A class is like a blueprint for creating objects. It defines what fields and methods the objects will have. Syntax: class ClassName { fields; methods; }",
    "object_creation": "To create an object, you use the new keyword. Example: Person person = new Person();",
    "constructor": "A constructor is a special method that sets up an object. It has the same name as the class and no return type. Example: public Person(String name) { this.name = name; }",
    "methods": "Methods define what an object can do. Syntax: returnType methodName(params) { code }. Example: public void printInfo() { System.out.println(name); }",
    "method_parameters": "Method parameters are the values you pass into a method. Example: public void setAge(int age) { this.age = age; }",
    "return_values": "Methods can return a value using the return keyword. The type of the return must match what the method declares. Example: public int getAge() { return age; }",
    
    # Access modifiers
    "public_private": "In Java, public means anyone can access it, but private means only within the same class. It's all about hiding stuff inside objects.",
    "access_modifiers": "Java's got 4 access modifiers: public (everyone can access), protected (same package or subclasses), default (same package), and private (just the class)."
}
