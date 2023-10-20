import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def is_knight_move_possible(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    return (dx == 1 and dy == 2) or (dx == 2 and dy == 1)

def main():
    st.title("Проверка хода коня")
    canvas = np.zeros((8, 8))

    x1, y1 = st.columns(2)
    with x1:
        st.write("Выберите координату x1:")
        x1_coord = st.slider("", min_value=1, max_value=8, value=1)
    with y1:
        st.write("Выберите координату y1:")
        y1_coord = st.slider("", min_value=1, max_value=8, value=1)

    x2, y2 = st.columns(2)
    with x2:
        st.write("Выберите координату x2:")
        x2_coord = st.slider("", min_value=1, max_value=8, value=2)
    with y2:
        st.write("Выберите координату y2:")
        y2_coord = st.slider("", min_value=1, max_value=8, value=3)

    if st.button("Проверить"):
        if is_knight_move_possible(x1_coord, y1_coord, x2_coord, y2_coord):
            st.success("Конь может перейти с ({}, {}) на ({}, {}) за один ход".format(x1_coord, y1_coord, x2_coord, y2_coord))
        else:
            st.error("Конь не может перейти с ({}, {}) на ({}, {}) за один ход".format(x1_coord, y1_coord, x2_coord, y2_coord))

    # Plotting the chessboard with knight and target cell
    fig, ax = plt.subplots()
    ax.imshow(canvas, cmap='binary')
    ax.scatter(x1_coord-1, y1_coord-1, color='red', marker='s', s=100, label='Knight')
    ax.scatter(x2_coord-1, y2_coord-1, color='blue', marker='s', s=100, label='Target')
    ax.set_xticks(np.arange(8))
    ax.set_yticks(np.arange(8))
    ax.set_xticklabels(np.arange(1, 9))
    ax.set_yticklabels(np.arange(1, 9))
    ax.grid(color='black', linewidth=1)
    ax.legend(loc='upper right')
    st.pyplot(fig)

if __name__ == "__main__":
    main()
