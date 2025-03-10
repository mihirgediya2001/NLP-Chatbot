"""
Test script for the Java Learning Chatbot.
This script simulates a conversation with the chatbot to demonstrate its capabilities.

Usage:
1. Run without arguments to go through all questions
2. Run with a number argument to ask that many random questions
   Example: python test_chatbot.py 5
"""

import sys
import random
from Chatbot_Controller import get_response


def simulate_conversation(num_questions=None):
    print("************ Java Learning Chatbot Conversation ************")
    print("------------------------------------------------------------")
    
    # Start with greeting and then mix other questions
    questions = [
        # Basic interactions
        "Hello there",  # greet
        "What can you do?",  # what_can_you_do
        "Can you help me learn Java?",  # help
        "Thanks for the explanation",  # thank
        
        # If statements
        "Explain an if statement?",  # if_basic
        "How does if-else work in Java?",  # if_else
        "What is if-else-if ladder?",  # if_else_if
        "Tell me about nested if statements.",  # if_nested
        "What kind of conditions can I use in if statements?",  # if_condition
        "Give me an example of if statement",  # if_example
        "What's the ternary operator in Java?",  # if_ternary
        
        # For loops
        "What's a for loop?",  # for_basic
        "What are the components of a for loop?",  # for_components
        "Show me an example of a for loop in Java",  # for_example
        "How does for-each loop work with arrays?",  # for_each
        "What does break do in a loop?",  # for_break
        "How does continue work in loops?",  # for_continue
        "What is an infinite for loop?",  # for_infinite
        "Which is better, for or while loops?",  # for_vs_while
        
        # Data types and variables
        "What primitive types does Java have?",  # primitive_types
        "Tell me about reference types",  # reference_types
        "How do I declare variables in Java?",  # variable_declaration
        "What are the rules to name variables?",  # variable_naming
        "How do I create constants?",  # constants
        
        # Expressions and operators
        "What are expressions in Java?",  # expressions
        "What arithmetic operators can I use?",  # arithmetic_operators
        "How do assignment operators work?",  # assignment_operators
        "What comparison operators does Java have?",  # comparison_operators
        "Explain operator precedence in Java",  # precedence
        
        # Additional control flow
        "How does a while loop work?",  # while_loop
        "How do switch statements work?",  # switch_statement
        
        # Classes and objects
        "What is a class in Java?",  # class_basics
        "How do I create objects in Java?",  # object_creation
        "What are constructors?",  # constructor
        "How do methods work in Java?",  # methods
        "How do method parameters work?",  # method_parameters
        "Tell me about return values in methods",  # return_values
        
        # Access modifiers
        "What's the difference between public and private?",  # public_private
        "What access modifiers can I use in Java?",  # access_modifiers
        
        # wrong testcase for testing default
        "Tell me about Python"  # default,
    ]
    
    # First question is always hello
    first_question = questions[0]
    print(f"\nYou: {first_question}")
    response = get_response(first_question)
    print(f"Chatbot: {response}\n")
    
    remaining_questions = questions[1:]
    
    if num_questions:
        # If number specified, choose random questions
        num_to_ask = min(int(num_questions) - 2, len(remaining_questions))

        # choosing random questions from remaiing questions
        questions_to_ask = random.sample(remaining_questions, num_to_ask)
    else:
        # Otherwise use all questions
        questions_to_ask = remaining_questions
    
    # Ask each question and get response
    for question in questions_to_ask:
        print(f"You: {question}")
        response = get_response(question)
        print(f"Chatbot: {response}\n")
    
    # Always end with goodbye
    print("You: bye")
    response = get_response("bye")
    print(f"Chatbot: {response}\n")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            num_questions = int(sys.argv[1])
            if num_questions >= 3:
                    simulate_conversation(num_questions)
            else:
                print("Please provide a valid number for random questions")
                print("Usage: python Chatbot_test {number of testcases > 2}")
        except ValueError:
            print("Please provide a valid number for random questions")
            print("Usage: python Chatbot_test {number of testcases > 2}")
    else:
        simulate_conversation()