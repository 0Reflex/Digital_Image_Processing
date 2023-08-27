
% Name-Surname: Emine Aydın
% ID: 190315053

RGB = imread('toysflash.png');
RGB_gray = rgb2gray(RGB);
RGB_rot = imrotate(RGB,45);
subplot(2,2,1); imshow(RGB), title('RGB')
subplot(2,2,2); imshow(RGB_gray), title('Grayscale')
subplot(2,2,3); imshow(RGB_rot), title('Rotated')
subplot(2,2,4); imhist(RGB_gray), title('Histogram')



