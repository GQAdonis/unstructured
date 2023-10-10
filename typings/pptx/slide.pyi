from typing import Iterator, Optional

from pptx.shapes.shapetree import SlideShapes
from pptx.shared import ParentedElementProxy, PartElementProxy
from pptx.text.text import TextFrame

class _BaseSlide(PartElementProxy): ...

class NotesSlide(_BaseSlide):
    @property
    def notes_text_frame(self) -> Optional[TextFrame]: ...

class Slide(_BaseSlide):
    @property
    def has_notes_slide(self) -> bool: ...
    @property
    def notes_slide(self) -> NotesSlide: ...
    @property
    def shapes(self) -> SlideShapes: ...

class SlideLayout(_BaseSlide): ...

class SlideLayouts(ParentedElementProxy):
    def __getitem__(self, idx: int) -> SlideLayout: ...
    def __iter__(self) -> Iterator[SlideLayout]: ...
    def __len__(self) -> int: ...

class Slides(ParentedElementProxy):
    def __iter__(self) -> Iterator[Slide]: ...
    def __len__(self) -> int: ...
    def add_slide(self, slide_layout: SlideLayout) -> Slide: ...
