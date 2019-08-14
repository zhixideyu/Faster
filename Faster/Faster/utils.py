import mistune
from mistune import escape, escape_link
from pygments import highlight
from pygments.formatters import html
from pygments.lexers import get_lexer_by_name
from django.contrib.sites.models import Site


def block_code(text, lang, inlinestyles=False, linenos=False):
    """ markdown代码高亮 """
    if not lang:
        text = text.strip()
        return u'<pre><code>%s</code></pre>\n' % mistune.escape(text)

    try:
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = html.HtmlFormatter(
            noclasses=inlinestyles, linenos=linenos
        )
        code = highlight(text, lexer, formatter)
        if linenos:
            return '<div class="highlight">%s</div>\n' % code
        return code
    except:
        return '<pre class="%s"><code>%s</code></pre>\n' % (
            lang, mistune.escape(text)
        )


def get_current_site():
    site = Site.objects.get_current()
    return site


class BlogMarkDownRenderer(mistune.Renderer):
    """ 渲染 """

    def block_code(self, text, lang=None):
        # renderer has an options
        inlinestyles = self.options.get('inlinestyles')
        linenos = self.options.get('linenos')
        return block_code(text, lang, inlinestyles, linenos)

    def autolink(self, link, is_email=False):
        text = link = escape(link)

        if is_email:
            link = 'mailto:%s' % link
        if not link:
            link = "#"
        site = get_current_site()
        nofollow = "" if link.find(site.domain) > 0 else "rel='nofollow'"
        return '<a href="%s" %s>%s</a>' % (link, nofollow, text)

    def link(self, link, title, text):
        link = escape_link(link)
        site = get_current_site()
        nofollow = "" if link.find(site.domain) > 0 else "rel='nofollow'"
        if not link:
            link = "#"
        if not title:
            return '<a href="%s" %s>%s</a>' % (link, nofollow, text)
        title = escape(title, quote=True)
        return '<a href="%s" title="%s" %s>%s</a>' % (link, title, nofollow, text)


class CommonMarkdown:
    @staticmethod
    def get_markdown(value):
        renderer = BlogMarkDownRenderer(inlinestyles=False)
        mdp = mistune.Markdown(escape=True, renderer=renderer)
        return mdp(value)
