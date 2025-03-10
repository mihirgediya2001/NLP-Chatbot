import spacy
from Chatbot_Responses import responses 

def initialize_npl_model():
    return spacy.load("en_core_web_sm")

nlp = initialize_npl_model()

def get_response(user_input):
    doc = nlp(user_input.lower())
    
    # Extract lemmatized tokens for better matching
    tokens = [token.lemma_ for token in doc]
    
    # Check for greetings
    if any(greeting in tokens for greeting in ["hello", "hi", "hii", "hey", "greet"]):
        return responses["greet"]
    
    # Check for goodbye
    if any(bye in tokens for bye in ["bye", "goodbye", "exit", "quit"]):
        return responses["bye"]
    
    # Check for thanks
    if any(thanks in tokens for thanks in ["thanks", "thank", "appreciate"]):
        return responses["thank"]
    
    # Check for help request
    if "help" in tokens or "assist" in tokens or "guide" in tokens:
        return responses["help"]
    
    if any(q in user_input.lower() for q in ["who are you", "what can you do", "what do you do", "what are you capable of"]):
        return responses["what_can_you_do"]
    
    # Check for if statement related questions
    if "if" in tokens:
        if any(term in user_input.lower() for term in ["define", "explain", "basic"]):
            return responses["if_basic"]
        elif any(term in user_input.lower() for term in ["else if", "if-else-if", "else-if", "elseif", "ladder"]):
            return responses["if_else_if"]
        elif "else" in tokens:
            return responses["if_else"]
        elif any(term in user_input.lower() for term in ["nested", "inside", "nested-if"]):
            return responses["if_nested"]
        elif any(term in tokens for term in ["condition", "boolean", "test"]):
            return responses["if_condition"]
        elif any(term in tokens for term in ["example", "sample", "code"]):
            return responses["if_example"]
        else:
            return responses["default"]
    
    if any(q in user_input.lower() for q in ["ternary", "shorthand", "? :", "?:"]):
        return responses["if_ternary"]
    
    # Check for for loop related questions
    if "for" in tokens or "loop" in tokens:
        if "while" in tokens and not "for" in tokens:
            return responses["while_loop"]
        elif any(term in user_input.lower() for term in ["define", "explain", "basic"]):
            return responses["for_basic"]
        elif any(term in tokens for term in ["component", "part", "structure"]):
            return responses["for_components"]
        elif any(term in tokens for term in ["example", "sample", "code"]):
            return responses["for_example"]
        elif any(term in tokens for term in ["each", "enhanced", "foreach", "collection", "array"]):
            return responses["for_each"]
        elif "break" in tokens:
            return responses["for_break"]
        elif "continue" in tokens:
            return responses["for_continue"]
        elif any(term in tokens for term in ["infinite", "endless", "forever"]):
            return responses["for_infinite"]
        elif "while" in tokens:
            return responses["for_vs_while"]
        else:
            return responses["for_basic"]
    
    # Check for variable and data type related questions
    if any(term in tokens for term in ["primitive", "int", "double", "boolean", "char"]):
        return responses["primitive_types"]
    if any(term in tokens for term in ["reference", "object type", "class type"]):
        return responses["reference_types"]
    if "variable" in tokens or "declare" in tokens:
        if "name" in tokens or "naming" in tokens or "convention" in tokens:
            return responses["variable_naming"]
        else:
            return responses["variable_declaration"]
    if "constant" in tokens or "final" in tokens:
        return responses["constants"]
    
    # Check for expression and operator related questions
    if "expression" in tokens:
        return responses["expressions"]
    if any(term in tokens for term in ["arithmetic", "add", "subtract", "multiply", "divide"]):
        return responses["arithmetic_operators"]
    if any(term in tokens for term in ["assign", "assignment", "="]):
        return responses["assignment_operators"]
    if any(term in tokens for term in ["compare", "comparison", "equal", "greater", "less"]):
        return responses["comparison_operators"]
    if any(term in tokens for term in ["precedence", "order", "priority"]):
        return responses["precedence"]
    
    # Check for control flow questions
    if "while" in tokens:
        return responses["while_loop"]
    if "switch" in tokens:
        return responses["switch_statement"]
    
    # Check for class and object related questions
    if "class" in tokens:
        if any(term in tokens for term in ["basic", "define"]):
            return responses["class_basics"]
        elif "constructor" in tokens:
            return responses["constructor"]
        else:
            return responses["class_basics"]
    if "object" in tokens:
        if "create" in tokens or "new" in tokens:
            return responses["object_creation"]
        else:
            return responses["class_basics"]
    if "method" in tokens or "function" in tokens:
        if "parameter" in tokens or "argument" in tokens:
            return responses["method_parameters"]
        elif "return" in tokens:
            return responses["return_values"]
        else:
            return responses["methods"]
    if "constructor" in tokens:
        return responses["constructor"]
    
    # Check for access modifier related questions
    if ("public" in tokens and "private" in tokens) or "visibility" in tokens:
        return responses["public_private"]
    if any(term in tokens for term in ["access", "modifier", "protected", "default"]):
        return responses["access_modifiers"]
    
    # Default response if no pattern matches
    return responses["default"]