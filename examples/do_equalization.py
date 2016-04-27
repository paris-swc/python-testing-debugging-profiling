import matplotlib.pyplot as plt

import histograms

if __name__ == '__main__':
    # Load the example image (Note that the example will be a width x height x 3
    # matrix but the values in the last dimension are all identical because it is
    # a black-and-white image. We'll therefore ignore all but one value and make the
    # matrix into a 2D matrix of size width x height).
    image = plt.imread('Unequalized_Hawkes_Bay_NZ.png')[:, :, 0]
    plt.subplot(2, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.clim(0, 1)
    plt.subplot(2, 2, 2)
    histograms.plot_histogram(image)

    # Equalize the image histogram
    equalized = histograms.equalize(image)
    plt.subplot(2, 2, 3)
    plt.imshow(equalized, cmap='gray')
    plt.clim(0, 1)
    plt.subplot(2, 2, 4)
    histograms.plot_histogram(equalized)

    plt.show()  # not necessary when run from the jupyter notebook with inline images

