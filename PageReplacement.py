# VIRTUAL MEMORY & PAGE REPLACEMENT SIMULATOR

def display_step(page, frames, status, frame_count):
    # Helper function to handle the bracket formatting and "Empty" padding for all algorithms
    display_frames = [str(x) for x in frames] + ["Empty"] * (frame_count - len(frames))
    frame_str = "[" + ", ".join(display_frames) + "]"
    print(f"{page}\t{frame_str:<25}{status}")

def calculate_pages(logical_addresses, page_size):
    pages = []
    print("\n--- LOGICAL ADDRESS CALCULATION ---")
    print("Logical Address\tPage Number\tOffset")
    for address in logical_addresses:
        page_number = address // page_size
        offset = address % page_size
        pages.append(page_number)
        print(f"{address}\t\t{page_number}\t\t{offset}")
    return pages

def fifo(reference, frame_count):
    print("\n--- FIFO PAGE REPLACEMENT ---")
    print("Page\tFrames\t\t\t Status")
    frames = []
    pointer, faults = 0, 0
    for page in reference:
        if page in frames:
            status = "HIT"
        else:
            faults += 1
            status = "PAGE FAULT"
            if len(frames) < frame_count:
                frames.append(page)
            else:
                frames[pointer] = page
                pointer = (pointer + 1) % frame_count
        display_step(page, frames, status, frame_count)
    return faults

def lru(reference, frame_count):
    print("\n--- LRU PAGE REPLACEMENT ---")
    print("Page\tFrames\t\t\t Status")
    frames, recent = [], []
    faults = 0
    for page in reference:
        if page in frames:
            status = "HIT"
            recent.remove(page)
            recent.append(page)
        else:
            faults += 1
            status = "PAGE FAULT"
            if len(frames) < frame_count:
                frames.append(page)
            else:
                old_page = recent.pop(0)
                index = frames.index(old_page)
                frames[index] = page
            recent.append(page)
        display_step(page, frames, status, frame_count)
    return faults

def optimal(reference, frame_count):
    print("\n--- OPTIMAL PAGE REPLACEMENT ---")
    print("Page\tFrames\t\t\t Status")
    frames = []
    faults = 0
    for current in range(len(reference)):
        page = reference[current]
        if page in frames:
            status = "HIT"
        else:
            faults += 1
            status = "PAGE FAULT"
            if len(frames) < frame_count:
                frames.append(page)
            else:
                future = reference[current + 1:]
                replace_index = 0
                farthest = -1
                for i in range(len(frames)):
                    if frames[i] not in future:
                        replace_index = i
                        break
                    next_use = future.index(frames[i])
                    if next_use > farthest:
                        farthest = next_use
                        replace_index = i
                frames[replace_index] = page
        display_step(page, frames, status, frame_count)
    return faults

# --- MAIN PROGRAM EXECUTION ---
print("\nVIRTUAL MEMORY & PAGE REPLACEMENT SIMULATOR")
user_input = input("\nEnter logical addresses (space-separated): ")
logical_addresses = list(map(int, user_input.split()))
page_size = int(input("Enter page size: "))
frame_count = int(input("Enter number of frames: "))

reference_string = calculate_pages(logical_addresses, page_size)
print(f"\nREFERENCE STRING:\n{reference_string}")

fifo_faults = fifo(reference_string, frame_count)
lru_faults = lru(reference_string, frame_count)
optimal_faults = optimal(reference_string, frame_count)

print("\n--- FINAL COMPARISON ---")
print(f"FIFO\t\t:\t{fifo_faults}")
print(f"LRU\t\t:\t{lru_faults}")
print(f"Optimal\t\t:\t{optimal_faults}")

results = {"FIFO": fifo_faults, "LRU": lru_faults, "Optimal": optimal_faults}
best_algorithm = min(results, key=results.get)
print(f"\nBEST PERFORMANCE: {best_algorithm} ({results[best_algorithm]} Page Faults)")