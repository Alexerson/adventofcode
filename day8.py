import collections

from utils import data_import


# We use a recursive algorithm to extract metadata
def find_metadata(data):
    ''' Take a full dataset in input and extract the metadata '''

    # First, we extract what we can from the data we have
    children_count = data[0]
    metadata_count = data[1]
    data = data[2:]

    # Acc for the recursion
    metadatas = []

    # We extract each children recursively.
    for i in range(children_count):
        metadata, data = find_metadata(data)
        metadatas += metadata

    # Now that we extracted all children,
    # the first items of the reminders are the metadata of the first child
    metadata = data[:metadata_count]
    metadatas += metadata

    # We return the list of the metadatas so far,
    # as well as the reminder for an upper recursion loop
    return metadatas, data[metadata_count:]


def part1(data):
    metadatas = find_metadata(data)[0]
    return sum(metadatas)


# We use the same base function but we add the score computation
def find_metadata_and_score(data):
    children_count = data[0]
    metadata_count = data[1]
    data = data[2:]
    metadatas = []
    scores = []

    for i in range(children_count):
        metadata, score, data = find_metadata_and_score(data)
        metadatas += metadata
        scores.append(score)  # We store the score for each child

    metadata = data[:metadata_count]
    metadatas += metadata

    if children_count == 0:
        # If we have no child, the score is the sum of metadatas
        score = sum(metadatas)

    else:
        # If we have children, the score if the sum of the child score,
        # but we pick the child score based on the metadata index

        # If an index is too big, we ignore it

        # Metadata index starts at 1, so we retract 1 from it
        score = sum(
            scores[value - 1] for value in metadata if value <= len(scores)
        )

    # We return the list of the metadatas so far,
    # The score of the current node
    # as well as the reminder for an upper recursion loop
    return (metadatas, score, data[metadata_count:])


# Now part1 could be rewritten `find_metadata_and_score(data)[0]`


def part2(data):
    return find_metadata_and_score(data)[1]


if __name__ == '__main__':
    data = data_import('data/day8')
    data = [int(item) for item in data[0].split()]

    print('Solution of 1 is', part1(data))
    print('Solution of 2 is', part2(data))
