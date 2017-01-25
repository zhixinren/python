class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self, new_data):
        if new_data is None:
            return
        self.datas.append(new_data)

    def output_html(self):
        fou = open('fou.html','w')
        fou.write("<html>")
        fou.write("<body>")
        fou.write("<table>")
        for data in self.datas:
            fou.write("<tr>")
            fou.write("<td> %s </td>" % data['url'].encode('utf-8'))
            fou.write("<td> %s </td>" % data['title'].encode('utf-8'))
            fou.write("<td> %s </td>" % data['summary'].encode('utf-8'))
            fou.write("</tr>")
        fou.write("</table>")
        fou.write("</body>")
        fou.write("</html>")
