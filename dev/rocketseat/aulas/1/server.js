import http from 'node:http'

// - Criar usuários
// - Listagem usuários
// - Edicão de usuários
// - Remoção de usuários

// - HTTP
//    - Método HTTP
//    - URL

// GET, POST, PUT, PATCH, DELETE

// GET => Buscar um recurso do backend
// POST => CRiar um recurso no backend
// PUT => Atualizar um recurso no backend
// PATCH => Atualizar uma informação específica de um recurso no backend
// DELETE => Deletar um recurso do backend

// GET /users => Buscando usuários do backend
// POST /users => criar um usuário no backend

const users = []

const server = http.createServer((req, res) => {
  const { method, url } = req

  if (method == 'GET' && url == '/users') {
    return res
      .setHeader('Content-type', 'application/json')
      .end(JSON.stringify(users))
  }

  if (method == 'POST' && url == '/users') {
    users.push({
      id: 1,
      name: 'John Doe',
      email: 'johndoe@example.com'
    })

    return res.writeHead(201).end()
  }

  return res.writeHead(404).end()
})

server.listen(3333)
