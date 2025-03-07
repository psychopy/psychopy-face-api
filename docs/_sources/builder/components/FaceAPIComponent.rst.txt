.. _faceapicomponent:

-------------------------------
Face APIComponent
-------------------------------

Use the Face API JS library to get face and emotion data from a Camera Component

Categories:
    Responses
Works in:
    PsychoJS

**Note: Since this is still in beta, keep an eye out for bug fixes.**

Parameters
-------------------------------

Basic
===============================

.. _faceapicomponent-name:
Name 
    Name of this Component (alphanumeric or _, no spaces)
    
.. _faceapicomponent-startVal:
Start 
    When does the Component start?
    
.. _faceapicomponent-startEstim:
Expected start (s) 
    (Optional) expected start (s), purely for representing in the timeline
    
.. _faceapicomponent-startType:
Start type 
    How do you want to define your start point?
    
    Options:
    
    * time (s)
    
    * frame N
    
    * condition
    
.. _faceapicomponent-stopVal:
Stop 
    When does the Component end? (blank is endless)
    
.. _faceapicomponent-durationEstim:
Expected duration (s) 
    (Optional) expected duration (s), purely for representing in the timeline
    
.. _faceapicomponent-stopType:
Stop type 
    How do you want to define your end point?
    
    Options:
    
    * duration (s)
    
    * duration (frames)
    
    * time (s)
    
    * frame N
    
    * condition
    
.. _faceapicomponent-camera:
Camera 
    Camera Component whose footage to detect faces with.
    
Layout
===============================




.. _faceapicomponent-size:
Size [w,h] 
    Size of this stimulus (either a single value or x,y pair, e.g. 2.5, [1,2] 
    
.. _faceapicomponent-pos:
Position [x,y] 
    Position of this stimulus (e.g. [1,2] )
    
.. _faceapicomponent-units:
Spatial units 
    Units of dimensions for this stimulus
    
    Options:
    
    * from exp settings
    
    * deg
    
    * cm
    
    * pix
    
    * norm
    
    * height
    
    * degFlatPos
    
    * degFlat
    
.. _faceapicomponent-ori:
Orientation 
    Orientation of this stimulus (in deg)
    
    Options:
    
    * -360
    
    * 360
    
Appearance
===============================




.. _faceapicomponent-opacity:
Opacity 
    Opacity of the stimulus (1=opaque, 0=fully transparent, 0.5=translucent). Leave blank for each color to have its own opacity (recommended if any color is None).
    
Data
===============================




.. _faceapicomponent-saveStartStop:
Save onset/offset times 
    Store the onset/offset times in the data file (as well as in the log file).
    
.. _faceapicomponent-syncScreenRefresh:
Sync timing with screen refresh 
    Synchronize times with screen refresh (good for visual stimuli and responses based on them)
    
Testing
===============================




.. _faceapicomponent-disabled:
Disable Component 
    Disable this Component
    