def edit_dist(a, b):
    dp = list(range(len(b)+1))
    for i, ca in enumerate(a, 1):
        prev, dp[0] = dp[0], i
        for j, cb in enumerate(b, 1):
            prev, dp[j] = dp[j], prev if ca == cb else 1 + min(prev, dp[j], dp[j-1])
    return dp[-1]

if __name__ == "__main__":
    vocab = ["algorithm", "logarithm", "storage"]
    assert min(vocab, key=lambda w: edit_dist("algoritm", w)) == "algorithm"
    print("[PASS] 098_edit_distance_spellcheck")
