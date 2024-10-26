import asyncio
import random
import websockets

def add_noise(data, noise_level=0.1):
    """Randomly flip bits based on noise level."""
    noisy_data = bytearray(data)
    for i in range(len(noisy_data) * 8):
        if random.random() < noise_level:
            byte_index = i // 8
            bit_index = i % 8
            noisy_data[byte_index] ^= (1 << bit_index)  # Flip bit
    return bytes(noisy_data)

def hamming_encode_4bit(data):
    """Encodes 4-bit data into 7-bit Hamming code."""
    d = list(map(int, f"{data:04b}"))
    p1 = d[0] ^ d[1] ^ d[3]
    p2 = d[0] ^ d[2] ^ d[3]
    p4 = d[1] ^ d[2] ^ d[3]
    hamming_data = [p1, p2, d[0], p4, d[1], d[2], d[3]]
    return int("".join(map(str, hamming_data)), 2)

async def sender(websocket, text, noise_enabled=False, noise_level=0.1):
    packets = []
    for char in text:
        char_binary = format(ord(char), '08b')
        for i in range(0, 8, 4):
            segment = int(char_binary[i:i+4], 2)
            packets.append(hamming_encode_4bit(segment))
    
    for packet in packets:
        encoded_packet = bytes([packet])
        if noise_enabled:
            encoded_packet = add_noise(encoded_packet, noise_level)
        await websocket.send(encoded_packet)
        await asyncio.sleep(0.1)  # Simulate delay
    await websocket.send("done")  # Signal end of transmission

async def main():
    text = "hello my name is pritam das"  # Text to send
    async with websockets.serve(lambda ws, _: sender(ws, text, noise_enabled=False), "localhost", 8766):
        await asyncio.Future()  # Run server indefinitely

asyncio.run(main())
