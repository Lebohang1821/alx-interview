#!/usr/bin/python3
'''It is module for working with lockboxes
'''


def canUnlockAll(boxes):
    '''It looks if all boxes in list of boxes containing keys
    - other boxes can be unlocked given that first
    box is unlocked
    '''
    n = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        boxIdx = unseen_boxes.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[boxIdx])
            seen_boxes.add(boxIdx)
    return n == len(seen_boxes)
