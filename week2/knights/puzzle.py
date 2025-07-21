from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
base = And(
    (And(Or(AKnight,AKnave),Not(And(AKnight,AKnave)))),
)
said = And(AKnight,AKnave)
knowledge0 = And(
    base,
    Implication(AKnight, said), Implication(AKnave,Not(said))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
base = And(
    (And(Or(AKnight,AKnave),Not(And(AKnight,AKnave)))),
    (And(Or(BKnight,BKnave),Not(And(BKnight,BKnave))))
)
said = And(AKnave,BKnave)
knowledge1 = And(
    base,
    Implication(AKnight, said),
    Implication(AKnave,Not(said))

)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
base = And(
    (And(Or(AKnight,AKnave),Not(And(AKnight,AKnave)))),
    (And(Or(BKnight,BKnave),Not(And(BKnight,BKnave))))
)
said_A = Or(And(AKnave,BKnave),And(AKnight,BKnight))
said_B = Or(And(AKnave,BKnight),And(AKnight,BKnave))
knowledge2 = And(
    base,
    Implication(AKnight, said_A),
    Implication(AKnave,Not(said_A)),
    Implication(BKnight, said_B),
    Implication(BKnave,Not(said_B))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.  
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
base = And(
    (And(Or(AKnight,AKnave),Not(And(AKnight,AKnave)))),
    (And(Or(BKnight,BKnave),Not(And(BKnight,BKnave)))),
    (And(Or(CKnight,CKnave),Not(And(CKnight,CKnave))))
)
said_a = AKnave
said_B = Biconditional(BKnight,said_A)
said_B_1 = Biconditional(BKnight, CKnave)
said_C = Biconditional(CKnight,AKnight)    
knowledge3 = And(
    base,
    said_B,
    said_B_1,
    said_C
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
