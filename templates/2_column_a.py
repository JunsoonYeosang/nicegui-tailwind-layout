from nicegui import ui


def app():
    ui.colors(
        base_100="oklch(100% 0 0)",
        base_200="oklch(93% 0 0)",
        base_300="oklch(86% 0 0)",
    )

    ui.query(".nicegui-content").style("padding: 0; overflow: hidden;")

    with ui.element("div").classes("flex w-full h-screen"):
        # Sidebar
        # max-w : https://tailwindcss.com/docs/max-width
        with ui.element("div").classes("w-[30%] max-w-xs bg-base-200 p-4"):
            ui.label("Sidebar").classes("text-xl")

        # Main
        with ui.element("div").classes("grow bg-base-100 p-4"):
            ui.label("Content").classes("text-xl")
