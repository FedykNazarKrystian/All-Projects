h1, m1, s1 = map(int, input().split())
h2, m2, s2 = map(int, input().split())

start_seconds = h1 * 3600 + m1 * 60 + s1
end_seconds = h2 * 3600 + m2 * 60 + s2

if end_seconds < start_seconds:
    end_seconds += 24 * 3600

duration_seconds = end_seconds - start_seconds

h = duration_seconds // 3600
m = (duration_seconds % 3600) // 60
s = duration_seconds % 60

print(h, m, s)
