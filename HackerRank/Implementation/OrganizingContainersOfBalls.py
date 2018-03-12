def organizingContainers(container, n):
        sv = []
        sh = []
        for i in range(n):
            sv.append(0)
            sh.append(sum(container[i]))
            for j in range(n):
                sv[i] += container[j][i]
        sv.sort()
        sh.sort()
        if sv == sh:
            return "Possible"
        else:
            return "Impossible"

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n = int(input().strip())
        container = []
        for container_i in range(n):
           container_t = [int(container_temp) for container_temp in input().strip().split(' ')]
           container.append(container_t)
        result = organizingContainers(container, n)
        print(result)
