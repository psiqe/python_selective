<h1>Shop Game</h1>
<h3><h3>
<div>
<h2>
    <a href="https://selective-python-shop-game.onrender.com/">  
        Link API
    </a>
    >> selective-python-shop-game.onrender.com/ 
</h2>

## 📕 About

Projeto consiste em um sistema de e-commerce de jogos. O usuário além de ter o necessário para criação e gestão de conta, consegue adicionar produtos a um carrinho de compras (Cart), onde pode ser checado, verificando valor dos produtos, frete e valor total.

O Projeto foi criado em Python usando o framework do DjangoREST, utilizando ferramentas como ordering e filter para listagem especifica de produtos.

Este projeto serve como base para a construção de sistemas de e-commerce mais complexos, com a possibilidade de adição de novos recursos e funcionalidades a medida que seja necessário.


## 📖 [Docs](https://selective-python-shop-game.onrender.com/docs/swagger-ui/) 🦾

## 🛠️ Tools
- [Python](https://www.python.org/)
- [DjangoREST](https://www.django-rest-framework.org/)
- [Git Flow](https://docs.github.com/en/get-started/quickstart/github-flow)
- [JWT](https://jwt.io/)
- [PostgreSQL](https://www.postgresql.org/)
- [drf_spectacular](https://drf-spectacular.readthedocs.io/en/latest/#)

## Installing

```Bash
# Create a virtual environment with Python
    $ python -m venv venv
```

```Bash
# Install app dependencies ```pip```
    $ pip install -r requirements.txt
```

```Bash
# Generate and run the migrations
    $ python manage.py makemigrations
    $ python manage.py migrate
```

```Bash
# Start App
    $ python manage.py runserver
```


# URLS, Methods and Functionalities
## Account
| Account | api/accounts/ |
|---|---|
| `POST` | Utilizado para criar um registro de usuário |
| `GET` | Utilizado para listar o usuário o qual estiver logado |
| `PATCH` | Utilizado para atualziar dados do usuário o qual estiver logado |
| `DELETE` | Utilizado para deletar o usuário o qual estiver logado |

*With the exception of the POST method, all other requests rely on JWT authentication.*

#
## Carts
| Carts | api/carts/ |
|---|---|
| `GET` | Utilizado para listar todos os Carts do usuário logado |
|---|---|

| Carts | api/carts/uuid:pk/ |
|---|---|
| `GET` | Utilizado para listar o Cart ativo do usuário logado |

*All requests rely on JWT authentication.*

#
## Orders
| Orders | api/orders/ |
|---|---|
| `POST` | Utilizado para criar uma Order de inserção de Game no Cart |
| `GET` | Utilizado para listar todas as orders ativas |
|---|---|

| Orders | api/orders/uuid:pk/ |
|---|---|
| `GET` | Utilizado para listar a order passada como parametro da url |
| `PATCH` | Utilizado para atualizar a quantidade do produto na order passada como parametro da url |
| `DELETE` | *Developing* |

*All requests rely on JWT authentication.*

#
## Products(Games)
| Products | api/load_json// |
|---|---|
| `POST` | Utilizado para criar todos os produtos passados em um arquivo json, com os componentes necessários |
|---|---|

| Products | api/games/ |
|---|---|
| `GET` | Listagem de produtos armazenados |
**filtragem e ordenação disponível por configuração nos endpoits* 
| `POST` | *Developing* |
| `PATCH` | *Developing* |
| `DELETE` | *Developing* |
|---|---|

*All requests rely on JWT authentication.*

#
### *Filter
| Filter type | comand | function | ex |
|---|---|---|---|
 | `name` | "icontains" | filtrar elementos que contenham o valor passado | ~~URL~~/?name=*value* |
 | `score` | "gte" "lte" | filtrar elementos com typo maior ou menor que o valor passado, respectivamente. | ~~URL~~/?score_gte=*value* **/** ~~URL~~/?score_lte=*value* |
 | `price` | "gte" "lte" | filtrar elementos com typo maior ou menor que o valor passado, respectivamente. | ~~URL~~/?price_gte=*value* **/** ~~URL~~/?price_lte=*value* |

**__Os filtros podem ser combinados, ex: ~~URL~~/?name=*value*&score_lte=*value*&price_gte=*value*__**


### *Ordern
| Order type | comand | function | ex |
|---|---|---|---|
| `name` | = **/** =- | Ordernar os itens da resposta pelo name em ordem alfabética; de forma crescente ou decrescente respectivamente. | ~~URL~~/?ordering=name **/** ~~URL~~/?ordering=-name |
| `score` | = **/** =- | Ordena os itens da resposta pelo score, de forma crescente ou decrescente respectivamente.  | ~~URL~~/?ordering=score **/** ~~URL~~/?ordering=-score |
| `price` | = **/** =- | Ordena os itens da resposta pelo price, de forma crescente ou decrescente respectivamente. | ~~URL~~/?ordering=price **/** ~~URL~~/?ordering=-price |

**__A ordenação pode ser combinada, ex: ~~URL~~/?ordering=name$:ordering=-score__**


* **__Pode ser combinado também Filter e Ordern__**
