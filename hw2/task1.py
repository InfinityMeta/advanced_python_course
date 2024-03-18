from hw2.tex_generation.src.tex_generation_noonmare.generate_funcs import (
    generate_table,
    table_settings,
    generate_tex,
)

table_data = [["id", "name", "price"], [1, "cheese", 10], [2, "milk", 5]]

# Таблица с дефолтными параметрами
table_tex = generate_table(table_data)

# Таблица с кастомными параметрами
get_table = table_settings(sep_lines=True, caption="Customized table", centering=True)
customized_table_tex = get_table(table_data)

# Объединим в общий документ
tex_data = generate_tex(table_tex, customized_table_tex)

with open("artefacts/2.1_table.tex", "w") as f:
    f.write(tex_data)
