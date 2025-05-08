# QR Code Generator

A lightweight Python script that allows users to generate QR codes from any URL or text input. The output is a PNG image containing the QR code.

## 📌 Features

- Converts text or URLs into scannable QR codes.
- Saves the output as a PNG file.
- Minimal dependencies and easy to run.

## 🚀 How to Run the Script

### 1. Clone the Repository

If you're using GitHub:

```bash
git clone https://github.com/yourusername/qr-code-generator.git
cd qr-code-generator
```

2. Set Up the Environment
Make sure you have Python 3.x installed. Then install the required package:
pip install qrcode[pil]

3. Run the Script
Execute the script with:
python app.py

You'll see:
Enter the link to generate QR Code:
Enter any valid URL or text.

For example:
https://example.com
The script will then generate and save qrcode.png in the current directory.

File Structure:
qr-code-generator/
├── app.py         # Main QR code generation script
└── README.md      # Project documentation
