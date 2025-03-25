from email.mime import base
from nicegui import ui

# ui.add_head_html("""
#     <style type="text/tailwindcss">
#         .nicegui-content {
#             padding: 0;
#             overflow: hidden;
#         }
#     </style>
# """)


def app():
    ui.colors(
        base_100="oklch(100% 0 0)",
        base_200="oklch(93% 0 0)",
        base_300="oklch(86% 0 0)",
        base_400="oklch(80% 0 0)",
    )

    ui.query(".nicegui-content").style("padding: 0; overflow: hidden;")

    with ui.element("div").classes("flex flex-col w-full h-screen"):
        # Header
        with ui.element("header").classes("bg-base-300 p-4"):
            ui.label("Header").classes("text-xl")

        # Main
        with ui.element("div").classes("flex flex-1"):
            # MenuBar
            with ui.element("div").classes(
                "flex flex-col w-xs bg-base-400 p-4 items-center justify-start gap-4"
            ):
                ui.button(icon="home", color="base-100").props("flat round")
                ui.button(icon="search", color="base-100").props("flat round")

            # Left Sidebar
            with ui.element("div").classes("w-[20%] max-w-xs bg-base-200 p-4"):
                ui.label("Left Sidebar").classes("text-xl")

            # Content
            with ui.element("div").classes("grow bg-base-100 p-4"):
                ui.label("Content").classes("text-xl")

            # Right Sidebar
            with ui.element("div").classes("w-[20%] max-w-xs bg-base-200 p-4"):
                ui.label("Right Sidebar").classes("text-xl")

        # Footer
        with ui.element("footer").classes("bg-base-300 p-4"):
            ui.label("Footer").classes("text-xl")
