# ==========================================
# Ai.personal - Main Entry Point
# ==========================================

from brain.model_core import LocalBrain
from brain.memory import LocalMemory
from body.command_parser import CommandParser
from body.executor import Executor

def main():
    print("🤖 Initializing Ai.personal (Local Rule-Based Assistant)...")
    
    brain = LocalBrain()
    memory = LocalMemory()
    parser = CommandParser()
    executor = Executor()
    
    print("=" * 50)
    print("System Online. Type your command below (type 'exit' to quit):")
    print("=" * 50)
    
    while True:
        try:
            user_input = input("\nUser > ")
            if user_input.strip().lower() in ["exit", "quit"]:
                print("Shutting down assistant. Goodbye!")
                break
                
            parsed_data = parser.parse(user_input)
            if parsed_data["is_empty"]:
                continue
                
            # Process command through local brain
            response = brain.process_input(parsed_data["cleaned"])
            
            # Print response
            print(f"Assistant > {response}")
            
            # Save to local history memory
            memory.add_interaction(user_input, response)
            
        except KeyboardInterrupt:
            print("\nShutting down safely.")
            break

if __name__ == "__main__":
    main()
