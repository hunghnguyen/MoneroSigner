from typing import List

def idx2bytes(idx_list: List[int]) -> bytes:
    idxbin = ''.join([f'{idx:>011b}' for idx in idx_list])
    # idxbin = ''.join([bin(idx)[2:].zfill(11) for idx in idx_list])  # TODO: 2024-07-30: which is better
    if len(idxbin) % 8 != 0:
        idxbin += '0' * (8 - len(idxbin) % 8)
    idxbytes = b''
    for i in range(0, len(idxbin), 8):
        idxbytes  += int(idxbin[i:i+8], 2).to_bytes(1, byteorder='big')
    return idxbytes

def bytes2idx(data: bytes) -> List[int]:
    idxbin = ''.join(format(byte, '08b') for byte in data)
    idxbin = idxbin[:(len(idxbin) // 11) * 11]  # Remove excess bits
    idx_list = []
    for i in range(0, len(idxbin), 11):
        idx_list.append(int(idxbin[i:i+11], 2))
    return idx_list
