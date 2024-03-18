def make_row(row_data):
    row = " & ".join(map(str, row_data))
    return row + r" \\"


def generate_table(table_data):
    columns_num = len(table_data[0])
    cols = ["c" for _ in range(columns_num)]
    table_rows = []
    for row in table_data:
        table_rows.append(make_row(row))
    return "\n".join(
        [
            "\\begin{table}[h!]",
            f"\\begin{{tabular}}{{ {' '.join(cols)} }}",
            *table_rows,
            "\\end{tabular}",
            "\\end{table}",
        ]
    )


def table_settings(sep_lines=False, caption=None, centering=False):

    wrapper_head, wrapper_tail = [], []
    wrapper_head.append("\\begin{table}[h!]")
    sep = "|" if sep_lines else " "
    if centering:
        wrapper_head.append("\\centering")
    wrapper_tail.append("\\end{tabular}")
    if caption is not None:
        wrapper_tail.append(f"\\caption{{{caption}}}")
    wrapper_tail.append("\\end{table}")

    def generate_table(table_data):
        columns_num = len(table_data[0])
        cols = ["c" for _ in range(columns_num)]
        table_rows = []
        for row in table_data:
            table_rows.append(make_row(row))
        return "\n".join(
            [
                *wrapper_head,
                f"\\begin{{tabular}}{{ {sep.join(cols)} }}",
                *table_rows,
                *wrapper_tail,
            ]
        )

    return generate_table


def generate_image(image_path):
    return "\n".join(
        "\\begin{figure}[h]", f"\\includegraphics{{{image_path}}}", "\\end{figure}"
    )


def image_settings(width=10, height=5, caption=None, centering=False):

    wrapper_head, wrapper_tail = [], []
    wrapper_head.append("\\begin{figure}[h]")
    if centering:
        wrapper_head.append("\\centering")
    if caption is not None:
        wrapper_tail.append(f"\\caption{{{caption}}}")
    wrapper_tail.append("\\end{figure}")

    def generate_image_with_settings(image_path):
        return "\n".join(
            [
                *wrapper_head,
                f"\\includegraphics[width={width}cm, height={height}cm]{{{image_path}}}",
                *wrapper_tail,
            ]
        )

    return generate_image_with_settings


def generate_tex(*tex_blocks, document_class="article", packages=None):
    wrapper_head, wrapper_tail = [], []
    wrapper_head.append(f"\\documentclass{{{document_class}}}")
    if packages is not None:
        wrapper_head.extend(map(lambda pack: f"\\usepackage{{{pack}}}", packages))
    wrapper_head.append("\\begin{document}")
    wrapper_tail.append("\\end{document}")
    tex_document = "\n".join([*wrapper_head, *tex_blocks, *wrapper_tail])
    return tex_document
