"""
Module to perform histogram equalization.
Note that this code is buggy, it is used to demonstrate the debugger.
"""
import numpy
import matplotlib.pyplot as plt

def plot_histogram(data, n_bins=256):
    bins = numpy.linspace(0, 1, n_bins, endpoint=True)
    histogram, bins = numpy.histogram(data.flatten(), bins=bins, density=True)
    cdf = numpy.cumsum(histogram) / n_bins
    ax1 = plt.gca()
    ax1.plot(bins[:-1], histogram, lw=2)
    ax2 = ax1.twinx()
    ax2.plot(bins[:-1], cdf, 'r', lw=2)

def equalize(image, n_bins=256):
    """
    Perform histogram equalization on the given grayscale ``image`` (2D array
    of intensity values between 0 and 1), using ``n_bins`` bins for the
    histogram.
    Returns the equalized image.
    """
    bins = numpy.linspace(0, 1, n_bins, endpoint=True)
    bins, hist = numpy.histogram(image.flatten(), bins=bins, density=True)
    cdf = hist.cumsum() / n_bins
    # Invert the CDF by using numpy's interp function
    equalized = numpy.interp(image.flatten(), bins, cdf)

    # All this was performed on flattened versions of the image, reshape the
    # equalized image back to the original shape
    return equalized.reshape(image.shape)
