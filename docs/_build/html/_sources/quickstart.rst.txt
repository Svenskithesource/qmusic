.. default-role:: code

This is a quickstart reference to using QMusic API Wrapper.

=====
Usage
=====

.. code:: python

    from qmusic import Qmusic

    qm = Qmusic()
    channel = qm.get_channel()
    curr_song = channel.current_song()

    print(curr_song.title())