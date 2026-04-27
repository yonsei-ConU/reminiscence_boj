import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


trans = str.maketrans("aiyeouAIYEOUbkxznhdcwgpvjqtsrlmfBKXZNHDCWGPVJQTSRLMF", "eouaiyEOUAIYpvjqtsrlmfbkxznhdcwgPVJQTSRLMFBKXZNHDCWG")
print(input_().strip().translate(trans))
