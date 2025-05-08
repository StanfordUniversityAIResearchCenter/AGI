"""
Simplified Simulation of Artificial General Intelligence (AGI)

This model includes:
- A general knowledge base that can be expanded.
- Learning from new examples.
- Solving diverse problems.
- Handling multiple tasks.

Note: This is an educational symbolic model, not a real AGI.
"""

class AGI:
    def __init__(self):
        # Knowledge base as fact: explanation dictionary
        self.knowledge = {}
        # Memory of learning examples (input -> output)
        self.experiences = []

    def learn_fact(self, fact, explanation):
        """Learn a new fact with explanation"""
        self.knowledge[fact.lower()] = explanation
        print(f"Learned new fact: '{fact}'")

    def learn_from_example(self, example_input, example_output):
        """Learn from a new example"""
        self.experiences.append((example_input.lower(), example_output))
        print(f"Learned from example: '{example_input}' -> '{example_output}'")

    def answer_question(self, question):
        """Answer a question using knowledge and experiences"""
        question = question.lower()

        # Direct fact lookup
        if question in self.knowledge:
            print("Found answer in knowledge base.")
            return self.knowledge[question]

        # Partial match in knowledge
        for fact, explanation in self.knowledge.items():
            if fact in question or question in fact:
                print("Found partial match in knowledge base.")
                return explanation

        # Use learning experience to find answer
        for inp, outp in self.experiences:
            if inp in question:
                print("Found match in learning experiences.")
                return outp

        # Intelligent guess fallback
        print("Insufficient knowledge, making an educated guess.")
        return "I do not know the exact answer, I need to learn more."

    def do_math(self, expr):
        """Attempt to solve simple mathematical expressions"""
        try:
            result = eval(expr)
            print(f"Solved math expression: {expr} = {result}")
            return result
        except Exception:
            return "Cannot solve the math expression."

    def multitask(self, task_type, data):
        """Perform various tasks based on type"""
        if task_type == 'question':
            return self.answer_question(data)
        elif task_type == 'math':
            return self.do_math(data)
        else:
            return "Currently unsupported task type."

if __name__ == "__main__":
    agi = AGI()

    # Learn general facts
    agi.learn_fact("What color is the sky?", "The sky is blue during the day and usually black at night.")
    agi.learn_fact("What is the capital of Egypt?", "The capital of Egypt is Cairo.")

    # Learn from examples
    agi.learn_from_example("what is 2 + 2?", 4)
    agi.learn_from_example("how much is five minus two?", 3)

    # Tests

    # Direct question
    print("Question:", "What color is the sky?")
    print("Answer:", agi.multitask('question', "What color is the sky?"))

    print()

    # Partial question
    print("Question:", "Where is Cairo located?")
    print("Answer:", agi.multitask('question', "Where is Cairo located?"))

    print()

    # Experience-based question
    print("Question:", "what is 2 + 2?")
    print("Answer:", agi.multitask('question', "what is 2 + 2?"))

    print()

    # Math calculation
    print("Math:", "5 * (3 + 2)")
    print("Result:", agi.multitask('math', "5 * (3 + 2)"))

    print()

    # Unknown question
    print("Question:", "Who was the first astronaut?")
    print("Answer:", agi.multitask('question', "Who was the first astronaut?"))
