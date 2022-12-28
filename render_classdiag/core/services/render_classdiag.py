from core.services.render import GraphRenderBase


class RendererClassDiagram(GraphRenderBase):
    def identifier(self) -> str:
        return "#RendererClassDiagram"


    def name(self) -> str:
        return "RendererClassDiagram"


    def render(self) -> None:
        return None