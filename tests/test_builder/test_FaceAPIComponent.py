"""
Tests for the ExampleComponent class, essentially showcases how to implement basic tests on a Component.
"""

from psychopy_face_api.components.faceAPI import FaceAPIComponent
from psychopy.tests.test_experiment.test_components.test_base_components import BaseComponentTests, _TestLibraryClassMixin

class TestFaceAPIComponent(BaseComponentTests, _TestLibraryClassMixin):
    comp = FaceAPIComponent
    libraryClass = None
