def hanoi_tower(n, fr, tmp, to):
    if n == 1:
        print(f"Move disk 1 from {fr} to {to}")
        return
    hanoi_tower(n - 1, fr, to, tmp)
    print(f"Move disk {n} from {fr} to {to}")
    hanoi_tower(n - 1, tmp, fr, to)
n = int(input())
hanoi_tower(n, "A", "B", "C")