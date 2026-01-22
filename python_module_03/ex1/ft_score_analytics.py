import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    if len(sys.argv) != 1:
        scores = []
        score = 0
        total_score = 0
        high_score = 0
        low_score = 0
        try:
            low_score = int(sys.argv[1])
        except ValueError as e:
            print(e)
        for i in range(1, len(sys.argv)):
            try:
                score = int(sys.argv[i])
            except ValueError as e:
                print(e)
            scores.append(score)
            total_score += score
            if score > high_score:
                high_score = score
            if score < low_score:
                low_score = score
        print(f"Scores processed: {str(scores)}")
        print(f"Total players: {len(sys.argv) - 1}")
        print(f"Total score: {total_score}")
        print(f"Average score: {total_score / (len(sys.argv) - 1)}")
        print(f"High score: {high_score}")
        print(f"Low score: {low_score}")
        print(f"Score range: {high_score - low_score}")

    else:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ..."
        )
