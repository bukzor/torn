#!/usr/bin/env python3.12

from html.parser import HTMLParser

Attrs = list[tuple[str, str | None]]
Env = dict[str, str]


def convert_attrs(attrs: Attrs) -> tuple[Env, list[str]]:
    result: Env = {}
    for key, val in attrs:
        assert val is not None
        result[key] = val
    if "class" in result:
        classes = result["class"].split()
    else:
        classes = []
    return result, classes


class TornEstateMarketParser(HTMLParser):
    recording: bool = False
    tags: list[str] = []

    def handle_starttag(self, tag: str, attrs: Attrs) -> None:
        if not self.recording:
            attrsd, classes = convert_attrs(attrs)
            del attrs

            if "info-block" in classes or "modification" in classes:
                print("Encountered a start tag:", tag, attrsd)
                self.recording = True
        if self.recording:
            self.tags.append(tag)

    def handle_endtag(self, tag: str) -> None:
        if self.recording:
            assert (tag2 := self.tags.pop()) == tag, (tag2, tag)

        if not self.tags:
            self.recording = False

    def handle_data(self, data: str) -> None:
        if not self.recording:
            return

        data = data.strip()
        if not data:
            return
        print("Encountered some data  :", data)


def main():

    ###from html.parser import HTMLParser
    ###Element = ET.Element
    #### tree = ET.parse("properties.fixed.html")
    ###tree = ET.parse("property.1.html")
    ###root: Element = tree.getroot(parser=ET.XMLParser)
    ###market = root.find("./div[contains(@class, 'properties-selling-market')]")
    ###print(market)

    parser = TornEstateMarketParser()
    for line in open("property.1.html"):
        parser.feed(line)


if __name__ == "__main__":
    exit(main())
