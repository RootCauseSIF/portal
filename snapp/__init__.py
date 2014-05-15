from django.forms.widgets import Widget, MultiWidget, TextInput


class FancyMWidget(MultiWidget):
    def decompress(self, value):
            return ["WHOCARES","sdfdsfICARE"]

class MatrixWidget(Widget):


    def render(self, name, value, attrs=None):
        # x, y = attrs.dimensions
        widgets = []
        # widgets.append(TextInput())
        # widgets.append(TextInput())
        widgets.append(TextInput())
        widgets.append(TextInput())

        result = ""
        for w in widgets:
            result = result + w.render(name, value)

        mw = FancyMWidget(widgets)

        # print "THE END IS "
        # print mw.render("ONE", "TWO")
        # print "---"
        return mw.render("NAME", "VALUEX");
        # return result;
        # return "MOO"
        # return "attrs: " + str(self.attrs)
        # return "<h1>" + "matrix_rows::" + str("")+ str(attrs) + "attr:::" + name + "name:::" + str(self) + "self:::" + str(dir(self)) + "</h1>"
