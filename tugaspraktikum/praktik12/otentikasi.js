function auth(){
    const username = "arya"
    const password = "12345678"

    // tangkap input user
    let userInput = document.getElementById("username").value
    let passwordInput = document.getElementById("password").value

     if(username == userInput && password == passwordInput){
        alert("Login Berhasil")
        document.location = "home.html"
     } else{
        alert("Login Gagagl!")
     }
}