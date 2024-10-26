import asyncio
import websockets

def hamming_decode_7bit(data):
    """Decodes a 7-bit Hamming code and corrects single-bit errors."""
    d = list(map(int, f"{data:07b}"))
    p1 = d[0] ^ d[2] ^ d[4] ^ d[6]
    p2 = d[1] ^ d[2] ^ d[5] ^ d[6]
    p4 = d[3] ^ d[4] ^ d[5] ^ d[6]
    error_pos = p1 * 1 + p2 * 2 + p4 * 4
    if error_pos:
        d[error_pos - 1] ^= 1  # Correct the error
    return int("".join(map(str, d[2:3] + d[4:])), 2)

async def receiver(websocket, hamming_enabled=False):
    received_bits = []
    while True:
        packet = await websocket.recv()
        if packet == "done":
            break
        received_packet = packet[0]
        if hamming_enabled:
            decoded_data = hamming_decode_7bit(received_packet)
        else:
            decoded_data = received_packet & 0b1111  # Assume lower 4 bits for the character segment
        received_bits.append(format(decoded_data, '04b'))

    # Combine received 4-bit segments to reconstruct characters
    received_text = ""
    for i in range(0, len(received_bits), 2):
        char_binary = received_bits[i] + received_bits[i + 1]
        received_text += chr(int(char_binary, 2))

    print(f"Received Text: {received_text}")

async def main():
    async with websockets.connect("ws://localhost:8766") as websocket:
        await receiver(websocket, hamming_enabled=True)

asyncio.run(main())
