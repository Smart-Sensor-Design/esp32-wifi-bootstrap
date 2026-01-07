#!/usr/bin/env python3

import os


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    content_dir = os.path.abspath(os.path.join(script_dir, '..', 'content'))
    input_file = os.path.join(content_dir, 'connecting.html')
    output_file = os.path.join(content_dir, 'connecting.html.h')

    if not os.path.exists(input_file):
        print(f"❌ File not found: {input_file}")
        return

    if os.path.exists(output_file):
        confirm = input(
            f"⚠️ '{output_file}' already exists. Overwrite? (y/n): ").strip().lower()
        if confirm != 'y':
            print("❌ Aborted.")
            return

    with open(input_file, 'r', encoding='utf-8') as f:
        html = f.read()

    # Auto-generated from connecting.html
    # Keep output simple: one C string constant.
    lines = [line for line in html.splitlines() if line.strip()]
    c_lines = ['"' + line.lstrip().replace('\\', '\\\\').replace('"', '\\"') + '"' for line in lines]
    c_output = "// Auto-generated from connecting.html\n\n" + "const char *html_connecting = \n" + "\n".join(c_lines) + ";\n"

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(c_output)

    print(f"✅ Generated: {output_file}")


if __name__ == '__main__':
    main()
