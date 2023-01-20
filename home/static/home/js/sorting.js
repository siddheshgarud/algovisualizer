// Function to swap two dom elements with their height
function swap(el1, el2) {
    console.log('In swap()');

    let temp = el1.style.height;
    el1.style.height = el2.style.height;
    el2.style.height = temp;

}

// function to disable the visualization button from sorting page. It will fetch the algorithm name from dom element and will disable the relative button
 function disableSortingBtn(){
    algorithmname = $( "#algorithmname" ).html()

    if(algorithmname == "bubblesort"){
        document.querySelector(".bubblesort").disabled = true;
    }
    if(algorithmname == "insertionsort"){
        document.querySelector(".insertionsort").disabled = true;

    }
    if(algorithmname == "mergesort"){
        document.querySelector(".mergesort").disabled = true;

    }
    if(algorithmname == "quicksort"){
        document.querySelector(".quicksort").disabled = true;

    }
    if(algorithmname == "selectionsort"){
        document.querySelector(".selectionsort").disabled = true;
    }
}

// Function to enable the visualize button
function enableSortingBtn(){

    algorithmname = document.getElementById("username").textContent

    if(algorithmname == "bubblesort"){
        document.querySelector(".bubblesort").disabled = false;
    }
    if(algorithmname == "insertionsort"){
        document.querySelector(".insertionsort").disabled = false;

    }
    if(algorithmname == "mergesort"){
        document.querySelector(".mergesort").disabled = false;

    }
    if(algorithmname == "quicksort"){
        document.querySelector(".quicksort").disabled = false;

    }
    if(algorithmname == "selectionsort"){
        document.querySelector(".selectionsort").disabled = false;
    }

}

// Function to disable size slider button while sorting
function disableSizeSlider(){
    document.querySelector("#arr_sz").disabled = true;
}

// Function to enable size slider button
function enableSizeSlider(){
    document.querySelector("#arr_sz").disabled = false;
}

// Function to disable new array button while sorting
function disableNewArrayBtn(){
    document.querySelector(".newArray").disabled = true;
}

// function to enable new array button after sorting complete
function enableNewArrayBtn(){
    document.querySelector(".newArray").disabled = false;
}

// Function to wait for animation while sorting
function waitforme(milisec) {
    return new Promise(resolve => {
        setTimeout(() => { resolve('') }, milisec);
    })
}

// Get array size from user input
let arraySize = document.querySelector('#arr_sz');

// Use to update bar on page
arraySize.addEventListener('input', function(){
    console.log(arraySize.value, typeof(arraySize.value));
    createNewArray(parseInt(arraySize.value));
});

// Default input for waitforme function (260ms)
let delay = 260;

// Selecting speed slider from DOM
let delayElement = document.querySelector('#speed_input');

// Event listener to update delay time
delayElement.addEventListener('input', function(){
    console.log(delayElement.value, typeof(delayElement.value));
    delay = 320 - parseInt(delayElement.value);
});

// Creating array to store randomly generated numbers
let array = [];

// To create new bars right after opening the site
createNewArray();

// Function to create new random array for bars
function createNewArray(noOfBars = 60) {
    // Deleting the previous ol bars
    deleteChild();

    // creating an array of random numbers
    array = [];

    //Pushing random generated number in array within 1 to 250
    for (let i = 0; i < noOfBars; i++) {
        array.push(Math.floor(Math.random() * 250) + 1);
    }


    // select the div #bars element
    const bars = document.querySelector("#bars");

    // Creating multiple div using loop as present as bars
    for (let i = 0; i < noOfBars; i++) {
        const bar = document.createElement("div");
        bar.style.height = `${array[i]*2}px`;
        bar.classList.add('bar');
        bar.classList.add('flex-item');
        bar.classList.add(`barNo${i}`);
        bars.appendChild(bar);
    }
}

// Function to delete previous bars
function deleteChild() {
    const bar = document.querySelector("#bars");
    bar.innerHTML = '';
}

// Selecting newarray button from DOM and adding eventlistener
const newArray = document.querySelector(".newArray");
newArray.addEventListener("click", function(){
    console.log("From newArray " + arraySize.value);
    console.log("From newArray " + delay);
    enableSortingBtn();
    enableSizeSlider();
    createNewArray(arraySize.value);
});
