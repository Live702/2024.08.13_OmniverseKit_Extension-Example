import omni.ext
import omni.ui as ui
from omni.kit.widget.viewport import ViewportWidget

import omni.usd
import omni.physx as physx

from pxr import UsdGeom, Gf

import sys
import datetime

import omni.kit.viewport
#'''
class InscicoExample_1Extension(omni.ext.IExt):
    name = "Example_1"

    def on_startup(self, ext_id):
        self.box_rendered = False
        self.camera_added = False
        print("\n") 
        print(f"{datetime.datetime.now()} {self.name} Completed: init")
        #update scene
        try:
            if not self.box_rendered: 
                self.add_box_to_scene()
                print(f"{datetime.datetime.now()} {self.name} Added to Scene: box ")


            if not self.camera_added: 
                self.add_camera_to_scene()
                print(f"{datetime.datetime.now()} {self.name} Added to Scene: camera")

        except Exception as e:
            print(f"{datetime.datetime.now()} {self.name} Error: Scene: {type(e).__name__}: {e}") 

        #update ui
        try:
            self._window = ui.Window("My Window", width=1280, height=720+20)
            with self._window.frame:
                with ui.VStack():
                    # Viewport section
                    self.viewport_widget = ViewportWidget(resolution=(1280, 720))
                    self.viewport_api = self.viewport_widget.viewport_api

                    print(f"{datetime.datetime.now()} {self.name} Added to UI: window")

                    #print(dir(self.viewport_api))

        except Exception as e:
            print(f"{datetime.datetime.now()} {self.name} Error: UI: {type(e).__name__}: {e}") 

        print(f"{datetime.datetime.now()} {self.name} Completed: startup")

    def on_shutdown(self):
        try:
            self.viewport_widget.destroy()
            self._window.destroy()

        except Exception as e:
            print(f"{datetime.datetime.now()} {self.name} Error: shutdown {type(e).__name__}: {e}") 
        
        print(f"{datetime.datetime.now()} {self.name} Completed: shutdown")

    def add_box_to_scene(self):
        self.box_rendered = True

        stage = omni.usd.get_context().get_stage()
        prim_path = "/World/box" 

        cube_prim = stage.DefinePrim(prim_path, "Cube")

        UsdGeom.XformCommonAPI(cube_prim).SetTranslate((0, 0, 0)) 
        UsdGeom.Cube(cube_prim).CreateSizeAttr(1)

    def add_camera_to_scene(self):
        self.camera_added = True
        stage = omni.usd.get_context().get_stage()
        camera_path = "/World/myNewCamera" 
        camera_prim = stage.DefinePrim(camera_path, "Camera")
        UsdGeom.Camera(camera_prim).SetFocalLength(50.0)
        #viewport_api.camera_path = camera_path

        viewport_interface = omni.kit.viewport.get_viewport_interface()
        viewport = viewport_interface.get_active_viewport()
        if viewport:
            viewport.set_camera_path(camera_path)
#''' 
