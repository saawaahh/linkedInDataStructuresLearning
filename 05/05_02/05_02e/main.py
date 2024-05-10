# using a deque (pronounced deck) as a queue

from collections import deque

printer_queue = deque()

# use append to add items to the queue
printer_queue.append("TaylorSwiftTickets.pdf")
printer_queue.append("MarketingNotes.docx")
printer_queue.append("Proof.png")


while len(printer_queue) > 0:
    document = printer_queue.popleft()  # printing out documents in a FIFO
    print(f'Printing {document}')
