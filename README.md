# Rockular

A couple of minitest assertions for manually verifiying images and testing
them against known good perceptual hashes.

### lilcritic

lilcritic is the Python script used to manually validate images on test runs where
they do not yet have known good preceptual hashes generated.

A python script is used here since Python ships with Tk in its stdlib on most
platforms whereas ruby's Tk implementation is only there half the time.
