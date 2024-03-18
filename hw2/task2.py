from tex_generation_noonmare.generate_funcs import (
    table_settings,
    image_settings,
    generate_tex,
)

table_data = [["id", "name", "price"], [1, "cheese", 10], [2, "milk", 5]]
image_path = "./cheese_and_milk.png"

# Таблица с кастомными параметрами
get_table = table_settings(sep_lines=True, caption="Customized table", centering=True)
customized_table_tex = get_table(table_data)

# Картинка с кастомными параметрами
get_image = image_settings(caption="Customized image", centering=True)
customized_image_tex = get_image(image_path)

# Объединим в общий документ
tex_data = generate_tex(
    customized_table_tex, customized_image_tex, packages=["graphicx"]
)

with open("artefacts/2.2_table_and_images.tex", "w") as f:
    f.write(tex_data)
