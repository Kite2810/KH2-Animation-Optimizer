bl_info = {
    "name": "KH2 Animation Optimizer",
    "author": "Kité",
    "version": (1, 1),
    "blender": (3, 0, 0),
    "location": "3D Viewport > Sidebar > KH2 Anb Optimizer",
    "description": "Moves all Keyframes to evenly spaced intervals (1, 1.5, 2, 2.5, etc.)",
    "category": "Animation",
}

import bpy
from bpy.props import FloatProperty, IntProperty
from bpy.types import Operator, Panel, PropertyGroup


class EvenlyStaggerProperties(PropertyGroup):
    start: FloatProperty(
        name="Start Frame",
        default=1.0,
        description="Startpoint of the first Keyframe"
    )
    spacing: FloatProperty(
        name="Frame spacing",
        default=2.0,
        description="Time interval between the keyframes"
    )
    fps: IntProperty(
        name="New Frame Rate",
        default=60,
        min=1,
        description="Frame Rate"
    )


class ANIM_OT_evenly_stagger_keyframes(Operator):
    bl_idname = "anim.evenly_stagger_keyframes"
    bl_label = "Evenly distribute keyframes"
    bl_description = "Moves all Keyframes to evenly spaced intervals"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.object
        props = context.scene.evenly_stagger_props

        if not obj or not obj.animation_data or not obj.animation_data.action:
            self.report({'ERROR'}, "No Animated Armature found.")
            return {'CANCELLED'}

        action = obj.animation_data.action

        for fcurve in action.fcurves:
            keyframes = fcurve.keyframe_points

            for i, key in enumerate(keyframes):
                new_frame = props.start + (i * props.spacing)
                key.co.x = new_frame

        context.scene.render.fps = props.fps
        self.report({'INFO'}, f"Keyframes redistributed. FPS = {props.fps}")
        return {'FINISHED'}


class ANIM_PT_evenly_stagger_panel(Panel):
    bl_label = "KH2 Animation Optimizer"
    bl_idname = "ANIM_PT_evenly_stagger_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'KH2 Animation Optimizer'

    def draw(self, context):
        layout = self.layout
        props = context.scene.evenly_stagger_props

        layout.prop(props, "start")
        layout.prop(props, "spacing")
        layout.prop(props, "fps")
        layout.operator("anim.evenly_stagger_keyframes", icon='TIME')


# Registrierung
classes = (
    EvenlyStaggerProperties,
    ANIM_OT_evenly_stagger_keyframes,
    ANIM_PT_evenly_stagger_panel,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.evenly_stagger_props = bpy.props.PointerProperty(type=EvenlyStaggerProperties)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.evenly_stagger_props


if __name__ == "__main__":
    register()
