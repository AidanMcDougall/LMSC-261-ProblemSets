
//rand array
let picturelist = [
    '1Yeat_2093.png',
    '2Lancey_Foux_Life_in_Hell.jpeg',
    '3Travis_Scott_Astroworld.png',
    '4Baby_Keem_The_Melodic_Blue.jpeg',
    '5PinkPantheress_Heaven_Knows.png'
];
//def function to call random value from index
function randomPicture() {
    let picIndex = Math.floor(Math.random() * picturelist.length);
    return picturelist[picIndex];
}
//test to make sure correct data is being called
console.log(randomPicture());


//button
let button = document.querySelector('#clickID')

button.addEventListener('click', function() {

let displayText = document.querySelector('#displayText');

displayText.textContent = 'Mike Dean and DJ Khalil!';
})
