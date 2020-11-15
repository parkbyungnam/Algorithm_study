from sys import stdin, stdout

input()
arr = sorted(map(int, stdin.read().split()))
stdout.write('\n'.join(map(str,arr)))