# ==============================
# パーティリストの設定
# ==============================
# 初期状態と目標の並び順を設定
initial = ['D2', 'MT', 'ST', 'H1', 'H2', 'D1', 'D3', 'D4']
target = ['H1', 'H2', 'MT', 'ST', 'D1', 'D2', 'D3', 'D4']

# ==============================
# プログラム本体
# ==============================
def find_cycles(initial_positions, target_positions):
    cycles = []
    visited = [False] * len(initial_positions)
    
    position_mapping = {}
    for name, init_pos in initial_positions.items():
        target_pos = target_positions[name]
        position_mapping[init_pos] = target_pos
    
    for i in range(len(initial_positions)):
        if not visited[i]:
            cycle = []
            j = i
            while not visited[j]:
                visited[j] = True
                cycle.append(j)
                j = position_mapping[j]
            if len(cycle) > 1 and j == i:
                cycles.append(cycle)
    return cycles

def generate_commands(initial, target):
    initial_positions = {name: idx for idx, name in enumerate(initial)}
    target_positions = {name: idx for idx, name in enumerate(target)}
    
    cycles = find_cycles(initial_positions, target_positions)
    commands = []
    
    for cycle in cycles:
        for i in range(len(cycle) - 1, 0, -1):
            pos1 = cycle[i] + 1
            pos2 = cycle[i-1] + 1
            commands.append(f"/partysort {pos1} {pos2}")
    
    return commands

def simulate_command(current_state, command):
    pos1 = int(command.split()[1]) - 1
    pos2 = int(command.split()[2]) - 1
    current_state[pos1], current_state[pos2] = current_state[pos2], current_state[pos1]
    return current_state

# コマンドを生成
commands = generate_commands(initial, target)

# デバッグ出力
print("初期配置:", initial)
print("目標配置:", target)
print("\n=== コマンド実行シミュレーション ===")

current_state = initial.copy()
for i, command in enumerate(commands, 1):
    print(f"\nステップ {i}: {command}")
    current_state = simulate_command(current_state.copy(), command)
    print(f"実行後の配置: {current_state}")

print("\n=== 結果検証 ===")
print(f"最終配置: {current_state}")
print(f"目標配置: {target}")

if current_state == target:
    print("検証: True")
    print("最終的なコマンド:")
    for command in commands:
        print(command)
else:
    print("検証: False")