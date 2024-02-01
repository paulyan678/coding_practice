def k_reverse(head, k):
    if len(head) < k:
        return head
    
    num_reverses = len(head) // k

    for i in range(num_reverses):
        start = i*k
        end = (i+1)*k
        head[start:end] = head[start:end][::-1]
    return head
