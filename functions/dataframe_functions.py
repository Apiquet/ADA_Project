def magnify():
    return [dict(selector="th",
                 props=[("font-size", "8pt")]),
            dict(selector="td",
                 props=[('padding', "0em 0em")]),
            dict(selector="th:hover",
                 props=[("font-size", "12pt")]),
            dict(selector="tr:hover td:hover",
                 props=[('max-width', '200px'),
                        ('font-size', '12pt')])]
def highlight_text(data, color='red', text = ''):
    '''
    highlight the maximum in a Series or DataFrame
    '''
    attr = 'background-color: {}'.format(color)
    if data.ndim == 1:  # Series from .apply(axis=0) or axis=1
        is_max = data.str.contains(text)
        return [attr if v else '' for v in is_max]
    else:  # from .apply(axis=None)
        is_max = data.str.contains(text)
        return pd.DataFrame(np.where(is_max, attr, ''),
                            index=data.index, columns=data.columns)