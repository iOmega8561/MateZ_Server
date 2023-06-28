import Vapor

var env = try Environment.detect() // 1
let app = Application(env) // 2

//app.http.server.configuration.hostname = "143.225.56.163"
app.http.server.configuration.hostname = "0.0.0.0"
app.http.server.configuration.port = 9132

defer { // 3
    app.shutdown()
}

var clientConnections = Set<WebSocket>()

app.webSocket("chat") { req, client in
    clientConnections.insert(client)
    
    client.onClose.whenComplete { _ in
        clientConnections.remove(client)
    }
    
    
    client.onText { _, text in // 1
        do {
            guard let data = text.data(using: .utf8) else {
                return
            }

            let incomingMessage = try JSONDecoder().decode(SubmittedChatMessage.self, from: data) // 2
            let outgoingMessage = ReceivingChatMessage(
                message: incomingMessage.message,
                user: incomingMessage.user
            ) // 3
            let json = try JSONEncoder().encode(outgoingMessage) // 4
            
            guard let jsonString = String(data: json, encoding: .utf8) else {
                return
            }

            for connection in clientConnections {
                connection.send(jsonString) // 5
            }
        }
        catch {
            print(error) // 6
        }
    }
}

/*app.webSocket("chat") { req, client in // 5
    print("Connected:", client)
    client.onClose.whenComplete { _ in
        print("Disconnected:", client)
    }
}*/

try app.run() // 6


extension WebSocket: Hashable {
    public static func == (lhs: WebSocket, rhs: WebSocket) -> Bool {
        ObjectIdentifier(lhs) == ObjectIdentifier(rhs)
    }
    
    public func hash(into hasher: inout Hasher) {
        hasher.combine(ObjectIdentifier(self))
    }
}
