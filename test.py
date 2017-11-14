# from PIL import Image
# from PIL import ImageFilter
# from PIL import ImageOps
# from matplotlib import pyplot as plt
#
# # This module can classfy the image by Average Hash Method
# # The Hash Method is too strict,so this moudel suitable for finding image by Thumbnail
# #
# # author MashiMaroLjc
# # version 2016-2-17
#
# def getCode(img, size):
#     pixel = []
#     for x in range(0, size[0]):
#         for y in range(0, size[1]):
#             pixel_value = img.getpixel((x, y))
#             pixel.append(pixel_value)
#
#     avg = sum(pixel) / len(pixel)
#
#     cp = []
#
#     for px in pixel:
#         if px > avg:
#             cp.append(1)
#         else:
#             cp.append(0)
#     return cp
#
#
# def compCode(code1, code2):
#     num = 0
#     for index in range(0, len(code1)):
#         if code1[index] != code2[index]:
#             num += 1
#     return num
#
#
# def classfiy_aHash(image1, image2, size=(64, 64), exact=25):
#     ''' 'image1' and 'image2' is a Image Object.
#     You can build it by 'Image.open(path)'.
#     'Size' is parameter what the image will resize to it and then image will be compared by the algorithm.
#     It's 8 * 8 when it default.
#     'exact' is parameter for limiting the Hamming code between 'image1' and 'image2',it's 25 when it default.
#     The result become strict when the exact become less.
#     This function return the true when the 'image1'  and 'image2' are similar.
#     '''
#     image1 = image1.resize(size).convert('L').filter(ImageFilter.BLUR)
#     # image1.show()
#     image1 = ImageOps.equalize(image1)
#     code1 = getCode(image1, size)
#     print(code1)
#     image2 = image2.resize(size).convert('L').filter(ImageFilter.BLUR)
#     # image2.show()
#     image2 = ImageOps.equalize(image2)
#     code2 = getCode(image2, size)
#     print(code2)
#
#     assert len(code1) == len(code2), "error"
#
#     return compCode(code1, code2)
#
#
# from PIL import Image
# from PIL import ImageFilter
# from PIL import ImageOps
#
#
# # This module can classfy the image by dHash
# #
# # author MashiMaroLjc
# # version 2016-2-16
#
# def getCode(img, size):
#     result = []
#     # print("x==",size[0])
#     # print("y==",size[1]-1)
#
#     x_size = size[0] - 1  # width
#     y_size = size[1]  # high
#     for x in range(0, x_size):
#         for y in range(0, y_size):
#             now_value = img.getpixel((x, y))
#             next_value = img.getpixel((x + 1, y))
#
#             if next_value < now_value:
#                 result.append(1)
#             else:
#                 result.append(0)
#
#     return result
#
#
# def compCode(code1, code2):
#     num = 0
#     for index in range(0, len(code1)):
#         if code1[index] != code2[index]:
#             num += 1
#     return num
#
#
# def classfiy_dHash(image1, image2, size=(9, 8)):
#     ''' 'image1' and 'image2' is a Image Object.
#     You can build it by 'Image.open(path)'.
#     'Size' is parameter what the image will resize to it and then image will be compared to another image by the dHash.
#     It's 9 * 8 when it default.
#     The function will return the hamming code,less is correct.
#     '''
#     image1 = image1.resize(size).convert('L')
#     code1 = getCode(image1, size)
#
#     image2 = image2.resize(size).convert('L')
#     code2 = getCode(image2, size)
#
#     assert len(code1) == len(code2), "error"
#
#     return compCode(code1, code2)
from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps


# This module can classfy the image by dHash
#
# author MashiMaroLjc
# version 2016-2-16

def getCode(img, size):
    result = []
    # print("x==",size[0])
    # print("y==",size[1]-1)

    x_size = size[0] - 1  # width
    y_size = size[1]  # high
    for x in range(0, x_size):
        for y in range(0, y_size):
            now_value = img.getpixel((x, y))
            next_value = img.getpixel((x + 1, y))

            if next_value < now_value:
                result.append(1)
            else:
                result.append(0)

    return result


def compCode(code1, code2):
    num = 0
    for index in range(0, len(code1)):
        if code1[index] != code2[index]:
            num += 1
    return num


def classfiy_dHash(image1, image2, size=(8, 8)):
    ''' 'image1' and 'image2' is a Image Object.
    You can build it by 'Image.open(path)'.
    'Size' is parameter what the image will resize to it and then image will be compared to another image by the dHash.
    It's 9 * 8 when it default.
    The function will return the hamming code,less is correct.
    '''
    image1 = image1.resize(size).convert('L')
    code1 = getCode(image1, size)
    print(code1)

    image2 = image2.resize(size).convert('L')
    code2 = getCode(image2, size)
    print(code2)

    assert len(code1) == len(code2), "error"

    return compCode(code1, code2)
img1 = Image.open('/home/william/Download/lfj/004.jpg')
img2 = Image.open('/home/william/Download/lfj/005.jpg')
print(classfiy_dHash(img1,img2))