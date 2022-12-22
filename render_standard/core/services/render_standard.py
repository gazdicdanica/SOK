from core.services.render import GraphRenderBase


class RendererStandard(GraphRenderBase):
    def identifier(self) -> str:
        return "#RendererStandard"


    def name(self) -> str:
        return "RendererStandard"


    def render(self) -> None:
        return None