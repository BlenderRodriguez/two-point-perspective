import bpy
from bpy.types import Panel


class Camera_PT_Panel(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Camera"
    bl_label = "Two-Point Perspective"
    bl_idname = "VIEW3D_PT_two_point_perspective"

    def draw(self, context):
        layout = self.layout
        two_point_perspective = context.scene.two_point_perspective

        box = layout.box()

        row0 = box.row(align=True)
        col0_0 = row0.column()
        col0_0.prop(two_point_perspective, "custom_angle", text="Custom Angle")

        col0_1 = row0.column()
        col0_1.enabled = two_point_perspective.custom_angle
        col0_1.prop(two_point_perspective, "custom_angle_value", text="Angle")

        layout.separator()
        layout.operator("scene.two_point_perspective", icon="CON_CAMERASOLVER")
