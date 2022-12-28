from core.services.render import GraphRenderBase


class Renderer3(GraphRenderBase):
    def identifier(self) -> str:
        return "#Renderer3"


    def name(self) -> str:
        return "Renderer3"


    def render(self) -> None:
        return None