def get_lumis(as_picobarns: bool = False):
    # 2018 Measurement:
    # The CMS Collaboration. CMS luminosity measurement for the
    # 2018 data-taking period at √s = 13 TeV. 2019.
    #
    # 2017 Measurement:
    # The CMS Collaboration. CMS luminosity measurement for the
    # 2017 data-taking period at √s = 13 TeV. 2018.
    #
    # 2016 Measurement:
    # The CMS Collaboration. Precision luminosity measurement in
    # proton-proton colisions at √s = 13 TeV in 2015 and 2016 at CMS.
    # Eur. Phys. J. C, 81(9):800,2021.l
    #
    lumis = {
        "2018": 59.8,  # +/- 2.5%
        "2017": 41.5,  # +/- 2.3%
        "2016preVFP": 19.5,  # +/- 1.2%
        "2016postVFP": 16.8,  # +/- 1.2%
        "2016": 36.3,  # +/- 1.2%
        "Run 2": 137.6,
    }
    if as_picobarns:
        lumis = {k: v * 1000 for k, v in lumis.items()}
    return lumis


def get_categories():
    return {
        1: "eeet",
        2: "eemt",
        3: "eett",
        4: "eeem",
        5: "mmet",
        6: "mmmt",
        7: "mmtt",
        8: "mmem",
    }


def get_eras():
    return {
        "2016preVFP": "Summer16",
        "2016postVFP": "Summer16",
        "2017": "Fall17",
        "2018": "Autumn18",
    }


def get_category_labels():
    return {
        "tt": r"$ll\tau_h\tau_h$",
        "et": r"$ll e\tau_h$",
        "mt": r"$ll\mu\tau_h$",
        "em": r"$ll e\mu$",
    }