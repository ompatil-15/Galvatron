# Infinite Storage Glitch

import os
import re
import math
import shutil
import cv2 as cv 
import numpy as np

def extract_binary_data(file_path):
    try:
        binary_data = ''
        with open(file_path, 'rb') as file:
            byte = file.read(1)
            while byte:
                binary_representation = format(ord(byte), '08b')
                binary_data += binary_representation
                byte = file.read(1)
        return binary_data
    except FileNotFoundError:
        return None

def binary_to_file(binary_data, output_file_path):
    try:
        with open(output_file_path, 'wb') as file:
            bytes_data = bytes([int(binary_data[i:i+8], 2) for i in range(0, len(binary_data), 8)])
            file.write(bytes_data)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
    
def create_dict_of_arrays(binary_data, array_count, height, width):
    count = 0
    for i in range(1, array_count + 1):

        arrays[i] = 255 * np.ones((height, width), dtype=np.uint8)
        for y in range(height):
            if count == len(binary_data):
                break
            for x in range(width):
                if binary_data[count] == '1':
                    arrays[i][y, x] = 0
                count = count + 1
                if count == len(binary_data):
                    break
    return arrays

def create_binary_image(input_file_path, output_image_path, width, height):
    
    with open(input_file_path, 'r') as file:
        binary_data = file.read()

    array_count = math.ceil(len(binary_data) / (height*width))
    create_dict_of_arrays(binary_data, array_count, height, width)

    output_folder = output_image_path
    os.makedirs(output_folder, exist_ok=True)

    for n in range(1, array_count + 1):
        cv.imwrite(os.path.join(output_folder, f"{output_image_path}{n}.png"), arrays[n])
        cv.imshow('Binary Image', arrays[n])

    print('[2] - Succesfully generated video frames from binary data')

def extract_number_from_filename(filename):
    match = re.search(r'\d+', filename)
    if match:
        return int(match.group())
    else:
        return -1
    
def images_to_video(output_folder, output_video, width, height):
    frame_rate = 1
    frame_size = (width, height)

    fourcc = cv.VideoWriter_fourcc(*'mp4v')
    out = cv.VideoWriter(output_video, fourcc, frame_rate, frame_size)

    image_files = [f for f in os.listdir(output_folder) if f.endswith('.png')]
    image_files.sort(key=extract_number_from_filename)

    for filename in image_files:
        img = cv.imread(os.path.join(output_folder, filename))
        out.write(img) 

    out.release() 

    print('[3] - Completed encrypted video generation using frames of binary data')

def extract_frames_from_video(video_path, output_folder, threshold=128):
    os.makedirs(output_folder, exist_ok=True)

    cap = cv.VideoCapture(video_path)

    frame_count = 1

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        _, thresholded_frame = cv.threshold(frame, threshold, 255, cv.THRESH_BINARY)

        output_frame_filename = os.path.join(output_folder, f'frame_{frame_count:03d}.png')
        cv.imwrite(output_frame_filename, thresholded_frame)
        frame_count += 1

    cap.release()

    print(f"\n[1] - Succesfully extracted {frame_count - 1} frames from '{video_path}'")

def frames_to_binary(frames_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    image_files = [f for f in os.listdir(frames_folder) if f.endswith('.png')]
    image_files.sort(key=extract_number_from_filename)
    frame_count = 1
    for filename in image_files:
        image_path = os.path.join(frames_folder, filename)
        image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
        image_array = 1 - (image / 255)
        image_array = np.round(image_array)

        binary_string = ""

        for y in range(height):
            for x in range(width):
                if image_array[y, x] == 0:
                    binary_string += '0'
                else:
                    binary_string += '1'

        new_filename = f"frame{frame_count}.txt"
        
        output_file_path = os.path.join(output_folder, new_filename)
        
        with open(output_file_path, 'w') as file:
            file.write(binary_string)
            frame_count += 1
    print('[2] - Comleted decrypting video frames to binary data')

def binary_text_to_file(binary_text_folder, binary_file):
    binary_string = ""  
    image_files = [f for f in os.listdir(binary_text_folder) if f.endswith('.txt')]
    image_files.sort(key=extract_number_from_filename)

    for filename in image_files:
        with open(os.path.join(binary_text_folder, filename), 'r') as file:
            binary_data = file.read()
        binary_string += binary_data

    with open(binary_file, 'w') as file:
        file.write(binary_string)

while True:
    
    arrays = {}
    width = 480 
    height = 360
    output_binary_text = 'output_binary_text.txt'
    output_frames_folder = 'output_frames'
    frames_folder = 'frames'
    binary_text_folder = 'binary_text_folder'
    output_text_file = 'binary_text.txt'

  
    print("\nInfinite Storage Glitch Menu\n\n\t[1] Encrypt\n\t[2] Decrypt\n\t[3] Exit")

    menu = int(input('\nEnter menu choice: '))

    if menu == 1:

        input_file_path = input('File to encrypt [filename.ext]: ')
        output_video_path = input('Encrypted video [filename.mp4]: ')   

        extension = input_file_path.split('.')[1] 
        #print(extension)    
        extension = extension.encode('utf-8')
        extension = ''.join(format(byte, '08b') for byte in extension)
        while len(extension) < 32:
            extension = '0' + extension
        extension = 24*'1' + extension + 24*'1'    

        binary_data = extract_binary_data(input_file_path)
        binary_data += extension

        if binary_data:            
            print(f"\n[1] - '{input_file_path}' succesfully converted to binary data")
            with open(output_binary_text, 'w') as file: file.write(binary_data)
            create_binary_image(output_binary_text, output_frames_folder, width, height)
            images_to_video(output_frames_folder, output_video_path, width, height)
            print(f"[4] - File '{input_file_path}' succesfully encrpted to video '{output_video_path}'")
        else:
            print(f"[*] - File '{input_file_path}' not found")

    elif menu == 2:

        input_video_path = input('Encrypted video [filename.mp4]: ')
        output_file_path = input('Decrypted file to [filename.ext]: ')
        extract_frames_from_video(input_video_path, frames_folder)
        frames_to_binary(frames_folder, binary_text_folder)
        binary_text_to_file(binary_text_folder, output_text_file)

        with open(output_text_file, 'r') as file:
            raw_binary_data = file.read()
            pattern = r'1{24}([01]{32})1{24}'
            scope = -(height * width)
            matches = re.findall(pattern, raw_binary_data[scope:])
            if matches:
                extension = matches[0]
                extension = ''.join([chr(int(extension[i:i+8], 2)) if extension[i:i+8] != '00000000' else '' for i in range(0, len(extension), 8)])
            else:
                print("[*] - File corrupted")

        pattern_rem = r'1{24}([01]{32})1{24}.*'
        #raw_binary_data = raw_binary_data.replace(pattern, 80 * "0")
        raw_binary_data = re.sub(pattern_rem, '', raw_binary_data)
        output_file_path = f"{output_file_path}.{extension}"
        #print(raw_binary_data)

        if binary_to_file(raw_binary_data, output_file_path):
            print(f"[3] - Video '{input_video_path}' successfully decrypted to '{output_file_path}'")
        else:
            print("[*] - Failed to decrypt file")

    elif menu == 3:
         exit(0)

    else: 
        print('[*] - Valid menu options [1-3]')
    
    temp = [frames_folder, binary_text_folder, output_text_file, output_binary_text, output_frames_folder]

    for item in temp:
        if os.path.exists(item):
            if os.path.isfile(item):
                os.remove(item)
            elif os.path.isdir(item):
                shutil.rmtree(item)
