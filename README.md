For KH2 (ANB) use Frame spacing as 2.00 and FPS 60. That's the best option, without getting rotation issues (atleast I never encountered with that any).
For absurd long Animations, make sure, you use while exporting the sample rate option. (you may have to do some math, depending on your animation length)

Certain rotation issues could come, if Keyframes are under the 0.000 Line. Keep something like that in mind.


You can also use Frame spacing as 1.00 and FPS 30. But there is a chance, that some keyframes can suffer from Rotation issues.


You can also use Frame Spacing as 0.50 and FPS 15, but certain animation COULD suffer from rotation issues, if not done
correctly, but this will also greatly reduce the filesize of the output ANB. (which CAN be combined with sample rate 2.00)


For Recom/DDD/BBS Modding, you can keep it as Frame Spacing 1.00 and FPS 30, and it should work just normal.
Use the option aswell for Animations, you have exported, since the keyframes are not even and Framerate is set to 24. (Aset included)
(exception is through the BBSMeshView, that only has the framerate at 25. But for the Recomviewer, KH3DAnim and the Aset Exporter (khkh_xldMii), it's needed)


You can directly export it also as FBX now. (It disables, NLA Strips, Add leaf bones and Key all bones by default)
And change the Sample Rate there aswell. This should overall speed up the process a bit ^^
