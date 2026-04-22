from __future__ import annotations

import cProfile
import io
import pstats
import timeit
import tracemalloc

from bad_code import (
    build_task_report as bad_build_task_report,
    calculate_total as bad_calculate_total,
    find_user_index as bad_find_user_index,
    get_priority_label as bad_get_priority_label,
    get_sample_tasks as bad_get_sample_tasks,
    get_sample_users as bad_get_sample_users,
    process_tasks as bad_process_tasks,
)
from good_code import (
    build_task_report as good_build_task_report,
    calculate_total as good_calculate_total,
    find_user_index as good_find_user_index,
    get_priority_label as good_get_priority_label,
    get_sample_tasks as good_get_sample_tasks,
    get_sample_users as good_get_sample_users,
    index_users_by_id,
    index_users_by_name,
    process_tasks as good_process_tasks,
)


REPEAT_COUNT = 3000
PROFILE_REPEAT = 1500
NUMBER_DATA = list(range(1, 101))


def build_workload_payload():
    bad_users = bad_get_sample_users()
    bad_tasks = bad_get_sample_tasks()
    good_users = good_get_sample_users()
    good_tasks = good_get_sample_tasks()
    good_users_by_id = index_users_by_id(good_users)
    good_users_by_name = index_users_by_name(good_users)
    return bad_users, bad_tasks, good_users_by_id, good_users_by_name, good_tasks


BAD_USERS, BAD_TASKS, GOOD_USERS_BY_ID, GOOD_USERS_BY_NAME, GOOD_TASKS = (
    build_workload_payload()
)


def bad_workload():
    bad_calculate_total(NUMBER_DATA)
    bad_find_user_index(BAD_USERS, "Ira")
    bad_get_priority_label(3)
    bad_build_task_report(BAD_TASKS)
    bad_process_tasks(BAD_TASKS, BAD_USERS)


def good_workload():
    good_calculate_total(NUMBER_DATA)
    good_find_user_index(GOOD_USERS_BY_NAME, "Ira")
    good_get_priority_label(3)
    good_build_task_report(GOOD_TASKS)
    good_process_tasks(GOOD_TASKS, GOOD_USERS_BY_ID)


def measure_time():
    bad_time = timeit.timeit(bad_workload, number=REPEAT_COUNT)
    good_time = timeit.timeit(good_workload, number=REPEAT_COUNT)
    print("TIMEIT RESULTS")
    print(f"bad_code.py  : {bad_time:.4f} s")
    print(f"good_code.py : {good_time:.4f} s")
    print(f"speedup      : {bad_time / good_time:.2f}x")
    return bad_time, good_time


def measure_memory(func, label):
    tracemalloc.start()
    func()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"{label:<12} current={current / 1024:.1f} KiB peak={peak / 1024:.1f} KiB")
    return current, peak


def profile_workload(func, label):
    profiler = cProfile.Profile()
    profiler.enable()
    for _ in range(PROFILE_REPEAT):
        func()
    profiler.disable()
    stream = io.StringIO()
    stats = pstats.Stats(profiler, stream=stream).strip_dirs().sort_stats(
        "cumulative"
    )
    stats.print_stats(6)
    print(f"\nCPROFILE: {label}")
    print(stream.getvalue())


def main():
    print("=== TIMEIT ===")
    bad_time, good_time = measure_time()

    print("=== TRACEMALLOC ===")
    bad_current, bad_peak = measure_memory(bad_workload, "bad_code")
    good_current, good_peak = measure_memory(good_workload, "good_code")

    print("=== CPROFILE ===")
    profile_workload(bad_workload, "bad_code")
    profile_workload(good_workload, "good_code")

    print("=== SUMMARY ===")
    print(f"time delta    : {bad_time - good_time:.4f} s")
    print(f"memory delta  : {(bad_peak - good_peak) / 1024:.1f} KiB")
    print(f"final current  : {bad_current / 1024:.1f} KiB vs {good_current / 1024:.1f} KiB")


if __name__ == "__main__":
    main()