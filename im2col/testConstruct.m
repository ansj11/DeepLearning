function testConstruct()

img = imread('/home/ansj/dataSet/VOCdevkit/VOC2012/JPEGImages/2007_000027.jpg');
figure,imshow(img);
title('origin image')
cols = im2colstep(double(img),[3,3,3]);
% [U, S, V] = svd(cols',0);
[U, S, V] = svd(cols,'econ');

% assert U*U'=1
U'*U

% projection to U
proj = U' * cols;

% Construct
cols_cst = U * proj;
img_cst = col2imstep(cols_cst, [3 3 3], size(img), [1 1 1]);
figure,
subplot(1,2,1), imagesc(img);
title('origin image')
subplot(1,2,2), imagesc(uint8(img_cst));
title('construct image')
err = mean(mean(abs(double(img) - img_cst)));
fprintf("construct error: %.6f \n", err);
