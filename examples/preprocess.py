def whiten(data):
    """
    Return a whitened copy of the data, i.e. data with zero mean and unit
    variance.

    Parameters
    ----------
    data : ndarray
        The data to whiten.

    Returns
    -------
    whitened : ndarray
        The whitened data.
    """
    centered = data - data.mean()
    whitened = centered / data.std()
    return whitened
