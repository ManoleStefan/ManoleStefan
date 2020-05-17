import java.io.File
fun main(args : Array<String>) {
    val L = File("fis.txt").reader().readText()
    var i=0;
    var l1:String=""
    val diacritice :String="ăîâșțĂÎÂȘȚ"
    val normale :String="aiastAIAST"
    var viz= arrayOf(0,0,0,0,0,0,0,0,0,0)
    while(i<L.lastIndex-1) {
        if(diacritice.contains(L[i]))
            viz[diacritice.indexOf(L[i])]=1;
        if (!(L[i] == ' ' && L[i + 1] == ' ') ) {
            l1+=L[i];
        }
        i++;
    }
    var l2:String=""
    i=0
    while(i<l1.lastIndex-1) {
        if (!(l1[i] == '\r' && l1[i + 1] == '\n' ) ) {
            l2+=l1[i];
        }else i++;
        i++;
    }
    i=0
    while(i<10) {
        if (viz[i] == 1) {
            print(diacritice[i]+" ");
            l2 = l2.replace(diacritice[i], normale[i])
        }
        i++;
    }
    val words = l2.split("\n")
    var wordsfin:String=""
    words.forEach(){
        var trash: Boolean=true
        for(c in it){
            if (c in 'a'..'z' || c in 'A'..'Z')
                trash=false;
        }
        if(trash){
            println(it)
        }else
            wordsfin+=it+"\n"
    }
}