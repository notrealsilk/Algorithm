dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 상, 하, 좌, 우
tunnel = {1: [dxy[0], dxy[1], dxy[2], dxy[3]],  # 지하터널 구조물
          2: [dxy[0], dxy[1]],
          3: [dxy[2], dxy[3]],
          4: [dxy[0], dxy[3]],
          5: [dxy[1], dxy[3]],
          6: [dxy[1], dxy[2]],
          7: [dxy[0], dxy[2]]}

print(tunnel[3][0])