# * Memory Allocation Techniques


def fixed_memory_partition(process, mem):
    print("**********FIXED MEMORY PARTITIONING**********")
    print("process SIZES", "              ", "BLOCK-NO", "              ", "IF")
    no_of_blocks = len(mem)
    no_of_process = len(process)
    flag_m = [0] * no_of_blocks  # 0 is for available
    flag_f = [0] * no_of_process  # 0 is for not allocated
    TIF = 0
    for i in range(no_of_process):
        IF = 0
        for j in range(no_of_blocks):
            if flag_m[j] == 0 and mem[j] >= process[i] and process[i] > 0:
                flag_m[j] = 1
                flag_f[i] = 1
                # This is to find the internal fragmentation "IF"
                IF += mem[j] - process[i]
                TIF += IF
                # Print the
                print(
                    process[i],
                    "                              ",
                    j + 1,
                    "              ",
                    IF,
                )
                process[i] = 0
    print("total Internal fragmentation produced is: ", TIF, "\n\n")
    for i in range(no_of_process):

        if flag_f[i] == 0:
            print("file", i + 1, "could'nt be allocated to any block ", "\n")


def variable_memory_partition(process, mem):
    print("**********VARIABLE MEMORY PARTITION**********")
    print("process SIZES", "              ", "BLOCK-NO", "            ", "IF")
    no_of_blocks = len(mem)
    no_of_process = len(process)
    flag_m = [0] * no_of_blocks  # 0 is for available
    flag_f = [0] * no_of_process  # 0 is for not allocated
    TIF = 0
    best = []
    for i in range(no_of_process):
        IF = 0
        best = []
        for j in range(no_of_blocks):
            if flag_m[j] == 0 and mem[j] >= process[i] and process[i] > 0:
                best.append(mem[j] - process[i])
            elif mem[j] < process[i] or flag_m[j] == 1:
                best.append(10 ** 4)

        index = best.index(
            min(best)
        ) 
        flag_m[index] = 1
        flag_f[i] = 1
        IF = mem[index] - process[i]
        TIF += IF
        print(
            process[i],
            "                              ",
            index + 1,
            "              ",
            IF,
        )
        process[i] = 0
    print("total Internal fragmentation produced is:  ", TIF, "\n\n")

    for i in range(no_of_process):
        if flag_f[i] == 0:
            print("file", i + 1, "could'nt be allocated to any block ", "\n")


# * Page Replacement Techniques


def first_come_first_serve(pages, memory_size):
    print("******USING FIRST COME FIRST SERVE******")
    print("******MEMORY SIZE******", memory_size)
    memory = []
    currently_allocated_hole_index = 0
    while len(pages) > 0:
        print("******CURRENTLY IN MEMORY******", memory)
        selected_page = pages.pop(0)
        if not selected_page in memory:
            print("******SELECTED PAGE******", selected_page)
            if memory_size > len(memory):
                memory.append(selected_page)
            else:
                try:
                    memory[currently_allocated_hole_index] = selected_page
                    currently_allocated_hole_index += 1
                except IndexError:
                    pass
        else:
            print(f"******{selected_page} ALREADY IN MEMORY******")

    print("******ALL ALLOCATED******")


def least_recently_used(pages, memory_size):
    print("******USING LEAST RECENTLY USED******")
    print("******MEMORY SIZE******", memory_size)
    memory = []
    currently_allocated_hole_index = memory_size - 1
    while len(pages) > 0:
        print("**CURRENTLY IN MEMORY**", memory)
        selected_page = pages.pop()
        if not selected_page in memory:
            print("******SELECTED PAGE******", selected_page)
            if memory_size > len(memory):
                memory.append(selected_page)
            else:
                try:
                    memory[currently_allocated_hole_index] = selected_page
                    currently_allocated_hole_index -= 1
                except IndexError:
                    pass
        else:
            print(f"******{selected_page} ALREADY IN MEMORY******")

    print("******ALL ALLOCATED******")


if __name__ == "__main__":
    process = list(
        map(
            int,
            input("Enter process sizes to be stored (separated by space):  ").split(),
        )
    )

    x = tuple(process)

    process_list = list(x)
    memory_blocks = [2,3,4,5]
    # fixed_memory_partition(process_list, memory_blocks)
