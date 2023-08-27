

%Name-Surname: Emine Aydın
%ID: 190315053
sentinel='$';
I = imread('21.tif');
[height, width, ~] = size(I);
pixels = reshape(I, [],1);
pixels = double(pixels);
lsb_plane = bitget(pixels(:,1),1);
bits = reshape(lsb_plane', 1, []);
 message = '';
for i = 1:8:length(bits)
    byte = bits(i:i+7);
    byte_str = num2str(byte);
    byte_ascii = bin2dec(byte_str);
    char = native2unicode(byte_ascii);
    message = [message char];
    if char == sentinel
        break;
    end
end
reversedMessage = reverse(message);
disp(["Message: " + reversedMessage]);