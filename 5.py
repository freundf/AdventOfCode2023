from collections import namedtuple

DAY = 5

val_range = namedtuple("val_range", ["start", "end"])
val_mapping = namedtuple("val_map", ["start", "end", "offset"])


def part1() -> int:
    with open("input/5") as f:
        header = f.readline()
        lines = f.read()
    seeds: [int] = get_seeds(header)
    maps: [[val_mapping]] = build_maps(lines.strip())
    transformed_seeds = []
    for seed in seeds:
        transformed_seeds.append(transform_seed(seed, maps))

    return min(transformed_seeds)


def transform_seed(seed: int, maps: [[val_mapping]]) -> int:
    for mapping in maps:
        for m in mapping:
            if m.start <= seed <= m.end:
                seed = seed + m.offset
                break
    return seed


def get_seeds(line: str) -> list[int]:
    seeds = line.split(": ")[1].split(" ")
    seeds = [int(x) for x in seeds]
    return seeds


def build_maps(lines: str) -> [[val_mapping]]:
    maps = []
    map_listings = lines.split("\n\n")
    for mapping in map_listings:
        new_map = []
        for line in mapping.split("\n")[1::]:
            dest, src, length = line.split(" ")
            new_map.append(val_mapping(int(src), int(src) + int(length) - 1, int(dest) - int(src)))
        maps.append(new_map)
    return maps


def part2() -> int:
    with open("input/5") as f:
        header = f.readline()
        lines = f.read()
    seed_ranges: [val_range] = get_seed_ranges(header)
    maps = build_maps(lines.strip())
    for seed_map in maps:
        seed_ranges = transform_ranges(seed_ranges, seed_map)

    return min([seed_r.start for seed_r in seed_ranges])


def transform_ranges(val_ranges: [val_range], val_maps: [val_mapping]) -> [val_range]:
    new_ranges: [val_range] = []
    while not len(val_ranges) == 0:
        val_r = val_ranges.pop(0)
        mapped = False
        for val_map in val_maps:
            if val_r.start < val_map.start < val_r.end:
                val_ranges.append(val_range(val_r.start, val_map.start - 1))
            if val_r.end > val_map.end > val_r.start:
                val_ranges.append(val_range(val_map.end + 1, val_r.end))

            mapped_start = max(val_map.start, val_r.start)
            mapped_end = min(val_map.end, val_r.end)
            if mapped_start < mapped_end:
                new_ranges.append(val_range(mapped_start + val_map.offset, mapped_end + val_map.offset))
                mapped = True
                break

        if not mapped:
            new_ranges.append(val_r)

    return new_ranges


def get_seed_ranges(line: str) -> [val_range]:
    seeds = []
    seeds_ranges = line.split(": ")[1].split(" ")
    seeds_ranges = [int(x) for x in seeds_ranges]
    for i, seed in enumerate(seeds_ranges):
        if i % 2 == 1:
            continue
        seeds.append(val_range(seed, seed + seeds_ranges[i + 1] - 1))
    return seeds


if __name__ == "__main__":
    print(part1())
    print(part2())
