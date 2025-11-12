def count_level(records):
    level_count = {}
    for record in records:
        level_count[record.level] = level_count.get(record.level, 0) + 1
    return level_count

def top_tokens(records, n=3):
    record_tokens = {}
    for record in records:
        tokens = record.message.split()
        for token in tokens:
            if token in record_tokens:
                record_tokens[token] += 1
            else:
                record_tokens[token] = 1
    sorted_tokens = sorted(record_tokens.items(), key=lambda item: item[1], reverse=True)
    return sorted_tokens[:n]