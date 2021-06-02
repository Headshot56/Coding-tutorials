var bobX;
var jimX;
var bobY;
var jimY;
var bob_dist;
var jim_dist;
var targetX;
var targetY;


function setup(){
    createCanvas(600, 600);
    background(0);
    bobX = random(50, 550);
    jimX = random(50, 550);
    bobY = random(50, 550);
    jimY = random(50, 550);
    targetX = random(50, 550);
    targetY = random(50, 550);
    done = 0;
    print("bob = red");
    print("jim = green");
    print("Target = blue")
    print("We are finding closest one to the target");
    bob_dist = distance_calc(bobX, targetX, bobY, targetY);
    jim_dist = distance_calc(jimX, targetX, jimY, targetY);

    if (bob_dist < jim_dist){
        print("Bob is closer");
    }
    else{
        if (jim_dist < bob_dist){
            print("Jim is closer");
        }
    else{
        print("They are the same distance away.")
    }
    }

    print("jim", jim_dist);
    print("bob", bob_dist);

}

function distance_calc(x1, x2, y1, y2){
    let y = x2 - x1;
    let x = y2 - y1;

    return Math.sqrt(x * x + y * y);
}

function draw(){
    fill(255, 0 ,0);
    ellipse(bobX, bobY, 50, 50);
    fill(0, 255, 0);
    ellipse(jimX, jimY, 50, 50)
    fill(0, 0, 255);
    ellipse(targetX, targetY, 10, 10) 
}