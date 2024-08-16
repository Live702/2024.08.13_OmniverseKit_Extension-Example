#"""
import omni.ext
import omni.ui as ui
from omni.kit.widget.viewport import ViewportWidget

import omni.usd
import omni.physx as physx

from pxr import UsdGeom

import sys

#import pyautogui

class InscicoExample_1Extension(omni.ext.IExt):
    def __init__(self):
        print("trace")
        self.box_rendered = False
        self.mydebugstring = sys.executable
        #window_title = 'Discord'

    def on_startup(self, ext_id):
        print("[inscico.example_1] inscico example_1 startup")

        self._window = ui.Window("My Window", width=1280, height=720+20)
        with self._window.frame:
            with ui.VStack():
                # Viewport section
                self.viewport_widget = ViewportWidget(resolution=(1280, 720))
                self.viewport_api = self.viewport_widget.viewport_api

                if not self.box_rendered: 
                    self.add_box_to_scene()

                with ui.HStack():
                    ui.Label(
                        #"foo"
                        self.mydebugstring
                        )

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

    # def capture_and_ocr(window_title):
    #     try:
    #         # Find the window by title (you might need to adjust the title)
    #         window = pyautogui.getWindowsWithTitle(window_title)[0]

    #         while True:
    #             # Take a screenshot of the specified window
    #             screenshot = pyautogui.screenshot(region=(window.left, window.top, window.width, window.height))

    #             # Convert screenshot to OpenCV format (numpy array)
    #             frame = np.array(screenshot)
    #             frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    #             # Apply OCR to the captured frame
    #             results = reader.readtext(frame, detail=0)

    #             # Display detected text (console output)
    #             print("Detected Text:", results)

    #             # Draw bounding boxes and text on the frame (for visualization if needed)
    #             # (This part is similar to the previous code and can be uncommented if you want to display the image)

    #             # Check for stop signal (press 'q' to quit)
    #             if cv2.waitKey(1) & 0xFF == ord('q'):
    #                 cv2.destroyAllWindows()
    #                 break
    #     except IndexError:
    #         print(f"Window with title '{window_title}' not found.")
        
#""""