from dataclasses import dataclass, field


@dataclass
class Record:
    record_id: int
    parent_id: int


@dataclass
class Node:
    node_id: int
    children: list[int] = field(default_factory=list)


def BuildTree(records):
    records.sort(key=lambda x: x.record_id)
    if not records:
        return None

    root = records[0]
    if not (root.record_id == root.parent_id == 0):
        raise ValueError("Tree must start with id 0")

    if len(records) - 1 != records[-1].record_id:
        raise ValueError("Tree must be continuous")

    tree = Node(records[0].record_id)
    tree_map = {0: tree}
    for record in records[1:]:
        if record.record_id <= record.parent_id:
            raise ValueError("Parent id must be lower than child id")

        node = Node(record.record_id)
        tree_map[record.record_id] = node
        tree_map[record.parent_id].children.append(node)

    return tree
