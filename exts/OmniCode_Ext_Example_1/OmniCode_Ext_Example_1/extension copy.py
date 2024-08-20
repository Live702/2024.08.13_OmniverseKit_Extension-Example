import omni.ext
import omni.ui as ui
from omni.kit.widget.viewport import ViewportWidget

import omni.usd
import omni.physx as physx

from pxr import UsdGeom, Gf

import sys

class InscicoExample_1Extension(omni.ext.IExt):
    def __init__(self):
        print("trace")
        self.box_rendered = False

    def on_startup(self, ext_id):
        print("[inscico.example_1] inscico example_1 startup")

        self._window = ui.Window("My Window", width=1280, height=720+20)
        with self._window.frame:
            with ui.VStack():
                # Viewport section
                self.viewport_widget = ViewportWidget(resolution=(1280, 720))
                self.viewport_api = self.viewport_widget.viewport_api
                
                camera = viewport_window.get_active_camera()
                camera_position = Gf.Vec3d(3, 1.5, 0) 

                print(dir(self.viewport_api))

                if not self.box_rendered: 
                    self.add_box_to_scene()

    def on_shutdown(self):
        print("[inscico.example_1] inscico example_1 shutdown")
        self.viewport_widget.destroy()
        self._window.destroy()

    def add_box_to_scene(self):
        self.box_rendered = True

        stage = omni.usd.get_context().get_stage()
        prim_path = "/World/box" 

        cube_prim = stage.DefinePrim(prim_path, "Cube")

        UsdGeom.XformCommonAPI(cube_prim).SetTranslate((0, 0, 0)) 
        UsdGeom.Cube(cube_prim).CreateSizeAttr(1)