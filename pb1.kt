import kotlin.collections.zipWithNext


fun main() {

    var lista1   = listOf(1,21,75,39,7,2,35,7,8).toMutableList()
    var lista2: List<Pair<Int, Int>>
    var i  = 0
    var sum     = 0
    lista1 = lista1.filter { it>5 }.toMutableList()
    lista2 = lista1.zipWithNext()
    lista1 = listOf<Int>().toMutableList()
    lista2.onEach {
        lista1 = (lista1 + it.first*it.second).toMutableList()
    }

    println(lista1)
    while(i <= lista1.lastIndex)
    {
        if(i % 2 == 0)
        {
            sum += lista1.get(i)
        }
        i++
    }
    println(sum)

}