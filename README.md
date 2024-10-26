# Hamming Code Error Correction in WebSocket Communication

This repository demonstrates the use of Hamming Code to correct errors in data transmission over WebSockets. It includes a sender that encodes data with Hamming Code, transmits it (with optional noise injection to simulate errors), and a receiver that decodes and corrects any detected errors. This project provides a practical example of how error-correcting codes are implemented in real-world data communication systems.

## 🚀 Project Overview

In this project:
- **Sender**: Converts text data to binary, encodes each 4-bit segment using Hamming(7,4), and transmits it over WebSocket. Includes an option to simulate noise by randomly flipping bits in the packets.
- **Receiver**: Receives the encoded data, applies Hamming decoding to correct any single-bit errors, and reconstructs the original message to verify transmission integrity.

The project is structured for easy testing and exploration of error correction in a real-time environment.

### 📂 Project Structure
- `sender.py`: Encodes and sends the text data, applying Hamming Code and noise simulation.
- `receiver.py`: Receives and decodes the data, applying Hamming correction if enabled, and reconstructs the transmitted message.

### 🛠️ Getting Started

1. **Install Dependencies**: Ensure you have Python and the `websockets` library installed:
   ```bash
   pip install websockets
   ```
2. **Run the Sender**: Start the sender in one terminal instance:
   ```bash
   python sender.py
   ```
3. **Run the Receiver**: In a second terminal instance, start the receiver:
   ```bash
   python receiver.py
   ```

### 💡 How It Works
The sender encodes each character into binary, divides it into segments, applies Hamming encoding, and transmits it over WebSocket. The receiver decodes each segment, corrects errors using Hamming Code, and reassembles the message, ensuring integrity.

### 🧩 Contributing

We welcome contributions! Here’s how you can help:
- **Improve Encoding/Decoding Efficiency**: Suggest optimizations in data handling and error correction.
- **Add More Error Simulation Options**: Implement different noise patterns to simulate more complex transmission errors.
- **Extend Hamming Code Implementation**: Experiment with other versions of Hamming Code or error-correcting codes.

**Feel free to fork this repo, submit pull requests, and share your ideas! Together, we can make this project a comprehensive guide to error correction.**

### 📄 License
This project is open-source and available under the MIT License.

---

Let’s make data communication resilient, one bit at a time! ✨
