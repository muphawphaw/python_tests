const jsonObj = [{
    name: 'htet htet',
    age : 23,
    marriage : false
},
{
    name: 'kaung kaung',
    age : 16,
    marriage : true
}]

const convertedToString = JSON.stringify(jsonObj); //javascript obj to json string
localStorage.setItem("person",convertedToString);

const personFromLocalstorage = localStorage.getItem("person");
console.log(personFromLocalstorage)

const convertedToJavascriptObj = JSON.parse(convertedToString)// json string to javascript datatype
console.log(convertedToJavascriptObj[1].name)