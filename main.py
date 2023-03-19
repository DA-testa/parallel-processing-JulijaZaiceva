def parallel_processing(n, m, data):
    output = []
    thread_status = []
    thread_seconds = []
    for i in range(n):
        thread_status.append(True)
        thread_seconds.append(0)

    next_task_index = 0

    count_sec = 0
    while True:
        for i in range(n):
            if thread_status[i]:
                thread_status[i] = False
                thread_seconds[i] = data[next_task_index]
                output.append(str(i) + " " + str(count_sec))
                next_task_index += 1
                if next_task_index == m:
                    return output

        for i in range(n):
            thread_seconds[i] += -1
            if thread_seconds[i] == 0:
                thread_status[i] = True

        count_sec += 1


def main():
    split = list(map(int, input().split()))
    n = split[0]
    m = split[1]
    data = list(map(int, input().split()))

    result = parallel_processing(n, m, data)

    for i in result:
        print(i)


if __name__ == "__main__":
    main()
