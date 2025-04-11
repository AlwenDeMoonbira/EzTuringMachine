class TuringMachine:
    def __init__(self, tape, initial_state, transitions, accept_state):
        self.tape = list(tape)
        self.head_position = 0
        self.current_state = initial_state
        self.transitions = transitions  # 格式: {(state, symbol): (new_state, new_symbol, move)}
        self.accept_state = accept_state

    def step(self):
        if self.current_state == self.accept_state:
            return False  # 已停止


        current_symbol = self.tape[self.head_position] if self.head_position < len(self.tape) else 'a'
        key = (self.current_state, current_symbol)

        if key not in self.transitions:
            return False  # 无转移规则，停止

        new_state, new_symbol, move = self.transitions[key]
        
        # 更新磁带
        if self.head_position < len(self.tape):
            self.tape[self.head_position] = new_symbol
        else:
            self.tape.append(new_symbol)  # 扩展磁带（处理末尾空白）

        # 更新状态
        self.current_state = new_state

        # 移动磁头
        if move == 'R':
            self.head_position += 1
        elif move == 'L':
            self.head_position -= 1

        return True

    def run(self, verbose=False):
        if verbose:
            print(f"初始磁带: {''.join(self.tape)}")
            print(f"初始状态: {self.current_state}, 磁头位置: {self.head_position}")

        steps = 0
        while self.step():
            steps += 1
            if verbose:
                print(f"步骤 {steps}: 状态={self.current_state}, 磁带={''.join(self.tape)}, 磁头位置={self.head_position}")

        if verbose:
            print(f"停止状态: {self.current_state}")
            print(f"最终磁带: {''.join(self.tape)}")

        return ''.join(self.tape).rstrip('a')  # 去除右侧空白符号


# 任务1：擦除所有 '1'（输入字母表 {1}，外部字母表 {a, 1}）
def task1_erase_all_ones(input_tape):
    transitions = {
        ('q0', '1'): ('q1', 'a', 'R'),  # 擦除第一个 '1'，右移
        ('q1', '1'): ('q1', 'a', 'R'),  # 继续擦除 '1'，右移
        ('q1', 'a'): ('q_accept', 'a', 'R'),  # 遇到空白，接受
        ('q0', 'a'): ('q_accept', 'a', 'R')  # 输入为空，直接接受
    }
    tm = TuringMachine(input_tape, 'q0', transitions, 'q_accept')
    return tm.run(verbose=True)


# 任务2：在末尾添加一个 '1'（输入字母表 {1}，外部字母表 {a, 1}）
def task2_append_one(input_tape):
    transitions = {
        ('q0', '1'): ('q0', '1', 'R'),  # 向右移动，跳过 '1'
        ('q0', 'a'): ('q_accept', '1', 'R')  # 遇到空白，写入 '1'，接受
    }
    tm = TuringMachine(input_tape, 'q0', transitions, 'q_accept')
    return tm.run(verbose=True)


if __name__ == "__main__":
    print("===== 任务1：擦除所有 '1' =====")
    input_tape = input("输入二进制字符串（例如 '111'）: ").strip() or '111'
    print(f"输入: {input_tape}")
    output_tape = task1_erase_all_ones(input_tape)
    print(f"输出: {output_tape} (期望: 空字符串)")

    print("\n===== 任务2：在末尾添加一个 '1' =====")
    input_tape = input("输入二进制字符串（例如 '11'）: ").strip() or '11'
    print(f"输入: {input_tape}")
    output_tape = task2_append_one(input_tape)
    print(f"输出: {output_tape} (期望: {input_tape + '1'})")
    x=input("按回车键退出")

