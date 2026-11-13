
import heapq

def huffman(chars, freq):
    heap = []

    for i in range(len(chars)):
        heap.append((freq[i], i, chars[i]))

    heapq.heapify(heap)

    while len(heap) > 1:
        f1, _, c1 = heapq.heappop(heap)
        f2, _, c2 = heapq.heappop(heap)

        heapq.heappush(
            heap, (f1 + f2, len(heap) + 100, [c1, c2])
        )

    def display(node, code):
        if isinstance(node, str):
            print(node, ":", code)
        else:
            display(node[0], code + "0")
            display(node[1], code + "1")

    print("Huffman Codes:")
    display(heap[0][2], "")


n = int(input("Enter number of characters: "))

chars = []
freq = []

for i in range(n):
    chars.append(input("Enter character: "))
    freq.append(int(input("Enter frequency: ")))

huffman(chars, freq)
