import itertools
import collections


def make_graph(text):
    graph = collections.defaultdict(set)
    for aa, *bbs in map(str.split, text.replace(':', '').splitlines()):
        graph[aa] |= set(bbs)
        for bb in bbs:
            graph[bb] |= {aa}
    return graph


def rank_wires(graph, n_cycles=100, n_top=20):
    tally = collections.Counter()
    for aa, bb in sorted(itertools.combinations(graph, 2))[:n_cycles]:
        path = shortest_path(graph, aa, bb)
        tally.update(frozenset(pair) for pair in zip(path, path[1:]))
    return [k for k, _ in tally.most_common(n_top)]


def shortest_path(graph, aa, bb):
    state = {aa: None}
    seen = {}
    while bb not in state:
        state = {new: old for old in state for new in graph[old] if new not in seen}
        seen |= state

    path = [bb]
    while path[-1] != aa:
        path.append(seen[path[-1]])
    return path


def cut(graph, wires):
    graph = graph.copy()
    for aa, bb in wires:
        graph[aa] = graph[aa] - {bb}
        graph[bb] = graph[bb] - {aa}
    return graph


def subgraphs(graph):
    conns = []
    while graph:
        state = {next(iter(graph))}
        seen = set()
        while state:
            state = {new for old in state for new in graph[old] if new not in seen}
            seen |= state
        conns.append(seen)
        for node in seen:
            graph.pop(node)
    return conns


text = open(0).read()
graph = make_graph(text)
wires = rank_wires(graph)
for triplet in itertools.combinations(wires, 3):
    mod_graph = cut(graph, triplet)
    subs = subgraphs(mod_graph)
    if len(subs) == 2:
        print(len(subs[0]) * len(subs[1]))
        break
