#!/bin/python3
import sys
import json
from pypdf import PdfWriter, PdfReader


def main():
    input_path = sys.argv[1]
    choreo_json = sys.argv[2]

    with open(choreo_json, 'r') as file:
        choreo = json.load(file)
    scenes = choreo["Scenes"]

    reader = PdfReader(input_path)
    writer = PdfWriter()
    writer.append(reader)

    for page_num, scene in enumerate(scenes, start = 2):
        writer.add_outline_item(scene["Name"], page_number=page_num)

    with open(input_path, "wb") as f:
        writer.write(f)


if __name__ == "__main__":
    main()

