import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    if len(sys.argv) != 1:
        scores: list[int] = []

        for i in range(1, len(sys.argv)):
            try:
                score: int = int(sys.argv[i])
                scores.append(score)
            except ValueError as e:
                print(f"Error: {e}")

        if scores:
            total_score: int = sum(scores)
            high_score: int = max(scores)
            low_score: int = min(scores)

            print(f"Scores processed: {scores}")
            print(f"Total players: {len(scores)}")
            print(f"Total score: {total_score}")
            print(f"Average score: {total_score / len(scores)}")
            print(f"High score: {high_score}")
            print(f"Low score: {low_score}")
            print(f"Score range: {high_score - low_score}")
        else:
            print("No valid scores provided.")
    else:
        print("No scores provided. Usage: python3 \
ft_score_analytics.py <score1> <score2> ...")
