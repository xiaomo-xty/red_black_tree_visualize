# 指定编译器
CC = gcc

# 指定编译选项
CFLAGS = -Wall -g

# 指定目标文件和可执行文件名称
OBJS = rbtree.o cJson.o rbtree_to_json.o
TARGET = rbtree_program
HTML_FILE = red_black_tree_visualization.html
IMG_FILE = red_black_tree.png

# 生成可执行文件
$(TARGET): $(OBJS)
	$(CC) -o $@ $^

# 编译红黑树源文件
rbtree.o: rbtree.c rbtree.h
	$(CC) $(CFLAGS) -c rbtree.c

# 编译 cJSON 源文件
cJson.o: cJson.c cJson.h
	$(CC) $(CFLAGS) -c cJson.c

# 编译 rbtree_to_json 源文件
rbtree_to_json.o: rbtree_to_json.c rbtree.h cJson.h
	$(CC) $(CFLAGS) -c rbtree_to_json.c

# 清理生成的文件
clean:
	rm -f $(OBJS) $(TARGET)

# 运行可执行文件
run: $(TARGET)
	./$(TARGET)

# 运行 draw_tree.py 生成可视化
visualize_image: $(TARGET)
	./$(TARGET)
	python3 draw_tree_graphviz.py
	xdg-open $(IMG_FILE) || start $(IMG_FILE)

visualize_page: $(TARGET)
	./$(TARGET)
	python3 draw_tree.py
	xdg-open $(HTML_FILE) || start $(HTML_FILE)
	

.PHONY: clean run visualize_image visualize_page
