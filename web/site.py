
import webapp2


class TreeTypeHandler(webapp2.RequestHandler):
    def get(self):
        j = '{ root: {expanded: true,children: [ { text: "Companies", expanded: true, children: [{ text: "CSP", leaf: true },{ text: "Distributor", leaf: true}] },{ text: "Orders", leaf: true }] } }'
        self.response.write(j)