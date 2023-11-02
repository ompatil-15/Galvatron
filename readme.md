# Galvatron - Infinite Storage Glitch

!(https://github.com/ompatil-15/Galvatron/blob/master/assets/video.mp4)

## Overview

Galvatron is a Python-based tool designed to encode and decode binary data into obscure videos. It utilizes a unique approach to data storage and retrieval, converting binary data into frames of a binary image that can be assembled into an encrypted video, and vice versa. The generated encrypted videos can also be uploaded to platforms like YouTube, providing a creative way to achieve what seems like 'infinite' storage in the cloud. 

This README provides an overview of the tool's main functionality, its use cases, and instructions for use.

## Features

- **Encoding Data into Videos**:
  - Convert binary data from a file into a binary string.
  - Append the binary representation of the file's extension.
  - Divide binary data into frames of a binary image.
  - Save frames as individual PNG images and create an encrypted video.

- **Decoding Videos into Data**:
  - Extract frames from an encrypted video.
  - Convert frames back into binary data.
  - Extract the original file extension from the binary data.
  - Convert binary data into a file with the extracted extension.

- **Menu Interface**:
  - Choose between encoding and decoding options using a menu-driven interface.

- **Cleanup**:
  - Automatically remove temporary files and folders created during the process.

## Usage

1. **Encoding a File into a Video**:
   - Run the tool and choose the encoding option from the menu.
   - Provide the file you want to encode and the output video filename.
   - The tool will create an encrypted video with your data.

2. **Decoding a Video into a File**:
   - Run the tool and choose the decoding option.
   - Specify the input encrypted video file and the desired output filename.
   - The tool will extract the data and create a file with the original extension.

   ![Usage](/assets/usage.png)

## Use Cases

- Experimenting with unconventional data storage methods.
- Hiding data within video files.
- Obfuscating file extensions.

## Notes

- This tool is only for Educational purposes, Don't use for any illegal activity.
- Please use this tool with caution, especially for important data. It may not provide the same level of security as conventional encryption methods.


