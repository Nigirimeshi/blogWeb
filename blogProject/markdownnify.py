from markdown import markdown

from .settings import (
    MARKDOWNX_MARKDOWN_EXTENSIONS,
    MARKDOWNX_MARKDOWN_EXTENSION_CONFIGS,
)

def markdownify(content):
    md = markdown(
        text=content,
        extensions=MARKDOWNX_MARKDOWN_EXTENSIONS,
        extension_configs=MARKDOWNX_MARKDOWN_EXTENSION_CONFIGS
    )
    return md