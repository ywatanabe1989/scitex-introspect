"""scitex-introspect quickstart: IPython-style introspection of any module."""

import scitex_introspect


def main():
    # 1. q("dotted.path"): signature + docstring report, like `func?` in IPython.
    info = scitex_introspect.q("os.path.join")
    print("--- q('os.path.join') ---")
    print(info)
    assert info  # returns dict-like result with metadata
    assert "join" in str(info)

    # 2. dir("module"): list attributes/members of a module (string-resolved).
    members = scitex_introspect.dir("math")
    print("\ndir('math') summary:", str(members)[:160])
    assert "sqrt" in str(members)

    # 3. get_docstring: extract a docstring for a dotted path.
    doc = scitex_introspect.get_docstring("math.sqrt")
    print("\ndocstring math.sqrt:", repr(str(doc)[:80]))
    assert doc

    # 4. list_api: enumerate the module's public API tree (depth-limited).
    api = scitex_introspect.list_api("math", max_depth=1)
    print("\nlist_api('math') preview:", str(api)[:120])


if __name__ == "__main__":
    main()
