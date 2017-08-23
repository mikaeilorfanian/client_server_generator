from server_generator.server_generator import BottleServer, MagicRouter


class HelloNameURLHandler(MagicRouter):
    route_name = 'hello_name'

    def handler(self):
        return 'hello {}'.format(self.name)


app = BottleServer(
    HelloNameURLHandler(),
)
app.run()
