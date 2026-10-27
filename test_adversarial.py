
from src.atomic_claims import extract_atomic_claims
from src.evaluator import evaluate_claim


TEST_CASES = [
    {
        "name": "Exact Match",
        "source": "The bridge is 500 meters long.",
        "response": "The bridge is 500 meters long.",
        "expected": "grounded"
    },
    {
        "name": "Paraphrase",
        "source": "The bridge is 500 meters long.",
        "response": "The bridge has a length of 500 meters.",
        "expected": "grounded"
    },
    {
        "name": "Numerical Change",
        "source": "The bridge is 500 meters long.",
        "response": "The bridge is 550 meters long.",
        "expected": "contradiction"
    },
    {
        "name": "Date Change",
        "source": "The company was founded in 2010.",
        "response": "The company was founded in 2015.",
        "expected": "contradiction"
    },
    {
        "name": "Entity Change",
        "source": "Ramesh completed the project.",
        "response": "Suresh completed the project.",
        "expected": "contradiction"
    },
    {
        "name": "Unsupported Claim",
        "source": "The company operates in India.",
        "response": "The company has 25 offices.",
        "expected": "unsupported"
    },
    {
        "name": "Negation",
        "source": "The project is located in Delhi.",
        "response": "The project is not located in Delhi.",
        "expected": "contradiction"
    }
]


def run_adversarial_tests():

    results = []

    for test in TEST_CASES:

        claims = extract_atomic_claims(
            test["response"]
        )

        predictions = []

        for claim in claims:

            result = evaluate_claim(
                claim,
                test["source"],
                threshold=0.60
            )

            predictions.append(
                result["label"]
            )

        results.append({
            "name": test["name"],
            "expected": test["expected"],
            "predictions": predictions
        })

    return results
