def get_stars(starcat_time, quaternion, radius=1.5):
    import agasc
    from Ska.quatutil import radec2yagzag
    from chandra_aca.transform import yagzag_to_pixels
    stars = agasc.get_agasc_cone(quaternion.ra, quaternion.dec,
                                 radius=radius,
                                 date=starcat_time)

    if 'yang' not in stars.colnames or 'zang' not in stars.colnames:
        # Add star Y angle and Z angle in arcsec to the stars table.
        # radec2yagzag returns degrees.
        yags, zags = radec2yagzag(stars['RA_PMCORR'], stars['DEC_PMCORR'], quaternion)
        stars['yang'] = yags * 3600
        stars['zang'] = zags * 3600

    # Update table to include row/col values corresponding to yag/zag
    rows, cols = yagzag_to_pixels(stars['yang'], stars['zang'], allow_bad=True)
    stars['row'] = rows
    stars['col'] = cols

    return stars