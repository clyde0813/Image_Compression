from io import BytesIO
from PIL import Image
import os


def compress(image):
    im = Image.open('original/'+image)
    im_io = BytesIO()
    im.save(im_io, 'JPEG', quality=60)
    with open('compressed/Compressed_'+image+'.jpg', 'wb') as file:
        file.write(im_io.getvalue())
    original_image_size = os.path.getsize('original/'+image)
    compressed_image_size = os.path.getsize('compressed/Compressed_'+image+'.jpg')
    print('Original Lena Size : ', original_image_size, '\nCompressed Lena Size : ', compressed_image_size,
          '\nCompression Percent : ', original_image_size / compressed_image_size * 100, '%')


file_list = os.listdir('original')
for file in file_list:
    compress(file)

'''
https://stackoverflow.com/questions/67629703/compressing-a-video-file-in-python-with-the-standard-library

Video files are already compressed. You cannot compress them further, at least not significantly.

Your only option would be to decompress them, and then recompress them with a more effective compressor, e.g. HEVC.
'''
