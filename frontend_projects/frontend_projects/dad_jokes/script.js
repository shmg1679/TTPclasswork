const jokeE1 = document.getElementById('joke')
const jokeBthn = document.getElementById('jokeBtn')

jokeBthn.addEventListener('click', generateJoke)

generateJoke()

//USINGF ASYNC/AWAIT
async function generateJoke(){
    const config = {
        headers: {
            Accept: 'application/json',
        }
    }

    const res = await fetch('https://icanhasdadjoke.com',config)

    const data = await res.json()

    jokeE1.innerHTML = data.joke
}