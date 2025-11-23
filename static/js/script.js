window.addEventListener("load" , function(){
   let id = window.location.hash.replace("#" , "")
   
   if(id){
       let el = document.getElementById(id)
       if(el){
           el.scrollIntoView({behavior :"smooth" , block :"center"})
       }
   }
})
