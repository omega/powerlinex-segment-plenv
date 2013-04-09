# Powerline eXtenstion for plenv

An attempt at a proof of concept powerline custom segment, to try to figure out
the propper way of writing those. This adds a segment with a virtualenv method.

First install the addon:

    pip install -U --user git+https://github.com/omega/powerlinex-segment-plenv.git

If you make a theme, you can include a custom `segment_data`:

    "version": {
        "before": "ⓔ  "
    },

And then add this to your prefered spot under `segments`:

    {
        "module": "powerlinex.segment.plenv",
        "name": "version"
    },

Whenever you are in a folder with a non-default perl version specified, it will
add a segment showing the perl version name.

The `highlight_group` of the segment returned is `perl_version`, `virtualenv`,
in that order. This will be highlighted in the same way as `virtualenv`, unless
you specify something else in the `perl_version` color.
