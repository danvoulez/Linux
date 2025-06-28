#!/usr/bin/env python3
"""Minimal LogLine parser."""

def parse_logline(text):
    lines = [l.rstrip('\n') for l in text.splitlines() if l.strip()]
    root_container = {'children': []}
    stack = [(-1, root_container)]  # (indent, node)
    for line in lines:
        indent = len(line) - len(line.lstrip(' '))
        while indent <= stack[-1][0] and len(stack) > 1:
            stack.pop()
        content = line.strip()
        if content.startswith('- type:'):
            typ = content.split(':', 1)[1].strip()
            node = {'type': typ, 'children': []}
            stack[-1][1]['children'].append(node)
            stack.append((indent, node))
        elif ':' in content:
            key, val = content.split(':', 1)
            key = key.strip()
            val = val.strip()
            if val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
            curr = stack[-1][1]
            if val == '':
                curr[key] = []
                stack.append((indent, {'children': curr[key]}))
            else:
                curr[key] = val
        # ignore lines without ':'
    return root_container['children']

if __name__ == '__main__':
    import sys, json
    with open(sys.argv[1]) as f:
        data = parse_logline(f.read())
    print(json.dumps(data, indent=2))
