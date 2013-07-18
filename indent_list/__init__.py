__version__ = "0.1.0"


class IndentList(list):

    def __init__(self, items):
        self._indent = 0
        self._indent_str = ""

        super(IndentList, self).__init__(items)

    def append(self, item, indent=True):
        if indent:
            item = self._indent_item(item)
        super(IndentList, self).append(item)

    def extend(self, items):
        super(IndentList, self).extend([
            self._indent_item(item) for item in items])

    @property
    def indent(self):
        return self._indent

    @indent.setter
    def indent(self, value):
        self._indent = value
        self._indent_str = self._indent * " "

    def _indent_item(self, item):
        return "%s%s" % (self._indent_str, str(item))


class indent(object):

    def __init__(self, items, indent=4):
        self._indent = indent

        if isinstance(items, IndentList):
            self._items = items
        else:
            self._items = IndentList(items)

    def __enter__(self):
        self._items.indent += self._indent
        return self._items

    def __exit__(self, type, value, tb):
        self._items.indent -= self._indent


if __name__ == "__main__":
    with indent([]) as items:
        items.append("hello")
        items.append("hello")

        with indent(items) as items:
            items.append("hi")

            with indent(items) as items:
                items.extend(["bye", "bye"])

            items.append("hi")

    print "\n".join(items)
