class Coleccion extends Array {
    unirse(separador) {
        return this.join(separador);
    }

    esColeccion() {
        return this.isArray();
    }

    aCadena() {
        return this.toString();
    }

    saltar() {
        return this.pop();
    }

    empujar(articulo) {
        return this.push(articulo);
    }

    desplazar() {
        return this.shift()
    }

    longitud() {
        return this.length
    }
}