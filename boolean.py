import streamlit as st

def is_knight_move_possible(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    return (dx == 1 and dy == 2) or (dx == 2 and dy == 1)

def main():
    st.title("Проверка хода коня")
    x1 = st.slider("Введите координату x1 (1-8)", min_value=1, max_value=8, value=1)
    y1 = st.slider("Введите координату y1 (1-8)", min_value=1, max_value=8, value=1)
    x2 = st.slider("Введите координату x2 (1-8)", min_value=1, max_value=8, value=2)
    y2 = st.slider("Введите координату y2 (1-8)", min_value=1, max_value=8, value=3)

    if st.button("Проверить"):
        if is_knight_move_possible(x1, y1, x2, y2):
            st.success("Конь может перейти с ({}, {}) на ({}, {}) за один ход".format(x1, y1, x2, y2))
        else:
            st.error("Конь не может перейти с ({}, {}) на ({}, {}) за один ход".format(x1, y1, x2, y2))

if __name__ == "__main__":
    main()
